"""Extract page text and render local review sheets without changing sources."""

import argparse
import hashlib
from pathlib import Path
import tempfile

import pymupdf


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('pdf', type=Path)
    parser.add_argument('--pages', type=int, nargs='+')
    args = parser.parse_args()
    with pymupdf.open(args.pdf) as document:
        pages = args.pages or list(range(1, len(document) + 1))
        if any(number < 1 or number > len(document) for number in pages):
            parser.error('Page numbers must be within the document')
        output = Path(tempfile.mkdtemp(prefix='cs146s-pdf-'))
        print(f'PyMuPDF: {pymupdf.VersionBind}')
        print(f'Source: {args.pdf.resolve()}')
        print(f'SHA256: {hashlib.sha256(args.pdf.read_bytes()).hexdigest()}')
        print(f'Page count: {len(document)}; review images: {output}')
        for number in pages:
            page = document[number - 1]
            print(f'\n=== PAGE {number} ===\n{page.get_text(sort=True)}')
        for start in range(0, len(pages), 4):
            group = pages[start:start + 4]
            with pymupdf.open() as sheet:
                canvas = sheet.new_page(width=1600, height=1000)
                for index, number in enumerate(group):
                    x = (index % 2) * 800
                    y = (index // 2) * 500
                    canvas.insert_text((x + 10, y + 18), f'PAGE {number}')
                    canvas.show_pdf_page(
                        pymupdf.Rect(x, y + 24, x + 800, y + 500),
                        document,
                        number - 1
                    )
                image = output / f'pages-{group[0]:02d}-{group[-1]:02d}.png'
                canvas.get_pixmap(matrix=pymupdf.Matrix(1.5, 1.5)).save(image)
                print(f'REVIEW_SHEET: {image}')


if __name__ == '__main__':
    main()
