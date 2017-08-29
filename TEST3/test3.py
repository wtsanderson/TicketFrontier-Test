import sys

WEEKDAYS = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]

with open(sys.argv[1], "r") as file:
    rawText = file.read()

rawText = rawText.split("\n")
rawText = rawText[:len(rawText)-1]

# Structure of elements of byYear is as follows:
# [year, total accidents in that year, average wounded per accident, total wounded for that year,
#  average killed per accident in that year, total killed that year]
byYear = []
year = "1851"
accidentsYear = 0
totalWoundedYear = 0
totalKilledYear = 0

# Structure of byWeekday elements are as follows:
# [Name of weekday, accidents for that day of week, total wounded for that day, total killed that day]
byWeekday = {"Sun": ["Sunday", 0, 0, 0], "Mon": ["Monday", 0, 0, 0], "Tue": ["Tuesday", 0, 0, 0], "Wed": ["Wednesday", 0, 0, 0], "Thu": ["Thursday", 0, 0, 0], "Fri": ["Friday", 0, 0, 0], "Sat": ["Saturday", 0, 0, 0]}

for entry in rawText:
    data = entry.split()
    entryYear = data[6]
    day = data[3]

    byWeekday[day][1] += 1
    byWeekday[day][2] += int(data[9])

    # New Year, add totals to data structure
    if (entryYear != year):
        avgWounded = round(float(totalWoundedYear) / float(accidentsYear), 2)
        avgKilled = round(float(totalKilledYear) / float(accidentsYear), 2)

        byYear.append([year, int(accidentsYear), avgWounded, totalWoundedYear, avgKilled, totalKilledYear])

        # Reset variables
        accidentsYear = 1
        totalWoundedYear = int(data[9])
        totalKilledYear = int(data[7])
        year = entryYear
        byWeekday[day][3] = int(data[7])
    # Same year, add to current totals.
    else:
        byWeekday[day][3] = int(data[7]) - totalKilledYear
        accidentsYear += 1
        totalWoundedYear += int(data[9])
        totalKilledYear = int(data[7])

print("BY YEAR")
for entry in byYear:
    print(entry[0] + "\t" + str(entry[1]) + "\t" + str(entry[2]) + "\t" + str(entry[3]) + "\t" + str(entry[4]) + "\t" + str(entry[5]))

print("BY WEEKDAY")
for day in WEEKDAYS:
    if (not day in ["Wed", "Thu", "Sat"]):
        print(byWeekday[day][0] + "\t\t"  + str(byWeekday[day][1]) + "\t" + str(byWeekday[day][2]) + "\t" + str(byWeekday[day][3]))

    else:
        print(byWeekday[day][0] + "\t"  + str(byWeekday[day][1]) + "\t" + str(byWeekday[day][2]) + "\t" + str(byWeekday[day][3]))
