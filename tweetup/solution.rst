Objective
----------

To create a package which will post facebook status.

Code
-----

.. code:: python
    
    #!/usr/bin/env python

    from cmd2 import Cmd
    import sys
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

Run
----

1. Create a new virtual env and activate it.

::
    
    $  virtualenv virt4
    New python executable in virt4/bin/python
    Installing setuptools............done.
    Installing pip...............done.
    $  source virt4/bin/activate

2. Install the package

::
    
    $ pip install -i https://testpypi.python.org/pypi facebpost


3. Run facebpost

::
    
    $  facebpost

Output
-------

::
    
    (Cmd) fbpost this is a test status

    (Cmd) fb_pic_upload moto.jpg
