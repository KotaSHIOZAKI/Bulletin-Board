from django import forms
from .models import Thread

class BoardCreateForm(forms.ModelForm):
    class Meta:
        model = Thread
        fields = ('title', 'content')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'