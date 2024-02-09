import pandas as pd
import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/top/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    movies = soup.find(
        "ul",
        class_="ipc-metadata-list ipc-metadata-list--dividers-between sc-71ed9118-0 kxsUNk compact-list-view ipc-metadata-list--base",
    ).find_all(
        "li", class_="ipc-metadata-list-summary-item sc-1364e729-0 caNpAE cli-parent"
    )

    data = []
    for movie in movies:
        name = movie.find("h3", class_="ipc-title__text").text.strip("1234567890. ")

        rank = (
            movie.find("h3", class_="ipc-title__text")
            .get_text(strip=True)
            .split(".")[0]
        )
        year = movie.find(
            "span", class_="sc-be6f1408-8 fcCUPU cli-title-metadata-item"
        ).text
        rating = (
            movie.find(
                "span",
                class_="ipc-rating-star ipc-rating-star--base ipc-rating-star--imdb ratingGroup--imdb-rating",
            )
            .text.split("(")[0]
            .strip()
        )

        data.append([rank, name, year, rating])

    df = pd.DataFrame(data, columns=["Movie Rank", "Movie Name", "Release Year", "Rating"])
    df.to_csv("TOP_Rated_Movies.csv", index=False)
    print("Successfully scraped data from IMDb and saved as 'TOP_Rated_Movies.csv'")
else:
    print("Failed to retrieve data from IMDb. Status Code:", response.status_code)
