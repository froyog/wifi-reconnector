import os
import time
import socket
import sys
import getopt
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
        #     return False
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(2)
            s.connect(("www.baidu.com", 80))
            return True
        except:
            self.count += 1
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
            if self.count >= 5:
                log("Unable to reconnect, exiting")
                break
            if not self.isConnected():
                log("No connection, reconnecting...")
                self.disconnect()
                self.connect()
                time.sleep(2)
                continue
            else:
                self.count = 0
                log("Still connected. See you in %s seconds" % self.timeout)
            time.sleep(self.timeout)

def main(argv):
    ssid = ""
    timeout = 30

    try:
        opts, args = getopt.getopt(argv, "s:t:", ["ssid=", "timeout="])
    except getopt.GetoptError:
        print("unknown option")
        print("usage: reconnector.py -s <ssid> -t <timeout>")
        print("   or: reconnector.py --ssid=<ssid> --timeout=<timeout>")
        return

    for opt, arg in opts:
        if opt in ("-s", "--ssid"):
            ssid = arg
        elif opt in ("-t", "--timeout"):
            timeout = int(arg)

    try:
        reconnecter = Reconnecter(ssid, timeout)
        reconnecter.start()
    except ValueError as e:
        print("Error: %s" % e)
        return

if __name__ == "__main__":
    main(sys.argv[1:])