from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, 'index.html')

def login(request):
    APP_KEY = 'c143f6d80aae41f4dd5eea279803c34a'
    REDIRECT_URI = '/accounts'
    KAKAO_HOST = 'kauth.kakao.com'
    KAKAO_AUTH_URL = f'https://{KAKAO_HOST}/oauth/authorize?client_id={APP_KEY}&redirect_uri={REDIRECT_URI}&response_type=code'
    return redirect(KAKAO_AUTH_URL)