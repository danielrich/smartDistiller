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

class modifiedProxyRequest(Request):
   """
   Used by Proxy to implement a simple web proxy.
   Code pulled from twisted. MIT license just a temp test
   @ivar reactor: the reactor used to create connections.
   @type reactor: object providing L{twisted.internet.interfaces.IReactorTCP}
   """

   protocols = {'http': proxy.ProxyClientFactory}
   ports = {'http': 80}

   def __init__(self, channel, queued, reactor=reactor):
      Request.__init__(self, channel, queued)
      self.reactor = reactor


   def process(self):
      print ("WHO")
      parsed = urlparse.urlparse(self.uri)
      protocol = parsed[0]
      host = parsed[1]
      port = self.ports[protocol]
      if ':' in host:
         host, port = host.split(':')
         port = int(port)
      rest = urlparse.urlunparse(('', '') + parsed[2:])
      if not rest:
         rest = rest + '/'
      class_ = self.protocols[protocol]
      headers = self.getAllHeaders().copy()
      if 'host' not in headers:
         headers['host'] = host
      self.content.seek(0, 0)
      s = self.content.read()
      clientFactory = class_(self.method, rest, self.clientproto, headers,
      s, self)
      self.reactor.connectTCP(host, port, clientFactory)

# I am stamping on the existing proxy
proxy.ProxyRequest = modifiedProxyRequest

class ProxyFactory(http.HTTPFactory):
   protocol = proxy.Proxy

reactor.listenTCP(8080, ProxyFactory())
reactor.run()
