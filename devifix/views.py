from django.shortcuts import render, redirect
from orders.models import Order
from django.contrib.auth.decorators import login_required
from accounts.forms import ProfileForm
from django.contrib import messages
from django.db.models import Q
def home(request):
    return render(request, "landing-page.html")

@login_required(login_url="accounts:login-userpro")
def userpro_welcome(request):
   
        if request.user.is_userpro:
            profile_form = ProfileForm(request.POST,request.FILES, instance=request.user.profile)
            if profile_form.is_valid():
                profile_form.save()
                messages.success(request, ('Your profile was successfully updated'))
                return render(request, "welcome/userpro-welcome.html", {'profile_form': profile_form})
        

    
        else:
            profile_form = ProfileForm(instance=request.user.profile)
            return redirect("accounts:login-userpro")
        
    
    


@login_required(login_url="accounts:login-userwork")
def userwork_welcome(request):

        if request.user.is_userwork:
            profile_form = ProfileForm(request.POST,request.FILES, instance=request.user.profile)
            if profile_form.is_valid():
                profile_form.save()
                messages.success(request, ('Your profile was successfully updated'))
                
                return render(request, "welcome/userwork-welcome.html", {'profile_form': profile_form})
            
        else:
            profile_form = ProfileForm(instance=request.user.profile)
            return redirect("accounts:login-userwork")
        
   
# Search

def search_post(request):

  
    search_post = request.GET.get('search')
    if search_post:
        offers = Order.objects.filter(Q(user__username__icontains=search_post)| Q(user__company__icontains=search_post))
    else:
        offers = Order.objects.all().order_by("-date_posted")
    return render(request, 'search/search.html', {'offers': offers})

#Cockpit

def cockpit(request):
    if request.user.is_authenticated:
        offers = Order.objects.all()
        return render(request, "cockpit/cockpit.html", {'offers': offers})
    else:
        return redirect("accounts:login-userpro")