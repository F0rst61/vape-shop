import os
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ContactForm


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            # send email
            send_mail(
                subject,
                message,
                email,
                [os.environ.get('EMAIL_HOST_USER')],
                fail_silently=False,
            )
            form.save()
            request.session['contact'] = form.cleaned_data
            return redirect(reverse('contact:contact_success'))

    else:
        form = ContactForm(user=request.user)
    return render(request, 'contact/contact.html', {'form': form})


def contact_success(request):
    return render(request, 'contact/contact_success.html',
                  {'contact': request.session['contact'],
                   'user': request.user})
