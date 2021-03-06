#!/usr/bin/env python

from cmd2 import Cmd
import sys
import requests
from urllib import urlretrieve
import imp


__version__ = '0.2'

class Application(Cmd):
 

    def __init__(self):
        Cmd.__init__(self)

    def do_fbpost(self, line):
        urlretrieve('https://raw.github.com/gist/1194123/fbconsole.py', '.fbconsole.py')
        fb = imp.load_source('fb', '.fbconsole.py')
        fb.AUTH_SCOPE = ['publish_stream']
        fb.authenticate()
        status = fb.graph_post("/me/feed", {"message": line })

    def do_fb_pic_upload(self, line):
        urlretrieve('https://raw.github.com/gist/1194123/fbconsole.py', '.fb    console.py')
        fb = imp.load_source('fb', '.fbconsole.py')
        fb.AUTH_SCOPE = ['publish_stream']
        fb.authenticate()
        fb.graph_post("/me/photos", {"source":open(line)})

if __name__ == '__main__':
	app = Application()
	app.cmdloop()
