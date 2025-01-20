import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

#Uses beautiful soup to scrape an article of the best movies of all time. It then puts the list into
# a file, sorting it from 1 - 100.
request = requests.get(URL)
soup = BeautifulSoup(request.content, 'html.parser')
movies = soup.find_all('h3',class_='title')
movie_list = []

for movie in movies:
    movie_list.append(movie.text)
movie_list.reverse()

with open('movie_list.txt', 'w') as file:
    file.write('\n'.join(movie_list))

