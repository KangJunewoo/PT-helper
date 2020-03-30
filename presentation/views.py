from django.shortcuts import render
from pdf2image import convert_from_path, convert_from_bytes
from pdf2image.exceptions import (
    PDFInfoNotInstalledError,
    PDFPageCountError,
    PDFSyntaxError
)

def pdfToImages():
    images = convert_from_path('example.pdf')
    i = 1
    for image in images:
	    image.save('image' + str(i) + '.jpg', 'JPEG')
	    i = i + 1