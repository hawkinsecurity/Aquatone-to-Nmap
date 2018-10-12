import json
import sys
from collections import OrderedDict
from socket import inet_aton
import struct
import nmap

#Opens aquatone's json file 
hostfile = open("hosts.json", "r+")
hosts = json.load(hostfile)
seen = OrderedDict()
hostfile.close()
for k ,v in hosts.iteritems():
    ips = v
    if ips not in seen:
        seen[ips] = v
    test = sorted(seen.values(), key=lambda ip: struct.unpack("!L", inet_aton(ip))[0])
ipoutput = open("iplist.txt", "w+")
for i in test:
    ipoutput.write(i+"\n")
