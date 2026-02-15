import os,json

FILENAME = "movies.json"

def load_movies():
    if not os.path.exists(FILENAME):
        return []
    with open(FILENAME,'r',encoding='utf-8') as f:
        return json.load(f)
        
def save_movies(movies):
    with open(FILENAME,'w',encoding='utf-8') as f:
        json.dump(movies,f,indent=2)

def add_movies(movies):
    title = input('Enter name of movie :').strip()
    
    if any(movie["title"].lower() == title.lower() for movie in movies):
        print('Movie already exists!')
        return
        
    genre = input('Whats the genre of movie :').strip()
    
    try:
        rating = float(input('Enter rating(0-10) :'))
        if not 0 <= rating <= 10:
            raise ValueError
        
    except ValueError:
        print('please enter a valid number')
        return
    
    movies.append(
        {
            "title":title,
            "genre":genre,
            "rating":rating
        }
    )
    save_movies(movies)
    print('Movie added')
    
def search_movies(movies):
    term = input('Enter name of movie or genre to search :').strip().lower()
    results = [
        movie for movie in movies
        if term in movie['title'].lower() or term in movie['genre'].lower()
        
    ]
    if not results:
        print('No matches found')
        return
    print(f'Found {len(results)} matches')
    
    for movie in results:
        print(f'{movie["title"]} -- {movie["genre"]} -- {movie["rating"]}/10')
        
        
def view_movies(movies):
    if not movies:
        print('No movies in database')
        return
    print(f'Total movies: {len(movies)}')
    for movie in movies:
        print(f'{movie["title"]} -- {movie["genre"]} -- {movie["rating"]}/10')

def run_movie_db():
    movies = load_movies()
    while True:
        print('\nMovie Database')
        print('1. Add Movie')
        print('2. View Movies')
        print('3. Search Movies')
        print('4. Exit')
        
        choice = input('Enter your choice :').strip()
        
        match choice:
            case '1':
                add_movies(movies)
            case '2':
                view_movies(movies)
            case '3':
                search_movies(movies)
            case '4':
                print('Goodbye!')
                break
            case _:
                print('Invalid choice, try again')

run_movie_db()