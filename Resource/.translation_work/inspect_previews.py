from pathlib import Path

from PIL import Image, ImageDraw


root = Path(__file__).resolve().parent
for folder in sorted(root.glob('*.preview')):
    files = sorted(folder.glob('*.PNG'), key=lambda path: int(''.join(filter(str.isdigit, path.stem))))
    for start in range(0, len(files), 12):
        batch = files[start:start + 12]
        sheet = Image.new('RGB', (1280, 385 * ((len(batch) + 1) // 2)), 'white')
        for offset, path in enumerate(batch):
            image = Image.open(path).convert('RGB')
            image.thumbnail((640, 360))
            x, y = (offset % 2) * 640, (offset // 2) * 385
            sheet.paste(image, (x, y + 25))
            ImageDraw.Draw(sheet).text((x + 5, y + 5), path.stem, fill='black')
        sheet.save(root / (folder.stem + f'.pages{start + 1}.jpg'))
