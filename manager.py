#!/usr/bin/python
# -*- coding: iso-8859-1 -*-
__author__ = 'anna'

import zerorpc
import multiprocessing
from zerorpc import zmq
import subprocess
import json
import urlparse
import urllib
import nmap

# manager import
from ConfigParser import SafeConfigParser

from argparse import ArgumentParser
import shlex
import psycopg2
import threading
from subprocess import Popen, PIPE
import traceback, time, sys, os
import random, numpy
from multiprocessing import Pool
import csv
import pxssh
import getpass

# importar el init.py
class ManagerOps():

    # hosts
    # credentials
    # config

    # tenir un fitxer de status, per no torna a repetir procés

    HOST_STATUS = {}


    def __init__(self):
        print 'ManagerExecutive'


    def setup(self, args):
        print 'ManagerOps {}'.format(args['cmd'][0])

        h = {
            'ip': args['ip'][0],
            'passwd': args['login'][0],
            'user': args['login'][0]
        }
        print h
        hostname = args['hostname'][0]
        print hostname
        self.downloadBenchBox(h,hostname)
        self.installVagrantVBox(h,hostname)

    def downloadBenchBox(self, h, hostname):  # tell all the hosts to download BenchBox

        if self.HOST_STATUS[hostname] > 2: return False
        print 'downloadBenchBox'
        str_cmd = "" \
                  "echo 'check if Git is installed...'; " \
                  "echo '%s' | sudo -S apt-get install git; " \
                  "echo 'check if BenchBox is installed...'; " \
                  "if [ -d BenchBox ]; then " \
                  "cd BenchBox;" \
                  "git pull; " \
                  "else " \
                  "git clone --recursive https://github.com/2XL/BenchBox.git; " \
                  "fi;" \
                  "" % h['passwd']
        print str_cmd

        self.rmi(h['ip'], h['user'], h['passwd'], str_cmd) # utilitzar un worker del pool

        '''
        versió pool
        '''
        print 'downloadBenchBox/OK: {}'.format(hostname)


    def installVagrantVBox(self, h, hostname):    # tell all the hosts to install VirtualBox and Vagrant
        print 'installVagrantVBox'

        str_cmd = "" \
                  "if [ -d BenchBox ]; then " \
                  "cd BenchBox;" \
                  "git pull; " \
                  "cd vagrant/scripts; " \
                  "echo '%s' | sudo -S ./installVagrantVBox.sh; " \
                  "fi;" \
                  "" % h['passwd']
        print str_cmd

        self.rmi(h['ip'], h['user'], h['passwd'], str_cmd)
        print 'installVagrantVBox/OK: {}'.format(hostname)


    def downloadVagrantBoxImg(self, h, hostname):  # tell the hosts to download Vagrant box to use
        print 'downloadVagrantBoxImg'
        str_cmd = "" \
                  "if [ -d BenchBox ]; then " \
                  "cd BenchBox;" \
                  "git pull; " \
                  "cd vagrant/scripts; " \
                  "./installDependencies.sh; " \
                  "fi;" \
                  ""
        #print str_cmd
        self.rmi(h['ip'], h['user'], h['passwd'], str_cmd)
        print 'downloadVagrantBoxImg/OK: {}'.format(hostname)


    def assignStereoTypeToProfile(self, h, hostname):
        print 'assignStereoTypeToProfile'
        str_cmd = "" \
                  "if [ -d BenchBox ]; then " \
                  "cd BenchBox;" \
                  "git pull; " \
                  "cd vagrant; " \
                  "echo '%s' > profile; " \
                  "fi; " % h['profile']

        #print str_cmd
        self.rmi(h['ip'], h['user'], h['passwd'], str_cmd)

        print 'assignStereoTypeToProfile/OK: {} :: {}'.format(hostname, h['profile'])



    def assignCredentialsToProfile(self, h, hostname):
        str_cmd = "" \
                  "if [ -d BenchBox ]; then " \
                  "cd BenchBox; " \
                  "git pull; " \
                  "cd vagrant; " \
                  "echo '%s' > ss.stacksync.key; " \
                  "echo '%s' > ss.owncloud.key; " \
                  "echo '%s' > hostname; " \
                  "echo 'Run: clients configuration scripts: '; " \
                  "cd scripts; " \
                  "./config.owncloud.sh; " \
                  "./config.stacksync.sh; " \
                  "echo 'clients configuration files generated'; " \
                  "fi; " % (h['cred-stacksync'],h['cred-owncloud'], h['hostname'])
        # print str_cmd
        self.rmi(h['ip'], h['user'], h['passwd'], str_cmd)
        print 'credentials/OK: {}:[{}] => {} / {}'.format(hostname)


    def assignSyncServer(self, h, hostname, args):

        # print 'sserver'
        # print config
        owncloud_ip = args['owncloud-ip']
        stacksync_ip = args['stacksync-ip']

        str_cmd = "" \
                  "if [ -d BenchBox ]; then " \
                  "cd BenchBox/vagrant; " \
                  "echo '%s' > ss.stacksync.ip; " \
                  "echo '%s' > ss.owncloud.ip; " \
                  "fi; " % (stacksync_ip, owncloud_ip)

        # print str_cmd
        self.rmi(h['ip'], h['user'], h['passwd'], str_cmd)
        print 'sserver/OK {} : {}'.format(hostname)



    def vagrantUp(self, h, hostname):
        print 'run: Call Vagrant init at each host: {}'.format(hostname)
        str_cmd = "" \
                  "if [ -d BenchBox ]; then " \
                  "cd BenchBox;" \
                  "git pull; " \
                  "cd vagrant; " \
                  "echo '-------------------------------'; " \
                  "ls -l *.box; " \
                  "vagrant -v; " \
                  "VBoxManage --version; " \
                  "echo '-------------------------------'; " \
                  "VBoxManage list runningvms | wc -l > running; " \
                  "vagrant up sandBox; " \
                  "vagrant provision sandBox; " \
                  "vagrant up benchBox; " \
                  "vagrant provision benchBox; " \
                  "else " \
                  "echo 'Vagrant Project not Found!??'; " \
                  "fi;" \
                  ""
        # print str_cmd
        self.rmi(h['ip'], h['user'], h['passwd'], str_cmd)
        print 'run/OK {}/{}'.format(hostname)


    def start_node_server(self, h):
        print 'run the nodejs monitor server at each Dummy Host'

        str_cmd = "cd BenchBox/monitor; " \
                  "nohup /usr/local/bin/npm start & "
        self.rmi(h['ip'], h['user'], h['passwd'], str_cmd)
        print 'nodeserver running at {}:{}'.format(h['ip'], '5000')




    def rmi(self, hostname, login, passwd, cmd, callback=None):
        while True:
            try:
                options={"StrictHostKeyChecking": "no", "UserKnownHostsFile": "/dev/null", "timeout": "3600"}
                s = pxssh.pxssh()
                s.login(hostname, login, passwd)
                s.timeout = 3600 # set timeout to one hour
                s.sendline(cmd) # run a command
                s.prompt() # match the prompt
                #print s.before # print everyting before the prompt
                # s.sendline ('uptime;df -h') # running multiple lines
                s.logout()
            except pxssh.ExceptionPxssh, e:
                print "pxssh failed on login."
                print str(e)
                continue
            break

        if callback:
            return callback()





# this is the manager server

class Manager(object):

    hosts = None
    config = None


    ops = ManagerOps()

    def loadHosts(self):
        print 'loadHosts'

    def loadConfig(self):
        print 'loadConfig'



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
        bashCommand = name # "{}".format(name)
        output = subprocess.check_output(['bash','-c', urllib.unquote_plus(bashCommand)])
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

    def rpc(self, url):
        print 'Request: -> rpc to dummyhost'
        print url # full url

        str = urlparse.urlparse(url)
        print str
        print str.query
        argslist = urlparse.parse_qs(str.query)
        toExecute = getattr(self.ops, argslist['cmd'][0])
        toExecute(argslist)
        print argslist
        return argslist

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
