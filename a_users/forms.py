from django.forms import ModelForm
from django import forms
from .models import User


class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("image", "info")
        widgets = {
            "image": forms.FileInput(),
            "info": forms.Textarea(attrs={"rows": 3, "placeholder": "Add information"}),
        }
