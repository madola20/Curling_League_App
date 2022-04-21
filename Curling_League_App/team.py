from Curling_League_App.identified_object import IdentifiedObject
from Curling_League_App.team_member import TeamMember
from Curling_League_App.exceptions.duplicate_oid import DuplicateOid
from Curling_League_App.exceptions.duplicate_email import DuplicateEmail

class Team(IdentifiedObject):



    def __init__(self, oid, name):
        super().__init__(oid)
        self.name = name
        self._members = []

    @property
    def members(self):
        return self._members


    def add_member(self, member):
        #if member not in self._members:
            #self._members.append(member)\
        theMemberOid = getattr(member, "oid")
        if len(self._members) == 0:
            self._members.append(member)
        else:
            for eachMember in self._members:
                if theMemberOid != getattr(eachMember, "oid"):
                    #self._members.append(member)
                    continue
                else:

                    raise DuplicateOid(member)
            theMemberEmail = getattr(member, "email").lower()
            for eachMember in self._members:
                if theMemberEmail != getattr(eachMember, "email").lower():
                    #self._members.append(member)
                    continue
                else:

                    raise DuplicateEmail(member)
            self._members.append(member)


    def member_named(self, s):
     for teammate in self._members:
        theName = teammate.name
        if s is theName:
            return teammate

    def remove_member(self, member):
        if member in self._members:
            self._members.remove(member)

    def send_email(self, emailer, subject, message):
        members_emails = []
        for teammate in self._members:
            members_emails.append(teammate.email)
        emailer.send_plain_email(members_emails, subject, message)

    def __str__(self):
        return str(self.name + ": " + str(len(self._members)))

"""
if __name__ == '__main__':
    
    t = Team(1, "Flintstones")
    t.add_member(TeamMember(2, "Fred", "fred@bedrock"))
    t.add_member(TeamMember(3, "Barney", "barney@bedrock"))
    t.add_member(TeamMember(6, "Bread", "wiMa@bedrock"))
    t.add_member(TeamMember(4, "Wilma", "wima@bedrock"))
    print(t.member_named("Barney"))
    print(t.members[1])
    print(t)
    """