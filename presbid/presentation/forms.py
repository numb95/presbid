from django import forms
from presbid.presentation.models import Presentation, Comment

class AddPresentation(forms.ModelForm):
    class Meta:
        model = Presentation
        fields = ['title', 'description']