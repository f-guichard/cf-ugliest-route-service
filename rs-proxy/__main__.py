# -*- coding: UTF-8 -*-

from flask import Flask
from flask import jsonify
from flask import request
from flask import make_response
import requests
import os
import json

#Pattern standard pour gerer le dual stack CF/Legacy
if os.getenv("PORT") > 1024:
   cfPort = int(os.getenv("PORT"))
else:
   cfPort = 8080

app = Flask(__name__)

myRSAnswer = '{ "sentence": "too bad" }'
container = os.uname()[1]

#See https://docs.cloudfoundry.org/services/route-services.html
try:
    with open('rs-proxy/sentence_day.json', 'r') as json_response:
        myRSAnswer = json.load(json_response)
except Exception, e:
    print repr(e)

#Cloudfoundry needed routes
@app.route('/')
def index():
    param_XCFFU = request.headers['X-Cf-Forwarded-Url']
    param_XCFPS = request.headers['X-Cf-Proxy-Signature']
    param_XCFPM = request.headers['X-Cf-Proxy-Metadata']
    print("\nRecu du GoRouter : ")
    print("\nX-Cf-Forwarded-Url : %s") % (param_XCFPS)
    print("\nX-Cf-Proxy-Signature : %s") % (param_XCFFU)
    print("\nX-Cf-Proxy-Metadata : %s") % (param_XCFPM)
    forward_headers = {'X-Cf-Proxy-Signature': param_XCFPS, 'X-Cf-Proxy-Metadata': param_XCFPM}
    # On refoward a lappli initiale via lurl contenue dans X-Cf-Forwarded-Url 
    r = requests.get(param_XCFFU, headers=forward_headers)
    print("\nRecu : %s") % (r.text)
    response = make_response("<br>Recu de {} : {} <br> Ajoute par le route-service : {} <br>".format(param_XCFFU, r.text, myRSAnswer))
    response.headers['X-RS-ContainerID'] = container
    response.status_code = 200
    return response

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=cfPort)
