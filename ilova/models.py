from audioop import reverse

from django.db import models
from django.urls import reverse

class Category(models.Model):
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='images/',null=True)

    def __str__(self):
        return self.name

class Region(models.Model):
    name=models.CharField(max_length=100,null=True)
    image=models.ImageField(upload_to='images/',null=True)

    def __str__(self):
        return self.name

# Create your models here.
class News(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.CASCADE,blank=True,null=True)
    title=models.CharField(max_length=300)
    text=models.TextField()
    date=models.DateTimeField(auto_now=True)
    image=models.ImageField(upload_to='images/')
    author=models.ForeignKey('auth.User',on_delete=models.CASCADE)

    def __str__(self):
      return self.title

    def get_absolute_url(self):
        return reverse('detail',args=[str(self.pk)])