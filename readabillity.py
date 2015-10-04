import urllib
import urllib.parse
import urllib.request
import json

READABILITY_API = {
    'token': '68cfe740446c5179fb0db79268cb105c841de080',
    'secret': 'LSnEdrBgXeKk4HLPXWgPVMfSghMw8SJ2'
}

BASE = 'https://www.readability.com/api/content/v1/parser'
def load(url):
    url = urllib.parse.quote(url)
    u = '{0}?url={1}&token={2}'.format(BASE, url, READABILITY_API['token'])
    request = urllib.request.Request(u)
    response = urllib.request.urlopen(request)
    response_data = response.read().decode('utf8')
    data = json.loads(response_data)
    # print(response.url)
    # json_data = response.raw.read() #.decode('utf8')
    # print(json_data)
    # data = json.loads(json_data)
    return data
