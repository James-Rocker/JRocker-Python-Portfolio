import imp
import pip

package = 'urllib'

try:
    imp.find_module(package)
    found = True
except ImportError:
    print ('Error ' + package + ' library is missing ')
    var = input("Do you want to install the " + package + " library? ")
    if var in ['no','n','No','N','NO']:
        print ('Error, '+ package + ' not installed, please install the library before attempting to run this program')
    else:
        pip.main(['install', package])

package = 'json'

try:
    imp.find_module(package)
    found = True
except ImportError:
    print ('Error ' + package + ' library is missing ')
    var = input("Do you want to install the " + package + " library? ")
    if var in ['no','n','No','N','NO']:
        print ('Error, '+ package + ' not installed, please install the library before attempting to run this program')
    else:
        pip.main(['install', package])

import urllib, json
url = "http://maps.googleapis.com/maps/api/geocode/json?address=googleplex&sensor=false"
response = urllib.urlopen("http://maps.googleapis.com/maps/api/geocode/json?address=googleplex&sensor=false")
data = json.loads(response.read())

print (data)
