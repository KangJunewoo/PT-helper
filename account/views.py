from django.shortcuts import render, redirect
from django.http import HttpResponse
import requests

'''
정리를 해보자면
/login : 로그인 처리 후 /login_process로 리다이렉트되는데, 이 때 authorize_code가 넘어감.
    client_id : api키
    redirect_uri : 리다이렉트해줄 uri
    response_type : code

/login_process : 여기서 사용자 토큰을 post로 요청해야함. authorize_code를 얻어내서
    grant_type : authorization_code
    client_id : api키
    redirect_Uri : ★리다이렉트 된 uri★
    code : 아까 그 authorize_code

    그러면 뭐 한 5개의 응답이 오는데 그 중 access_token에만 관심.
    그걸로

/info : 헤더 authorization에 'Bearer {access_token}' 넣어주고 요쳥해주면 됨.
    그러면 유저의 정보가 쫘라라라락~
'''


# Create your views here.
def index(request):
    return render(request, 'index.html')

def login(request):
    REDIRECT_URI = 'http://localhost:8000/account/login_process'
    KAKAO_HOST = 'kauth.kakao.com'
    APP_KEY = 'c143f6d80aae41f4dd5eea279803c34a'
    
    KAKAO_AUTH_URL = f'https://{KAKAO_HOST}/oauth/authorize?client_id={APP_KEY}&redirect_uri={REDIRECT_URI}&response_type=code'
    return redirect(KAKAO_AUTH_URL)
        

def login_process(request):
    kakao_access_code = request.GET['code']
    print()
    url = 'https://kauth/kakao/com/oauth/token'
    headers={'Content-type':'application/x-www-form-urlencoded; charset=utf-8'}
    APP_KEY = 'c143f6d80aae41f4dd5eea279803c34a'
    body={
        'grant_type' : 'authorization_code',
        'client_id': APP_KEY,
        'redirect_uri':'http://localhost:8000/account',
        'code':kakao_access_code,
    }
    kakao_response=requests.post(url, headers=headers, data=body)
    print(kakao_response)
    return render('/index')
'''
def info(request):
    KAKAO_HOST = 'kauth.kakao.com'
    KAKAO_INFO_URL = f'https://{KAKAO_HOST}/v2/user/me'
    client = Client()
    response = client.get(KAKAO_INFO_URL)
    return HttpResponse(response)
'''