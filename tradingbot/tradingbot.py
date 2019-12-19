import time
import hmac
import hashlib
import requests
import json

def check_depositaddr(config):
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
   
def clear_orders_prev(config):
   apifunc = '/market/getopenorders'
   apikey = config['apikey']
   apisecret = config['apisecret']
   market = config['maincoin'] + '-' + config['currency']
   nonce =  str(int(time.time()))
   path =   '/api/v1' + apifunc + '?apikey=' +  apikey + '&nonce=' + nonce + '&market=' + market
   uri = 'https://shorelinecrypto.com' + path
   signature = hmac.new(apisecret, msg=uri, digestmod=hashlib.sha512).hexdigest()
   
   # print(uri)
   # print(signature)
   datadict = {'host': 'shorelinecrypto.com',
            'path': path
            }

   headerdict = {'apisign':  signature}

   request = requests.get(
      url=uri, data=datadict, headers = headerdict)

   
   out_dict = json.loads(request.text)
   # print(out_dict)
   for myorder in out_dict['result']:
      if float(myorder['Price']) == config['price']:
           cancel_order(config, myorder['OrderUuid'])
   
           
def clear_orders_all(config):
   apifunc = '/market/getopenorders'
   apikey = config['apikey']
   apisecret = config['apisecret']
   market = config['maincoin'] + '-' + config['currency']
   nonce =  str(int(time.time()))
   path =   '/api/v1' + apifunc + '?apikey=' +  apikey + '&nonce=' + nonce + '&market=' + market
   uri = 'https://shorelinecrypto.com' + path
   signature = hmac.new(apisecret, msg=uri, digestmod=hashlib.sha512).hexdigest()
   
   # print(uri)
   # print(signature)
   datadict = {'host': 'shorelinecrypto.com',
            'path': path
            }

   headerdict = {'apisign':  signature}

   request = requests.get(
      url=uri, data=datadict, headers = headerdict)

   
   out_dict = json.loads(request.text)
   # print(out_dict)
   for myorder in out_dict['result']:
      cancel_order(config, myorder['OrderUuid'])

def cancel_order(config, uuid):
   apifunc = '/market/cancel'
   apikey = config['apikey']
   apisecret = config['apisecret']
   nonce =  str(int(time.time()))
   path =   '/api/v1' + apifunc + '?apikey=' +  apikey + '&nonce=' + nonce + '&uuid=' + uuid
   uri = 'https://shorelinecrypto.com' + path
   
   signature = hmac.new(apisecret, msg=uri, digestmod=hashlib.sha512).hexdigest()
   datadict = {'host': 'shorelinecrypto.com',
            'path': path
            }

   headerdict = {'apisign':  signature}

   request = requests.get(
      url=uri, data=datadict, headers = headerdict)

   print(request.text)

   
def place_trade(config):
   clear_orders_all(config)
   if (config['strategy'] == 'sellonly'):
      apifunc = '/market/selllimit'
   else:
      assert False, "Fatal, only sellonly supported"
   currency = config['currency']
   apikey = config['apikey']
   apisecret = config['apisecret']
   market = config['maincoin'] + '-' + config['currency']
   quantity = str(config['amount'])
   rate = str(config['price'])

   nonce =  str(int(time.time()))
   path =   '/api/v1' + apifunc + '?apikey=' +  apikey + '&nonce=' + nonce + '&market=' + market + '&quantity=' + quantity + '&rate=' + rate
   uri = 'https://shorelinecrypto.com' + path
   
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
