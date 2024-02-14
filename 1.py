import csv
import requests
from bs4 import BeautifulSoup

url = "https://www2.daad.de/deutschland/studienangebote/international-programmes/en/result/?q=&degree%5B%5D=2&degree%5B%5D=10&lang%5B%5D=2&fos=&cert=&admReq=&langExamPC=&scholarshipLC=&langExamLC=&scholarshipSC=&langExamSC=&langDeAvailable=&langEnAvailable=&lvlEn%5B%5D=&modStd%5B%5D=7&cit%5B%5D=&tyi%5B%5D=1&ins%5B%5D=&fee=1&bgn%5B%5D=&dat%5B%5D=&prep_subj%5B%5D=&prep_degree%5B%5D=&sort=4&dur=&subjects%5B%5D=&limit=10&offset=&display=grid#tab_result-grid"

# Send a GET request to the URL
response = requests.get(url)

# Check if the status code is 200
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all elements with class 'c-ad-carousel c-masonry__item c-masonry__item--result-list mb-5'
    courses = soup.find_all('div', class_='c-ad-carousel c-masonry__item c-masonry__item--result-list mb-5')

    # Open CSV file in write mode
    with open('courses.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        
        # Write header row
        writer.writerow(['Name', 'University', 'Subject', 'Languages', 'Beginning', 'Duration', 'Tuition Fees per Semester'])
        
        # Loop through each course
        for course in courses:
            # Extract name
            name = course.find('span', class_='js-course-title u-hide@sm').text.strip()

            # Extract university
            university = course.find('span', class_='c-ad-carousel__subtitle c-ad-carousel__subtitle--small js-course-academy').text.strip()

            # Extract subject
            subject = course.find('ul', class_='c-ad-carousel__data-list c-ad-carousel__data-list--not-colored p-0').find('li').text.strip()

            # Extract languages
            languages = course.find_all('ul', class_='c-ad-carousel__data-list c-ad-carousel__data-list--not-colored p-0')[1].find('li').text.strip()

            # Extract beginning
            beginning = course.find_all('ul', class_='c-ad-carousel__data-list c-ad-carousel__data-list--not-colored p-0')[2].find('li').text.strip()

            # Extract duration
            duration = course.find_all('ul', class_='c-ad-carousel__data-list c-ad-carousel__data-list--not-colored p-0')[3].find('li').text.strip()

            # Extract tuition fees per semester
            tuition_fees = course.find_all('ul', class_='c-ad-carousel__data-list c-ad-carousel__data-list--not-colored p-0')[4].find('li').text.strip()

            # Write row to CSV file
            writer.writerow([name, university, subject, languages, beginning, duration, tuition_fees])
else:
    print("Failed to retrieve data. Status code:", response.status_code)
