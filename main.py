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
        else:
            print("there is no such country as", sys.argv[3])


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
        total = {}
        for i in bronze:
            total[i] = bronze[i] + silver[i] + gold[i]
        while len(total) > 0:
            key = max(total, key=total.get)
            print(f"{key} - {bronze[key]} - {silver[key]} - {gold[key]}")
            total.pop(key)


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


# task 4
if sys.argv[2] == "-interactive":
    filename = sys.argv[1]
    first = 2020
    first_city = "SASSADSAFGDSHDGASHDGAS"
    results = {}
    bronze = {}
    silver = {}
    gold = {}
    country = input()
    with open(filename, 'r') as file:
        line = file.readline()
        for line in file.readlines():
            line = line[0:-1]
            participant = Participant(*line.split("\t"))
            if participant.noc == country or participant.team == country:
                if int(participant.year) < first:
                    first = int(participant.year)
                    first_city = participant.city
                if participant.year not in results:
                    results[participant.year] = 0
                    bronze[participant.year] = 0
                    silver[participant.year] = 0
                    gold[participant.year] = 0
                if participant.medal == "Bronze":
                    bronze[participant.year] += 1
                    results[participant.year] += 1
                elif participant.medal == "Silver":
                    silver[participant.year] += 1
                    results[participant.year] += 1
                elif participant.medal == "Gold":
                    gold[participant.year] += 1
                    results[participant.year] += 1
    if first != 2020:
        print("First year:", first, "First city: ", first_city)
        print(f"Best year: {max(results, key=results.get)} - {max(results.values())}")
        print(f"Worst year: {min(results, key=results.get)} - {min(results.values())}")
        k = 0
        for i in bronze.values():
            k += i
        print("Average bronzes:", int(k/len(bronze)))
        k = 0
        for i in silver.values():
            k += i
        print("Average silvers:", int(k / len(silver)))
        k = 0
        for i in gold.values():
            k += i
        print("Average golds:", int(k/len(gold)))
    else:
        print("there is no such country as", country)

