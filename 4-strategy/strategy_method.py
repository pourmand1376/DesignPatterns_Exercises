from abc import ABC, abstractmethod

class Encryptor(ABC):
    @abstractmethod
    def encrypt(self,message):
        pass

class DESEncryptor(Encryptor):
    def encrypt(self,message):
        print("Encrypting message using DES")

class AESEncryptor(Encryptor):
    def encrypt(self,message):
        print("Encrypting message using AES")

class ChatClient(object):
    def __init__(self, encryptionAlgorithm:Encryptor):
        self.encryptionAlgorithm = encryptionAlgorithm

    def send(self, message):
        self.encryptionAlgorithm.encrypt(message)
        print("Sending the encrypted message...")

def main():
    chatClient = ChatClient(AESEncryptor())
    chatClient.send('hello')

if __name__ == "__main__":
    main()