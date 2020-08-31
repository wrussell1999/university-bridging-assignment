from django.shortcuts import render, get_object_or_404, redirect
from home.models import Bio, Social

def home(request):
    return render(request, 'home/base.html')

def content(request):
    bio = list(Bio.objects.all())[0]
    socials = list(Social.objects.all())[0]
    return render(request, 'home/content.html', {'bio': bio, 'socials': socials})

def bio(request):
    bio = list(Bio.objects.all())[0]
    return render(request, 'home/bio.html', {'bio': bio})
