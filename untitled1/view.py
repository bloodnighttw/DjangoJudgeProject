from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.models import auth, User

ad = int
ad = 0


def index(request):
    global ad
    ad = ad + 1
    print(str(ad))
    return render(request, "extend.html", {"content": str(ad)})


def register(request):
    if request.user.is_authenticated:
        return redirect('/index')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('/index')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


def login(request):
    if request.user.is_authenticated:
        return redirect('/index')

    print("bang")
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            print("redit")
            return redirect("/index")
        else:
            messages.info(request, "Login failed")
            print("sssddddd")
            return redirect("/login")
    else:
        print("bangssss")
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/index')