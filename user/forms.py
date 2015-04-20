__author__ = 'Administrator'
from django import forms
from django.forms.extras.widgets import SelectDateWidget


class UserRegisterForm(forms.Form):
    user_name = forms.CharField(label='用户名', max_length=100,error_messages={ 'required':'邮箱不能为空'})
    birthday = forms.DateField(label='生日', widget=SelectDateWidget())
    # sex = forms.ChoiceField(label='性别')
    password = forms.CharField(label='密码', widget=forms.PasswordInput())
    password2 = forms.CharField(label='确认密码', widget=forms.PasswordInput())
    email = forms.EmailField(label='邮箱',error_messages={ 'required':'邮箱不能为空'})
    tag = forms.CharField(label='标签', widget=forms.Textarea())


class UserLoginForm(forms.Form):
    user_name = forms.CharField(label='用户名', max_length=100,error_messages={ 'required':'邮箱不能为空'})
    password = forms.CharField(label='密码', widget=forms.PasswordInput())

