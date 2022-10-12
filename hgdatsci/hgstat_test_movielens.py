#
import hgsysinc
from hgstat_test_movie import (
    hgstat_ratings_dict__ratings,
    check_rvalue__ratings_dict_by_Id,
    hgstat_avg_rating_dict__ratings_dict,
    hgstat_count_rating_dict__ratings_dict,
    hgstat_time_dict__ratings,
)

#===============================
#===============================
#---------------
# https://grouplens.org/datasets/movielens/
# MovieLens Latest Datasets
# 
# Small: 100,000 ratings and 3,600 tag applications applied to 9,000 movies by 600 users. 
# Last updated 9/2018.
#
# README.html
# ml-latest-small.zip (size: 1 MB)
#
# ==>           197,979 links.csv
# ==>           494,431 movies.csv
# ==>         2,483,723 ratings.csv
# ==>             8,342 README.txt
# ==>           118,660 tags.csv
#---------------

#
movielens_filepath = '../ext-src/movie_dataset/movielens/ml-latest-small/'

def hgstat_ratings_movielens():
    #---------------
    # format: ratings
    #---------------
    # userId,movieId,rating,timestamp
    # 1,1,4.0,964982703
    # 1,3,4.0,964981247
    # 1,6,4.0,964982224
    #---------------
    import pandas as pd 
    csv_data = movielens_filepath + 'ratings.csv'
    ratings =  pd.read_csv(csv_data)

    #=ratings.sort_values(by=['movieId'])
    #---------------
    #=print(ratings)
    #---------------
    #= 출력결과 :  <ratings.csv>
    #=         userId  movieId  rating   timestamp
    #= 0            1        1     4.0   964982703
    #= 1            1        3     4.0   964981247
    #= 2            1        6     4.0   964982224
    #= 3            1       47     5.0   964983815
    #= 4            1       50     5.0   964982931
    #= ...        ...      ...     ...         ...
    #= 100831     610   166534     4.0  1493848402
    #= 100832     610   168248     5.0  1493850091
    #= 100833     610   168250     5.0  1494273047
    #= 100834     610   168252     5.0  1493846352
    #= 100835     610   170875     3.0  1493846415
    #= 
    #= [100836 rows x 4 columns]
    #---------------

    #---------------
    #=print(ratings.columns)
    #=print(ratings.columns.values)
    #=print(ratings.columns.values.tolist()) 
    #---------------
    #= Index(['userId', 'movieId', 'rating', 'timestamp'], dtype='object')
    #= ['userId' 'movieId' 'rating' 'timestamp']
    #= ['userId', 'movieId', 'rating', 'timestamp']
    #---------------
    return ratings

def hgstat_movies_movielens(ModifyTilteYear=False, PrintSample=False):
    #---------------
    # format: movies
    #---------------
    # movieId,title,genres
    # 1,Toy Story (1995),Adventure|Animation|Children|Comedy|Fantasy
    # 2,Jumanji (1995),Adventure|Children|Fantasy
    # 3,Grumpier Old Men (1995),Comedy|Romance
    #---------------
    import pandas as pd 
    csv_data = movielens_filepath + 'movies.csv'
    movies =  pd.read_csv(csv_data)

    if(PrintSample == True):
        print(movies)
        #---------------
        #= 출력결과 :  <movies.csv>
        #=       movieId  ...                                       genres
        #= 0           1  ...  Adventure|Animation|Children|Comedy|Fantasy
        #= 1           2  ...                   Adventure|Children|Fantasy
        #= 2           3  ...                               Comedy|Romance
        #= 3           4  ...                         Comedy|Drama|Romance
        #= 4           5  ...                                       Comedy
        #= ...       ...  ...                                          ...
        #= 9737   193581  ...              Action|Animation|Comedy|Fantasy
        #= 9738   193583  ...                     Animation|Comedy|Fantasy
        #= 9739   193585  ...                                        Drama
        #= 9740   193587  ...                             Action|Animation
        #= 9741   193609  ...                                       Comedy
        #= 
        #= [9742 rows x 3 columns]
        #---------------
        #---------------

        #---------------
        #=print(movies.columns)
        #=print(movies.columns.values)
        #=print(movies.columns.values.tolist())
        #---------------
        # Index(['movieId', 'title', 'genres'], dtype='object')
        # ['movieId' 'title' 'genres']
        # ['movieId', 'title', 'genres']
        #---------------

        #---------------
        # 시작부터 일부 출력해본다.
        #---------------
        print(),print(),
        print(movies.columns.values)
        for i in range(len(movies)):
            print(movies.iloc[i].to_list())
            if((i + 1) >= 10): # 10개만 출력
                break

    #---------------
    # {title}에 발표 연도가 포함되어 있어서 연도를 분리해야 한다.
    #---------------
    if(ModifyTilteYear == True):
        new_titles = []
        new_release = []
        movie_num = len(movies)
        for i in range(movie_num):
            title = movies.iloc[i]['title']
            # 'Toy Story (1995)' --> 'Toy Story'와 '(1995)'로 분리
            new_title = title[:-7] # ' (1995)' : 7글자
            new_year = title[len(title) - 6:] # '(1995)' : 앞에 공백을 지워서 6글자

            #
            new_year = new_year.replace('(','') # '(1995)' ==> '1995)'
            new_year = new_year.replace(')','') # '(1995)' ==> '1995'

            try: # 중간에 비정상적인 데이터가 있을 수 있다.
                new_year = int(new_year)
            except ValueError: # ValueError: invalid literal for int() with base 10: 'ylon 5'
                #=print(f"[{movies.iloc[i]['movieId']}] ValueError: invalid literal for int() with base 10: 'ylon 5'")
                new_year = 0

            #
            new_titles.append(new_title)
            new_release.append(new_year)
        #
        movies.insert(2, "origin_title", new_titles, True) 
        movies.insert(3, "release", new_release, True) 
    #
    return movies

def hgstat_genres_list_movielens(ModifyTilteYear=False):
    #---------------
    # format: movies
    #---------------
    # movieId,title,genres
    # 1,Toy Story (1995),Adventure|Animation|Children|Comedy|Fantasy
    # 2,Jumanji (1995),Adventure|Children|Fantasy
    # 3,Grumpier Old Men (1995),Comedy|Romance
    #---------------
    movies =  hgstat_movies_movielens(ModifyTilteYear=ModifyTilteYear)
    #=movies.sort_values(by=['id'])

    #---------------
    #=print(movies)
    #---------------
    #= 출력결과 :  <movies.csv>
    #=       movieId  ...                                       genres
    #= 0           1  ...  Adventure|Animation|Children|Comedy|Fantasy
    #= 1           2  ...                   Adventure|Children|Fantasy
    #= 2           3  ...                               Comedy|Romance
    #= 3           4  ...                         Comedy|Drama|Romance
    #= 4           5  ...                                       Comedy
    #= ...       ...  ...                                          ...
    #= 9737   193581  ...              Action|Animation|Comedy|Fantasy
    #= 9738   193583  ...                     Animation|Comedy|Fantasy
    #= 9739   193585  ...                                        Drama
    #= 9740   193587  ...                             Action|Animation
    #= 9741   193609  ...                                       Comedy
    #= 
    #= [9742 rows x 3 columns]
    #---------------
    #---------------

    #---------------
    #=print(movies.columns)
    #=print(movies.columns.values)
    #=print(movies.columns.values.tolist())
    #---------------
    # Index(['movieId', 'title', 'genres'], dtype='object')
    # ['movieId' 'title' 'genres']
    # ['movieId', 'title', 'genres']
    #---------------

    #============================
    #============================
    genres_list_raw = movies['genres'].tolist()
    #=print(f'genres_list_raw: {len(genres_list_raw)}')
    #=print(*genres_list_raw, sep='\n')

    genres_list = []
    for raw in genres_list_raw:
        item_list = raw.split('|')
        genres_list.append(item_list)
        #=print(f'{raw} ===> {item_list}')

    #=print(f'genres_list: {len(genres_list)}')
    #=print(*genres_list, sep='\n')

    return genres_list

def hgstat_genres_dict_movielens(ModifyTilteYear=False, imax_exc=False):
    #---------------
    # format: movies
    #---------------
    # movieId,title,genres
    # 1,Toy Story (1995),Adventure|Animation|Children|Comedy|Fantasy
    # 2,Jumanji (1995),Adventure|Children|Fantasy
    # 3,Grumpier Old Men (1995),Comedy|Romance
    #---------------

    movies =  hgstat_movies_movielens(ModifyTilteYear=ModifyTilteYear)
    #=movies.sort_values(by=['id'])

    #---------------
    #=print(movies)
    #---------------
    #= 출력결과 :  <movies.csv>
    #=       movieId  ...                                       genres
    #= 0           1  ...  Adventure|Animation|Children|Comedy|Fantasy
    #= 1           2  ...                   Adventure|Children|Fantasy
    #= 2           3  ...                               Comedy|Romance
    #= 3           4  ...                         Comedy|Drama|Romance
    #= 4           5  ...                                       Comedy
    #= ...       ...  ...                                          ...
    #= 9737   193581  ...              Action|Animation|Comedy|Fantasy
    #= 9738   193583  ...                     Animation|Comedy|Fantasy
    #= 9739   193585  ...                                        Drama
    #= 9740   193587  ...                             Action|Animation
    #= 9741   193609  ...                                       Comedy
    #= 
    #= [9742 rows x 3 columns]
    #---------------
    #---------------

    #---------------
    #=print(movies.columns)
    #=print(movies.columns.values)
    #=print(movies.columns.values.tolist())
    #---------------
    # Index(['movieId', 'title', 'genres'], dtype='object')
    # ['movieId' 'title' 'genres']
    # ['movieId', 'title', 'genres']
    #---------------

    #============================
    #============================
    gentres_key = 'IMAX'
    genres_dict = {}
    for mi in range(len(movies)):
        movieId = movies.iloc[mi]['movieId']
        genres = movies.iloc[mi]['genres']

        genres_list = genres.split('|')
        #=print(f'{genres} ===> {genres_list}')

        if(imax_exc == True): # 'IMAX'는 제와
            if(gentres_key in genres_list):
                genres_list.remove(gentres_key)
        #
        genres_dict[movieId] = genres_list
    #
    return genres_dict, movies

def hgstat_title_list_movielens(ModifyTilteYear=False):
    #---------------
    # format: movies
    #---------------
    # movieId,title,genres
    # 1,Toy Story (1995),Adventure|Animation|Children|Comedy|Fantasy
    # 2,Jumanji (1995),Adventure|Children|Fantasy
    # 3,Grumpier Old Men (1995),Comedy|Romance
    #---------------
    movies =  hgstat_movies_movielens(ModifyTilteYear=ModifyTilteYear)
    #=movies.sort_values(by=['id'])

    #---------------
    #=print(movies)
    #---------------
    #= 출력결과 :  <movies.csv>
    #=       movieId  ...                                       genres
    #= 0           1  ...  Adventure|Animation|Children|Comedy|Fantasy
    #= 1           2  ...                   Adventure|Children|Fantasy
    #= 2           3  ...                               Comedy|Romance
    #= 3           4  ...                         Comedy|Drama|Romance
    #= 4           5  ...                                       Comedy
    #= ...       ...  ...                                          ...
    #= 9737   193581  ...              Action|Animation|Comedy|Fantasy
    #= 9738   193583  ...                     Animation|Comedy|Fantasy
    #= 9739   193585  ...                                        Drama
    #= 9740   193587  ...                             Action|Animation
    #= 9741   193609  ...                                       Comedy
    #= 
    #= [9742 rows x 3 columns]
    #---------------
    #---------------

    #---------------
    #=print(movies.columns)
    #=print(movies.columns.values)
    #=print(movies.columns.values.tolist())
    #---------------
    # Index(['movieId', 'title', 'genres'], dtype='object')
    # ['movieId' 'title' 'genres']
    # ['movieId', 'title', 'genres']
    #---------------

    #============================
    #============================
    title_list = movies['title'].tolist()
    #=print(f'title_list: {len(title_list_raw)}')
    #=print(*title_list, sep='\n')

    return title_list

def hgstat_title_dict_movielens(ModifyTilteYear=False):
    #---------------
    # format: movies
    #---------------
    # movieId,title,genres
    # 1,Toy Story (1995),Adventure|Animation|Children|Comedy|Fantasy
    # 2,Jumanji (1995),Adventure|Children|Fantasy
    # 3,Grumpier Old Men (1995),Comedy|Romance
    #---------------

    movies =  hgstat_movies_movielens(ModifyTilteYear=ModifyTilteYear)
    #=movies.sort_values(by=['id'])

    #---------------
    #=print(movies)
    #---------------
    #= 출력결과 :  <movies.csv>
    #=       movieId  ...                                       genres
    #= 0           1  ...  Adventure|Animation|Children|Comedy|Fantasy
    #= 1           2  ...                   Adventure|Children|Fantasy
    #= 2           3  ...                               Comedy|Romance
    #= 3           4  ...                         Comedy|Drama|Romance
    #= 4           5  ...                                       Comedy
    #= ...       ...  ...                                          ...
    #= 9737   193581  ...              Action|Animation|Comedy|Fantasy
    #= 9738   193583  ...                     Animation|Comedy|Fantasy
    #= 9739   193585  ...                                        Drama
    #= 9740   193587  ...                             Action|Animation
    #= 9741   193609  ...                                       Comedy
    #= 
    #= [9742 rows x 3 columns]
    #---------------
    #---------------

    #---------------
    #=print(movies.columns)
    #=print(movies.columns.values)
    #=print(movies.columns.values.tolist())
    #---------------
    # Index(['movieId', 'title', 'genres'], dtype='object')
    # ['movieId' 'title' 'genres']
    # ['movieId', 'title', 'genres']
    #---------------

    #============================
    #============================
    title_dict = {}
    for mi in range(len(movies)):
        movieId = int(movies.iloc[mi]['movieId'])
        title = movies.iloc[mi]['title']

        #
        title_dict[movieId] = title
    return title_dict, movies

def hgstat_release_list_movielens():
    #---------------
    # format: movies
    #---------------
    # movieId,title,genres
    # 1,Toy Story (1995),Adventure|Animation|Children|Comedy|Fantasy
    # 2,Jumanji (1995),Adventure|Children|Fantasy
    # 3,Grumpier Old Men (1995),Comedy|Romance
    #---------------
    ModifyTilteYear = True # 'title'을 정확하게 찾으려면 이렇게 호출
    # 'Toy Story (1995)' --> 'Toy Story'와 '1995'로 분리
    movies =  hgstat_movies_movielens(ModifyTilteYear=ModifyTilteYear)
    #=movies.sort_values(by=['id'])

    #---------------
    #=print(movies)
    #---------------
    #= 출력결과 :  <movies.csv>
    #=       movieId  ...                                       genres
    #= 0           1  ...  Adventure|Animation|Children|Comedy|Fantasy
    #= 1           2  ...                   Adventure|Children|Fantasy
    #= 2           3  ...                               Comedy|Romance
    #= 3           4  ...                         Comedy|Drama|Romance
    #= 4           5  ...                                       Comedy
    #= ...       ...  ...                                          ...
    #= 9737   193581  ...              Action|Animation|Comedy|Fantasy
    #= 9738   193583  ...                     Animation|Comedy|Fantasy
    #= 9739   193585  ...                                        Drama
    #= 9740   193587  ...                             Action|Animation
    #= 9741   193609  ...                                       Comedy
    #= 
    #= [9742 rows x 3 columns]
    #---------------
    #---------------

    #---------------
    #=print(movies.columns)
    #=print(movies.columns.values)
    #=print(movies.columns.values.tolist())
    #---------------
    # Index(['movieId', 'title', 'genres'], dtype='object')
    # ['movieId' 'title' 'genres']
    # ['movieId', 'title', 'genres']
    #---------------

    #============================
    #============================
    release_list = movies['release'].tolist()
    #=print(f'release_list: {len(release_list_raw)}')
    #=print(*release_list, sep='\n')

    return release_list, movies

def hgstat_dicts_movielens(ModifyTilteYear=False, imax_exc=False):
    #---------------
    # format: movies
    #---------------
    # movieId,title,genres
    # 1,Toy Story (1995),Adventure|Animation|Children|Comedy|Fantasy
    # 2,Jumanji (1995),Adventure|Children|Fantasy
    #---------------

    movies =  hgstat_movies_movielens(ModifyTilteYear=ModifyTilteYear)
    #=movies.sort_values(by=['id'])

    #---------------
    #=print(movies)
    #---------------
    #= 출력결과 :  <movies.csv>
    #=       movieId  ...                                       genres
    #= 0           1  ...  Adventure|Animation|Children|Comedy|Fantasy
    #= 1           2  ...                   Adventure|Children|Fantasy
    #= 2           3  ...                               Comedy|Romance
    #= 3           4  ...                         Comedy|Drama|Romance
    #= 4           5  ...                                       Comedy
    #= ...       ...  ...                                          ...
    #= 9737   193581  ...              Action|Animation|Comedy|Fantasy
    #= 9738   193583  ...                     Animation|Comedy|Fantasy
    #= 9739   193585  ...                                        Drama
    #= 9740   193587  ...                             Action|Animation
    #= 9741   193609  ...                                       Comedy
    #= 
    #= [9742 rows x 3 columns]
    #---------------
    #---------------

    #---------------
    #=print(movies.columns)
    #=print(movies.columns.values)
    #=print(movies.columns.values.tolist())
    #---------------
    # Index(['movieId', 'title', 'genres'], dtype='object')
    # ['movieId' 'title' 'genres']
    # ['movieId', 'title', 'genres']
    #---------------

    gentres_key = 'IMAX'
    genres_dict = {}
    title_dict = {}
    for mi in range(len(movies)):
        movieId = int(movies.iloc[mi]['movieId'])
        genres = movies.iloc[mi]['genres']
        genres_list = genres.split('|')
        #=print(f'{genres} ===> {genres_list}')

        if(imax_exc == True): # 'IMAX'는 제와
            if(gentres_key in genres_list):
                genres_list.remove(gentres_key)
        #
        genres_dict[movieId] = genres_list
        #-----
        #-----
        title = movies.iloc[mi]['title']
        title_dict[movieId] = title
    #
    return title_dict, genres_dict, movies

def hgstat_dataframe_movielens():
    #---------------
    # format: movies
    #---------------
    # movieId,title,genres
    # 1,Toy Story (1995),Adventure|Animation|Children|Comedy|Fantasy
    # 2,Jumanji (1995),Adventure|Children|Fantasy
    # 3,Grumpier Old Men (1995),Comedy|Romance
    #---------------
    import pandas as pd 
    csv_data = movielens_filepath + 'movies.csv'
    movies =  pd.read_csv(csv_data)

    #=print(movies.columns)
    #=print(movies.columns.values)
    #=print(movies.columns.values.tolist())
    #---------------
    # Index(['movieId', 'title', 'genres'], dtype='object')
    # ['movieId' 'title' 'genres']
    # ['movieId', 'title', 'genres']
    #---------------

    #---------------
    #=print(movies)
    #---------------
    #= 출력결과 :  <movies.csv>
    #=     movieId  ...                                       genres
    #= 0            1  ...  Adventure|Animation|Children|Comedy|Fantasy
    #= 1            2  ...                   Adventure|Children|Fantasy
    #= 2            3  ...                               Comedy|Romance
    #= 3            4  ...                         Comedy|Drama|Romance
    #= 4            5  ...                                       Comedy
    #= ...        ...  ...                                          ...
    #= 62418   209157  ...                                        Drama
    #= 62419   209159  ...                                  Documentary
    #= 62420   209163  ...                                 Comedy|Drama
    #= 62421   209169  ...                           (no genres listed)
    #= 62422   209171  ...                       Action|Adventure|Drama
    #= 
    #= [62423 rows x 3 columns]
    #---------------

    #
    #---------------
    # format: ratings
    #---------------
    # userId,movieId,rating,timestamp
    # 1,1,4.0,964982703
    # 1,3,4.0,964981247
    # 1,6,4.0,964982224
    #---------------

    #
    csv_data = movielens_filepath + 'ratings.csv'

    #=ratings = pd.read_csv(csv_data) # @0
    #=ratings = pd.read_csv(csv_data, usecols = ['userId','movieId','rating']) # @1
    ratings = pd.read_csv(csv_data, usecols = [0,1,2]) # @2

    #---------------
    #= @0
    #= Index(['userId', 'movieId', 'rating', 'timestamp'], dtype='object')
    #= ['userId' 'movieId' 'rating' 'timestamp']
    #= ['userId', 'movieId', 'rating', 'timestamp']
    #= 
    #= @1
    #= Index(['userId', 'movieId', 'rating'], dtype='object')
    #= ['userId' 'movieId' 'rating']
    #= ['userId', 'movieId', 'rating']
    #=
    #= @2
    #= Index(['userId', 'movieId', 'rating'], dtype='object')
    #= ['userId' 'movieId' 'rating']
    #= ['userId', 'movieId', 'rating']
    #---------------
    #-----------------------
    # ml-latest-small 데이터는 많지 않아서 다 읽어도 된다.
    #-----------------------
    #=# 데이터가 너무 많으면 2d-dataFrame 변환이 안 되므로 일부만 선택
    #=ratings_num = 100000 # 10만개
    #=ratings_num = 200000 # 20만개
    #=ratings_num = 300000 # 30만개
    #=ratings_num = 500000 # 50만개
    #=ratings = ratings.head(ratings_num)
    #-----------------------

    #---------------
    #=print(ratings)
    #---------------
    #= 출력결과 :  <ratings.csv>
    #=         userId  movieId  rating   timestamp
    #= 0              1      296     5.0  1147880044
    #= 1              1      306     3.5  1147868817
    #= 2              1      307     5.0  1147868828
    #= 3              1      665     5.0  1147878820
    #= 4              1      899     3.5  1147868510
    #= ...          ...      ...     ...         ...
    #= 499995    3445     8042     4.0
    #= 499996    3445     8154     4.0
    #= 499997    3445     8188     4.0
    #= 499998    3445     8260     3.5
    #= 499999    3445     8360     3.0
    #= ...        ...      ...     ...
    #= 25000090  162541    50872     4.5  1240953372
    #= 25000091  162541    55768     2.5  1240951998
    #= 25000092  162541    56176     2.0  1240950697
    #= 25000093  162541    58559     4.0  1240953434
    #= 25000094  162541    63876     5.0  1240952515
    #= 
    #= [25000095 rows x 4 columns]
    #---------------

    return movies, ratings

def hgstat_movielens_datas():
    movies, ratings = hgstat_dataframe_movielens()
    #=ratings.sort_values(by=['movieId'])

    # {dataFrame.pivot_table}은  데이터가 많으면 사용할 수 없다. (FullData == True)
    #=== type 1
    #=movie_table = ratings.pivot_table(index='userId', columns='movieId', values='rating')
    #=movie_table.fillna(0, inplace=True) # {NaN}을 '0'으로 바꿈
    #=== type 2
    movie_table = ratings.pivot_table(index='userId', columns='movieId', values='rating', fill_value = 0) # 'NaN' 변경
    movie_lists = movie_table.to_numpy()

    #---------------
    #= print(movie_lists)
    #---------------
    #= [[0. 0. 0. ... 0. 0. 0.]
    #= [0. 0. 0. ... 0. 0. 0.]
    #= [0. 0. 0. ... 0. 0. 0.]
    #= ...
    #= [0. 0. 0. ... 0. 0. 0.]
    #= [4. 0. 0. ... 0. 0. 0.]
    #= [5. 0. 0. ... 0. 0. 0.]]
    #---------------
    #---------------
    #= print(movie_table)
    #---------------
    #= 출력결과 :  <ratings.csv>
    #= movieId  1       2       3       4       ...  206861  207309  208002  208793
    #= userId                                   ...                                
    #= 1           0.0     0.0     0.0       0  ...     0.0     0.0     0.0     0.0
    #= 2           3.5     0.0     0.0       0  ...     0.0     0.0     0.0     0.0
    #= 3           4.0     0.0     0.0       0  ...     0.0     0.0     0.0     0.0
    #= 4           3.0     0.0     0.0       0  ...     0.0     0.0     0.0     0.0
    #= 5           4.0     0.0     0.0       0  ...     0.0     0.0     0.0     0.0
    #= ...         ...     ...     ...     ...  ...     ...     ...     ...     ...
    #= 2067        4.0     0.0     3.0       0  ...     0.0     0.0     0.0     0.0
    #= 2068        0.0     0.0     0.0       0  ...     0.0     0.0     0.0     0.0
    #= 2069        0.0     2.5     0.0       0  ...     0.0     0.0     0.0     0.0
    #= 2070        0.0     0.0     0.0       0  ...     0.0     0.0     0.0     0.0
    #= 2071        3.0     0.0     0.0       0  ...     0.0     0.0     0.0     0.0
    #= ...
    #= 3441        0.0     3.0     0.0     3.0  ...     0.0       0     0.0       0
    #= 3442        4.0     0.0     0.0     0.0  ...     0.0       0     0.0       0
    #= 3443        3.5     0.0     0.0     0.0  ...     0.0       0     0.0       0
    #= 3444        0.0     0.0     0.0     0.0  ...     0.0       0     0.0       0
    #= 3445        4.0     0.0     0.0     0.0  ...     0.0       0     0.0       0
    #= 
    #= [3445 rows x 17466 columns] 
    #---------------


    return movies, movie_table, movie_lists

#===============================
#===============================
def hgstat_get_title__movies_by_movieId(movieId, movies):
    movie_title = ''

    #=print(movies[movies['movieId'] == movieId])
    movies_find = movies[movies['movieId'] == movieId]
    if(len(movies_find['title'].values) <= 0): # 제목이 없는 경우
        return movie_title
    
    movie_title = movies_find['title'].values[0]
    #=print(len(movie_title), ':', movie_title)

    return movie_title

def hgstat_get_release__movies_by_movieId(movieId, movies):
    movie_release = ''

    #=print(movies[movies['movieId'] == movieId])
    movies_find = movies[movies['movieId'] == movieId]
    if(len(movies_find['release'].values) <= 0): # 출시일이 없는 경우
        return movie_release    
    movie_release = movies_find['release'].values[0]
    #=print(len(movie_release), ':', movie_release)

    return movie_release

def hgstat_ratings_dict__movlens(UserBase=True, CutYearBelow=None):
    #---------------
    # format: ratings
    #---------------
    # userId,movieId,rating,timestamp
    # 1,110,1.0,1425941529
    # 1,147,4.5,1425942435
    # 1,858,5.0,1425941523
    #---------------
    ratings = hgstat_ratings_movielens()
    ratings_dict, userIdList, movieIdList = \
        hgstat_ratings_dict__ratings(ratings, 
        UserBase=UserBase, CutYearBelow=CutYearBelow)
    #
    return ratings_dict, userIdList, movieIdList

def hgstat_time_dict__movlens(UserBase=True, CutYearBelow=None):
    #---------------
    # format: ratings
    #---------------
    # userId,movieId,rating,timestamp
    # 1,110,1.0,1425941529
    # 1,147,4.5,1425942435
    # 1,858,5.0,1425941523
    #---------------
    ratings = hgstat_ratings_movielens()
    time_dict, userIdList, movieIdList = \
        hgstat_time_dict__ratings(ratings, UserBase=UserBase, CutYearBelow=CutYearBelow)
    #
    return time_dict, userIdList, movieIdList


def hgstat_avg_ratings_dict__movlens(ratings_dict=None, UserBase=True):
    if(ratings_dict == None):
        ratings_dict, userIdList, movieIdList = hgstat_ratings_dict__movlens(UserBase=UserBase)
    avg_ratings_dict = hgstat_avg_rating_dict__ratings_dict(ratings_dict)
    return avg_ratings_dict

def hgstat_count_ratings_dict__movlens(ratings_dict=None, UserBase=True):
    if(ratings_dict == None):
        ratings_dict, userIdList, movieIdList = hgstat_ratings_dict__movlens(UserBase=UserBase)
    count_ratings_dict = hgstat_count_rating_dict__ratings_dict(ratings_dict)
    return count_ratings_dict

def hgstat_get_movieId__movies_by_title(movies, title):
    #---------
    # 아래 방식으로 하면 안 된다.
    #---------
    # 'Toy Story (1995)' --> 'Toy Story'와 '(1995)'로 분리
    # {title}에 발표 연도가 포함되어 있어서 연도를 분리해야 한다.
    #=movie_info = movies.loc[movies['title'] == title]
    #---------
    movie_info = movies.loc[movies['origin_title'] == title] # 'title'을 정확하게 찾으려면 이렇게 호출
    #=print(f'{title}: {movie_info}')
    #=print(f'{title}: {movie_info.iloc[0]}')
    movieId = movie_info.iloc[0]['movieId']
    #=print(f"movieId: {movieId}")

    return movieId

def check_rvalue__ratings_dict_ml_by_title(title, movieIdList, userIdList, 
    movie_ratings_dict, movies,
    debugPrint=False, ProcMod=0): 
    #---------------------
    if(debugPrint == True):
        print(f'{title} : 상관계수 계산')

    #---------------------
    movieId = hgstat_get_movieId__movies_by_title(movies, title)
    movieId = int(movieId) # 'str' 타입으로 바뀐 경우가 있다.

    check_rvalue__ratings_dict_by_Id(movieId, userIdList, movie_ratings_dict, 
    keyIdList=movieIdList,
    debugPrint=debugPrint, ProcMod=ProcMod)

#================================
#================================
from unittest import TestCase, main

class HGTest(TestCase):
    def test_funstat(self):
        import hgsysinc
        hgsysinc._print_function_name_()


#---------------------
#---------------------
if __name__ == '__main__':
    main()

