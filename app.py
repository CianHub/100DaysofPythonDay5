from collections import defaultdict, namedtuple, Counter, deque
import csv
import random
from urllib.request import urlretrieve

movie_data = 'https://raw.githubusercontent.com/pybites/challenges/solutions/13/movie_metadata.csv'
movies_csv = 'movies.csv'
urlretrieve(movie_data, movies_csv)

Movie = namedtuple('Movie', 'title year score')


def get_movies_by_director(data=movies_csv):
    """Extracts all movies from csv and stores them in a dictionary
       where keys are directors, and values is a list of movies (named tuples)"""
    directors = defaultdict(list)
    with open(data, encoding='utf-8') as f:
        # Converts each CSV line into an OrderedDict
        for line in csv.DictReader(f):
            # Extracts the values from the line
            try:
                director = line['director_name']
                movie = line['movie_title'].replace('\xa0', '')
                year = int(line['title_year'])
                score = float(line['imdb_score'])
            except ValueError:
                continue

            # Creates a new instance of Movie namedTuple using the values
            m = Movie(title=movie, year=year, score=score)

            # Creates a key for director and appends the Movie namedTuple to blank list the defaultDict was initialised with
            directors[director].append(m)

    return directors


get_movies_by_director()
