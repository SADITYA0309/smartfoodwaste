from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.db import models

class FoodItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    name = models.CharField(max_length=100)
    expiry_date = models.DateField()
    quantity = models.IntegerField()
    image = models.ImageField(upload_to='food_images/', null=True, blank=True)
    alert_sent = models.BooleanField(default=False) 
    

    def __str__(self):
        return self.name
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)

class Item(models.Model):
    name = models.CharField(max_length=255)
    mfd = models.DateField()  # Manufacturing Date
    exp = models.DateField()  # Expiry Date
    purchase_date = models.DateField()

    def __str__(self):
        return self.name
    
class FoodHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=100)
    manufacturing_date = models.DateField()
    expiry_date = models.DateField()
    purchase_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.product_name} - {self.user.username}"
<<<<<<< HEAD

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"Notification for {self.user.username}"
=======
>>>>>>> b3f9822bebec3b90f8b8c02c56acc278ad26fcad
