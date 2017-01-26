import csv

claim_data = {}

# {22: {'Female':0, 'Male': 0, 'Ages < 65':0, 'Ages 65 - 74': 0, 'Ages 75+': 0}}


def grab_row(raw_file):
    with open('data.csv', 'r') as data_in:
        reader = csv.DictReader(data_in)
        for row in reader:
            filter(row)


def filter(line):
    state = int(line['State Code from Claim (SSA)'])
    gender = int(line['Gender Code from Claim'])
    age = int(line['LDS Age Category'])

    male = 0
    female = 0
    less65 = 0
    less74 = 0
    greater75 = 0

    if gender == 0:
        pass
    elif gender == 1:
        male += 1
    elif gender == 2:
        female += 1

    if age == 0:
        pass
    elif age == 1:
        less65 += 1
    elif age == 2 or age == 3:
        less74 += 1
    elif age == 4 or age == 5 or age == 6:
        greater75 += 1

    if state not in claim_data:
        claim_data[state] = {'Female': female, 'Male': male, 'Ages < 65': less65,
                             'Ages 65 - 74': less74, 'Ages 75+': greater75}
    else:
        female = female + claim_data[state]['Female'],
        male = male + claim_data[state]['Male'],
        less65 = less65 + claim_data[state]['Ages < 65'],
        less74 = less74 + claim_data[state]['Ages 65 - 74'],
        greater75 = greater75 + claim_data[state]['Ages 75+']
        claim_data[state] = {'Female': female, 'Male': male, 'Ages < 65': less65,
                             'Ages 65 - 74': less74, 'Ages 75+': greater75}


grab_row('data.csv')
print(len(claim_data))

print(claim_data[22], claim_data[22]['Female'], type(claim_data[22]['Female']))
print(claim_data[1])
