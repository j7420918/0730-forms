from django.db import models

class Sampleapp(models.Model):
    title=models.CharField(max_length=300)
    pub_date=models.DateTimeField('date published')
    body=models.TextField()
    image= models.ImageField()


class Profile(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    
    def __str__(self):
        return self.title

# Create your models here.
