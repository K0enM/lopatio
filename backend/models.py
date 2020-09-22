from datetime import date
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Nickname(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  nickname = models.CharField(max_length=50)

  def __str__(self):
      return self.nickname
  
class Quote(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  quote = models.CharField(max_length=200)
  date = models.DateField(default=date.today)
  
  def __str__(self):
      return f"{self.user.first_name}: \"{self.quote}\""
  
class LeaderbordPosition(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  position = models.PositiveSmallIntegerField()

  def __str__(self):
      return f"{self.user.first_name}: positie {self.position}"
  