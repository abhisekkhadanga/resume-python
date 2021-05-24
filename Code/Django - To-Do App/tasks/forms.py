from django import forms
from .models import Task

class Taskform(forms.ModelForm):
    title= forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Add new task...'}))

    class Meta:
        model = Task
        fields = '__all__'