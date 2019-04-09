# sonycamera.py
Small library to use sony cameras api with python 3
## Dependencies
To run this library you'll need requests
## Functions
### connect()
It lets you find the partial endpoint of the camera
### request(endpoint, request)
It lets you make a request to the camera.
Note that request is a python dictionary object and it must follow the syntax specified in sony's documentation.
## Example
```
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
```
