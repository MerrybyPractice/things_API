from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class thing(models.Model): 
  title = models.CharField(max_length=256) 
  belongs_to = models.ForeignKey(User, on_delete=models.CASCADE) 

  def __str__(self): 
    return self.titie, self.belongs_to