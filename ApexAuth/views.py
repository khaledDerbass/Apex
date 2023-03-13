from django.shortcuts import render

def signup(request):
    return render(request, 'auth/signup.html')

def handlelogin(request):
    return render(request, 'auth/login.html')

def handlelogout(request):
    return render(request, 'auth/login.html')

def resetpassword(request):
    return render(request, 'auth/resetpass.html')