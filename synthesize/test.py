import time
import socket
import random
import wget
import urllib2
import json

class GraphiteClient():
    def __init__(self, host='localhost', port='22003'):
        self.hostname = host
        self.port = port

    def collect_string(self, name, val, timestamp):
        sock = socket.socket()
        sock.connect((self.hostname, self.port))
        sock.send("%s %d %d\n" % (name, val, timestamp))
        sock.close()

    def collect_pickle(self, name, val, timestamp):
        sock = socket.socket()
        sock.connect((self.hostname, 2004))
        sock.send("%s %d %d\n" % (name, val, timestamp))
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
    itv = 1


    metric = '{}.{}.{}'.format(hostname, test_id, key)

    for x in range(0, ops, 1):
        gc.collect_string(metric, randValue(), tsNow())
        time.sleep(itv)

    url = 'https://{}:8443/render/?target={}&format=json&from=-60second'.format(graphiteUrl, metric)
    req = urllib2.Request(url)
    res = urllib2.urlopen(req)
    data = json.load(res)
    print data



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