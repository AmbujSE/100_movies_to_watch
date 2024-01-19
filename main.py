import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
web_page = response.text
soup = BeautifulSoup(web_page, 'html.parser')
movie_list = []
for movie in soup.find_all(name="h3", class_="title"):
    movie_list.append(movie.getText())

movie_list = movie_list[::-1]
print(movie_list)
# n = -1
# while n > -101:
#     print(movie_list[n])
#     n -= 1

with open("movies.txt", "w", encoding="utf-8") as file:
    for movie in movie_list:
        file.write(f"{movie}\n")
