from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from common.models.http import es_get

@csrf_exempt
def get(req):
    q = req.GET or req.POST
    return HttpResponse(es_get(q))

@csrf_exempt
def test(req):
    q = req.GET or req.POST
    host = 'test'
    return HttpResponse(es_get(q,host=host))