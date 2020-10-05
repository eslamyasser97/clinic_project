from django.shortcuts import render

from project.settings import EMAIL_HOST_USER
from .models import Info
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

def send_message(request):
    myinfo = Info.objects.first()

    if request.method == 'POST':
        subject = request.POST['subject']
        email = request.POST['email']
        message = request.POST['message']

        print(subject)
        print(email)
        print(message)
        send_mail(
            subject, # SUBJECT
            message, #message
            email, # from email
            ['eslam.yasser.hassan@gmail.com'], # to email (support mail)
        )
        context = {'myinfo': myinfo,'subject':subject}
        return render(request, 'contact/contact.html', context)
        print(subject)
        print(email)
        print(message)
    else:
        context = {'myinfo':myinfo}
        return render(request,'contact/contact.html',context)