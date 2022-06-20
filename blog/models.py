from email.policy import default
from django.db import models

# Create your models here.
class post(models.Model):
    Tittle=models.CharField(max_lenght=200)
    Text=models.TextField(max_length=500)
    Author=models.ForeignKey(get_user_model=models.CASCADE)
    created_date=models.DateTimeField(auto_now=False)
    published_date=models.DateTimeField(default)
