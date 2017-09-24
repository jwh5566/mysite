
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render
import datetime
from mysite.forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings


def hello(request):
    return HttpResponse("Hello world!")


def current_datetime(request):
    now = datetime.datetime.now()
    # html = "<html><body>It is now %s.</body></html>" % now
    # t = get_template('current_datetime.html')
    # html = t.render(Context({'current_date': now}))
    # return HttpResponse(html)
    return render(request, 'current_datetime.html', {'current_date': now})


def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    # html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    # return HttpResponse(html)
    return render(request, 'hours_ahead.html', {'hour_offset': offset, 'next_time': dt})


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                cd['message'],
                settings.EMAIL_HOST_USER,
                [cd.get('email', 'noreply@example.com'),]
            )
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm(
            initial={'subject':  'I love your site!'}
        )
    return render(request, 'contact_form.html', {'form': form})


def thanks(request):
    return HttpResponse('Thanks for your comment.')