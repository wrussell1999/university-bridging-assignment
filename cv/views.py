from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from cv.models import Education, Experience, Skill, Project
from cv.forms import EducationForm, ExperienceForm, SkillForm, ProjectForm

def cv_page(request):
    educations = Education.objects.all()
    experiences = Experience.objects.all()
    skills = Skill.objects.all()
    projects = Project.objects.all()
    return render(request, 'cv/cv.html', {'educations': educations, 'experiences': experiences, 'skills': skills, 'projects': projects})

@login_required
def new_education(request):
    if request.method == "POST":
        form = EducationForm(request.POST)
        if form.is_valid():
            education = form.save(commit=False)
            education.save()
            return redirect('/cv/', pk=education.pk)
    else:
        form = EducationForm()
    return render(request, 'cv/new_education.html', {'form': form})

@login_required
def new_experience(request):
    if request.method == "POST":
        form = ExperienceForm(request.POST)
        if form.is_valid():
            experience = form.save(commit=False)
            experience.save()
            return redirect('/cv/', pk=experience.pk)
    else:
        form = ExperienceForm()
    return render(request, 'cv/new_experience.html', {'form': form})

@login_required
def new_skill(request):
    if request.method == "POST":
        form = SkillForm(request.POST)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.save()
            return redirect('/cv/', pk=skill.pk)
    else:
        form = SkillForm()
    return render(request, 'cv/new_skill.html', {'form': form})

@login_required
def new_project(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.save()
            return redirect('/cv/', pk=project.pk)
    else:
        form = ProjectForm()
    return render(request, 'cv/new_project.html', {'form': form})

@login_required
def remove_education(request, pk):
    education = get_object_or_404(Education, pk=pk)
    education.delete()
    return redirect('/cv/')

@login_required
def remove_experience(request, pk):
    experience = get_object_or_404(Experience, pk=pk)
    experience.delete()
    return redirect('/cv/')

@login_required
def remove_skill(request, pk):
    skill = get_object_or_404(Skill, pk=pk)
    skill.delete()
    return redirect('/cv/')

@login_required
def remove_project(request, pk):
    project = get_object_or_404(Project, pk=pk)
    project.delete()
    return redirect('/cv/')
