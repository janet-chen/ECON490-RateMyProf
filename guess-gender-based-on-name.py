import gender_guesser.detector as gender
import csv
import re


d = gender.Detector()
def guessGender(name):
    return d.get_gender(name)

def getGender(fullname):
    #pattern = '(.*)\s'
    pattern = '^(\w*)'
    result = re.search(pattern, fullname)
    firstname_space = result.group()

    # get rid of whitespace after name
    # whitespace_pattern = '\s+'
    # replace = ''
    # firstname = re.sub(whitespace_pattern, replace, firstname_space) 

    gender = d.get_gender(firstname_space)
    return gender

with open('data/reviews.csv', 'r') as instr:
    with open('data/test_gender.csv', 'w') as ostr:
        # allows to read each line as row[0], row[1], etc
        csv_reader = csv.reader(instr, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                gender = getGender(row[1])
                print(gender, file=ostr)
                line_count += 1
        print(f'Processed {line_count} lines.')
