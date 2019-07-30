from tmdbv3api import TMDb
tmdb = TMDb()
tmdb.api_key = 'API Key'

tmdb.language = 'en'
tmdb.debug = True

from tmdbv3api import Movie
movie = Movie()

def movieSearch(movieName):
    search = movie.search(movieName)
    
    return search[1].title