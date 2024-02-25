from django import forms
from .models import uploaded_file

class uploaded_file_form(forms.ModelForm):
    class Meta:
        model=uploaded_file
        fields = ["file"]

    def clean_file(self):
        file = self.cleaned_data['file']
        file_name = file.name
        file_extension = file_name.split('.')[-1]
        self.cleaned_data['file_name'] = file_name
        self.cleaned_data['file_extension'] = file_extension
        return file