from django import forms
from .models import apply , clinic
from django.contrib.auth.models import User


class ApplyForm(forms.ModelForm):
    class Meta:
        model = apply
        fields = ['name','telephone','ssid','email']


class Add_Clinic(forms.ModelForm):
    class Meta:
        model = clinic
        fields = '__all__'
        exclude = ('admin','slug',)