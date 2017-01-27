import csv

claim_data = {}
STATE = 'State'
FEMALE = 'Female'
MALE = 'Male'
AGE_LOW = 'Ages < 65'
AGE_MID = 'Ages 65 - 74'
AGE_HIGH = 'Ages 75+'


def grab_row(raw_file):
    with open('data.csv', 'r') as data_in:
        reader = csv.DictReader(data_in)
        for row in reader:
            filter(row)


def filter(line):
    state = int(line['State Code from Claim (SSA)'])
    gender = int(line['Gender Code from Claim'])
    age = int(line['LDS Age Category'])

    maleCount = 0
    femaleCount = 0
    less65 = 0
    less74 = 0
    greater75 = 0

    if gender == 0:
        pass
    elif gender == 1:
        maleCount += 1
    elif gender == 2:
        femaleCount += 1

    if age == 0:
        pass
    elif age == 1:
        less65 += 1
    elif age == 2 or age == 3:
        less74 += 1
    elif age == 4 or age == 5 or age == 6:
        greater75 += 1

    if state not in claim_data:
        claim_data[state] = {STATE: state, FEMALE: femaleCount, MALE: maleCount, AGE_LOW: less65,
        AGE_MID: less74, AGE_HIGH: greater75}
    else:
        currState = claim_data[state]
      # print(str(claim_data[state][FEMALE]) + ' (' + str(type(claim_data[state][FEMALE])) + ")")
        currState[STATE] = state
        currState[FEMALE] += femaleCount
        currState[MALE] += maleCount
        currState[AGE_LOW] += less65
        currState[AGE_MID] += less74
        currState[AGE_HIGH] += greater75


def write():
    selection = 0
    with open('DataOut.csv', 'w') as TargetFile:
        fieldnames = [STATE, FEMALE, MALE, AGE_LOW, AGE_MID, AGE_HIGH]
        writer = csv.DictWriter(TargetFile, fieldnames=fieldnames)
        writer.writeheader()
        while selection in range (0, 100):

            try:
                writer.writerow(claim_data[selection])
            except KeyError:
                pass
            finally:
                selection += 1


def main():
    print('Grabbing data...')
    grab_row('data.csv')
    print('Writing your new file DataOut.csv.')
    write()
    print('Writing file complete.')

if __name__ == '__main__':
    main()
