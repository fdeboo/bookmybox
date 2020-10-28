from django.shortcuts import render, get_object_or_404
from .models import Event

def all_events(request):
    """ A view to sholl all events, including sorting and search queries """
    template = 'events/events.html'
    events = Event.objects.all()
    context = {
        "events": events,
    }
    
    return render(request, template, context)

def event_detail(request, event_id):
    """ A view to show individual event details """
    event = get_object_or_404(Event, pk=event_id)

    template = 'events/event-detail.html'
    context = {
        "event": event,
    }

    return render(request, template, context)