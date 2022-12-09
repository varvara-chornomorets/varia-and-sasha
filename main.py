import sys


class Participant:

    def __init__(self, id, name, sex, age, height, weight, team, noc, games, year, season, city, sport, event, medal):
        self.id = id
        self.name = name
        self.sex = sex
        self.age = age
        self.height = height
        self.weight = weight
        self.team = team
        self.noc = noc
        self.games = games
        self.year = year
        self.season = season
        self.city = city
        self.sport = sport
        self.event = event
        self.medal = medal


if sys.argv[2] == "-medals":
    with open(sys.argv[1], 'r') as file:
        line = file.readline()
        counter = 0
        while counter < 10:
            line = file.readline()[0:-1]
            participant = Participant(*line.split("\t"))
            if (participant.team == sys.argv[3] or participant.noc == sys.argv[3]) and participant.year == sys.argv[4] and participant.medal != "NA":
                print(participant.name, participant.sport, participant.medal)
                counter += 1
