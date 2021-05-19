from pythonping import ping
import os
import logging

class Ping_Class():
    def __init__(self) -> None:
        pass

    def check_ping(self,ip):
        response = os.system("ping -c 1 " + ip)
        # and then check the response...
        if response == 0:
            pingstatus = "Network Active"
            return pingstatus, True
        else:
            pingstatus = "Network Error"
            logging.error("Ping Error: " + ip)
            return pingstatus ,False
