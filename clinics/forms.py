from django import forms
from .models import  Clinic
from django.contrib.auth.models import User





class Add_Clinic(forms.ModelForm):
    class Meta:
        model = Clinic
        fields = '__all__'
        exclude = ('admin','slug',)