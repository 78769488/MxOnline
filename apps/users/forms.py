#!/usr/bin/env python
# -*- coding=utf-8 -*-
# by zhangrf
from django import forms

# 登录表单
class LoginForm(forms.Form):
    # 用户名 密码不能为空
    username = forms.CharField(required=True)
    password = forms.PasswordInput()
