"""
This is the config core
"""

import urlparse
from urllib import quote as urlquote

from twisted.internet import reactor
from twisted.internet.protocol import ClientFactory
from twisted.web.resource import Resource
from twisted.web.server import NOT_DONE_YET
from twisted.web.http import HTTPClient, Request, HTTPChannel
import FilterCore

def getWebAddress():
   """
   This should return the web address of the local config server
   so an end user can configure the system
   """

   return "http://localhost"

