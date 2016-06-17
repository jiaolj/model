from conf.settings import HTTP
import urllib,urllib2

def es_get(arg,host='default'):
    query = HTTP[host]['HOST'] + HTTP[host]['path'] + '?' + urllib.urlencode(arg)
    req = urllib2.Request(url=query)
    try:
        content = urllib2.urlopen(req).read()
    except:
        return 'read error, need right url'
    return content
