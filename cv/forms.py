from django import forms
from cv.models import Education, Experience, Skill, Project

class EducationForm(forms.ModelForm):
    
    class Meta:
        model = Education
        fields = ('institute', 'education_type', 'start_date', 'finish_date', 'course')
        
class ExperienceForm(forms.ModelForm):

    class Meta:
        model = Experience
        fields = ('company', 'job_title', 'start_date', 'finish_date')

class SkillForm(forms.ModelForm):

    class Meta:
        model = Skill
        fields = ('content', 'years_experience')

class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = ('title', 'content')
