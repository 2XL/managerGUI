import zerorpc


# this is the manager server

class Manager(object):

    def hello(self, name):
        print "Requset: -> name {}".format(name)
        return "Response: -> client: Hello from manager, %s" % name

    def goodbye(self, name):
        print 'Request: name {}'.format(name)
        return "Response: -> client: Goodbye from manager, %s" % name

    def bad(self):
        raise Exception('xD')



s = zerorpc.Server(Manager())
s.bind("tcp://0.0.0.0:4242")
s.run()