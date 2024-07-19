from abc import ABC, abstractmethod

class EmailProvider(ABC):
    @abstractmethod
    def download_emails(self):
        pass

class EmailClient():
    def __init__(self):
        self.providers = []

    def add_provider(self, provider: EmailProvider):
        self.providers.append(provider)

    def download_emails(self):
        for provider in self.providers:
            provider.download_emails()

class YahooProvider(EmailClient):
    def download_emails(self):
        print("downlading email from yahoo")

# unchangable, this is from external libraries
# how would you add this Gmail Client to your system?
class GmailClient():
    def connect(self):
        print("connecting to gmail")

    def get_emails(self):
        print("get emails ...")

    def disconnect(self):
        print("disconnecting")

email = EmailClient()
email.add_provider(YahooProvider())
email.download_emails()
    