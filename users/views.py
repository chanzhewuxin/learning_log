from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

# def login_sys(request):
#     username=request.POST.get('username')
#     password = request.POST.get('password')
#     user = authenticate(request,username=username,password=password)
#     if user is not None:
#         login(request,user)
#         return HttpResponseRedirect(reverse("learning_logs:index"))
    
#     return render(request,"users/login.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('learning_logs:index'))


def register(request):
    """注册新用户"""
    if request.method != 'POST':
        # 显示空的注册表单
        form = UserCreationForm()
    else:
        # 处理填写好的表单
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            authenticate_user= authenticate(username=new_user.username,password=request.POST['password1'])
            login(request,authenticate_user)
            return HttpResponseRedirect(reverse('learning_logs:index'))
        
    context = {'form':form}
    return render(request,'users/register.html',context)


