import zerorpc


# this is the manager server

class Manager(object):

    def hello(self, name):
        return "Hello, %s" % name

    def goodbye(self, name):
        return "Goodbye, %s" % name

    def bad(self):
        raise Exception('xD')



s = zerorpc.Server(Manager())
s.bind("tcp://0.0.0.0:4242")
s.run()