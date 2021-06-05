import requests
import logging
import sys
import socket

class Request_Class:
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) '\
           'AppleWebKit/537.36 (KHTML, like Gecko) '\
           'Chrome/75.0.3770.80 Safari/537.36'}

    def __init__(self) -> None:
        pass

    def check_request(self,address):
        try:
            address = "http://" + address
            response = requests.get(
                address,  timeout=60, headers=self.headers)
        except:
            print("Request Error: "+ address + str(sys.exc_info()))
            logging.error("Request Error: " + address + str(sys.exc_info()))
            self.check_addrinfo(address)
            return False
        if response.status_code == 200:
            return  True
        else:
            print("Request Error: " + address)
            logging.error("Request Error: " + address)
            self.check_addrinfo(address)
            return False

    def check_addrinfo(self,address):
        try:
            Liste =  socket.getaddrinfo(address,0)
            for ergebnis in Liste:
                print("Adressabfrage: " + address + ergebnis[4][0])
                logging.error("Adressabfrage: " + address + ergebnis[4][0])
        except:
            print("Adressabfrage: "+ address + str(sys.exc_info()))
            logging.error("Adressabfrage: "+ address + str(sys.exc_info()))