from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.urls import reverse
from . import models
from .forms import  Add_Clinic
from django.contrib.auth import authenticate , login
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.http import HttpResponse

def clinic_list(request):
    clinic_list = models.clinic.objects.all()
    context = {'clinics' : clinic_list}
    return render(request,'clinic/Clinics_list.html',context)

def clinic_detail(request,slug):
    clinic_detail = models.clinic.objects.get(slug=slug)
    current_user = request.user
    apply = models.apply()
    if request.method=='POST':

        apply.clinic=clinic_detail
        apply.user=current_user
        apply.name=current_user
        apply.telephone=current_user.profile.telephone
        apply.email=current_user.email
        apply.ssid=current_user.profile.image
        apply.save()
        context = {'clinic_detail':clinic_detail,'user_data':current_user}
        return render(request,'clinic/apply_done.html',context)
        print("done")

    else:
        apply
    context = {'clinic_detail' : clinic_detail, 'apply' : apply,'user_data':current_user}
    return render(request,'clinic/Clinics_detail.html',context)


@login_required()
def clinic_profile(request):
    return render(request,'clinic/Clinic-Profile.html', {})

def add_clinic(request):

    if request.method=="POST":
        form = Add_Clinic(request.POST, request.FILES)
        print("test")
        if form.is_valid():
            form = form.save(commit=False)
            form.admin = request.user
            form.save()
            return redirect(reverse("clinics:clinic_list"))
            print("done")
    else:
        form = Add_Clinic()

    context = {'form':form}
    return render(request,'clinic/add_clinic.html',context)