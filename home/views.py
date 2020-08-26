from django.shortcuts import render, get_object_or_404, redirect
from .models import Bio, Socials

def home(request):
    return render(request, 'home/base.html')

def bio(request):
    bio = list(Bio.objects.all())[0]
    print(bio)
    return render(request, 'home/bio.html', {'bio': bio})

def socials(request):
    socials = Socials()
    return render(request, 'home/socials.html', {'socials': socials})
