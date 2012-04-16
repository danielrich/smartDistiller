import ProxyCore
from twisted.web import http
from twisted.internet import reactor
from twisted.python import log
import urlparse
from urllib import quote as urlquote
import sys

#log.startLogging(sys.stdout)

class ProxyFactory(http.HTTPFactory):
   protocol = ProxyCore.Proxy

reactor.listenTCP(8080, ProxyFactory())
reactor.run()
