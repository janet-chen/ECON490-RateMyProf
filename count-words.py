from __future__ import division
import csv
import nltk
from string import punctuation

from gendersets import female_set
from gendersets import male_set

#tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

# this code reads each review and counts the number of male or female biased words and wries it in a new document
def assignGenderBias(review, gender):
    male_count = 0
    female_count = 0
    words = review.split()
    for word in words:
        word = word.lower()
        if word in female_set:
            female_count += 1
        if word in male_set:
            male_count += 1
    
    if gender == "female":
        return female_count
    else:
        return male_count

def countMaleWords():
    with open('../data/reviews.csv', 'r') as instr:
        with open('../data/male-bias-scores.csv', 'w') as ostr:
            # allows to read each line as row[0], row[1], etc
            csv_reader = csv.reader(instr, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    print(f'Column names are {", ".join(row)}')
                    line_count += 1
                else:
                    review = row[2]
                    GBscore = assignGenderBias(review, "male")
                    print(GBscore, file=ostr)
                    line_count += 1
            print(f'Processed {line_count} lines.')

def countFemaleWords():
    with open('../data/reviews.csv', 'r') as instr:
        with open('../data/female-bias-scores.csv', 'w') as ostr:
            # allows to read each line as row[0], row[1], etc
            csv_reader = csv.reader(instr, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    print(f'Column names are {", ".join(row)}')
                    line_count += 1
                else:
                    review = row[2]
                    GBscore = assignGenderBias(review, "female")
                    print(GBscore, file=ostr)
                    line_count += 1
            print(f'Processed {line_count} lines.')

def countWordsFem():
    with open('../data/regression.csv', 'r') as instr:
        with open('../data/num-words.csv', 'w') as ostr:
            # allows to read each line as row[0], row[1], etc
            csv_reader = csv.reader(instr, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    print(f'Column names are {", ".join(row)}')
                    line_count += 1
                else:
                    fem_words = row[7]
                    total_words = row[8]
                    normalizedScore = int(fem_words)  / int(total_words)
                    print(normalizedScore, file=ostr)
                    line_count += 1
            print(f'Processed {line_count} lines.')


def countWordsMale():
    with open('../data/regression.csv', 'r') as instr:
        with open('../data/num-words.csv', 'w') as ostr:
            # allows to read each line as row[0], row[1], etc
            csv_reader = csv.reader(instr, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    print(f'Column names are {", ".join(row)}')
                    line_count += 1
                else:
                    male_words = row[6]
                    total_words = row[8]
                    normalizedScore = int(male_words)  / int(total_words)
                    print(normalizedScore, file=ostr)
                    line_count += 1
            print(f'Processed {line_count} lines.')


countWordsMale()

def normalizeGenderedWordsByTotalWords():
    with open('../data/regression.csv', 'r') as instr:
        with open('../data/normalized-gender-wordcount.csv', 'w') as ostr:
            # allows to read each line as row[0], row[1], etc
            csv_reader = csv.reader(instr, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    print(f'Column names are {", ".join(row)}')
                    line_count += 1
                else:
                    review = row[2]
                    numWords = len(review.split())
                    print(numWords, file=ostr)
                    line_count += 1
            print(f'Processed {line_count} lines.')

def calculateBiasScore(female_wordcount, male_wordcount):
    if female_wordcount > male_wordcount:
        gender_bias_score = female_wordcount / (female_wordcount + male_wordcount)
        print(gender_bias_score)
        return gender_bias_score
    if female_wordcount < male_wordcount:
        gender_bias_score = male_wordcount / (female_wordcount + male_wordcount)
        print(gender_bias_score)
        return gender_bias_score
    if female_wordcount == male_wordcount:
        return 0

def printBiasScore():
    with open('../data/bias-word-counts.csv', 'r') as instr:
        with open('../data/bias-scores.csv', 'w') as ostr:
            # allows to read each line as row[0], row[1], etc
            csv_reader = csv.reader(instr, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    print(f'Column names are {", ".join(row)}')
                    line_count += 1
                else:
                    female_wordcount = row[0]
                    male_wordcount = row[1]
                    GBscore = calculateBiasScore(female_wordcount, male_wordcount)
                    print(GBscore, file=ostr)
                    line_count += 1
            print(f'Processed {line_count} lines.')
