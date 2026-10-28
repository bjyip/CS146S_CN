import io
import zipfile
from pathlib import Path

from PIL import Image, ImageDraw


root = Path(__file__).resolve().parent.parent
for source in sorted((root / 'Fall2025').glob('*.pptx')):
    tiles = []
    with zipfile.ZipFile(source) as archive:
        destination = root / '.translation_work' / (source.stem + '.media')
        destination.mkdir(exist_ok=True)
        for name in archive.namelist():
            if not name.startswith('ppt/media/'):
                continue
            (destination / Path(name).name).write_bytes(archive.read(name))
            try:
                image = Image.open(io.BytesIO(archive.read(name))).convert('RGB')
            except Exception:
                continue
            if image.width < 150 or image.height < 80:
                continue
            image.thumbnail((640, 400))
            tile = Image.new('RGB', (660, 440), 'white')
            tile.paste(image, ((660 - image.width) // 2, 30))
            ImageDraw.Draw(tile).text((10, 10), name, fill='black')
            tiles.append(tile)
    if tiles:
        sheet = Image.new('RGB', (1320, 440 * ((len(tiles) + 1) // 2)), '#dddddd')
        for index, tile in enumerate(tiles):
            sheet.paste(tile, ((index % 2) * 660, (index // 2) * 440))
        sheet.save(root / '.translation_work' / (source.stem + '.images.jpg'))
        print(f'{source.name}: {len(tiles)} inspectable images')
