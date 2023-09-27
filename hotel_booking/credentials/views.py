from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages,auth#for message

# Create your views here.
def register(request):
    if request.method == 'POST':
        uname=request.POST['uname']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        password=request.POST['pass']
        cpassword=request.POST['cpass']
        # print(uname,fname,lname,email,password)
        if password==cpassword:
            if User.objects.filter(username=uname).exists():
                messages.info(request,"User name exist")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email aready esist")
                return  redirect('register')
            else:
                user=User.objects.create_user(username=uname,password=password,first_name=fname,last_name=lname,email=email)
                user.save()
                print("user created")
        else:
            messages.info(request,"Password mismatch")

        return redirect("/")
    return render(request,"register.html")
def login(request):
    if request.method == 'POST':
        uname=request.POST['uname']
        password=request.POST['pass']
        print(uname,password)
        user=auth.authenticate(username=uname,password=password)
        print(user)
        if user is not None:
            auth.login(request,user)
            print("success")
            return redirect('/')
        else:
            messages.info(request,"error in login")
            return redirect('login')
    return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')