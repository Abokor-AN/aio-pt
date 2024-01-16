from django.db import models


# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=25)
    password = models.CharField(max_length=50)
    email = models.EmailField()
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    date_of_birth = models.DateField(auto_now=True)
    date_of_joining = models.DateField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    image = models.ImageField(upload_to='profile_pics', default="default_profile.png")

    def __str__(self):
        return self.username
