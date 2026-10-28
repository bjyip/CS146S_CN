import json
import posixpath
import re
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

from pptx import Presentation


ROOT = Path(__file__).resolve().parent.parent
REL = {'r': 'http://schemas.openxmlformats.org/package/2006/relationships'}
EMBED = '{http://schemas.openxmlformats.org/officeDocument/2006/relationships}embed'
DRAWING = {'a': 'http://schemas.openxmlformats.org/drawingml/2006/main'}


def image_slides(source):
    locations = {}
    with zipfile.ZipFile(source) as archive:
        for name in archive.namelist():
            if not re.fullmatch(r'ppt/slides/slide\d+\.xml', name):
                continue
            relname = posixpath.join(posixpath.dirname(name), '_rels', posixpath.basename(name) + '.rels')
            if relname not in archive.namelist():
                continue
            relationships = {
                node.attrib['Id']: posixpath.normpath(posixpath.join(posixpath.dirname(name), node.attrib['Target']))
                for node in ET.fromstring(archive.read(relname)).findall('r:Relationship', REL)
            }
            slide = int(re.search(r'(\d+)\.xml', name)[1])
            for node in ET.fromstring(archive.read(name)).findall('.//a:blip', DRAWING):
                image = relationships.get(node.attrib.get(EMBED))
                if image:
                    locations.setdefault(image, set()).add(slide)
    return locations


def main():
    summary = ['# 图片文字中文译文', '', '原始截图保持不变，中文译文同时补充在相应幻灯片的演讲备注中。代码、命令、网址和产品名称保留原文。', '']
    for source in sorted((ROOT / 'Fall2025').glob('*.pptx')):
        mapping = json.loads((ROOT / '.translation_work' / (source.stem + '.images.zh.json')).read_text(encoding='utf-8'))
        locations = image_slides(source)
        additions = {}
        summary.extend([f'## {source.name}', ''])
        for image, text in mapping.items():
            if image not in locations:
                raise ValueError(f'{source.name}: unused image translation {image}')
            pages = sorted(locations[image])
            summary.extend([f'### 第 {"、".join(map(str, pages))} 页：{posixpath.basename(image)}', '', text, ''])
            for page in pages:
                additions.setdefault(page, []).append(f'【图片文字中文译文：{posixpath.basename(image)}】\n{text}')
        if not mapping:
            summary.extend(['此课件的图片无需补充自然语言译文。', ''])
        target = ROOT / 'Fall2025_cn' / source.name
        deck = Presentation(target)
        note_parts = {}
        for page, paragraphs in additions.items():
            notes = deck.slides[page - 1].notes_slide
            frame = notes.notes_text_frame
            frame.add_paragraph().text = '\n\n'.join(paragraphs)
            note_parts[str(notes.part.partname).lstrip('/')] = notes.part.blob
        temporary = target.with_suffix('.tmp')
        with zipfile.ZipFile(target) as archive, zipfile.ZipFile(temporary, 'w') as result:
            for info in archive.infolist():
                result.writestr(info, note_parts.get(info.filename, archive.read(info.filename)))
        temporary.replace(target)
        print(f'{source.name}: {len(mapping)} image translations added to {len(additions)} slide notes')
    (ROOT / 'Fall2025_cn' / '图片文字中文译文.md').write_text('\n'.join(summary), encoding='utf-8')


if __name__ == '__main__':
    main()
