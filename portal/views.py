from django.shortcuts import render

def portal(request):
    """ A view to ren=turn the index page """
    template = 'portal/portal.html'
    context = {}
    
    return render(request, template, context)