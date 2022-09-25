import time
from bs4 import BeautifulSoup
import requests


def scrape_online():
    print("Scraping online...")
    html_text = requests.get(
        'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation='
    ).text

    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

    for job in jobs:
        company_name = job.find('h3', class_='joblist-comp-name').text.strip()
        skills = job.find('span', class_='srp-skills').text.replace(' ', '').strip()
        published_date = job.find('span', class_='sim-posted').span.text
        salary = job.find('strong')
        more_info = job.header.h2.a['href']

        print('=' * 50)
        print(f'Company Name: {company_name}')
        print(f'Required Skills: {skills}')
        print(f'Published Date: {published_date}')
        print(f'More Info: {more_info}')
        print('=' * 50)


def scrape_local():
    with open('home.html', 'r') as html_file:
        content = html_file.read()

        soup = BeautifulSoup(content, 'lxml')

        course_cards = soup.find_all('div', class_='card')
        for course in course_cards:
            course_name = course.h5.text
            course_price = course.a.text.split()[-1]

            print(f'{course_name} costs {course_price}')


if __name__ == "__main__":
    while True:
        scrape_online()
        time.sleep(5)
