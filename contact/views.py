from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail, BadHeaderError
from .forms import ContactForm

def contactSubmit(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            trueFrom = 'daniel.g.carter.11@gmail.com'
            fullMessage = 'You have recieved a message from: ' + from_email + '\n\n' + 'subject: ' + subject + '\n\n' + message
            try:
                send_mail(subject, fullMessage, trueFrom, [trueFrom])
            except BadHeaderError:
                return HttpResponse('Invalid Header Found.')
            return render(request, "success.html")
    return render(request, 'contactForm.html', {'form': form})

    


    
