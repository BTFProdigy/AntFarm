import csv
import os

MY_FILE = str(os.getcwd() + '/test.csv')
print(MY_FILE)

magcost = []
lootcost = []

# open csv and pull columns into dict
with open('test.csv') as csv_in:
    csv_read = csv.DictReader(csv_in)
    for row in csv_read:
        print (row)
        value = row['cost']
        if row['dep'] != 'icu':
            try:
                magcost.append(float(value))
            except ValueError:
                print(
                    "Could not convert '{}' to "
                    "a float...skipping.".format(value)
                )
        else:
            try:
                lootcost.append(float(value))
            except ValueError:
                print(
                    "Could not convert '{}' to "
                    "a float...skipping.".format(value)
                )



print(sum(magcost))

print(sum(lootcost))
