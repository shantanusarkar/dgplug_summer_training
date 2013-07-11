#!/usr/bin/env python

file = open("/proc/mounts") # Opens file /proc/mount.
print file.read() # Reads the file and prints it.
file.close() # Close the file.
