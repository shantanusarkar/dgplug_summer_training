#!/usr/bin/env python

file = open("/proc/mounts")
print file.read()
file.close()
