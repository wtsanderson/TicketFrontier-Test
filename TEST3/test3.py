import sys

with open(sys.argv[1], "r") as file:
    raw_text = file.read()

raw_text = raw_text.split("\n")
raw_text = raw_text[:len(raw_text)-1]

byYear = []
year = "1851"
accidents = 0
totalWounded = 0
totalKilled = 0

for entry in raw_text:
    data = entry.split()
    entryYear = data[6]
    # New Year, add to data structure
    if (entryYear != year):
        avgWounded = float(totalWounded) / float(accidents)
        avgKilled = float(totalKilled) / float(accidents)

        byYear.append([year, int(accidents), avgWounded, totalWounded, avgKilled, totalKilled])

        # Reset variables
        accidents = 1
        totalWounded = int(data[9])
        totalKilled = int(data[7])
        year = entryYear
    #
    else:
        accidents += 1
        totalWounded += int(data[9])
        totalKilled = int(data[7])

print("BY YEAR")
for entry in byYear:
    print(entry[0] + "\t" + entry[1] + "\t" + entry[2] + "\t" + entry[3] + "\t" + entry[4] + "\t" + entry[5])

