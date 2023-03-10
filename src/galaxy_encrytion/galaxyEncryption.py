# Galaxy Encryption Module. Made by GalaxyGamerYT
from os import path
from cryptography.fernet import Fernet

print("Thank you for using Galaxy Encryption")

class galaxyEncryption:
    fernet = None
    def key(self):
        """
        Generates the key and/or loads the key.
        """
        if not path.exists("key.key"):
            # key generation
            key = Fernet.generate_key()

            # string the key in a file
            with open('key.key', 'wb') as filekey:
                filekey.write(key)
            
        else:
            # opening the key
            with open('filekey.key', 'rb') as filekey:
                key = filekey.read()
            
        # using the key
        self.fernet = Fernet(key)

    def decryptFile(self, path: str) -> str:
        """
        Decrypts the given contents of the file path.
        Needs the key function to have run.
        """
        if self.fernet != None:
            # opening the encrypted file
            with open(path, 'rb') as file:
                encrypted = file.read()
            
            # decrypting the file
            decrypted = self.fernet.decrypt(encrypted)
            return decrypted
        else:
            raise Exception("You need to generate/load a key using the key method of this module.")
    
    def encryptFile(self, path: str, content: str) -> str:
        """
        Encrypts the given content and writes to a file.
        Needs the key function to have run.
        """
        if self.fernet != None:
            encrypted = self.fernet.encrypt(content)
    
            with open(path, 'wb') as file:
                file.write(encrypted)
            return encrypted
        else:
            raise Exception("You need to generate/load a key using the key method of this module.")
