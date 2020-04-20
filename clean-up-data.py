import csv
from gendersets import female_duplicates_set
from gendersets import male_duplicates_set

def removeDuplicates(words):
    cleaned_set= []
    for word in words:
        word = word.lower()
        if word not in cleaned_set:
            cleaned_set.append(word)
    return cleaned_set


female_set = []
#female_set = removeDuplicates(female_duplicates_set)
print(female_set)

male_set = []
#male_set = removeDuplicates(male_duplicates_set)
print(male_set)

def merge_files():
# code for combining datasets
# import csv
    reader = csv.reader(open('../data/regression2.csv', 'r'))
    reader1 = csv.reader(open('../data/num-words.csv', 'r'))
    writer = csv.writer(open('../data/regression.csv', 'w'))
    for row in reader:
         row1 = next(reader1)
         writer.writerow(row + row1)

merge_files()