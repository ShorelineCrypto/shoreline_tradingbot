import time
import hmac
import hashlib
import requests

def place_trade(config):
   apifunc = '/account/getdepositaddress'
   currency = config['currency']
   apikey = config['apikey']
   apisecret = config['apisecret']
   
   nonce =  str(int(time.time()))
   uri = 'https://shorelinecrypto.com/api/v1' + apifunc + '?apikey=' +  apikey + '&nonce=' + nonce + '&currency=' +  currency
   path =   '/api/v1' + apifunc + '?apikey=' +  apikey + '&nonce=' + nonce + '&currency=' +  currency
   
   signature = hmac.new(apisecret, msg=uri, digestmod=hashlib.sha512).hexdigest()
   
   print(uri)
   print(signature)
   datadict = {'host': 'shorelinecrypto.com',
            'path': path
            }

   headerdict = {'apisign':  signature}

   request = requests.get(
      url=uri, data=datadict, headers = headerdict)

   print(request.text)
