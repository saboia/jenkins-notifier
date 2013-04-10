#!/usr/bin/env python
#-*- coding:utf-8 -*-

from lxml import html as lhtml
import httplib2
import time


import sys
import Growl
import getopt

"""Growl Ping

    -h/--help
        Displays this message

    -t/--title
        Specify the title of the notification

    -m/--message
        Specify the message to be displayed

    -i/--icon
        A path to an image

    -s/--sticky
        Make the notification sticky
"""

class GrowlPing(object):

    def __init__(self):
        self.icon_path = '/Users/saboia/Projetos/jenkins-notifier/jenkins.png'
        self.app_name = 'Growl Ping'
        self.notifications = ['update']
        self.title = 'Growl Ping Notification'
        self.message = 'This notification was generated by growl-ping.py'
        self.sticky = False

        self.process_opts()

        try: self.icon = Growl.Image.imageFromPath(self.icon_path)
        except: self.icon = None

    def usage(self, code, msg=''):
        if code: fd = sys.stderr
        else: fd = sys.stdout
        print __doc__
        if msg: print >> fd, msg
        sys.exit(code)

    def process_opts(self):
        try:
            opts, args = getopt.getopt(sys.argv[1:], 'ht:m:i:s',
                                       ['help', 'title', 'message',
                                        'icon', 'sticky'])
        except getopt.error, msg:
            self.usage(1, msg)

        for opt, arg in opts:
            if opt in ('-h', '--help'):
                self.usage(0)
            elif opt in ('-t', '--title'):
                self.title = arg
            elif opt in ('-m', '--message'):
                self.message = arg
            elif opt in ('-i', '--icon'):
                self.icon_path = arg
            elif opt in ('-s', '--sticky'):
                self.sticky = True

    def run(self):
        self.notify()

    def ping(self):
        return

    def notify(self,dias):
        title = "Jenkins Notifier"
        message = "Teste para o build %s" % dias
        notification = 'update'
        g = Growl.GrowlNotifier(self.app_name, self.notifications,
                                applicationIcon=self.icon)
        g.register()
        g.notify(notification, title, message, sticky=True, priority=1)


