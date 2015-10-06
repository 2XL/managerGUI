import time
import socket
import random


class GraphiteClient():
    def __init__(self, host='localhost'):
        self.hostname = host

    def collect_string(self, name, val, timestamp):
        sock = socket.socket()
        sock.connect((self.hostname, 2003))
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

    gc = GraphiteClient('10.30.103.95')

    hostname = 'Joanna'
    test_id = tsNow()
    key = 'random'
    value = None

    ops = 10
    itv = 1

    for x in range(0, ops, 1):
        gc.collect_string('{}.{}.{}'.format(hostname, test_id, key), randValue(), tsNow())
        time.sleep(itv)