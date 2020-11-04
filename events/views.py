from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Event, Category


def all_events(request):
    """ A view to show all events, including sorting and search queries """
    template = "events/events.html"
    events = Event.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                """ Annotates each object in the QuerySet with the provided
                list of query expressions."""
                events = events.annotate(lower_name=Lower('name'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
                events = events.order_by(sortkey)

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

    current_sorting = f'{sort}_{direction}'

    context = {
        "events": events,
        "search_term": query,
        "current_categories": categories,
        "current_sorting": current_sorting,
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
