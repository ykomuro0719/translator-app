from django import forms
from .models import FileModel

class UploadFileForm(forms.ModelForm):
    src_file = forms.FileField()
    class Meta:
        model = FileModel
        fields = ['src_file','dst_file']

