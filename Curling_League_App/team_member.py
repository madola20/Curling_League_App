from Curling_League_App.identified_object import IdentifiedObject


class TeamMember(IdentifiedObject):

    def __init__(self, oid, name, email):
        super().__init__(oid)
        self._name = name
        self._email = email

    @property
    def name(self):
        return self._name

    @property
    def email(self):
        return self._email


    def send_email(self, emailer, subject, message):
        #send_it = FakeEmailer
        #send_it.send_plain_email(self, emailer, subject, message)
        emailer.send_plain_email([self.email], subject, message)

    def __str__(self):
        return f"{self.name}<{self.email}>"

if __name__ == '__main__':
    tm = TeamMember(2, "Fred", "fred@bedrock")
    #TeamMember(3, "Barney", "barney@bedrock")
    #TeamMember(4, "Wilma", "wima@bedrock")
    print(tm)