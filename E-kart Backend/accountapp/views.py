from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
# Create your views here.
'''

'''

def user_login(request):
    context={}
    if request.method=="GET":

        return render(request,'accounts/login.html')
    else:
        #fetch and store post from data
        uname=request.POST['uname']
        upass=request.POST['upass']
        #validation
        if uname=='' or upass=='' :
            context['errmsg']="Fields cannot be empty"
            return render(request,'accounts/login.html',context)
        else:
            #select * from auth_user where username=uname and password=upass;
            u=authenticate(username=uname,password=upass)
            #print("Value:",u)
            if u is not None:
                login(request,u)
                return redirect('/')
            else:
                context['errmsg']="Invalid Username or Password"
                return render(request,'accounts/login.html',context)

            return HttpResponse("User fetched")


def user_register(request):
    context={}
    if request.method=="GET":

        return render(request,'accounts/register.html')
    else:
        #fetch and store post from data
        uname=request.POST['uname']
        uemail=request.POST['uemail']
        upass=request.POST['upass']
        ucpass=request.POST['ucpass']

        #validation
        if uname=='' or uemail=='' or upass=='' or ucpass=='':
            context['errmsg']="Fields cannot be empty"
            return render(request,'accounts/register.html',context)
        elif len(upass)<8:
            context['errmsg']="Password must be minimum 8 characters in length"
            return render(request,'accounts/register.html',context)
        elif ucpass.isdigit():
            context['errmsg']="Password cannot be entirely in digit"
            return render(request,'accounts/register.html',context)
        elif upass!=ucpass:
            context['errmsg']="Password and Confirm Password mismatch"
            return render(request,'accounts/register.html',context)
        else:
            u=User.objects.create(username=uname,email=uemail)
            u.set_password(upass)
            u.save()
            context['success']="User created Successfully"
            return render(request,'accounts/register.html',context)

def user_logout(request):
    logout(request)
    return redirect('/')
