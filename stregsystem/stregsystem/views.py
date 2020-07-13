from django.http import HttpResponse
from django.template import RequestContext
from django.template.loader import get_template
from django.shortcuts import *
from catalog.models import *

def index(request):
    args = {
        'head_title': 'Stregsystem',
        'products': Listing.objects.all()
    }
    return render(request, 'stregsystem/index.html', args)

def quick(request):
		print(request.POST['quickbuy'])
		return HttpResponse("Not implemented yet.")
    
def sale(request):
		args = {
			'head_title': 'Stregsystem',
			'products': Listing.objects.all(),
			'bought': 'You just bought 1000L milk.'
		}
		return render(request, 'stregsystem/index.html',args)

def usermenu(request):
    return HttpResponse("Not implemented yet.")
