from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User


# Extending User Model Using a One-To-One Link
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default='default.jpg', upload_to='images/users')
    bio = models.TextField("Bio",)

    def __str__(self):
        return self.user.username