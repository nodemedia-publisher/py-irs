import hgsysinc
from hgstat_test_movie import hgstat_get_genres_similarity_by_movieId2
from hgstat_test_movielens import (
    hgstat_dicts_movielens,
)
#---------------
# movies 데이터를 사전으로 변환
#---------------
ModifyTilteYear = True # 'title'을 정확하게 찾으려면 이렇게 호출
# 'Toy Story (1995)' --> 'Toy Story'와 '(1995)'로 분리

title_dict_, genres_dict, movies = hgstat_dicts_movielens(ModifyTilteYear=ModifyTilteYear)
#=print('title_dict:', len(title_dict_))
print(f'genres_dict [{len(genres_dict)}]:')

#----------------
#----------------
# 'Toy Story'와 'Groundhog Day' 장르 유사도 측정
#=FindInx = 0 # 첫 번째 영화() #= 0: Toy Story
FindMovieId = 1 # 첫 번째 영화() #= : Toy Story
CompMovieId = 1265 # 'Groundhog Day'

print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
print('# 장르 가중치 기준(장르 포함 일치) ')
print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
#=GenresRawMode = True # {GenresRawMode:True} 장르 가중치 적용(장르 포함 일치)
GenreSimilarity, GenreIntersec = hgstat_get_genres_similarity_by_movieId2 \
            (FindMovieId, CompMovieId, genres_dict, GenresRawMode=True)
print(f'[{FindMovieId} ^ {CompMovieId}] GenreSimilarity: %.3f' % GenreSimilarity)
print(f'GenreIntersec [{len(GenreIntersec)}] : {GenreIntersec}')
print(),print(),print()

print('#----------------')
print('#----------------')
# 'Toy Story'와 'Monsters, Inc.' 장르 유사도 측정
#=FindInx = 0 # 첫 번째 영화() #= 0: Toy Story
FindMovieId = 1 # 첫 번째 영화() #= : Toy Story
CompMovieId = 4886 # 'Monsters, Inc.'

print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
print('# 장르 가중치 기준(장르 포함 일치) ')
print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
#=GenresRawMode = True # {GenresRawMode:True} 장르 가중치 적용(장르 포함 일치)
GenreSimilarity, GenreIntersec = hgstat_get_genres_similarity_by_movieId2 \
            (FindMovieId, CompMovieId, genres_dict, GenresRawMode=True)
print(f'[{FindMovieId} ^ {CompMovieId}] GenreSimilarity: %.3f' % GenreSimilarity)
print(f'GenreIntersec [{len(GenreIntersec)}] : {GenreIntersec}')
#=print(),print(),print()



'''
처리 결과:
=============================================

genres_dict [9742]:
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# 장르 가중치 기준(장르 포함 일치)
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
[1 ^ 1265] GenreSimilarity: 0.400
GenreIntersec [2] : {'Comedy', 'Fantasy'}



#----------------
#----------------
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# 장르 가중치 기준(장르 포함 일치)
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
[1 ^ 4886] GenreSimilarity: 1.000
GenreIntersec [5] : {'Fantasy', 'Animation', 'Children', 'Adventure', 'Comedy'}

'''
