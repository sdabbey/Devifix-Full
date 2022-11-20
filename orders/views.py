from .models import Order
from django.conf import settings
from django.shortcuts import render, get_object_or_404, redirect
# User = settings.AUTH_USER_MODEL
from django import forms
from django.contrib import messages
import datetime
from accounts.models import User
from django.urls import reverse
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# Create your views here.

# class OrderListView(ListView):
#     model = Order
#     template_name = "orders/userpro-orders.html"
#     context_object_name = 'orders'
#     ordering: ['-date_posted']
#     paginate_by = 5

class OrderCreateView(LoginRequiredMixin, CreateView):
    model = Order
    fields = ['title', 'description', 'budget', 'date_posted', 'image']
    template_name = "orders/userpro-create-offer.html"
   
    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()
        
        form = super(OrderCreateView, self).get_form(form_class)
        form.fields['title'].widget = forms.TextInput(attrs={'placeholder': 'Title'})
        form.fields['description'].widget = forms.Textarea(attrs={'placeholder': 'Description'})
        form.fields['budget'].widget = forms.NumberInput(attrs={'placeholder': 'Budget'})        
        form.fields['image'].widget = forms.FileInput(attrs={'placeholder': 'Budget', 'class': 'custom-file-input', 'id': "inputFile"})        
        
        return form

    def form_valid(self, form):
        form.instance.user = self.request.user
    
       
        return super().form_valid(form)

class UserProOrderListView(ListView):
    model = Order
    template_name = "orders/userpro-orders.html"
    context_object_name = 'orders'
   
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Order.objects.filter(user=user).order_by('-date_posted')

class UserProOrderUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Order
    fields = ['title', 'description', 'budget', 'date_posted', 'image']
    template_name = "orders/userpro-update-offer.html"
    
    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()

        form = super(UserProOrderUpdateView, self).get_form(form_class)
        form.fields['title'].widget = forms.TextInput(attrs={'placeholder': 'Title'})
        form.fields['description'].widget = forms.Textarea(attrs={'placeholder': 'Description'})
        form.fields['budget'].widget = forms.NumberInput(attrs={'placeholder': 'Budget'})        
        form.fields['image'].widget = forms.FileInput(attrs={'placeholder': 'Budget', 'class': 'custom-file-input', 'id': "inputFile"})        
        return form
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        order = self.get_object()
        if self.request.user == order.user:
            return True
        return False

class UserProOrderDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Order
    template_name = "orders/userpro-order-confirm-delete.html"


    def test_func(self):
        order = self.get_object()
        if self.request.user == order.user:
            return True
        return False
    
    def get_success_url(self):
        return reverse("orders:userpro-orders", kwargs={"username": self.request.user})
    def form_valid(self, form, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()
        form = super(UserProOrderDeleteView, self).get_form(form_class)
        form.instance = self.request.user
        return super().form_valid(form)

 
def favorite_orders(request, pk):
    if request.method == 'POST':
        favorite = Order.objects.get(pk=pk)
        user = request.user
        user.favorites.add(favorite)
        messages.add_message(request, messages.INFO, 'Deal Favorited.')
        return redirect('homepage')



