import sys, os
from netconf import netconf_connect, netconf_load_config, netconf_terminate, netconf_xget_leaf_value, netconf_xget_config_container_value, netconf_xget_container_value
import time

def main():
    gatewayip="192.168.209.1"
    port=830
    user="root"
    password="hadm1_123"

    if len(sys.argv)!=3:
        print "Usage: netconf_load_config.py <host> <config.xml>"
        return -1
    host=sys.argv[1]
    filename=sys.argv[2]
    f = open(filename, 'r')

    netconf_host = netconf_connect(host, port, user, password)
    if netconf_host == None:
        print "[FAILED] Connecting to ip=%(ip)s:" % {'ip':host}
        return(-1)

    ret = netconf_load_config(netconf_host, str(f.read()))
    if ret==0:
        print "[OK]"
    else:
        print "[FAILED]: netconf_load_config"
        return(-1)

    netconf_terminate(netconf_host)

    return 0

exit(main())