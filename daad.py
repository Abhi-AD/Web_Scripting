import re
import requests
from bs4 import BeautifulSoup

url = "https://www2.daad.de/deutschland/studienangebote/international-programmes/en/result/?q=&degree%5B%5D=2&degree%5B%5D=10&lang%5B%5D=2&fos=&cert=&admReq=&langExamPC=&scholarshipLC=&langExamLC=&scholarshipSC=&langExamSC=&langDeAvailable=&langEnAvailable=&lvlEn%5B%5D=&modStd%5B%5D=7&cit%5B%5D=&tyi%5B%5D=1&ins%5B%5D=&fee=1&bgn%5B%5D=&dat%5B%5D=&prep_subj%5B%5D=&prep_degree%5B%5D=&sort=4&dur=&subjects%5B%5D=&limit=10&offset=&display=grid#tab_result-grid"

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    div_elements = soup.find_all(
        "div", class_="c-ad-carousel c-masonry__item c-masonry__item--result-list mb-5"
    )
    
    for div in div_elements:
        # Extract Course_name
        course_name = div.find("span", class_="js-course-title u-hide@sm")
        course_name = course_name.text if course_name else " "

        # Extract Course_Subject
        course_subject = div.find(
            "span",
            class_="c-ad-carousel__data-item c-ad-carousel__data-item--single-line",
        )
        course_subject = course_subject.text if course_subject else " "

        # Extract Course_language
        course_language = div.find_all(
            "span",
            class_="c-ad-carousel__data-item c-ad-carousel__data-item--single-line",
        )
        course_language = course_language[1].text if len(course_language) > 1 else " "

        # Extract Beginner
        beginner = div.find_all(
            "span",
            class_="c-ad-carousel__data-item c-ad-carousel__data-item--single-line",
        )
        beginner = beginner[2].text if len(beginner) > 2 else " "

        # Extract Course_Durations
        course_durations = div.find_all(
            "span",
            class_="c-ad-carousel__data-item c-ad-carousel__data-item--single-line",
        )
        course_durations = (
            course_durations[3].text if len(course_durations) > 3 else " "
        )

        # Extract Tuition_fee/years
        tuition_fee = div.find_all(
            "span",
            class_="c-ad-carousel__data-item c-ad-carousel__data-item--single-line",
        )
        tuition_fee = tuition_fee[4].text if len(tuition_fee) > 4 else " "
        
        # Print the extracted data
        print("Course Name:", course_name)
        print("Course Subject:", course_subject)
        print("Language:", course_language)
        print("Beginner:", beginner)
        print("Duration:", course_durations)
        print("Tuition Fee:", tuition_fee)
        print("\n")

else:
    print("Failed to retrieve data from the URL. Status Code:", response.status_code)
