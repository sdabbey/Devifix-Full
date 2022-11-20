from django.shortcuts import render, redirect
from django.contrib import messages
from .models import UserPro, UserWork, User
from .forms import UserProForm, UserWorkForm, SetPasswordForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.http import HttpResponse

from django.core.mail import send_mail
import math, random
from django.conf import settings


#UserPro
def create_user_pro(request):
    if request.method == "POST":
        check1 = False
        check2 = False
        
        form = UserProForm(request.POST)
    
        company = request.POST.get('company')
        username = request.POST.get('first_name')
        date_of_birth = request.POST.get('date_of_birth')
        address = request.POST.get('address')
        email = request.POST.get('email')
        postcode = request.POST.get('postcode')
        location = request.POST.get('location')
        country = request.POST.get('country')
        number = request.POST.get('number')
       
        
      
       
        if UserPro.objects.filter(first_name=username).exists():
            check1 = True
            messages.error(request, 'Username already exists',
                        extra_tags='alert alert-warning alert-dismissible fade show')
        if UserPro.objects.filter(email=email).exists():
            check2 = True
            messages.error(request, 'Email already registered',
                        extra_tags='alert alert-warning alert-dismissible fade show')

        if check1 or check2:
            messages.error(
                request, "Registration Failed", extra_tags='alert alert-warning alert-dismissible fade show')
            return redirect('accounts:register-userpro')

        else:

            userpro = UserPro.objects.create(
                company=company, first_name=username, date_of_birth=date_of_birth, address=address, email=email, postcode=postcode, location=location, country=country, number=number, password="me")
            user = User.objects.create_user(username=username, email=email, password="", company=company, is_userpro=True)
            
            if user is not None:
                login(request, user)
            messages.success(
                request, f'Thanks for registering {userpro.first_name}!', extra_tags='alert alert-success alert-dismissible fade show')
            return redirect("accounts:userpro-register-password")
    else:
        form = UserProForm()
    return render(request, 'accounts/userpro_register.html', {'form': form})

def login_user_pro(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
       
        user = authenticate(username=username, password=password)
        
        if user is not None:
            if user.is_userpro:    
                login(request, user)
                return redirect('userpro-welcome')
            else:
                 messages.error(request, "User is not a userpro. Enter a username registered to UserPro",
                           extra_tags='alert alert-warning alert-dismissible fade show')
        else:
            
            messages.error(request, "Username Or Password is incorrect!!",
                           extra_tags='alert alert-warning alert-dismissible fade show')

    return render(request, "accounts/userpro_login.html")

def logout_user(request):
    logout(request)
    return redirect('homepage')

def get_userpro_password_set_page(request):
    
    user = request.user
    if request.method == 'POST':
        form = SetPasswordForm(user, request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your password has been changed")
            return redirect('accounts:login-userpro')
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)

    form = SetPasswordForm(user)
    return render(request, 'accounts/userpro-register-password.html', {'form': form})

#UserWork

def create_user_work(request):
    if request.method == "POST":
        check1 = False
        check2 = False
        
        form = UserWorkForm(request.POST)
    
        company = request.POST.get('company')
        username = request.POST.get('first_name')
        email = request.POST.get('email')
        number = request.POST.get('number')
       
        
      
       
        if UserWork.objects.filter(first_name=username).exists():
            check1 = True
            messages.error(request, 'Username already exists',
                        extra_tags='alert alert-warning alert-dismissible fade show')
        if UserWork.objects.filter(email=email).exists():
            check2 = True
            messages.error(request, 'Email already registered',
                        extra_tags='alert alert-warning alert-dismissible fade show')

        if check1 or check2:
            messages.error(
                request, "Registration Failed", extra_tags='alert alert-warning alert-dismissible fade show')
            return redirect('accounts:register-userwork')

        else:

            userwork = UserWork.objects.create(
                company=company, first_name=username, email=email, number=number, password="me")
            user = User.objects.create_user(username=username, email=email, password="", company=company, is_userwork=True)
            email = userwork.email
            if user is not None:
                login(request, user)
            messages.success(
                request, f'Thanks for registering {userwork.first_name}!', extra_tags='alert alert-success alert-dismissible fade show')
            return redirect("accounts:userwork-register-password")
    else:
        form = UserWorkForm()
    return render(request, 'accounts/userwork_register.html', {'form': form})

def login_user_work(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
      
        user = authenticate(username=username, password=password)
        
        if user is not None:
            if user.is_userwork: 
                login(request, user)   
                return redirect('userwork-welcome')
            else:
                 messages.error(request, "User is not a userwork. Enter a username registered to UserPro",
                           extra_tags='alert alert-warning alert-dismissible fade show')
        else:
            messages.error(request, "Username Or Password is incorrect!!",
                           extra_tags='alert alert-warning alert-dismissible fade show')

    return render(request, "accounts/userwork_login.html")




def get_userwork_password_set_page(request):
    user = request.user
    if request.method == 'POST':
        form = SetPasswordForm(user, request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your password has been changed")
            return redirect('accounts:login-userwork')
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)

    form = SetPasswordForm(user)
    return render(request, 'accounts/userwork-register-password.html', {'form': form})



def generateOTP():
    digits = "0123456789"
    OTP = ""
    for i in range(4):
        OTP += digits[math.floor(random.random() * 10)]
    return OTP

def send_otp(request):
    email=request.POST.get("email")
    print(email)
    o=generateOTP()
    from_email = settings.EMAIL_HOST_USER
    htmlgen = '<p> Your OTP is <strong></strong></p>'
    send_mail('OTP request', o, from_email, [email], fail_silently=False, html_message=htmlgen)
    return HttpResponse(o)

