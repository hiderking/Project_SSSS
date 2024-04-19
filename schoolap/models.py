from django.db import models

# Create your models here.

class ViewerContacts(models.Model):
    id = models.AutoField(primary_key=True)
    fullname=models.CharField(max_length=200)
    email=models.EmailField(max_length=200)
    subject=models.CharField(max_length=200)
    message=models.CharField(max_length=500)
    submitDate=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.fullname


