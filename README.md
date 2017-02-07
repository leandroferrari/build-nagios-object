# build-nagios-object
Build nagios objects from txt files.

## Objects type supported:
* host
* hostgroup
* service
* servicegroup
* contact
* contactgroup
* timeperiod
* command
* servicedependency
* serviceescalation
* hostextinfo
* serviceextinfo

## TXT file format:
    object:[object type]
    key:value

### TXT file exemple:
    object:host
    host_name:host_hell
    alias:host_hell
    address:192.168.0.168
    hostgroup:server_group
    contacts:admin
    display_name:Host Hell
    notes:some note here
