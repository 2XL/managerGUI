import time
import socket
import random
import wget
import urllib2
import json

class GraphiteClient():
    def __init__(self, host='localhost', portstr='22003', portpickle='22004'):
        self.hostname = host
        self.portstr = portstr
        self.portpickle = portpickle

    def collect_string(self, name, value, timestamp):
        sock = socket.socket()
        sock.connect((self.hostname, self.portstr))
        sock.send("%s %d %d\n" % (name, value, timestamp))

        sock.close()

    def collect_pickle(self, name, value, timestamp):
        sock = socket.socket()
        sock.connect((self.hostname, self.portpickle))
        sock.send("%s %d %d\n" % (name, value, timestamp))
        sock.close()


def tsNow():
    return int(time.time())


def randValue():
    return random.randint(0, 100)


if __name__ == "__main__":

    graphiteUrl = 'ast03'
    graphitePort = 22003
    gc = GraphiteClient(graphiteUrl, graphitePort)

    hostname = 'Joanna'
    test_id = tsNow()
    key = 'random'
    value = None

    ops = 10
    itv = 10


    metric = '{}.{}.{}'.format(hostname, test_id, key)
    print metric
    for x in range(0, ops, 1):
        gc.collect_string(metric, randValue(), tsNow())
        time.sleep(itv)

    url = 'https://{}:8443/render/?target={}&format=json&from=-60second'.format(graphiteUrl, metric)
    req = urllib2.Request(url)
    res = urllib2.urlopen(req)
    data = json.load(res)
    print data


    # http://serverfault.com/questions/593157/graphite-shows-none-for-all-data-points-even-though-i-send-it-data
    # http://stackoverflow.com/questions/17045549/graphite-render-precision-lower-than-1-minute
    '''
    CARBON_SERVER = 'ast03'
    CARBON_PORT = 22003

    message = 'foo.bar.baz 42 %d\n' % int(time.time())

    print 'sending message:\n%s' % message
    sock = socket.socket()
    sock.connect((CARBON_SERVER, CARBON_PORT))
    sock.sendall(message)
    sock.close()
    '''