from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm
from django.contrib.auth import login, authenticate, logout
# Create your views here.

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request=request, data=request.POST)
        if form.is_valid():
            # cleaned data : form valid 통과한 데이터
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request=request, username=username, password=password) #???
            if user: # user가 authenticate 되지 않을 경우 : user ~ None
                login(request, user)
                return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'account.html', { 'form': form, 'page': "로그인" })

def logout_view(request):
    logout(request)
    return redirect('home')

def register_view(request):
    if request.method == "POST":
        # 우리가 폼으로 받은 데이터로 유저를 만들어야 하므로
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            # 회원가입 하자마자 로그인 된 상태
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'account.html', { 'form': form, 'page': "회원가입" })