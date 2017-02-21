import base64
import json
import sys
from urllib.request import Request,urlopen

request = Request("https://api.twitter.com/oauth2/token")
request.add_header('Content-Type','application/x-www-form-urlencoded;charset=UTF-8')
request.add_header('Authorization','Basic %s' % "M2NxR2JlVFZMcEI5cjdzQ3V1dFllUFhoNDpVRFdWNjNkR05UTlNMYkRDZmdHdEJ3Ym5XSGZjTFdWRER1TElmYlFKUFFnTXdnRjRubA==")
request_data = 'grant_type=client_credentials'.encode('ascii')
request.data =request_data
response = urlopen(request)
raw_data = response.read().decode('utf-8')
data = json.loads(raw_data)