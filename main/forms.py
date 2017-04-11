from django import forms

from .models import User

class UpdateProfile(forms.ModelForm):

    class Meta:
        model = User
        fields = ('email', 'is_active', 'is_admin', 'firstName', 'lastName')