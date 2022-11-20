from django.db import models
from django.conf import settings
User = settings.AUTH_USER_MODEL
from django.utils import timezone
from django.urls import reverse
# Create your models here.

class Order(models.Model):
    user = models.ForeignKey(User,  on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    budget = models.IntegerField()
    date_posted = models.DateTimeField(default=timezone.now)
    image = models.ImageField(default='default.jpg', upload_to='order_pics')
    open = models.BooleanField(default=True)
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("orders:userpro-orders", kwargs={"username": self.user.username})
    