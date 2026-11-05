import argparse
import json
import re
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET


ROOT = Path(__file__).resolve().parent.parent
RESOURCE = ROOT.parent / 'Resource'
OUTPUT = ROOT / 'reference' / 'slides' / 'fall2025'
NS = {'a': 'http://schemas.openxmlformats.org/drawingml/2006/main'}


def parts(archive):
    return sorted(
        (name for name in archive.namelist()
         if re.fullmatch(r'ppt/(slides/slide|notesSlides/notesSlide)\d+\.xml', name)),
        key=lambda name: (name.split('/')[1], int(re.search(r'(\d+)\.xml', name)[1]))
    )


def extract():
    work = RESOURCE / '.translation_work'
    work.mkdir(exist_ok=True)
    for source in sorted((RESOURCE / 'Fall2025').glob('*.pptx')):
        records = []
        with zipfile.ZipFile(source) as archive:
            for name in parts(archive):
                tree = ET.fromstring(archive.read(name))
                for index, paragraph in enumerate(tree.findall('.//a:p', NS)):
                    runs = [node.text or '' for node in paragraph.findall('.//a:t', NS)]
                    text = ''.join(runs)
                    if text.strip():
                        records.append({'id': f'{name}:{index}', 'text': text, 'runs': runs})
        target = work / (source.stem + '.source.json')
        target.write_text(json.dumps(records, ensure_ascii=False, indent=2), encoding='utf-8')
        print(f'{source.name}: {len(records)} paragraphs, {sum(len(r["text"]) for r in records)} characters')


def generate():
    OUTPUT.mkdir(parents=True, exist_ok=True)
    for source in sorted((RESOURCE / 'Fall2025').glob('*.pptx')):
        translation = RESOURCE / '.translation_work' / (source.stem + '.zh.json')
        mapping = json.loads(translation.read_text(encoding='utf-8'))
        used = set()
        with zipfile.ZipFile(source) as archive, zipfile.ZipFile(OUTPUT / source.name, 'w') as result:
            selected = set(parts(archive))
            for info in archive.infolist():
                data = archive.read(info.filename)
                if info.filename in selected:
                    # Replace only text payloads, leaving namespaces, layout and all other XML intact.
                    paragraphs = list(re.finditer(rb'<a:p(?:\s[^>]*)?(?:/>|>.*?</a:p>)', data, re.DOTALL))
                    for index, match in reversed(list(enumerate(paragraphs))):
                        key = f'{info.filename}:{index}'
                        if key not in mapping:
                            continue
                        values = mapping[key]
                        if isinstance(values, str):
                            values = [values]
                        text_matches = list(re.finditer(rb'<a:t(?:\s[^>]*)?>(.*?)</a:t>', match[0], re.DOTALL))
                        if len(values) != len(text_matches):
                            raise ValueError(f'{source.name} {key}: expected {len(text_matches)} runs, got {len(values)}')
                        paragraph = match[0]
                        for text_match, value in reversed(list(zip(text_matches, values))):
                            escaped = value.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
                            paragraph = paragraph[:text_match.start(1)] + escaped.encode('utf-8') + paragraph[text_match.end(1):]
                        data = data[:match.start()] + paragraph + data[match.end():]
                        used.add(key)
                    ET.fromstring(data)
                result.writestr(info, data)
        if used != set(mapping):
            raise ValueError(f'Unused translations: {set(mapping) - used}')
        print(f'Generated {source.name}: {len(used)} translated paragraphs')


def check():
    for source in sorted((RESOURCE / 'Fall2025').glob('*.pptx')):
        records = json.loads((RESOURCE / '.translation_work' / (source.stem + '.source.json')).read_text(encoding='utf-8'))
        translation = RESOURCE / '.translation_work' / (source.stem + '.zh.json')
        if not translation.exists():
            print(f'PENDING {source.name}')
            continue
        mapping = json.loads(translation.read_text(encoding='utf-8'))
        if set(mapping) != {record['id'] for record in records}:
            raise ValueError(f'{source.name}: translation keys do not match source')
        unchanged = []
        for record in records:
            values = mapping[record['id']]
            if not isinstance(values, list) or len(values) != len(record['runs']):
                raise ValueError(f'{source.name} {record["id"]}: invalid run count')
            if not all(isinstance(value, str) for value in values):
                raise ValueError(f'{source.name} {record["id"]}: invalid text type')
            if ''.join(values) == record['text'] and re.search(r'[A-Za-z]{3,}', record['text']):
                unchanged.append(record['text'])
        print(f'CHECKED {source.name}: {len(records)} paragraphs; retained English: {json.dumps(unchanged, ensure_ascii=False)}')
        target = OUTPUT / source.name
        if not target.exists():
            continue
        with zipfile.ZipFile(source) as original, zipfile.ZipFile(target) as result:
            if original.namelist() != result.namelist() or result.testzip() is not None:
                raise ValueError(f'{source.name}: archive structure changed or damaged')
            selected = set(parts(original))
            for name in original.namelist():
                if name not in selected and original.read(name) != result.read(name):
                    raise ValueError(f'{source.name}: unexpected change to {name}')
                if name.endswith('.xml'):
                    ET.fromstring(result.read(name))
                if name in selected:
                    tree = ET.fromstring(result.read(name))
                    for index, paragraph in enumerate(tree.findall('.//a:p', NS)):
                        key = f'{name}:{index}'
                        if key in mapping:
                            actual = [node.text or '' for node in paragraph.findall('.//a:t', NS)]
                            if actual != mapping[key]:
                                raise ValueError(f'{source.name} {key}: output text does not match translation')
            print(f'VERIFIED {source.name}: archive, XML, text and original assets intact')


def audit():
    for source in sorted((RESOURCE / 'Fall2025').glob('*.pptx')):
        with zipfile.ZipFile(source) as archive:
            selected = set(parts(archive))
            slides = [name for name in selected if name.startswith('ppt/slides/')]
            images = [name for name in archive.namelist() if name.startswith('ppt/media/')]
            print(f'{source.name}: {len(slides)} slides, {len(images)} media assets')
            for name in archive.namelist():
                if name.endswith('.xml') and name not in selected:
                    tree = ET.fromstring(archive.read(name))
                    text = [node.text for node in tree.findall('.//a:t', NS) if node.text and node.text.strip()]
                    if text:
                        print(f'  OTHER TEXT {name}: {json.dumps(text, ensure_ascii=False)}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('action', choices=['extract', 'generate', 'check', 'audit'])
    args = parser.parse_args()
    {'extract': extract, 'generate': generate, 'check': check, 'audit': audit}[args.action]()
