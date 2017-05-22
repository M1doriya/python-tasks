import os
import platform
import json
import sys
import psutil
import uuid
from netifaces import AF_INET, AF_INET6, AF_LINK, AF_PACKET, AF_BRIDGE
import netifaces as ni
import socket
import requests
REMOTE_SERVER = "www.google.com"
def is_connected():
    try:
        host = socket.gethostbyname(REMOTE_SERVER)
        s = socket.create_connection((host, 80), 2)
        return True 
    except:
            pass
            return False
info={}

info['system']={}
info['system']['MAC'] = ':'.join(['{:02x}'.format((uuid.getnode() >> i) & 0xff) for i in range(0,8*6,8)][::-1])
info['system']['processortype'] = platform.machine()
info['system']['hostname'] = platform.node()
info['system']['os'] = platform.system()
info['system']['kernelversion'] = platform.release()
if(is_connected()):    
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('8.8.8.8', 1))  # connect() for UDP doesn't send packets
    info['system']['private ip'] = s.getsockname()[0]
    info['system']['public ip']=requests.get('http://ip.42.pl/raw').text
with open('info.json', 'w') as outfile:
    json.dump(info, outfile)
