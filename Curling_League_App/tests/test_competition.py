import datetime
import unittest

#from competition import Competition
#from team import Team
from Curling_League_App.competition import Competition
from Curling_League_App.team import Team


class CompetitionTests(unittest.TestCase):
    def test_create(self):
        now = datetime.datetime.now()
        t1 = Team(1, "Team 1")
        t2 = Team(2, "Team 2")
        t3 = Team(3, "Team 3")
        c1 = Competition(1, [t1, t2], "Here", None)
        c2 = Competition(2, [t2, t3], "There", now)

        self.assertEqual("Here", c1.location)
        self.assertEqual(1, c1.oid)
        self.assertIsNone(c1.date_time)
        self.assertEqual(2, len(c1.teams_competing))
        self.assertIn(t1, c1.teams_competing)
        self.assertIn(t2, c1.teams_competing)
        self.assertNotIn(t3, c1.teams_competing)

        self.assertEqual("There", c2.location)
        self.assertEqual(2, c2.oid)
        self.assertEqual(now, c2.date_time)
        self.assertEqual(2, len(c2.teams_competing))
        self.assertNotIn(t1, c2.teams_competing)
        self.assertIn(t2, c2.teams_competing)
        self.assertIn(t3, c2.teams_competing)

    def test_str(self):
        now = datetime.datetime.now()
        t1 = Team(1, "Team 1")
        t2 = Team(2, "Team 2")
        t3 = Team(3, "Team 3")
        now = now.strftime("%m/%d/%Y, %H:%M:%S")
        c1 = Competition(1, [t1, t2], "Here", None)
        c2 = Competition(2, [t2, t3], "There", now)

        self.assertEqual("Competition at There on " + str(now) + " with 2 teams", str(c2))
        self.assertEqual("Competition at Here with 2 teams", str(c1))