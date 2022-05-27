from django.shortcuts import render, redirect
# from .models import UserModel
from django.http import HttpResponse

class UserClass:
    def __init__(self,email,password):
        self.email = email
        self.password = password

    def sign_up_view(request):
        if request.method == 'GET':
            return render(request, 'user/index.html')
        elif request.method == 'POST':
            email = request.POST.get('email', None)
            password = request.POST.get('password', None)


            if "@" not in email:
                return HttpResponse("이메일 형식 에러"),401

            if len(password) <= 8:
                return HttpResponse("비밀번호 길이 에러"), 401
            else:

                new_user = UserModel()
                new_user.email = email
                new_user.password = password
                new_user.save()

                return HttpResponse("회원가입 완료")

