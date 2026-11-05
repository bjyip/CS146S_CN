"""Print page-located PPTX text for source review without changing files."""

import argparse
import posixpath
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET


NS = {
    'a': 'http://schemas.openxmlformats.org/drawingml/2006/main',
    'p': 'http://schemas.openxmlformats.org/presentationml/2006/main',
    'r': 'http://schemas.openxmlformats.org/officeDocument/2006/relationships'
}
REL = 'http://schemas.openxmlformats.org/package/2006/relationships'


def review(path):
    with zipfile.ZipFile(path) as archive:
        presentation = ET.fromstring(archive.read('ppt/presentation.xml'))
        relations = ET.fromstring(archive.read('ppt/_rels/presentation.xml.rels'))
        targets = {item.get('Id'): item.get('Target') for item in relations}
        slides = presentation.findall('p:sldIdLst/p:sldId', NS)
        print(f'\nFILE {path.name}: {len(slides)} pages')
        for page, slide in enumerate(slides, 1):
            target = targets[slide.get(f'{{{NS["r"]}}}id')]
            name = posixpath.normpath(posixpath.join('ppt', target))
            if target.startswith('/'):
                name = target.lstrip('/')
            tree = ET.fromstring(archive.read(name))
            print(f'\nPAGE {page} [{name}]')
            for paragraph in tree.findall('.//a:p', NS):
                text = ''.join(node.text or '' for node in paragraph.findall('.//a:t', NS))
                if text.strip() and text.strip() != 'themodernsoftware.dev':
                    print(text)
            pictures = len(tree.findall('.//p:pic', NS))
            tables = len(tree.findall('.//a:tbl', NS))
            print(f'[visual review pending: pictures={pictures}, tables={tables}]')
            relation_name = posixpath.join(posixpath.dirname(name), '_rels', posixpath.basename(name) + '.rels')
            if relation_name not in archive.namelist():
                continue
            for relation in ET.fromstring(archive.read(relation_name)).findall(f'{{{REL}}}Relationship'):
                if not relation.get('Type', '').endswith('/notesSlide'):
                    continue
                note_target = relation.get('Target')
                note_name = posixpath.normpath(posixpath.join(posixpath.dirname(name), note_target))
                if note_target.startswith('/'):
                    note_name = note_target.lstrip('/')
                note = ET.fromstring(archive.read(note_name))
                texts = []
                for shape in note.findall('.//p:sp', NS):
                    placeholder = shape.find('p:nvSpPr/p:nvPr/p:ph', NS)
                    if placeholder is not None and placeholder.get('type') in {'sldNum', 'hdr', 'ftr', 'dt'}:
                        continue
                    for paragraph in shape.findall('.//a:p', NS):
                        text = ''.join(node.text or '' for node in paragraph.findall('.//a:t', NS))
                        if text.strip():
                            texts.append(text)
                if texts:
                    print('NOTES:')
                    print('\n'.join(texts))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('files', nargs='+', type=Path)
    args = parser.parse_args()
    for source in args.files:
        review(source)
