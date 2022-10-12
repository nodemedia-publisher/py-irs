import hgsysinc
from hgstat_test_movielens import hgstat_movies_movielens
#-----
movies = hgstat_movies_movielens() # movielens movies 읽어오기 
print(movies)
print('movies.columns:', movies.columns.values)

# 시작부터 일부 출력
for i in range(len(movies)):
    print(movies.iloc[i].to_list())
    if((i + 1) >= 3):
        break

'''
처리 결과:
================================
      movieId  ...                                       genres
0           1  ...  Adventure|Animation|Children|Comedy|Fantasy
1           2  ...                   Adventure|Children|Fantasy
2           3  ...                               Comedy|Romance
3           4  ...                         Comedy|Drama|Romance
4           5  ...                                       Comedy
...       ...  ...                                          ...
9737   193581  ...              Action|Animation|Comedy|Fantasy
9738   193583  ...                     Animation|Comedy|Fantasy
9739   193585  ...                                        Drama
9740   193587  ...                             Action|Animation
9741   193609  ...                                       Comedy

[9742 rows x 3 columns]
movies.columns: ['movieId' 'title' 'genres']
[1, 'Toy Story (1995)', 'Adventure|Animation|Children|Comedy|Fantasy']        
[2, 'Jumanji (1995)', 'Adventure|Children|Fantasy']
[3, 'Grumpier Old Men (1995)', 'Comedy|Romance']


'''