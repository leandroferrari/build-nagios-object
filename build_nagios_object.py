#!/usr/bin/env pyhton

import os
import sys
import jinja2
from string import rstrip

# jinja2 environment
loader = jinja2.FileSystemLoader(os.getcwd())
jenv = jinja2.Environment(loader=loader)
define_template = jenv.get_template("templates/object_template.j2")

# command line argument parse
try:
    file_txt = str(sys.argv[1])
except IndexError:
    print "usage: python nagios_object.py [txt_file]"
    sys.exit(0)

# open txt file
r = open(file_txt, "r")

# jinja2 variables
object = ""
host_name = ""
key_value = []

# read txt file and populate jinja2 variables
for line in r.readlines():
    print line.splitlines()
    key = line.split(":")[0]
    value = line.split(":")[1]
    if key == "object":
        object = value.rstrip("\n")
        items = {key : value.rstrip("\n")}
        key_value.append(items)
    elif key == "host_name":
        host_name = value.rstrip("\n")
        items = {key : value.rstrip("\n")}
        key_value.append(items)
    else:
        items = {key : value.rstrip("\n")}
        key_value.append(items)

# call jinja2 template
define_file = define_template.render(host_name=host_name, object=object, list=key_value)

# write cfg file
w = open("object_file/" + host_name + ".cfg", "w")
w.write(define_file)
w.close()
print define_file
