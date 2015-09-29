import zerorpc
import multiprocessing
from zerorpc import zmq
import subprocess
import json

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
        print 'Request: -> cmd {}'.format(name)
        return "Response: -> client: Cmd from manager, %s" % name

    def list(self, name):
        print 'Request: -> list {}'.format(name)
        bashCommand = "ls {}".format(name)
        output = subprocess.check_output(['bash','-c', bashCommand])
        # json.dumps("Response: -> client: List from manager " % name),
        return  output.split('\n')

    def bad(self):
        raise Exception('xD')


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
