from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.hollywoodreporter.com/lists/100-best-films-ever-hollywood-favorites-818512")
movie_webpage = response.text
soup = BeautifulSoup(movie_webpage, "html.parser")

movies = soup.find_all(name="h1", class_="list-item__title")
movie_list = [movie.getText() for movie in movies]
movie_list_reverse = movie_list[::-1]
print(movie_list_reverse)

for num in range(len(movie_list_reverse)):
    data = f"{num+1}) {movie_list_reverse[num]}\n"
    with open("movies.txt", mode="a") as file:
        file.write(data)
