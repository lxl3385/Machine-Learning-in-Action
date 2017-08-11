#! ~/mainML/
"""  test the Aliyun API server  """
# -*- coding: utf-8 -*-

import urllib
import urllib2
import sys 


host = 'http://jshmgsdmfb.market.alicloudapi.com'
path = '/shouji/query'
method = 'GET'
appcode = 'f1716bb3e5074e08b97f761d2288a492'
querys = 'shouji=13456755448'
bodys = {}
url = host + path + '?' + querys

request = urllib2.Request(url)
request.add_header('Authorization', 'APPCODE ' + appcode)
response = urllib2.urlopen(request)
content = response.read()
if (content):
    print(content)