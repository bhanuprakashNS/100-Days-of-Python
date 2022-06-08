# ............. Scraping Empire online website to get Top 100 movies' names .......... #
# ........... Created and modified by N.S.Bhanuprakash on 28-04-2022 ................. #

import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

website = requests.get(URL)
website_html = website.text

soup = BeautifulSoup(website_html, "html.parser")
# print(soup.prettify())

# with open("movie_website.html", "w") as file:
#     file.write(soup.prettify())

titles = soup.find_all(name="h3", class_="title")
# print(titles)

movie_list = []
with open("movies_list.txt", "w") as file:
    for num in range(len(titles)-1, -1, -1):
        movie_detail = titles[num].string
        movie_list.append(movie_detail)
        file.write(f"{movie_detail}\n")
print(movie_list)
# ................. OR .......................... #
# movie_list = [movie.string for movie in titles]
# movie_list = movie_list[::-1]
# with open("movies_list.txt", "w") as file:
#     for movie in movie_list:
#         file.write(f"{movie}\n")
# print(movie_list)
# ............................................... #
