"""
This is the filter core

"""

import urlparse
from urllib import quote as urlquote

from twisted.internet import reactor
from twisted.internet.protocol import ClientFactory
from twisted.web.resource import Resource
from twisted.web.server import NOT_DONE_YET
from twisted.web.http import HTTPClient, Request, HTTPChannel
import ConfigCore

whiteList = {"www.google.com":"partial test further"}

def failFiltering(uriToTest):
   parser = urlparse.urlparse(uriToTest)
   print ("here I am")
   print (uriToTest)
   if parser.netloc in whiteList :
      print ("Yes we passed")
      return False
   print ("no we failed")
   return True
