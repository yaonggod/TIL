import json
from pprint import pprint

    

def movie_info(movies, genres):
    movies_list = []
    for movie in movies:
        genre_names = []
        for id in movie['genre_ids']: # [18, 80]
            for genre in genres: # [{}, {}, {}, ...]
                for key, value in genre.items(): # {"id": 28, "name": "Action"}
                    if value == id:
                        genre_names.append(genre['name'])
                
        movies_list.append({'genre_names' : genre_names,
                'id' : movie['id'],
                'overview' : movie['overview'],
                'title' : movie['title'],
                'vote_average' : movie['vote_average']})
            
    return movies_list
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))