import requests
import random
from faker import Faker  # Import Faker library for generating fake data
from datetime import datetime, timedelta

fake = Faker()

def generate_random_birthdate():
    start_date = datetime(1900, 1, 1)
    end_date = datetime.now() - timedelta(days=365*18)  # Assuming authors are at least 18 years old
    random_date = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))
    return random_date.strftime("%Y-%m-%d")

def generate_random_nationality():
    nationalities = ["American", "British", "Canadian", "French", "German", "Japanese", "Russian", "Chinese", "Indian"]
    return random.choice(nationalities)

def generate_random_address():
    return fake.address()

def generate_random_phone_number():
    return fake.phone_number()

def fetch_random_books(num_books=2000):
    base_url = "https://www.googleapis.com/books/v1/volumes"
    books = []
    iterations = 0

    while len(books) < num_books:
        # Generate a random index to get a random page of books
        random_index = str(random.randint(1, 100))
        params = {
            "q": "subject:fiction",  # You can adjust the query to fit your needs
            "startIndex": random_index,
            "maxResults": min(40, num_books - len(books)),  # Limiting to 40 to avoid exceeding API limits
            "orderBy": "newest"  # You can change the order if needed
        }
        response = requests.get(base_url, params=params)
        iterations += 1

        if response.status_code == 200:
            data = response.json()
            books.extend(data.get("items", []))
        else:
            print("Failed to fetch books:", response.status_code)
            break

    for i, book in enumerate(books[:num_books], start=1):
        title = book['volumeInfo']['title']
        authors_info = book['volumeInfo'].get('authors', ['Unknown'])
        authors = ", ".join(authors_info)
        publisher = book['volumeInfo'].get('publisher', 'Unknown Publisher')
        published_date = book['volumeInfo'].get('publishedDate', 'Unknown')
        isbn_13 = next((identifier['identifier'] for identifier in book['volumeInfo'].get('industryIdentifiers', []) if identifier['type'] == 'ISBN_13'), 'Unknown')
        page_count = book['volumeInfo'].get('pageCount', 'Unknown')
        average_rating = book['volumeInfo'].get('averageRating', 'Unknown')
        
        # Generate random birthdate and nationality for each author
        authors_birthdates = [generate_random_birthdate() for _ in authors_info]
        authors_nationalities = [generate_random_nationality() for _ in authors_info]
        
        # Generate random address and phone number for publisher
        publisher_address = generate_random_address()
        publisher_phone = generate_random_phone_number()

        print(f"{i}. {title}")
        print(f"   Authors: {authors}")
        for author, birthdate, nationality in zip(authors_info, authors_birthdates, authors_nationalities):
            print(f"      - {author}: Birthdate: {birthdate}, Nationality: {nationality}")
        print(f"   Publisher: {publisher}")
        print(f"      - Address: {publisher_address}")
        print(f"      - Phone: {publisher_phone}")
        print(f"   Published Date: {published_date}")
        print(f"   ISBN-13: {isbn_13}")
        print(f"   Page Count: {page_count}")
        print(f"   Average Rating: {average_rating}")
        print(f"   Iteration: {iterations}")
        print()

    return books[:num_books]

