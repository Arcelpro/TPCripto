import logging
from fernet_gui import FernetGUI
from cryptography.fernet import Fernet
from cryptography.fernet import InvalidToken
import time
import base64
TTL = 30

class TimeFernetGUI(FernetGUI):
    def encrypt(self, message):
        '''
        chiffre le message
        '''
        TFE = Fernet(self.key)
        message = bytes(message, "utf-8")
        temps = int(time.time())
        return TFE.encrypt_at_time(message,current_time= temps)

    def decrypt(self, message: bytes):
        '''
        déchiffre le message 
        '''
        try:
            TFDE = Fernet(self.key)
            message = base64.b64decode(message["data"])
            temps= int(time.time())
            return TFDE.decrypt_at_time(message, ttl = TTL, current_time=temps).decode('utf-8')
        

        except InvalidToken:
            return "INVALID TOKEN"

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    client = TimeFernetGUI()
    client.create()
    client.loop()