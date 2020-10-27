from django.shortcuts import render
from events.models import Event, Category

def portal(request):
    """ A view to sholl all products, including sorting and search queries """
    template = 'portal/portal.html'
    events = Event.objects.all()
    context = {
        "events": events,
    }
    
    return render(request, template, context)