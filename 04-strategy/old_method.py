class ChatClient(object):
    def __init__(self, encryptionAlgorithm):
        self.encryptionAlgorithm = encryptionAlgorithm

    def send(self, message):
        """ generated source for method send """
        if self.encryptionAlgorithm == "DES":
            print("Encrypting message using DES")
        elif self.encryptionAlgorithm == "AES":
            print("Encrypting message using AES")
        else:
            raise ValueError("Unsupported encryption algorithm")
        print("Sending the encrypted message...")

def main():
    chatClient = ChatClient('DES')
    chatClient.send('hello')

if __name__ == "__main__":
    main()