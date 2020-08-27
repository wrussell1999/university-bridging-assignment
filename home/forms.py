from django import forms

from .models import Bio, Social

class BioForm(forms.ModelForm):

    class Meta:
        model = Bio
        fields = ('title', 'text')

class SocialForm(forms.ModelForm):
    
    class Meta:
        model = Social
        fields = ('github', 'twitter', 'linkedin', 'email')
