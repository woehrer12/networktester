#Importe Python Pakete
import time
import logging

#Importe eigene Pakete
import Ping
import config
import Request

#Klassen deklerationen
Ping = Ping.Ping_Class()
Request = Request.Request_Class()

#Logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)
handler = logging.FileHandler("logs/loop.log")
formatter = logging.Formatter('%(asctime)s:%(levelname)s-%(message)s')
handler.setFormatter(formatter)
handler.setLevel(logging.INFO)
logger.addHandler(handler)

#Initialisieren
ip_list = ["8.8.8.8","8.8.4.4","2001:4860:4860::8888","2001:4860:4860::8844","google.de","google.com","ipv6.google.com","192.168.50.1","192.168.0.1"]
address_list = ["google.de","vodafone.de"]
config.config()
starttime = int(time.time())
looptime = 0


while True:
    if looptime < int(time.time()):
        looptime = int(time.time()) + 60
        for ip in ip_list:
            Ping.check_ping(ip)
        for address in address_list:
            Request.check_request(address)

