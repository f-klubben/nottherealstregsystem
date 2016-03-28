from django.http import HttpResponse
from django.template import RequestContext
from django.template.loader import get_template
from catalog.models import *

def index(request):
    template = get_template('stregsystem/index.html')
    listings = Listing.objects.all()
    variables = RequestContext(request, {
        'head_title': 'Stregsystem',
        'products': listings,
    })
    output = template.render(variables)
    return HttpResponse(output)

def sale(request):
    template = get_template('stregsystem/index.html')
    listings = Listing.objects.all()
    variables = RequestContext(request, {
        'head_title': 'Stregsystem',
        'products': listings,
        'bought': 'You just bought 1000L milk'
    })
    output = template.render(variables)
    return HttpResponse(output)

def userinfo(request):
    return HttpResponse("Not implemented yet.")
