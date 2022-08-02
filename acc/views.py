from django.shortcuts import render, redirect
from .models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import check_password
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'acc/index.html')

def userlogin(request):
    if request.method == "POST":
        un = request.POST.get("uname")
        up = request.POST.get("upass")
        u = authenticate(username=un, password=up)
        if u:
            login(request, u)
            return redirect("acc:index")
        else: #20 일차에 메세지
            messages.error(request, "계정정보가 일치하지 않습니다")
    return render(request, 'acc/login.html')

def userlogout(request):
    logout(request)
    return redirect("acc:index")

def signup(request):
    if request.method == "POST":
        un = request.POST.get("uname")
        up = request.POST.get("upass")
        uc = request.POST.get("ucomm")
        ui = request.FILES.get("upic")
        try:
            User.objects.create_user(username=un, password=up, comment=uc, point=0, pic=ui)
            messages.success(request, "가입에 성공하셨습니다!")
            return redirect("acc:login")
        except:
            messages.error(request, "USERNAME 이 중복되었습니다!")
    return render(request, "acc/signup.html")

def profile(request):
    return render(request, 'acc/profile.html')

def update(request):
    if request.method == "POST":
        u = request.user
        um = request.POST.get("umail")
        uc = request.POST.get("ucomm")
        ui = request.FILES.get("upic")
        u.email, comment = um, uc
        if ui:
            u.pic.delete()
            u.pic = ui
        u.save()
        return redirect("acc:profile")
    return render(request, 'acc/update.html')

def chpass(request):
    if request.method == "POST":
        cp = request.POST.get("cpass")
        u = request.user
        if check_password(cp, u.password):
            np = request.POST.get("npass")
            u.set_password(np)
            u.save()
            return redirect("acc:login")
        else:
            messages.error(request, "패스워드가 일치하지 않습니다")
        return redirect("acc:update")

def delete(request):
    cp = request.POST.get("cpass")
    u = request.user
    if check_password(cp, u.password):
        u.pic.delete()
        u.delete()
        return redirect("acc:index")
    else:
        messages.error(request, "패스워드가 일치하지 않습니다")
    return redirect("acc:profile")