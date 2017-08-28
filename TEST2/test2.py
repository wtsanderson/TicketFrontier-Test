import urllib, sys

BASE_URL = "http://www2.stat.duke.edu/courses/Spring01/sta114/data/andrews.html"
DATA_URL = "http://www2.stat.duke.edu/courses/Spring01/sta114/data/"
MONTHS = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

## Direct Download of table to .dat file
## Assumes that format of single digit table numbers in commandline input HAS a leading 0 as in: 
## python test2.py 05.1
## RATHER THAN:
## python test2.py 5.1

if (len(sys.argv) == 2):
    tableNumber = sys.argv[1]
    print("Downloading table " + tableNumber + " ...")
    tableURL = DATA_URL + "Andrews/T" + tableNumber
    
    # In case of connection failure.
    try:
        urllib.urlretrieve(tableURL, "output.dat")
    except IOError:
        print("Table not found.")

## Normal operation of the script downloads the html from the BASE_URL, parses it into a
## data structure, and then prints it.

request = urllib.urlopen(BASE_URL)
html = request.read()

# Cleaning steps, isolating the table, beginning html is irrelevant

tableHtml = html.split("\n")[19:]

# Parsing the table, adding to data structure
# format of structure is a list of lists: [[tableName1, tableURL1, description1], [tableName2...]]
data = []

tableName = ""
tableURL = ""
description = ""

for line in tableHtml:
    # New entry in data structure
    # Because the html for this table follows a common structure, the parsing can be hard coded
    if ("<TR>" in line):
        line = line.replace("&nbsp; ", "0")
        tableURL = line[17:30]
        description = line[55:]
        tableName = line[32:42]
    # End of an entry, must check to see if there is a month in the description, add to data if so
    elif ("</TR>" in line):
        stripped = " " + line.lstrip()
        description += stripped[:len(stripped)-10]

        for word in description.split():
            if word in MONTHS:
                data.append([tableName, tableURL, description])

        tableName = ""
        tableURL = ""
        description = ""
        
    # Middle entry, adds to description only
    else:
        stripped = " " + line.lstrip()
        description += stripped

for entry in data:
    absoluteURL = DATA_URL + entry[1]
    print(entry[0] + "\t" + absoluteURL)
