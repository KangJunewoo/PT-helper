from django.shortcuts import render
from pdf2image import convert_from_path, convert_from_bytes
from pdf2image.exceptions import (
    PDFInfoNotInstalledError,
    PDFPageCountError,
    PDFSyntaxError
)
#from .models import PDF, Quecard

# 일단 함수형으로 view짜기 
# Page rendering
def home(request):
	# 유저 세션으로 페이지 결정
	user_session = request.session.get('user')
	if user_session:
		# content = {}
		return render(request, 'index.html', content)
	else:
		return render(request, 'login.html')

def uploads(request):
	return render(request, 'makePT.html')

# Logic
def pdfToImages():
    images = convert_from_path('example.pdf')
    i = 1
    for image in images:
	    image.save('image' + str(i) + '.jpg', 'JPEG')
	    i = i + 1
		#Quecard.save()