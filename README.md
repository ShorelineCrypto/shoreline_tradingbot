# shoreline_tradingbot


## What is Shoreline TradingBot?

Shoreline TradingBot is open sourced project that offers simple trading strategy for cryptocurrency listed at
ShorelineCrypto Exchange.  The current trading strategies available are "buysell", "buyonly", "sellonly" on fixed price and fixed
amount. 

By default setting, the tradingbot will automatically cancell orders and re-initiate bot orders in every 5 minutes. 

ShorelineCrypto API interface will be used in this python code. 

### NewEnglandcoin (NENG) Fully Tested

While the tradingbot is expected to work on all coins listed at ShorelineCrypto exchange, only NewEnglandcoin (NENG) on NENG/DOGE pair and Marinecoin (MTC) on MTC/DOGE pair were fully tested by dev on all three strategies. 

## Windows 10

### How to Install shoreline_tradingbot?

 - Download v2.7.x version of windows python from https://www.python.org/downloads/windows/ and install it.
 - Open a window command prompt terminal, run below command to install the requests module 

```
     set PATH=C:\Python27;C:\Python27\Scripts;%PATH%
     pip install requests
```

## MacOS or Linux - How to Install

python 2.7 typically is default at MacOs or Linux. Install requests if it is missing:

```
     sudo pip install requests
```


### How to run Shoreline TradingBot in window 10?
  - Download and unpack the releast file in windows 10 using 7-Zip,
  - Copy and rename one of example file into a file name "shorelinetradingbot.conf".
  - Inside ShorelineCrypto account designated for trading bot use, click "Add key" to create api key. Click enable "Read info", "Trade limit", copy and paste the api key and secret
   word into file "shorelinetradingbot.conf".
  - modify the strategy and proper price and amount
  - "double click the file "bot.bat"

### How to run Shoreline TradingBot in MacOs or Linux?
  - Download release zip file, and unpack it,
  - Copy and rename one of example file into a file name "shorelinetradingbot.conf".
  - Inside ShorelineCrypto account designated for trading bot use, click "Add key" to create api key. Click enable "Read info", "Trade limit", copy and paste the api key and secret
   word into file "shorelinetradingbot.conf".
  - modify the strategy and proper price and amount
  - run below command in terminal:
```
   python main.py -h
   python main.py
``` 


## buyonly strategy
  - limit buy order at "price" and fixed amount. The amount can be either "DOGE" or the other coin name of the trading pair.
  
## sellonly strategy
  - limit sell order at "price" and fixed amount. The amount can be either "DOGE" or the other coin name of the trading pair.
  
## buysell strategy
  - simultaneously placing buy limit order at "buyprice" and sell limit order at "sellprice" at fixed amount. The amount can be either "DOGE" or the other coin name of the trading pair.


## License


Shoreline_TradingBot is released under the terms of the MIT license. See `COPYING` for more
information or see http://opensource.org/licenses/MIT.


