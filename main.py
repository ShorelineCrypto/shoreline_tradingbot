#!/usr/bin/env python2.7
"""
Shoreline TradingBot is simple trading strategy bot that can buy or sell coins listed at ShorelineCrypto Exchange automatically
at fixed price and fixed amount.
"""



################################################################################
# Preamble.
################################################################################

# Python standard library imports.
import argparse
import time
import datetime
import itertools
import platform
import os.path
import re
import sys

# Modules in this package.
import tradingbot.utils as utils


# Safety for cases when shebang is bypassed.
assert sys.version_info[0] == 2 and sys.version_info[1] >= 7, 'Python version 2.7 (or a later 2.x version) required; you have version: {}.{}.{}'.format(
    *sys.version_info[0:3])



################################################################################
# Main Function
################################################################################

class UserInputException(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return repr(self.message)


def main(args):
    """Main execution functions.

    """
    osname = platform.system()
    print "Your Computer Platform is: {}".format(osname)
    if osname == 'Linux':
       tmpFile1 = os.path.join(os.path.expanduser("~"), '.shorelinetradingbot',  args.conf)
       tmpFile2 = os.path.join(os.path.dirname(
           utils.getPathOfThisFile()), 'shorelinetradingbot.conf')
    elif osname == 'Windows':
       tmpFile1 = os.path.join(os.path.expandvars("%userprofile%"), 'AppData\Roaming\shorelinetradingbot',args.conf)
       tmpFile2 = os.path.join(os.path.dirname(
           utils.getPathOfThisFile()), 'shorelinetradingbot.conf')
    elif osname == 'Darwin':
       tmpFile1 = os.path.join(os.path.expanduser("~"), 'Library/Application Support/shorelinetradingbot',  args.conf)
       tmpFile2 = os.path.join(os.path.dirname(
           utils.getPathOfThisFile()), 'shorelinetradingbot.conf')
    else:
        assert False, "Error: unsupported operating system: {}".format(osname)

    print "Your config filepath at user based folder is at: {}".format(tmpFile1)
    
    if utils.isReadable(tmpFile1):
        BotConfigFile = tmpFile1
        print "config found: {}".format(tmpFile1)
    elif utils.isReadable(tmpFile2):
        BotConfigFile = tmpFile2
        print "config found: {}".format(tmpFile2)
    else:
        assert False, "Error in reading shoreline trading bot Config File. Please create config file either at {} or {}".format(tmpFile1,tmpFile2)


    # Loading configuration file
    configFile = open(BotConfigFile, 'rU')
    config = dict([(k, None) for k in ['apikey', 'apisecret', 'strategy','tradingpair', 'price', 'amount']])

    # TODO: Properly Loading config from file
    for line in configFile:
        if line.startswith('#') or re.match(r'^\s+$', line):
            continue
        m1 = re.search(
            r'^apikey=(\S+)\s*$', line, re.M)
        if m1 :
            config['apikey'] = m1.group(1)
        
        m2 = re.search(
            r'^apisecret=(\S+)\s*$', line, re.M)
        if m2:
            config['apisecret'] = m2.group(1)
        
        m3 = re.search(
            r'^strategy=(\S+)\s*$', line, re.M)
        if m3:
            config['strategy'] = m3.group(1)
        
        m4 = re.search(
            r'^tradingpair=(\S+)\s*$', line, re.M)
        if m4 :
            config['tradingpair'] = m4.group(1)
        
        m5 = re.search(
            r'^price=([\d\.]+)\s*$', line, re.M)
        if m5:
            config['price'] = float(m5.group(1))
        
        m6 = re.search(
            r'^amount=([\d.]+)\s*(\S+)\s*$', line, re.M)
        if m6:
            config['amount'] = m6.group(1) +  m6.group(2)
        
    # window will crash on os.fync on read only file
    # a simple close
    configFile.close()

    assert config['apikey'] is not None, "apikey missing in config!"
    assert config['apisecret'] is not None, "rpcpassword missing in config!"
    
    print config
 
    print "Shoreline Trading Bot started!"
 
    while True:
        
        minutes = args.interval * 60
        time.sleep(minutes)


################################################################################
# Command Line executions - Argument Parsing.
################################################################################

if __name__ == '__main__':

    # ===============================================================================
    # Parse and validate command-line args and input config.
    # ===============================================================================

    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument('--interval', type=int, nargs='?', default=5 , 
                        help='minutes to wait between each check on ShorelineCrypto Exchange orderbook, [default: 5]')
    parser.add_argument('--conf', nargs='?', type=str, default="shorelinetradingbot.conf" ,
                        help='Configuration file to be used for trading bot[default: shorelinetradingbot.conf]')
    
    args = parser.parse_args()
    # running main function
    main(args)
    
