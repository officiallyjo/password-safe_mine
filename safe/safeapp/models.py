from django.db import models

# Create your models here.
class PasswordModel(models.Model):
    METHOD =(
        ('faceboook','facebook'),
        ('instagram','instagram'),
        ('google','google'),
        ('email','email'),
        ('github','github'),
    )
    site_name=models.CharField(max_length=200 , null = True)
    url_site = models.URLField(max_length=500 , null=True)
    signup_method =models.CharField(max_length=200,null=True,choices=METHOD)
    email = models.CharField(max_length=200, null = True)
    username =models.CharField(max_length=200, null = True)
    password =models.CharField(max_length=200, null = True)

    def __str__(self):
        return self.site_name