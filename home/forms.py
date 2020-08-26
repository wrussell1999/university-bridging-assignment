from django import forms

from .models import Bio

class BioForm(forms.ModelForm):

    class Meta:
        model = Bio
        fields = ('text')