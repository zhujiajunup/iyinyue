from django.shortcuts import render_to_response
from django.http import *
from django.utils import timezone
from user.models import IUser, Music, PlayList
import json
import hashlib

# def index(request):
#     return render_to_response('user/register.html', locals())


#  用户注册
def register(request):
    if request.method == 'POST':
        user = IUser()
        user_name = request.POST.get('user_name', None)
        user_email = request.POST.get('user_email', None)
        user_password = request.POST.get('user_password', None)

        default_list = PlayList()  # 创建默认播放列表
        default_list.play_list_name = u'默认播放列表'  # 默认播放列表名

        default_list.save()
        user.save()
        user.play_list.add(default_list)

        user.user_name = user_name
        user.email = user_email
        user.password = hashlib.sha1(user_password.encode(encoding='utf-8')).hexdigest()

        user.save()
        # TODO
        return HttpResponse(1)
    return render_to_response('user/register.html', locals())


# 用户登录
def login(request):
    if request.method == 'POST':
        user_name = request.POST.get('user_name', None)  # 获取用户名
        password = request.POST.get('user_name', None)
        try:
            user = IUser.objects.get(user_name=user_name)
        except IUser.DoesNotExist:
            raise Http404("User does not exist")
        if user.password != hashlib.sha1(password.encode(encoding='utf-8')).hexdigest():
            HttpResponse("password error")
        # TODO return value
        user.last_time = timezone.now()
        user.save()
        return HttpResponse(1)
    return render_to_response('user/login.html', locals())


# 获取用户基本信息
def get_user_info(request):
    if request.method == 'GET':
        user_name = request.GET['user_name']
        user = IUser.objects.get(user_name=user_name)
        user_info_json = {
            'user_name': user.user_name,
            'head_img': user.head_img
        }
        return HttpResponse(json.dumps(user_info_json), content_type='application/json')

#
# def hello(request):
#     return render_to_response('user/hello.html', locals())
#
# def test(request):
#     if request.method == 'GET':
#         param = request.REQUEST.get('param', None)
#         return HttpResponse(json.dumps(param), content_type="application/json")
#     return render_to_response('user/hello.html', locals())
#
# def register(request): # 注册用户
#     if request.method == 'POST':
#         uf = UserRegisterForm(request.POST)
#         if uf.is_valid():
#
#             user_name = uf.cleaned_data['user_name']
#             password1 = hashlib.sha1((uf.cleaned_data['password']).encode(encoding='utf-8')).hexdigest()  # 加密
#             password2 = hashlib.sha1((uf.cleaned_data['password2']).encode(encoding='utf-8')).hexdigest()
#             birthday = uf.cleaned_data['birthday']
#            # user.sex = uf.cleaned_data['sex']
#             email = uf.cleaned_data['email']
#             tag = uf.cleaned_data['tag']
#             errors = []
#             userRegisterForm = UserRegisterForm({'user_name':user_name, 'password':password1, 'password2':password2,
#                 'tag':tag, 'email':email, 'birthday':birthday})
#             if not userRegisterForm.is_valid():
#                 errors.extend(userRegisterForm.errors.values())
#                 return render_to_response('user/register.html', RequestContext(request,{'uf':uf}))
#             if password1 != password2:
#                 errors.append("密码输入不一致，请重新输入")
#                 return render_to_response('user/register.html', RequestContext(request,{'uf':uf}))
#             filterResult = User.objects.filter(user_name=user_name)
#             if len(filterResult) > 0 :
#                 errors.append("用户名已经存在")
#                 return render_to_response('user/register.html', RequestContext(request,{'uf':uf}))
#             user = User()
#             user.user_name = user_name
#             user.password = password1
#             user.birthday = birthday
#             user.tag = tag
#             user.email = email
#             user.last_time = timezone.now()
#             user.save()
#             return HttpResponse("successful")
#     uf = UserRegisterForm()
#     return render_to_response('user/register.html', RequestContext(request, {'uf':uf}))
#
# def login(request):
#     if request.method == 'POST':
#         userLoginForm = UserLoginForm(request.POST)
#         if userLoginForm.is_valid():
#             user_name = userLoginForm.cleaned_data['user_name']
#             password = userLoginForm.cleaned_data['password']
#             try:
#                 user = User.objects.get(user_name=user_name)
#             except User.DoesNotExist:
#                 raise Http404("User does not exist")
#             if user.password != hashlib.sha1(password.encode(encoding='utf-8')).hexdigest():
#                 HttpResponse("password error")
#             return HttpResponse("login successful")
#     userLoginForm = UserLoginForm()
#     return render_to_response('user/login.html', RequestContext(request, {'userLoginForm':userLoginForm}))