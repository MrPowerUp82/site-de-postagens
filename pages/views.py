from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views.generic import TemplateView
from posts.models import Publica
from allauth.socialaccount.models import SocialAccount
import os
from django.http import HttpResponseRedirect
#class HomePageView(TemplateView):
 #   template_name="home.html"

# Create your views here.


def home(request):
    posts=Publica.objects.all()
    user=request.user
    return render(request,'home.html',{'posts':posts,
    'users':user,
    })

def post(request):
    if request.user.is_authenticated:
        return render(request,"create_post.html")
    else:
        return render(request,'user_not.html')



def create_post(request):
    if request.user.is_authenticated:
        try:
            content=request.POST.get('content')
            title=request.POST.get('title')
            image=request.FILES['image']
            user=request.user
            imageup=Publica.objects.create(image=image, author=user, content=content,title=title)
            posts=Publica.objects.all()
            return HttpResponseRedirect("/")
        except:
            return render(request,'error.html')
    else:
        return render(request,'user_not.html')



