import json
from pprint import pprint


def movie_info(movie, genres):
    genre_names = []
    for id in movie['genre_ids']: # [18, 80]
        for genre in genres: # [{}, {}, {}, ...]
            for key, value in genre.items(): # {"id": 28, "name": "Action"}
                if value == id:
                    genre_names.append(genre['name'])
                
    return {'genre_names' : genre_names,
            'id' : movie['id'],
            'overview' : movie['overview'],
            'title' : movie['title'],
            'vote_average' : movie['vote_average']}
        

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))