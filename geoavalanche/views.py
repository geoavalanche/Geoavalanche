import json

from geoavalanche import settings
from django.core.mail import send_mail
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, render_to_response

GEOAVALANCHE_EMAIL_ADDRESS = settings.GEOAVALANCHE_EMAIL_ADDRESS

def contactus(request):
    errors = []
    if request.method == 'POST':
        if not request.POST.get('contact-name', ''):
            errors.append('Enter a full name.')
        if request.POST.get('contact-email') and '@' not in request.POST['contact-email']:
            errors.append('Enter a valid e-mail address.')
        if not request.POST.get('contact-message', ''):
            errors.append('Enter a message.')
        if not errors:
            send_mail(
                request.POST['contact-name'],
                request.POST['contact-message'],
                request.POST['contact-email'],
                [GEOAVALANCHE_EMAIL_ADDRESS],#email address where message is sent.
            )
            #return HttpResponse(json.dumps({"success":True}), content_type="application/json")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'), {'errors': errors})
            #print request
    # return render(request, 'contact.html',{'errors': errors})
    #return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'), {'errors': errors})
    # return render_to_response(request, 'contactus.html',{'errors': errors})


#def thanks(request):
    #return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
#    return render(request, 'index.html')
