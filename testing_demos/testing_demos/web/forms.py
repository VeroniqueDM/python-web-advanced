from django import forms
from django.forms import modelform_factory

from testing_demos.web.models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


# Model Form Factory Function

ProfileForm2 = modelform_factory(Profile, fields= '__all__')