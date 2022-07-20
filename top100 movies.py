import requests
from bs4 import BeautifulSoup

response = requests.get("https://web.archive.org/web/20200518055830/https://www.empireonline.com/movies/features/best-movies-2/")
website_response = response.text


soup = BeautifulSoup(website_response, "html.parser")

all_movies = soup.find_all(name="h3", class_="title")
movie = []
movie_title = [item.getText() for item in all_movies]
list_of_movies = (movie_title[::-1])

with open("movie_list.text", mode='w') as data:
    for i in list_of_movies:
        data.write(f"{i}\n")
