from django.shortcuts import render
from pdf2image import convert_from_path, convert_from_bytes
from pdf2image.exceptions import (
    PDFInfoNotInstalledError,
    PDFPageCountError,
    PDFSyntaxError
)

# 유저 세션으로 페이지 결정
def home(request):
	user_session = request.session.get('user')
	if user_session:
		# content = {}
		return render(request, 'presentation/index.html', content)
	else:
		return render(request, 'presentation/login.html')

def pdfToImages():
    images = convert_from_path('example.pdf')
    i = 1
    for image in images:
	    image.save('image' + str(i) + '.jpg', 'JPEG')
	    i = i + 1