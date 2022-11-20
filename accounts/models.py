from django.db import models
from django.contrib.auth.models import AbstractUser
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.hashers import make_password
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings
from orders.models import Order
User = settings.AUTH_USER_MODEL
# Create your models here.
class User(AbstractUser):
    is_userpro = models.BooleanField('userpro', default=False)
    is_userwork = models.BooleanField('userwork', default=False)
    company = models.CharField(max_length=100)
    favorites = models.ManyToManyField(Order, related_name='saved_by', null=True, blank=True)

class UserPro(models.Model):
    company = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(auto_now=False, auto_now_add=False)
    address = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    postcode = models.CharField(max_length=50, blank=False)
    location = models.CharField(max_length=50)
    country = CountryField(blank_label='(select country)')
    number = PhoneNumberField(null=False,blank=False)
    password = models.CharField(max_length=50, default=False)
    
  
    is_email_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.first_name

    # def save(self, *args, **kwargs):
    #     self.password = make_password(self.password)
    #     super(UserPro, self).save(*args, **kwargs)

class UserWork(models.Model):
    company = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    number = PhoneNumberField(null=False,blank=False)
    password = models.CharField(max_length=50, default=False)
    
    is_email_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.first_name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='user.jpg', upload_to='user_pics')

    def __str__(self):
        return self.user.username
    
    
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
      instance.profile.save()
        
    

