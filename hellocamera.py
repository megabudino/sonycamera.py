import sonycamera

#will take a photo if flash is off
#check sony documentation for API syntax
endpoint = sonycamera.connect()

endpoint = endpoint + '/camera'
request = {"method" : "getFlashMode", "params" : [], "id" : 1, "version" : "1.0"}

if sonycamera.request(endpoint, request) == 'off':
    sonycamera.request(endpoint)
else:
    print('Flash is on')
