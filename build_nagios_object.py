#!/usr/bin/env pyhton

import os
import sys
import jinja2
from string import rstrip

# command line argument parse
try:
    file_txt = str(sys.argv[1])
except IndexError:
    print "usage: python nagios_object.py [txt_file]"
    sys.exit(0)

# jinja2 environment
loader = jinja2.FileSystemLoader(os.getcwd())
jenv = jinja2.Environment(loader=loader)
define_template = jenv.get_template("templates/object_template.j2")

# def open file mode: "r" = read, "a" = append
r = open(file_txt, "r")

# jinja2 variables
object = ""
host_name = ""
key_value = []

def write_file(host_name):
    # call jinja2 template
    define_file = define_template.render(host_name=host_name, 
                                        object=object, 
                                        list=key_value)
    # write cfg file
    w = open("object_file/" + host_name + ".cfg", "a")
    w.write(define_file)
    w.close()
    print define_file

# read txt file and populate jinja2 variables
for line in r.readlines():
    #print line.splitlines()
    if line == "\n":
        write_file(host_name)
        object = ""
        host_name = ""
        key_value = []
    else:
        key = line.split(":")[0]
        value = line.split(":")[1]

        if key == "object":
            object = value.rstrip("\n")
            #items = {key : value.rstrip("\n")}
            #key_value.append(items)
        elif key == "host_name":
            host_name = value.rstrip("\n")
            items = {key : value.rstrip("\n")}
            key_value.append(items)
        else:
            items = {key : value.rstrip("\n")}
            key_value.append(items)

write_file(host_name)