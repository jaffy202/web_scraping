import requests
from bs4 import BeautifulSoup

response = requests.get('https://web.archive.org/web/20200518073855/https:'
                        '//www.empireonline.com/movies/features/best-movies-2/')
mov_web_page = response.text

soup = BeautifulSoup(mov_web_page, 'html.parser')

movies_tag = soup.find_all('h3', class_='title')
movies_list = []
for tag in movies_tag:
    movie = tag.getText()
    movies_list.append(movie)

ordered_movies_list = movies_list[::-1]

with open('movies.txt', 'w', encoding='utf-8') as file:
    for ranked_movie in ordered_movies_list:
        file.write(f"{ranked_movie}\n")
