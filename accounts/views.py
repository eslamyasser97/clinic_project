from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import SignupForm , UserForm , ProfileForm
from .models import Profile
from django.urls import reverse

# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username,password=password)
            login(request,user)
            print('done')
            return redirect('/accounts/profile')
    else:
        form = SignupForm()
    context={'form':form}
    return render(request,'registration/signup.html',context)

@login_required()
def profile(request):
    prof = Profile.objects.get(user=request.user)
    context = {'profile':prof}
    return render(request,'accounts/profile.html',context)


@login_required()
def edit_profile(request):
    profile = Profile.objects.get(user=request.user)

    if request.method == 'POST':
        userform = UserForm(request.POST,instance=request.user)
        profileform = ProfileForm(request.POST,request.FILES,instance=profile,)
        print('done1')
        if userform.is_valid() and profileform.is_valid():
            userform.save()
            myprofile = profileform.save(commit=False)
            myprofile.user = request.user
            myprofile.save()
            return redirect(reverse("accounts:profile"))
            print('done2')
    else:
        userform = UserForm(instance=request.user)
        profileform = ProfileForm(instance=profile)
    context = {'userform':userform,'profileform':profileform}
    return render(request, 'accounts/profile_edit.html', context)
