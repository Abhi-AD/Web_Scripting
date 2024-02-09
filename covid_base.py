# # # #connecting for the other website
from bs4 import BeautifulSoup
import requests
url = BeautifulSoup('https://www.worldometers.info/coronavirus/', 'html.parser')
print(url)
soup = requests.get(url)
print(soup)


# # # #show the data in the code
row_data = soup.text
row_data = BeautifulSoup(row_data, "lxml")
# print(row_data)


# # # #select data
table_code = row_data.table
# print(table_code)



# # # #selecting data
tags = table_code.find_all('tr')
# print(tags)


# # # #collecting the data
data = []
for tag in tags:
    y = tag.text.split('\n')
    if y[1] !="":
        data.append(y[1:])
# print(data)


# # # # # save the data in csv file
# import csv
# file = open('covid_data.csv', 'w')
# a = csv.writer(file)
# a.writerows(data)
# file.close()





# # # pandas select data
import pandas as pd
df = pd.read_csv('covid_data.csv', encoding="latin1")
# print(df)

# # # Replacing ',' from dataframe
country = df['Country,Other']
TotalCases = df['TotalCases'].dropna()
Totalrecovered = df['TotalRecovered'].dropna()
New_TotalCases = list(map(lambda x: int(x.replace(',', '')), list(TotalCases)))
New_Totalrecovered = list(map(lambda x: int(x.replace(',', '')), list(Totalrecovered)))
# print(TotalCases)



# # Visualizing the data
import plotly.graph_objects as go
fig = go.Figure([go.Bar(x=country[0:10], y=New_TotalCases[0:10])])
fig.show()



import plotly.graph_objects as go
fig = go.Figure(data=[
    go.Bar(name='TotalCases', x=country[0:10], y=New_TotalCases[0:10]),
    go.Bar(name='TotalRecovered', x=country[0:10], y=New_Totalrecovered[0:10])
])
# Change the bar mode
fig.update_layout(barmode='group')
fig.show()