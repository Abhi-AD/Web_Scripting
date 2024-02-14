import openpyxl
import requests
from bs4 import BeautifulSoup

url = "https://www2.daad.de/deutschland/studienangebote/international-programmes/en/result/?q=&degree%5B%5D=2&degree%5B%5D=10&lang%5B%5D=2&fos=&cert=&admReq=&langExamPC=&scholarshipLC=&langExamLC=&scholarshipSC=&langExamSC=&langDeAvailable=&langEnAvailable=&lvlEn%5B%5D=&modStd%5B%5D=7&cit%5B%5D=&tyi%5B%5D=1&ins%5B%5D=&fee=1&bgn%5B%5D=&dat%5B%5D=&prep_subj%5B%5D=&prep_degree%5B%5D=&sort=4&dur=&subjects%5B%5D=&limit=10&offset=&display=grid#tab_result-grid"

response = requests.get(url)
if response.status_code == 200:
    html_content = response.text

    # Parse HTML with BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find all div elements with class "c-ad-carousel__result-list-item"
    div_elements = soup.find_all('div', class_='c-ad-carousel__result-list-item')

    if div_elements:
        print(f"Found {len(div_elements)} courses.")

        # Create an Excel workbook and sheet
        workbook = openpyxl.Workbook()
        sheet = workbook.active

        # Write header row
        header = ['Course_name', 'Course_Subject', 'Course_language', 'Beginner', 'Course_Durations', 'Tuition_fee/years']
        sheet.append(header)

        # Iterate over div elements and extract information
        for div in div_elements:
            print(div.prettify())  # Print the div element for inspection
            # Extract Course_name
            course_name = div.find('span', class_='h-da-result-title')
            course_name = course_name.text.strip() if course_name else ''
            print(course_name)  # Print the extracted course name

            # Extract Course_Subject
            course_subject = div.find('span', class_='h-da-result-fos')
            course_subject = course_subject.text.strip() if course_subject else ''
            print(course_subject)  # Print the extracted course subject

            # Extract Course_language
            course_language = div.find('span', class_='h-da-result-lang')
            course_language = course_language.text.strip() if course_language else ''
            print(course_language)  # Print the extracted course language

            # Extract Beginner
            beginner = div.find('span', class_='h-da-result-start')
            beginner = beginner.text.strip() if beginner else ''
            print(beginner)  # Print the extracted beginner information

            # Extract Course_Durations
            course_durations = div.find('span', class_='h-da-result-duration')
            course_durations = course_durations.text.strip() if course_durations else ''
            print(course_durations)  # Print the extracted course duration

            # Extract Tuition_fee/years
            tuition_fee = div.find('span', class_='h-da-result-tuition-fee')
            tuition_fee = tuition_fee.text.strip() if tuition_fee else ''
            print(tuition_fee)  # Print the extracted tuition fee

            # Write data to Excel sheet
            sheet.append([course_name, course_subject, course_language, beginner, course_durations, tuition_fee])

        # Save the workbook
        workbook.save('DAAD.xlsx')
        print("Excel file 'DAAD.xlsx' created successfully.")
    else:
        print("No courses found on the page.")
else:
    print("Failed to fetch the page:", response.status_code)
