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

class GmailProviderAdapter(EmailClient):
    def download_emails(self):
        gmail_client=GmailClient()
        gmail_client.connect()
        gmail_client.get_emails()
        gmail_client.disconnect()

## or we could do
class GmailProviderAdapter2(EmailClient):
    def __init__(self, gmail_client: GmailClient):
        self.gmail_client = gmail_client
    
    def download_emails(self):
        self.gmail_client.connect()
        self.gmail_client.get_emails()
        self.gmail_client.disconnect()

email = EmailClient()
email.add_provider(YahooProvider())
email.add_provider(GmailProviderAdapter())
email.add_provider(GmailProviderAdapter2(GmailClient()))
email.download_emails()
    