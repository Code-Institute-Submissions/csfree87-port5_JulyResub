from django.shortcuts import render
from .forms import ContactForm
from django.contrib import messages


def contact_view(request):
    form = ContactForm()
    context = {'form': form}
    messages.success(request, ('Message Sent!'))
    return render(request, 'contact/contact.html', context)
