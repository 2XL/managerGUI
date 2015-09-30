import zerorpc
import multiprocessing
from zerorpc import zmq
import subprocess
import json
import urllib
import nmap
# this is the manager server

class Manager(object):

    def hello(self, name):
        print "Request: -> hello {}".format(name)
        return "Response: -> client: Hello from manager, %s" % name

    def goodbye(self, name):
        print 'Request: -> goodbye {}'.format(name)
        return "Response: -> client: Goodbye from manager, %s" % name

    def start(self, name):
        print 'Request: -> start {}'.format(name)
        return "Response: -> client: Start from manager, %s" % name

    def cmd(self, name):

        str = urllib.quote_plus(name)
        print name
        print str
        print 'Request: -> cmd {}'.format(name)
        bashCommand = "{}".format(name)
        output = subprocess.check_output(['bash','-c', bashCommand])
        # json.dumps("Response: -> client: List from manager " % name),
        return output.split('\n')


    def list(self, name):
        print 'Request: -> list {}'.format(name)
        bashCommand = "ls {}".format(name)
        output = subprocess.check_output(['bash','-c', bashCommand])
        # json.dumps("Response: -> client: List from manager " % name),
        return output.split('\n')

    def bad(self):
        raise Exception('xD')


    def nmap(self, port, ip):
        print 'Request: -> ping {}:{}'.format(ip, port)
        output = subprocess.check_output(['nmap','-p', port, ip])

        result = output.split('\n')
        print result
        if len(result) > 5:
            print result[5]
            print result[5].split()[1]
            # print result[5].split(' ', 1)
            if result[5].split()[1] == 'open':
                print result[5]
                print result[5].split()[1]
                return True
        return False

    def rpc(self):
        print 'Request: -> rpc to dummyhost'

def ManagerRPC():
    print 'ManagerRPC instance'
    s = zerorpc.Server(Manager())
    server_address = "tcp://0.0.0.0:4242"
    s.bind(server_address)
    s.run()


def main():
    process = multiprocessing.Process(target=ManagerRPC())
    process.start()

if __name__ == "__main__":
    print "Start manager"
    main()
    print "Finish manager"
