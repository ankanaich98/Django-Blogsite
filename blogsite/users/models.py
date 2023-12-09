from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from .enums import UserRoles


# Create your models here.

class ProfileModel(models.Model):
    user =models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='profile', validators=[FileExtensionValidator(['png','jpg'])])
    role = models.CharField(max_length=20, choices=[(role.name, role.value) for role in UserRoles],default= UserRoles.USER.name)

    def __str__(self):
        return self.user.username

    # def __str__(self):
    #     return f"{self.user.username} - {self.role}"
