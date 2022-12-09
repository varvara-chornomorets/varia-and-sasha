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


# task 1
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

# task 3
if sys.argv[2] == "-overall":
    with open(sys.argv[1], 'r') as file:
        line = file.readline()
        years = {}
        for i in range(1896, 2018, 2):
            years[i] = 0
        for country in sys.argv[3::]:
            for line in file.readlines():
                line = line[0:-1]
                participant = Participant(*line.split("\t"))
                if participant.team == country or participant.noc == country and participant.medal != "NA":
                    years[int(participant.year)] += 1
            print(max(years, key=years.get), max(years.values()))
            for i in range(1896, 2020, 4):
                years[i] = 0
