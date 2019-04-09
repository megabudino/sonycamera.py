import ssdp
import requests
import json
import xml.etree.ElementTree as ET

def connect():
    device = ssdp.discover('urn:schemas-sony-com:service:ScalarWebAPI:1')
    address = None
    if len(device) > 0:
        for x, y in device.items():
            address = x
            config = requests.get(address)
            root = ET.fromstring(config.text)
            #api endpoint path in xml
            endpoint = root[1][8][1][0][1].text
            return endpoint
    else:
        raise RuntimeError('No device found')

def request(endpoint, request = {"method" : "actTakePicture", "params" : [], "id" : 1, "version" : "1.0"}):
    if endpoint != None and "method" in request and "params" in request and "id" in request and "version" in request:
        response = requests.post(endpoint, json.dumps(request))
        if response.status_code == requests.codes.ok:
            rContent = response.json()
            if 'result' in rContent:
                return rContent['result']
            else:
                return rContent['error']
        else:
            raise ValueError('HTTP error: ' + str(response.status_code))
    else:
        raise ValueError('Something is missing in the request')
