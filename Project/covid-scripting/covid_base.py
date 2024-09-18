# # # #connecting for the other website
from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd

url = BeautifulSoup("https://www.worldometers.info/coronavirus/", "html.parser")
# print(url)
soup = requests.get(url)
# print(soup)

# # # #show the data in the code
row_data = soup.text
row_data = BeautifulSoup(row_data, "lxml")
# print(row_data)


# # # #select data
table_code = row_data.table
# print(table_code)

# # # #selecting data
tags = table_code.find_all("tr")
# print(tags)


# # # #collecting the data
data = []
for tag in tags:
    y = tag.text.split(
        "\n"
    )  # split: 	Splits the string at the specified separator, and returns a list
    if y[1] != "":
        data.append(y[1:])
# print(data)


# 1. Save data to CSV using the `with open` method
with open("csv/covid_data.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("Data saved to covid_data.csv using the 'with open' method.")

# 2. Save data to CSV using the traditional `open/close` method
file = open("csv/covid_data.csv", "w", newline="", encoding="utf-8")
writer = csv.writer(file)
writer.writerows(data)
file.close()

print("Data saved to covid_data.csv using the traditional 'open' method.")

# Load and display the data using Pandas
df = pd.read_csv("csv/covid_data.csv", encoding="utf-8", header=None)
# print(df)
print(df.head(10))
