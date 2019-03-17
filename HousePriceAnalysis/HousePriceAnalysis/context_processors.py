import requests
import json

def getuserip(request):
    ip = request.META['REMOTE_ADDR']
    url = "http://whois.pconline.com.cn/ipJson.jsp?ip=%s&json=true" % ip
    a = requests.get(url=url)
    info = json.loads(a.text)
    result = '苏州'
    try:
        if info["city"] != '':
            result = info["city"].split('市')[0]
    except:
        pass
    return {'location': result}