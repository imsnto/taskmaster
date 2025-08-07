from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms

User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User 
        fields = ('username', 'password1', 'password2')
        help_texts = {
            'username': '',
            'password2': '',
            'password2': ''
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'form-contrl', 'plcaeholder': field.label
            })