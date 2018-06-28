import os
import time
import socket
# from urllib import request

def log(content):
    now = time.localtime()
    print("[%s:%s:%s] %s" % (now[3], now[4], now[5], content))

class Reconnecter:
    def __init__(self, ssid, timeout):
        if not ssid:
            raise ValueError("ssid must be specificated")
        self.count = 0
        self.ssid = ssid
        self.timeout = timeout
        
    def isConnected(self):
        # Another approach
        # try:
        #     request.urlopen("https://www.baidu.com", timeout = 2)
        #     return True
        # except:
        #     self.count += 1
        #     return False
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(2)
            s.connect(("www.baidu.com", 80))
            return True
        except:
            return False

    def disconnect(self):
        log("Disconnecting...")
        os.system("netsh wlan disconnect")

    def connect(self):
        log("Connecting to %s..." % self.ssid)
        os.system("netsh wlan connect name=%s" % self.ssid)

    def start(self):
        while True:
            print("==============================")
            log("Checking internet connection...")
            if self.count == 6:
                log("Unable to reconnect, exiting")
                break
            if not self.isConnected():
                log("No connection, reconnecting")
                self.disconnect()
                self.connect()
                continue
            else:
                self.count = 0
                log("Still connected. See you in %s seconds" % self.timeout)
            time.sleep(self.timeout)

reconnecter = Reconnecter(None, 30)
reconnecter.start()