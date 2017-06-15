from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.shortcuts import render, redirect


def login(request):
    # member/login.html 생성
    #   username, password, button 에 있는 HTML생성
    #   POST요청이 올 경우 좌측 코드를 기반으로 로그인 완료 후 post_list로 이동
    #   실패할 경우 HttpResponse로 'Login invalid!' 띄워주기

    # member/urls.py 생성
    #   /member/login/으로 접근시 이 view로 오도록 설정
    #   config/urls.py에 member/urls.py를 include
    #       member/urls.py에 app_name설정으로 namespace지정
    if request.method == 'POST':
        user = authenticate(
            username=request.POST['username'],
            password=request.POST['password'],
        )
        if user is not None:
            login(request, user)
            return redirect(request, 'post:post_list')
        else:
            return HttpResponse('Login invalid!')

    else:
        return render(request, 'member/login.html')
