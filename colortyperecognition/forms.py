from django import forms

from .models import HairColor

class UploadFileForm(forms.Form):
  file = forms.FileField()