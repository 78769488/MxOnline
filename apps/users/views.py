from django.contrib.auth import authenticate, login
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.shortcuts import render
from django.views.generic.base import View

from users.models import UserProfile
from users.forms import LoginForm


# 邮箱和用户名都可以登录
# 基础ModelBackend类，因为字有authenticate方法
class CustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            # 不希望用户存在两个，get只能有一个。两个是get失败的一种原因，Q为使用并集查询
            user = UserProfile.objects.get(Q(username=username) | Q(email=username))

            # django的后台中密码加密，所以不能password=password
            # UserProfile继承的AbstractUser中有def check_password方法
            if user.check_password(password):
                return user
        except Exception as e:
            return None


class LoginView(View):
    def get(self, request):
        return render(request, "login.html")

    def post(self, request):
        # 实例化
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            # 获取用户提交的用户名和密码
            username = request.POST.get("username", None)
            password = request.POST.get("password", None)
            # 验证成功返回user对象，失败返回None
            user = authenticate(username=username, password=password)
            if user is not None:
                # 登录
                login(request, user)
                return render(request, "index.html")
            else:
                return render(request, "login.html",
                              {"msg": "用户名或密码错误", "login_form": login_form})
        # form.is_valid()已经判断不合法了，所以这里不需要再返回错误信息到前端了
        else:
            return render(request, "login.html", {"login_form": login_form})


class RegisterView(View):
    """用户注册"""
    def get(self, request):
        return render(request, 'register.html')
