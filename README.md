# build-nagios-object
Build nagios objects from txt files.

## Objects type supported:
* host;
* hostgroup;
* service;
* servicegroup;
* contact;
* contactgroup;
* timeperiod;
* command;
* servicedependency;
* serviceescalation;
* hostextinfo;
* serviceextinfo;

You can find more about objects definitions [here.] (https://assets.nagios.com/downloads/nagioscore/docs/nagioscore/3/en/objectdefinitions.html)

## TXT file format:
    object:[object type] **this line is required**
    key:value

### TXT file example:
    object:host
    host_name:host_hell
    alias:host_hell
    address:192.168.0.168
    hostgroup:server_group
    contacts:admin
    display_name:Host Hell
    notes:some note here

## Usage:
python build-nagios-object.py [txt file]