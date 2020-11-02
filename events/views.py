from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.db.models import Q
from django.conf import settings
from datetime import datetime
from .models import Event


def all_events(request):
    """ A view to show all events, including sorting and search queries """
    template = 'events/events.html'
    events = Event.objects.all()

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, "You didn't enter any search criteria!"
                    )
                return redirect(reverse('events'))
    context = {
        "events": events,
    }

    return render(request, template, context)


def event_detail(request, event_id):
    """ A view to show individual event details """
    event = get_object_or_404(Event, pk=event_id)

    template = 'events/event_detail.html'
    context = {
        "event": event,
    }

    return render(request, template, context)
