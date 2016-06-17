from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from conf.settings import ES
import urllib,urllib2,json

def get(dirs,arg,http='http',host='default'):
    query = http + '://' + ES[host]['HOST'] + dirs + '?' + urllib.urlencode(arg)
    req = urllib2.Request(url=query)
    try:
        content = urllib2.urlopen(req).read()
    except:
        return 'read error, need right url'
    return content

@csrf_exempt
def getUrl(req):
    '''
    example:/geturl/?args={"username":123,"password":123}&dirs=/spider_admin/user/register&host=default
    '''
    q = req.GET or req.POST
    host = q.get('host','default')
    http = q.get('http','http')
    dirs = q.get('dirs','/user/get')
    args = json.loads(q.get('args','{}'))
    return HttpResponse(get(dirs,args,http=http,host=host))