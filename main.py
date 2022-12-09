import sys
from cls import Participant


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
