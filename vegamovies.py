import pandas as pd
import re
import requests
from bs4 import BeautifulSoup

url = "https://vegamovies.ngo/"

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    movies = soup.find("div", class_="site__row sidebar-direction").find_all(
        "div", class_="post-item-wrap"
    )
    s_n = 0
    data = []
    for movie in movies:
        name = movie.find("h3", class_="entry-title h5 h6-mobile post-title").a
        title = name.text
        year = title.split("(")[1].split(")")[0]
        name_title = title.split(") ")[1].split(" {")[0]
        info = title.split("(")[-1].split(")")[0].strip()
        resolution_info = title.split("|")[-1].strip()
        url = name.get("href")

        # Add a check to ensure that the title string contains curly braces
        if "{" in title and "}" in title:
            langauage = title.split("{")[1].split("}")[0]
        else:
            langauage = "Language not available"

        s_n += 1
        data.append([s_n, name_title, year, info, resolution_info, langauage, url])
    df = pd.DataFrame(
        data,
        columns=[
            "S.N.",
            "Name",
            "Year",
            "Info",
            "Resolution Info",
            "Language",
            "URL",
        ],
    )
    # Save DataFrame to a CSV file
    df.to_csv("vegamovies_data.csv", index=False)
    print("Data saved to vegamovies_data.csv successfully.")

else:
    print("Failed to retrieve data from Vegamovie. Status Code:", response.status_code)
