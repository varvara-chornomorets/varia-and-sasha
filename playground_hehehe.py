with open("athlete_events", "r") as file:
    n = 0
    for line in file.readlines():
        print(n)
        n += 1
        print(line)
