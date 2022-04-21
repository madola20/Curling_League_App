from Curling_League_App.identified_object import IdentifiedObject
from Curling_League_App.competition import Competition
from Curling_League_App.exceptions.duplicate_oid import DuplicateOid
from Curling_League_App.exceptions.duplicate_email import DuplicateEmail

from Curling_League_App.team import Team
from Curling_League_App.team_member import TeamMember

class League(IdentifiedObject):

    def __init__(self, oid, name):
        super().__init__(oid)
        self.name = name
        self._teams = []
        self.the_competitions = []

    @property
    def teams(self):
        return self._teams

    @property
    def competitions(self):
        return self.the_competitions

    def add_team(self, team):
        #self._teams.append(team)
        theTeamOid = getattr(team, "oid")
        if len(self._teams) == 0:
            self._teams.append(team)
        else:
            for eachTeam in self._teams:
                if theTeamOid != getattr(eachTeam, "oid"):
                    # self._members.append(member)
                    continue
                else:

                    raise DuplicateOid(team)
            self._teams.append(team)

    def remove_team(self, team):
        theCompetitions = []
        for eachCompetition in self.competitions:
            a = eachCompetition.teams_competing[0]
            b = eachCompetition.teams_competing[1]
            if team is a or team is b:
                raise ValueError("That team is in a competition and cannot be removed from the league")
        self._teams.remove(team)


    def team_named(self, s):
        for team in self._teams:
            theTeam = getattr(team, "name")
            if s == theTeam:
                return team

    def add_competition(self, competition):
        #self.competitions.append(competition)
        theCompetition = getattr(competition, "teams")
        for eachTeam in theCompetition:
            if eachTeam not in self._teams:
                raise ValueError("Team is not in League")
        self.the_competitions.append(competition)




    def teams_for_member(self, member):
        return [team for team in self._teams if member in team.members]

    def competitions_for_team(self, team):
        return [competition for competition in self.the_competitions if team in competition.teams_competing]

    def competitions_for_member(self, member):
        member_teams = [team for team in self._teams if member in team.members]
        return [competition for competition in self.the_competitions if any(x in member_teams for x in competition.teams_competing)]

    def __str__(self):
        return self.name + ": " + str(len(self.teams)) + ", " + str(len(self.the_competitions))

if __name__ == '__main__':
    def build_league():
        league = League(1, "Some league")
        t1 = Team(1, "t1")
        t2 = Team(2, "t2")
        t3 = Team(3, "t3")



        all_teams = [t1, t2, t3]
        league.add_team(t1)
        league.add_team(t2)
        league.add_team(t3)
        tm1 = TeamMember(1, "Fred", "fred")
        tm2 = TeamMember(2, "Barney", "barney")
        tm3 = TeamMember(3, "Wilma", "wilma")
        tm4 = TeamMember(4, "Betty", "betty")
        tm5 = TeamMember(5, "Pebbles", "pebbles")
        tm6 = TeamMember(6, "Bamm-Bamm", "bam-bam")
        tm7 = TeamMember(7, "Dino", "dino")
        tm8 = TeamMember(8, "Mr. Slate", "mrslate")
        t1.add_member(tm1)
        t1.add_member(tm2)
        t2.add_member(tm3)
        t2.add_member(tm4)
        t2.add_member(tm5)
        t3.add_member(tm6)
        t3.add_member(tm7)
        t3.add_member(tm8)
        # every team plays every other team twice
        oid = 1
        for c in [Competition(oid := oid + 1, [team1, team2], team1.name + " vs " + team2.name, None)
                  for team1 in all_teams
                  for team2 in all_teams
                  if team1 != team2]:
            league.add_competition(c)




        return league


    league = League(1, "Some league")
    t1 = Team(1, "t1")
    t2 = Team(2, "t2")
    t3 = Team(3, "t3")

    league.add_team(t1)
    league.add_team(t2)
    league.add_team(t3)

    d = Team(4, "t4")
    league.add_team(d)

    c1 = Competition(1, [t1, t2], "here", None)
    league.add_competition(c1)

    c2 = Competition(2, [t2, t3], "here", None)
    league.add_competition(c2)

    c3 = Competition(3, [t1, t3], "here", None)
    league.add_competition(c3)

    print(league)
    print(league.teams)

    league.remove_team(d)
    print(league.teams)

    print(league.team_named("t3"))

