import sys
from cls import Participant


# task 1
if sys.argv[2] == "-medals":
    with open(sys.argv[1], 'r') as file:
        line = file.readline()
        counter = 0
        suitable_participants = []
        for line in file.readlines():
            line = line[0:-1]
            participant = Participant(*line.split("\t"))
            if (participant.team == sys.argv[3] or participant.noc == sys.argv[3]) and participant.year == sys.argv[4] and participant.medal != "NA":
                print(participant.name, participant.sport, participant.medal)
                if len(sys.argv) > 5:
                    if sys.argv[5] == "-output":
                        with open(sys.argv[6], 'a') as output_file:
                            output_file.write(participant.name+', '+participant.sport+', '+participant.medal+"\n")
                counter += 1
                suitable_participants.append(participant)
                if counter == 10:
                    break
        if len(suitable_participants) > 0:
            for type_of_medal in ["Gold", "Silver", "Bronze"]:
                number = 0
                for i in range(0, len(suitable_participants)):
                    if suitable_participants[i].medal == type_of_medal:
                        number += 1
                print(type_of_medal, number)
                if len(sys.argv) > 5:
                    if sys.argv[5] == "-output":
                        with open(sys.argv[6], 'a') as output_file:
                            output_file.write(type_of_medal+" "+str(number)+"\n")


# task 2
if sys.argv[2] == "-total":
    bronze = {}
    silver = {}
    gold = {}
    countries = []
    with open(sys.argv[1], 'r') as file:
        line = file.readline()
        for line in file.readlines():
            line = line[0:-1]
            participant = Participant(*line.split("\t"))
            if participant.year == sys.argv[3] and participant.medal == "Bronze":
                if participant.noc in bronze:
                    bronze[participant.noc] += 1
                else:
                    bronze[participant.noc] = 1
                    gold[participant.noc] = 0
                    silver[participant.noc] = 0
            if participant.year == sys.argv[3] and participant.medal == "Silver":
                if participant.noc in silver:
                    silver[participant.noc] += 1
                else:
                    silver[participant.noc] = 1
                    bronze[participant.noc] = 0
                    gold[participant.noc] = 0
            if participant.year == sys.argv[3] and participant.medal == "Gold":
                if participant.noc in gold:
                    gold[participant.noc] += 1
                else:
                    gold[participant.noc] = 1
                    bronze[participant.noc] = 0
                    silver[participant.noc] = 0
        for i in bronze:
            print(i+" - "+(str(gold[i]))+" - "+str(silver[i])+" - "+str(bronze[i]))


# task 3
if sys.argv[2] == "-overall":
    years = {}
    for country in sys.argv[3::]:
        for i in range(1896, 2018, 2):
            years[i] = 0
        with open(sys.argv[1], 'r') as file:
            line = file.readline()
            for line in file.readlines():
                line = line[0:-1]
                participant = Participant(*line.split("\t"))
                if (participant.team == country or participant.noc == country) and participant.medal != "NA":
                    years[int(participant.year)] += 1
            print(max(years, key=years.get), max(years.values()))
