import hgsysinc
from hgstat_test_movielens import hgstat_dicts_movielens
#---------------
# format: movies
#---------------
# movieId,title,genres
# 1,Toy Story (1995),Adventure|Animation|Children|Comedy|Fantasy
# 2,Jumanji (1995),Adventure|Children|Fantasy
# 3,Grumpier Old Men (1995),Comedy|Romance
#---------------
ModifyTilteYear = True # 'title'을 정확하게 찾으려면 이렇게 호출
# 'Toy Story (1995)' --> 'Toy Story'와 '(1995)'로 분리

title_dict, genres_dict, movies_ = \
    hgstat_dicts_movielens(ModifyTilteYear=ModifyTilteYear)
print('title_dict:', len(title_dict))
print(f'genres_dict:', len(genres_dict))
print()
print('순서\t영화ID\t영화 제목')
for ti, movieId in enumerate(title_dict):
    print(f'{ti+1}\t{movieId}\t{title_dict[movieId]}')
    if((ti + 1)>= 3):
        break
print()
print('순서\t영화ID\t장르 목록')
for li, movieId in enumerate(genres_dict):
    genres = genres_dict[movieId]
    print(f'{li+1}\t{movieId}\t{genres}')
    if((li + 1) >= 3):
        break



'''
처리 결과:
================================
title_dict: 9742
genres_dict: 9742

순서    영화ID  영화 제목
1       1       Toy Story (1995)
2       2       Jumanji (1995)
3       3       Grumpier Old Men (1995)

순서    영화ID  장르 목록
1       1       ['Adventure', 'Animation', 'Children', 'Comedy', 'Fantasy']   
2       2       ['Adventure', 'Children', 'Fantasy']
3       3       ['Comedy', 'Romance']

'''
