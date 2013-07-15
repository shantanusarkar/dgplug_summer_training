Objective
----------

Write a python script to print the latest share value of a company whose NASDAQ symbol would be given as command line argument.

Program
--------
::

    #!/usr/bin/env python

    import urllib2
    import sys

    def share(symbol):
        try:
            x = urllib2.urlopen('http://download.finance.yahoo.com/d/quotes.csv?s='+symbol+'&f=l1')
            value = float(x.read())
            if value == 0.00:
                print "NASDAQ code invalid"
            else:
                print "The current sharevalue for %s is %f" % (symbol,value)
        except:
            print "failed to open the finance.yahoo.com url. Check your internet connection."

    if __name__ == '__main__':
        if len(sys.argv) != 2:
            print "Invalid Entry. Enter a valid NASDAQ symbol"
            sys.exit(1)
        else:
            share(sys.argv[1])
            sys.exit(1)

To go to program click `here`_.

.. _here : https://github.com/shantanusarkar/dgplug_summer_training/blob/master/sharevalue/sharevalue.py

Run
----
::

    chmod +x sharevalue.py
    ./sharevalue.py <NASDAQ symbol>


or ::

    python sharevalue.py <NASDAQ symbol>


Output
------
::
    
    $ python sharevalue.py GOOG

    The current sharevalue for GOOG is 923.000000

