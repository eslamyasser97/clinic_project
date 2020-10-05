from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.urls import reverse
from .models import clinic
from .forms import ApplyForm , Add_Clinic
from django.contrib.auth import authenticate , login
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.http import HttpResponse

def clinic_list(request):
    clinic_list = clinic.objects.all()
    context = {'clinics' : clinic_list}
    return render(request,'clinic/Clinics_list.html',context)

def clinic_detail(request,slug):
    clinic_detail = clinic.objects.get(slug=slug)
    current_user = request.user

    if request.method=='POST':
        form = ApplyForm(request.POST , request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.clinic = clinic_detail
            form.save()
            print("done")

    else:
        form = ApplyForm()
    context = {'clinic_detail' : clinic_detail, 'form' : form,'user_data':current_user}
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