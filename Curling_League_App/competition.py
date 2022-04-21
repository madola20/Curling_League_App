from Curling_League_App.identified_object import IdentifiedObject
from Curling_League_App.team import Team
import datetime

class Competition(IdentifiedObject):

    def __init__(self, oid, teams, location, datetime):
        super().__init__(oid)
        self.teams = teams
        self.location = location
        self.date_time = datetime

    @property
    def teams_competing(self):
        return self.teams

    @teams_competing.setter
    def teams_competing(self, property):
        self.teams = property

    def send_email(self, emailer, subject, message):
        team_members_emails = None
        for x in self.teams:
            for y in x.members:
                team_members_emails.append(y)
        emailer.send_plain_email(team_members_emails, subject, message)

    # return a string like the following: "Competition at location on date_time with N teams"
    def __str__(self):

        if self.date_time is None:
            return str("Competition at " + str(self.location) + " with " + str(len(self.teams)) + " teams")
        else:
            return str("Competition at " + str(self.location) + " on " + str(self.date_time) + " with " + str(len(self.teams)) + " teams")

if __name__ == '__main__':
    now = datetime.datetime.now()
    t1 = Team(1, "Team 1")
    t2 = Team(2, "Team 2")
    t3 = Team(3, "Team 3")

    c1 = Competition(1, [t1, t2], "Here", None)
    c2 = Competition(2, [t2, t3], "There", now)
    print(c1)
