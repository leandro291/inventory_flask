import os
import bcrypt
from typing import Union
from cryptography.fernet import Fernet
import base64 

class PasswordHelper:

    def hash_password(self, password: str) -> str:
        bytes_password = password.encode('utf-8')
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(bytes_password, salt)
        return hashed_password.decode('utf-8')
    
    def verify_password(self, password: str, hashed_password: str) -> str:
        bytes_password = password.encode('utf-8')
        bytes_hash_password = hashed_password.encode('utf-8')
        return bcrypt.checkpw(bytes_password, bytes_hash_password)

class CryptoHelper:
    def __init__(self):
        self._key = os.getenv('FERNET_SECRET_KEY')
        self.validate_key()
        self.fernet = Fernet(self._key)

    def encrypt(self, value: Union[str, int, float, bool]) -> str:
        string_value = str(value)
        bytes_value = string_value.encode('utf-8')
        encrpyted_value = self.fernet.encrypt(bytes_value)
        return encrpyted_value.decode('utf-8')

    def decrypt(self, value: str) -> Union[str, int, float, bool]:
        bytes_value = value.encode('utf-8')
        decrypted_value = self.fernet.decrypt(bytes_value)
        return decrypted_value.decode('utf-8')
    
    def validate_key(self):
        if not self._key:
            raise ValueError('FERNET_SECRET_KEY is not set')
        
        try:
            bytes_key = base64.urlsafe_b64decode(self._key)

            if len(bytes_key) != 32:
                raise ValueError('Invalid key length')
        except ValueError as e:
            raise ValueError(f'{e}')

crypto_helper = CryptoHelper()
password_helper = PasswordHelper()
