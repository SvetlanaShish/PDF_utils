
from PyPDF2 import PdfReader, PdfWriter
from sys import argv

template = PdfReader(argv[1])
watermark = PdfReader(argv[2]).pages[0]
output = PdfWriter()

for page in template.pages:
  page.merge_page(watermark)
  output.add_page(page)
  with open('watermarked_output.pdf', 'wb') as file:
    output.write(file)