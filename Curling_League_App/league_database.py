import os.path
from os import path
import csv
import pickle
from Curling_League_App.league import League
from Curling_League_App.team import Team
from Curling_League_App.team_member import TeamMember

class LeagueDatabase:
    _sole_instance = None
    file_name = None
    _last_oid = 0
    the_leagues = []

    @classmethod
    def load(cls, file_name):
            try:
                with open(file_name, mode="rb") as file:
                        return pickle.load(file)
                        cls._sole_instance = file.read()
            except FileNotFoundError:
                print("ugh, sorry, it would be better to use the logging framework here but I don't want to go into it")
                backup = file_name + ".backup"
                if os.path.exists(backup):
                    with open(backup, mode="rb") as file:

                        return pickle.load(file)
                        cls._sole_instance = file.read()
                else:
                    return LeagueDatabase()



    @classmethod
    def instance(cls):
        if cls._sole_instance is None:
            cls._sole_instance = cls()
        return cls._sole_instance

    """
    Read only property
    returns: list of leagues being managed
    """
    def leagues(self):
        return self.the_leagues


    def add_league(self, league):
        self.the_leagues.append(league)


    def remove_league(self, league):
        try:
            self.the_leagues.remove(league)
        except:
            pass


    def next_oid(self):
        self._last_oid += 1
        return self._last_oid


    def save(self,file_name):
        if os.path.exists(file_name):
            new_file_name = file_name + ".backup"
            with open(new_file_name, mode="wb") as file:
                pickle.dump(LeagueDatabase.instance(), file)
        else:
            with open(file_name, mode="wb") as file:
                pickle.dump(LeagueDatabase.instance(), file)

    def import_league_teams(self, league, file_name):
        with open(file_name, newline='', encoding="utf-8") as csvfile:
            read_file = csv.reader(csvfile, quoting=csv.QUOTE_NONE)
            next(read_file)
            for row in read_file:
                if len(row) < 4:
                    team_name, teammate_name, teammate_email = row[0], row[1], row[2]
                else:
                    for item in row:
                        item.replace('"', '')
                        team_name, teammate_name, teammate_email = row[0], (row[1]+row[2]).replace('"', ''), row[3]

                #print(team_name, teammate_name, teammate_email)
                if league.team_named(team_name) is None:
                    new_team = Team(self._last_oid, team_name)
                    league.add_team(new_team)
                new_member = TeamMember(self._last_oid, teammate_name, teammate_email)
                new_team.add_member(new_member)

                self.next_oid()
                #print(new_member)





    def export_league_teams(self, league, file_name):
        with open(file_name, mode="w", newline='', encoding="utf-8") as csvfile:
            try:
                write_file = csv.writer(csvfile, delimiter=",", quoting=csv.QUOTE_MINIMAL)
                #, quotechar='"', quoting=csv.QUOTE_ALL
                header = ['Team name', 'Member name', 'Member email']
                write_file.writerow(header)
                theTeams = league.teams
                for teamm in theTeams:
                    the_members = teamm.members
                    team_name = getattr(teamm, "name")
                    for member in the_members:
                        write_file.writerow([team_name,getattr(member, "name"),getattr(member, "email")])
            except: print("There was an error")
        csvfile.close()



