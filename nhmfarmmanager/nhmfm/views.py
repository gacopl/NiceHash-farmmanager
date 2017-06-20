from django.http import HttpResponse
from django.template import loader

from .models import NHMHost
from django.http import JsonResponse
import urllib.request, json 


def index(request):
    nhm_hosts = NHMHost.objects.values()
    template = loader.get_template('index.html')
    context = {
        'rigs': nhm_hosts,
    }
    return HttpResponse(template.render(context, request))

def stats(request):
	if request.GET.get('ip'):
		with urllib.request.urlopen("http://" + request.GET['ip'] + ":8888/stats.json") as url:
			data = json.loads(url.read().decode())
	return JsonResponse(data, safe=False)