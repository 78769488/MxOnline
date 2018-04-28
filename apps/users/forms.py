#!/usr/bin/env python
# -*- coding=utf-8 -*-
# by zhangrf
from django import forms
from captcha.fields import CaptchaField

class LoginForm(forms.Form):
    """登录表单"""
    # 用户名 密码不能为空
    username = forms.CharField(required=True)
    password = forms.PasswordInput()


class RegisterForm(forms.Form):
    """注册表单"""
    email = forms.EmailField(required=True)
    password = forms.PasswordInput()
    # 验证码，字段里面可以自定义错误提示信息
    captcha = CaptchaField(error_messages={'invalid': '验证码错误'})

