import csv
import requests
import unidecode
from bs4 import BeautifulSoup


# get list of all accreditted universities in Canada from 4icu
def getListOfSchools():
    print("getting list of schools")
    URL = 'https://www.4icu.org/ca/'
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')
    schools_table = soup.find(class_='table table-hover')

    # get top 30 schools
    schools = []
    for school in schools_table.find_all('tr'):
        school = school.find('a', href=True)
        # hard coded to remove wrong names
        if school.text not in ['rank','Add University', '']:
            schools.append(school.text.lower())
    schools = schools[:30]
    print(schools)
    return schools

# make links of schools based on their official name
def makeLinksOfSchools(schools):
    print("making links of schools")
    URLs = []
    URL_BASE = 'https://www.ratemyprofessors.com/search.jsp?query='
    for school in schools:
        query_string = school.replace(' ', '+').replace('\'', '%27')
        query_string = unidecode.unidecode(query_string)
        URL = URL_BASE + query_string
        URLs.append(URL)
    return URLs
    
# make links for all instructors on first page of school search results
def getProfLinksForSchool(URL):
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find(class_='search_results')

    prof_elems = results.find_all('li', class_='listing PROFESSOR')
    prof_links = []

    acc = 0

    # create an array of links on the first page
    for prof_elem in prof_elems:
        # will need this later to find gender
        prof_name = prof_elem.find('span', class_='main')
        prof_link = prof_elem.find('a', href=True)
        prof_links.append(prof_link['href'])
        acc += 1
    print("number of prof links:", acc)
    return prof_links

def printReviewsForProf(URL):
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    reviews = soup.find_all(class_='Rating__Comments-sc-1rhvpxz-1 edLmhN')

    with open('prof_links.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow(prof_name)

    # prints every review on the page (first 20)
    for review in reviews:
        print(review.text.strip())
        print(',')

def printRatingsForProf(URL):
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')
    ratings = soup.find_all(class_='RatingValues__RatingValue-sc-6dc747-3 cKZySD')

    # prints every rating on the page (first 20)
    for rating in ratings:
        print(rating.text.strip())
        print(',')

def getRatingsAndReview(URL):
    URL = "https://www.ratemyprofessors.com/" + URL
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    reviews = soup.find_all(class_='Rating__Comments-sc-1rhvpxz-1 edLmhN')
    ratings = soup.find_all(class_="RatingValues__RatingContainer-sc-6dc747-1 jDpwIp")

    #init arrays to hold ratings
    quality_ratings = [];
    difficulty_ratings = [];

    for rating in ratings:
        rating_text = rating.text.strip()
        if ("Quality" in rating_text):
            quality_ratings.append(rating_text[7:])

    for rating in ratings:
        rating_text = rating.text.strip()
        if ("Difficulty" in rating.text.strip()):
            difficulty_ratings.append(rating_text[10:])

    index = 0

    prof_name = soup.find(class_='NameTitle__Name-dowf0z-0 cjgLEI')
    print(prof_name.text.strip())

    school = soup.find(class_="NameTitle__Title-dowf0z-1 wVnqu")
    school = school.find('a', href=True).text.strip()

    # prints every review on the page (up to 20)
    # for review in reviews:
    #     with open('reviews.csv', 'a') as file:
    #         writer = csv.writer(file)
    #         writer.writerow([school, prof_name.text.strip(), review.text.strip(), quality_ratings[index], difficulty_ratings[index] ])
    #     index += 1


def printAllReviews(prof_links):
    for prof_link in prof_links:
        URL = 'https://www.ratemyprofessors.com' + prof_link
        print(URL)
        printReviewsForProf(URL)


schools = []
URLs = []
schools = getListOfSchools()        
URLs = makeLinksOfSchools(schools)

# initialize array to hold individual RMP pages
prof_links = []

for URL in URLs:
    prof_links = getProfLinksForSchool(URL)
    #for prof_link in prof_links:
        #getRatingsAndReview(prof_link)
     # current count of different profs is 1717
