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


def overall_function(filename, countries_for_overall):
    info_about_every_year_for_country = calculate_overall(filename, countries_for_overall)
    for country in info_about_every_year_for_country:
        if not info_about_every_year_for_country[country]:
            print("there is no such country as", country)
            continue
        print(country,
              max(info_about_every_year_for_country[country], key=info_about_every_year_for_country[country].get),
              max(info_about_every_year_for_country[country].values()))


def overall_with_output(filename, countries_for_overall, output_file):
    overall_function(filename, countries_for_overall)
    info_about_every_country = calculate_overall(filename, countries_for_overall)
    with open(output_file, "w") as file:
        for country in info_about_every_country:
            if not info_about_every_country[country]:
                file.write(f"there is no such country as {country}")
            else:
                file.write(f"{country} "
                           f"{max(info_about_every_country[country], key=info_about_every_country[country].get)} "
                           f"{max(info_about_every_country[country].values())}\n")


def total_function(filename, year):
    suitable_countries = {}
    total_countries = {}
    with open(filename, "r") as file:
        line = file.readline()
        for line in file.readlines():
            participant = Participant(*line.strip().split("\t"))
            if participant.medal != "NA" and participant.year == year:
                if participant.noc not in suitable_countries:
                    suitable_countries[participant.noc] = {}
                    total_countries[participant.noc] = 0
                    for type_of_medal in types_of_medals:
                        suitable_countries[participant.noc][type_of_medal] = 0

                suitable_countries[participant.noc][participant.medal] += 1
                total_countries[participant.noc] += 1
        return suitable_countries, total_countries


def total_function_print(filename, year):
    suitable_countries, total_countries = total_function(filename, year)
    length_of_dict = len(total_countries)
    for i in range (0, length_of_dict):
        max_country = max(total_countries, key=total_countries.get)
        total_countries.pop(max_country)
        print(f"{max_country} - {suitable_countries[max_country]['Gold']} - {suitable_countries[max_country]['Silver']}"
              f" - {suitable_countries[max_country]['Bronze']}")
    # for country in suitable_countries:
    #     print(f"{country} - {suitable_countries[country]['Gold']} - {suitable_countries[country]['Silver']}"
    #           f" - {suitable_countries[country]['Bronze']}")


def total_function_output(filename, year, output_file):
    total_function_print(filename, year)
    suitable_countries = total_function(filename, year)
    with open(output_file, "w") as file:
        for country in suitable_countries:
            file.write(f"{country} - {suitable_countries[country]['Gold']}"
                       f" - {suitable_countries[country]['Silver']} - {suitable_countries[country]['Bronze']}\n")


def interactive(filename):
    # Додайте до програми команду -interactive після введеня якої програма
    # переходить у інтерактивний режим (тобто зчитує у циклі команди через input(), як ви звикли).
    # Користувач може вводити країну (за назвою або кодом), а програма має виводити статистику ц
    # ієї країни - перша участь у олімпіаді (рік та місце проведення), найуспішніша олімпіада
    # (за кількістю медалей, вивести це значення), найневдаліша,
    # та середня кількість медалей кожного типу на кожній олімпіаді
    country = input("Please, enter the name of the country you would love to get statistics about: ")
    results = {}
    bronze = {}
    silver = {}
    gold = {}
    first = 2020
    first_city = 'VARIAIIAAIIAIAIAIAI'
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

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    parser.add_argument("-medals", nargs="*", required=False)
    parser.add_argument("-output", required=False)
    parser.add_argument("-overall", nargs="*", required=False)
    parser.add_argument("-total", required=False)
    parser.add_argument("-interactive", action="store_true", required=False)
    args = parser.parse_args()
    filename = args.filename
    country_and_year = args.medals
    output = args.output
    countries_for_overall = args.overall
    year = args.total
    is_interactive = args.interactive
    if output and country_and_year:
        country, year = country_and_year
        task1_with_output(filename, country, year, output)
    elif country_and_year:
        country, year = country_and_year
        task1(filename, country, year)
    elif countries_for_overall and output:
        overall_with_output(filename, countries_for_overall, output)
    elif countries_for_overall:
        overall_function(filename, countries_for_overall)
    elif year and output:
        total_function_output(filename, year, output)
    elif year:
        total_function_print(filename, year)
    elif is_interactive:
        interactive(filename)


if __name__ == "__main__":
    main()


    # with open(filename, "r") as file:
    #     dict_with_years_and_medals = {}
    #     for line in file:
    #         participant = Participant(*line.strip().split("\t"))
    #         if participant.team == user_country or participant.noc == user_country:
    #             if int(participant.year) not in dict_with_years_and_medals:
    #                 dict_with_years_and_medals[int(participant.year)] = {}
    #                 dict_with_years_and_medals[int(participant.year)]["place"] = participant.city
    #                 for type_of_medals in types_of_medals:
    #                     dict_with_years_and_medals[int(participant.year)][type_of_medals] = 0
    #                 dict_with_years_and_medals[int(participant.year)]["total"] = 0
    #
    #             elif participant.medal != "NA":
    #
    #                 dict_with_years_and_medals[int(participant.year)][participant.medal] += 1
    #                 dict_with_years_and_medals[int(participant.year)]["total"] += 1
    #     print(dict_with_years_and_medals)
    #     first_
