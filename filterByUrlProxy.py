from twisted.web import proxy, http
from twisted.internet import reactor
from twisted.python import log
import urlparse
from urllib import quote as urlquote

from twisted.internet.protocol import ClientFactory
from twisted.web.resource import Resource
from twisted.web.server import NOT_DONE_YET
from twisted.web.http import HTTPClient, Request, HTTPChannel

import sys

log.startLogging(sys.stdout)

# I am stamping on the existing proxy
proxy.ProxyRequest = modifiedProxyRequest

class ProxyFactory(http.HTTPFactory):
   protocol = proxy.Proxy

reactor.listenTCP(8080, ProxyFactory())
reactor.run()
