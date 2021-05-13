from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField
from allauth.socialaccount.models import SocialAccount
from django.contrib.auth.models import User
from django.db.models.fields.related import ForeignKey
from django.conf import settings
import django.contrib.auth
# Create your models here.


class Publica(models.Model):
    author = models.CharField(max_length=40,null=True,blank=True)
    title= models.CharField(max_length=50)
    #content=RichTextUploadingField()
    content=models.TextField()
    image=models.FileField(null=True,blank=True)



    def __str__(self):
        return self.title

    class Meta:
        ordering=['-id']
