#Importe Python Pakete
import time
import logging

#Importe eigene Pakete
import Klassen.Ping
import config
import Klassen.Request
import Klassen.Address

#Klassen deklerationen
Ping = Klassen.Ping.Ping_Class()
Request = Klassen.Request.Request_Class()
Address = Klassen.Address.Address_Class()

#Logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)
handler = logging.FileHandler("logs/loop.log")
formatter = logging.Formatter('%(asctime)s:%(levelname)s-%(message)s')
handler.setFormatter(formatter)
handler.setLevel(logging.INFO)
logger.addHandler(handler)

#Initialisieren
ip_list = ["192.168.50.1","192.168.0.1"]
address_list = ["google.de","vodafone.de"]
config.config()
starttime = int(time.time())
looptime = 0


while True:
    if looptime < int(time.time()):
        looptime = int(time.time()) + 60
        #Ping Check
        #Eigene Adressen
        for ip in ip_list:
            Ping.check_ping(ip)
        #Ping Hostname BigData
        for ip in Address.hostname_bigData():
            Ping.check_ping(ip)
        #Ping DNS
        for ip in Address.ip_bigDNS():
            Ping.check_ping(ip)
        #HTTP Request
        for address in Address.hostname_bigData():
            Request.check_request(address)

