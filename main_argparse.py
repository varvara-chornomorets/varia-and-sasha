import argparse
from cls import Participant

types_of_medals = ["Gold", "Silver", "Bronze"]


def count_number_of_medals(type_of_medals, list_of_participants):
    number = 0
    for i in range(0, len(list_of_participants)):
        if list_of_participants[i].medal == type_of_medals:
            number += 1
    return number


def task1(filename, country, year):
    suitable_participants = []
    with open(filename, "r") as file:
        first_line = file.readline()
        head = first_line.strip().split("\t")
        for line in file.readlines():
            participant = Participant(*line.strip().split("\t"))
            if (participant.team == country or participant.noc == country) and participant.medal != "NA" and participant.year == year:
                suitable_participants.append(participant)

        for i in range(0, 10):
            participant = suitable_participants[i]
            print(f"{participant.name}-{participant.sport}-{participant.medal}")

        for type_of_medal in types_of_medals:
            k = count_number_of_medals(type_of_medal, suitable_participants)
            print(type_of_medal, k)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    parser.add_argument("-medals", action="store_true", required=False)
    parser.add_argument("country")
    parser.add_argument("year")
    args = parser.parse_args()
    filename = args.filename
    country = args.country
    year = args.year
    medals = args.medals
    if medals:
        task1(filename, country, year)


if __name__ == "__main__":
    print("I am main_2")
    main()
