#import os
import subprocess
import json
import sys
import schedule
import time
import pyrebase

# This line will run this code every Friday at 2 pm
#schedule.every().friday.at("14:00").do(run_script) commented out for demo and testing purposes

def run_script():
    #get network data
    direct_output = subprocess.check_output('sudo arp-scan -l', shell = True)
    s = direct_output.decode(sys.stdout.encoding)
    s = str(s)
    s.replace("//", "")
    data = s.replace('\n', '\t').split('\t')

    #remove header info
    data.pop(0)
    data.pop(0)

    #remove footer data
    data.pop()
    data.pop()
    data.pop()
    data.pop()    

    class pida:
        def __init__(self, ip, mac, dev):
            self.ip = ip
            self.mac = mac
            self.dev = dev

    ip = True
    mac = False
    dev = False
    tIp = ""
    tMac = ""
    tDev = ""
    l = []

    #from data list create objs with data to be stored as json
    for t in data:
        if ip:
            tIp = str(t)
            ip = False
            mac = True
        elif mac:
            tMac = str(t)
            mac = False
            dev = True
        elif dev:
            tDev = str(t)
            dev = False
            ip = True
            obj = pida(tIp, tMac, tDev)
            l.append(obj)

    #format as json
    j = json.dumps([ob.__dict__ for ob in l])
    #j = json.JSONEncoder(l)
    print(j)
    # commented out for demo and testing purposes
    # config = {
    #     deleted config for public github
    # }
    # 
    # firebase = pyrebase.initialize_app(config)
    # db = firebase.database()
    # db.child("users").set(j)