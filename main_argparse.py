import argparse
from cls import Participant

types_of_medals = ["Gold", "Silver", "Bronze"]


def count_number_of_medals(type_of_medals, list_of_participants):
    number = 0
    for i in range(0, len(list_of_participants)):
        if list_of_participants[i].medal == type_of_medals:
            number += 1
    return number


def find_suitable_and_medals(filename, country, year):
    available_countries = []
    suitable_participants = []
    available_years = []
    input_is_valid = True
    reason = ""
    with open(filename, "r") as file:
        file.readline()
        for line in file.readlines():
            participant = Participant(*line.strip().split("\t"))
            available_countries.append(participant.team)
            available_countries.append(participant.noc)
            available_years.append(participant.year)
            if (participant.team == country or participant.noc == country) and participant.medal != "NA" and participant.year == year:
                suitable_participants.append(participant)

        if country not in available_countries:
            input_is_valid = False
            reason = "There is no such country"
        if year not in available_years:
            input_is_valid = False
            reason = "Olympic games were not held that year"

        type_and_number_of_medals = {}

        for type_of_medal in types_of_medals:
            k = count_number_of_medals(type_of_medal, suitable_participants)
            type_and_number_of_medals[type_of_medal] = k

        return suitable_participants, type_and_number_of_medals, input_is_valid, reason


def task1(filename, country, year):
    suitable_participants, type_and_number_of_medals, input_is_valid, reason = find_suitable_and_medals(filename, country, year)
    if not input_is_valid:
        print(reason)
        return None
    for i in range(0, len(suitable_participants)):
        participant = suitable_participants[i]
        print(f"{participant.name}-{participant.sport}-{participant.medal}")
        if i == 10:
            break

    for element in type_and_number_of_medals:
        print(element, type_and_number_of_medals[element])


def task1_with_output(filename, country, year, file_to_output):
    task1(filename, country, year)
    suitable_participants, dict_with_medals, input_is_valid, reason = find_suitable_and_medals(filename, country, year)
    with open(file_to_output, 'w') as output_file:
        if not input_is_valid:
            output_file.write(reason)
            return None
        for i in range(0, len(suitable_participants)):
            output_file.write(f"{suitable_participants[i].name}-{suitable_participants[i].sport}-{suitable_participants[i].medal}\n")
            if i == 10:
                break
        for element in dict_with_medals:
            output_file.write(element)
            output_file.write("  ")
            output_file.write(str(dict_with_medals[element]))
            output_file.write("  ")


def calculate_overall(filename, countries_for_overall):
    list_of_countries = []
    # check if there is one country or more, creates list with all countries
    if type(countries_for_overall) == str:
        list_of_countries.append(countries_for_overall)
    else:
        list_of_countries = countries_for_overall

    info_about_every_year_for_country = {}
    for country in list_of_countries:
        info_about_every_year_for_country[country] = {}
        with open(filename, "r") as file:
            for i in range(1896, 2018, 2):
                info_about_every_year_for_country[country][i] = 0
            available_countries = []
            for line in file.readlines():
                participant = Participant(*line.strip().split("\t"))
                if (participant.team == country or participant.noc == country) and participant.medal != "NA":
                    info_about_every_year_for_country[country][int(participant.year)] += 1
                available_countries.append(participant.team)
                available_countries.append(participant.noc)
            if country not in available_countries:
                info_about_every_year_for_country[country] = False
    return info_about_every_year_for_country


def task2(filename, countries_for_overall):
    info_about_every_year_for_country = calculate_overall(filename, countries_for_overall)
    for country in info_about_every_year_for_country:
        if not info_about_every_year_for_country[country]:
            print("there is no such country as", country)
            continue
        print(country,
              max(info_about_every_year_for_country[country], key=info_about_every_year_for_country[country].get),
              max(info_about_every_year_for_country[country].values()))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    parser.add_argument("-medals", nargs="*", required=False)
    parser.add_argument("-output", required=False)
    parser.add_argument("-overall", nargs="*", required=False)
    args = parser.parse_args()
    filename = args.filename
    country_and_year = args.medals
    output = args.output
    countries_for_overall = args.overall
    if output and country_and_year:
        country, year = country_and_year
        task1_with_output(filename, country, year, output)
    elif country_and_year:
        country, year = country_and_year
        task1(filename, country, year)
    elif countries_for_overall and output:
        task2(filename, countries_for_overall)
    elif countries_for_overall:
        task2(filename, countries_for_overall)


if __name__ == "__main__":
    main()
