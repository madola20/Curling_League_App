import yagmail
import keyring


class Emailer:
    sender_address = None
    _sole_instance = None


    @classmethod
    def configure(cls, sender_address):
        cls.sender_address = sender_address

    @classmethod
    def instance(cls):
        if cls._sole_instance is None:
            cls._sole_instance = cls()
        return cls._sole_instance

    def send_plain_email(self, recipients, subject, message):
        keyring.get_password("system", "username")
        yag = yagmail.SMTP("programming.email.tester@gmail.com")

        for recipient in recipients:
            print(f"Sending mail to: " + recipient)
            yag.send(recipient, subject, message)

