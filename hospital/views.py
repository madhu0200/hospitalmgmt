from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from .forms import *
# Create your views here.

def home(request):
    return render(request,'home.html')


def register(request):
    if request.method=='POST':

        #checking the entered username is avalilable or not
        user_name = request.POST.get('user_name')
        existed_user=register_doctor.objects.filter(user_name=user_name).first()

        #if entered username is not available
        if existed_user is not None:
            messages.warning(request,user_name+' user name is not available ! please try another ')
            return render(request,'register.html')

        #checking the password and confirm password are same
        password=request.POST.get('password')
        password2=request.POST.get('password2')

        if password !=password2:
            messages.warning(request,'passwords are not matching')
            return render(request,'register.html')


        form=doctors(request.POST,request.FILES)
        print(request.POST,request.FILES)
        if form.is_valid():
                form.save()
                messages.success(request,'registered successfully')
                return render(request, 'signin.html')
        else:
                messages.warning(request,'error occur')


    return render(request,'register.html')


def signin(request):
    if request.method=='POST':
        #cheking the user have account or not
        username=request.POST.get('user_name')
        password=request.POST.get('password')
        auth=register_doctor.objects.filter(user_name=username,password=password).first()

        #authenticating the user

        if auth is not None:
            message=username+' logged in successfully'
            messages.success(request,message)
            return render(request,'dashboard.html',{'context':auth})
        else:
            message = username + ' enter details correctly !'
            messages.warning(request,message)
            return render(request,'signin.html')

    return render(request,'signin.html')


