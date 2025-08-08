from django import forms
from django.utils import timezone
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'priority', 'is_completed']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter task title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Enter task description'}),
            'due_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'priority': forms.Select(attrs={'class': 'form-select'}),
            'is_completed': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        due_date = cleaned_data.get('due_date')
        if due_date and due_date < timezone.now().date():
            raise forms.ValidationError('Due date cannot be in the past.')
        return cleaned_data