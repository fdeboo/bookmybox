from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.db.models import Q
from .models import Event, Category


def all_events(request):
    """ A view to show all events, including sorting and search queries """
    template = "events/events.html"
    events = Event.objects.all()
    query = None
    categories = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            events = events.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)
        if "q" in request.GET:
            query = request.GET["q"]
            if not query:
                messages.error(
                    request, "You didn't enter any search criteria!"
                )
                return redirect(reverse("events"))

            queries = Q(name__icontains=query) | Q(
                description__icontains=query
                )
            events = events.filter(queries)
    context = {
        "events": events,
        "search_term": query,
        "current_categories": categories,
    }

    return render(request, template, context)


def event_detail(request, event_id):
    """ A view to show individual event details """
    event = get_object_or_404(Event, pk=event_id)

    template = "events/event_detail.html"
    context = {
        "event": event,
    }

    return render(request, template, context)
