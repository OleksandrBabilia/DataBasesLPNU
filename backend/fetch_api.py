import requests
import pprint

url = 'https://openlibrary.org/' 
api_key = 'AIzaSyCLLuhOenMpFBMKRdAKP_QtbBgBagvKt8Y'


def get_books(suffix: str):
    response = requests.get(url+suffix)
    return response.json()

search_suffix = 'search.json?q=harry+potter' 
subject_suffix = 'subjects/fiction.json'

books = get_books(subject_suffix)

print(len(books['works']))

for book in books['works']:
    print(book['title'])
