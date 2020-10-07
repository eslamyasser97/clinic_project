from django import forms
from .models import  clinic
from django.contrib.auth.models import User





class Add_Clinic(forms.ModelForm):
    class Meta:
        model = clinic
        fields = '__all__'
        exclude = ('admin','slug',)