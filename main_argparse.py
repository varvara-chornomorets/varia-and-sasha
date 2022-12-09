import argparse

types_of_medals = ["Gold", "Silver", "Bronze"]
# def myFunc():
#     return


def count_number_of_medals(type_of_medals, occurrences):
    number = 0
    for i in range(0, len(occurrences)):
        if type_of_medals in occurrences[i]:
            number += 1
    return number


def task1(filename, country, year):
    occurrences = []
    with open(filename, "r") as file:
        first_line = file.readline()
        head = first_line.strip().split("\t")
        for line in file.readlines():
            data = line.strip().split("\t")
            if country == data[head.index("Team")] and year == data[head.index("Year")]:
                occurrences.append(data)
        for type_of_medal in types_of_medals:
            k = count_number_of_medals(type_of_medal, occurrences)
            print(type_of_medal, k)


def main():
    parser = argparse.ArgumentParser()
    # parser.add_argument("filename")
    parser.add_argument("--medals", action="store_true", required=False)
    parser.add_argument("country")
    parser.add_argument("year")
    args = parser.parse_args()
    print(args)
    # filename = args.filename
    filename = "athlete_events"
    country = args.country
    year = args.year
    medals = args.medals
    if medals:
        task1(filename, country, year)


if __name__ == "__main__":
    print("I am main_2")
    main()
