from django import forms
from .models import AudioModel

class AudioForm(forms.ModelForm):
    class Meta:
        model = AudioModel
        fields = ['audioname', 'audio']
