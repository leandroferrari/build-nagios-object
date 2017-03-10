#!/usr/bin/env pyhton

import os
import sys
import jinja2
from string import rstrip

# command line argument parse
try:
    file_txt = str(sys.argv[1])
except IndexError:
    print ""
    print "usage: python nagios_object.py [txt_file]"
    print ""
    sys.exit(0)

# jinja2 environment
loader = jinja2.FileSystemLoader(os.getcwd())
jenv = jinja2.Environment(loader=loader)
define_template = jenv.get_template("templates/object_template.j2")

# Open TXT file
r = open(file_txt, "r")

# Set jinja2 variables
object = ""
host_name = ""
key_value = []

# Function to write final cfg file
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

# Read TXT file and populate jinja2 variables
for line in r.readlines():
    if line == "\n":
        # Write the first object and so on when find a blank line in TXT file
        write_file(host_name)
        # Reset jinja2 variables
        object = ""
        host_name = ""
        key_value = []
    else:
        key = line.split(":")[0]
        value = line.split(":")[1]

        if key == "object":
            object = value.rstrip("\n")
        elif key == "host_name":
            host_name = value.rstrip("\n")
            items = {key : value.rstrip("\n")}
            key_value.append(items)
        else:
            items = {key : value.rstrip("\n")}
            key_value.append(items)

write_file(host_name)