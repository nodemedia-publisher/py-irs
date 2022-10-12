#---
#---
from unittest import TestCase, main
#=from math import nan
#=from numpy.core.numeric import NaN
from numpy.lib.function_base import average

import hgsysinc
from hgstat import hgCoefficient_low
from hgstat_test import find_reco__id_list
from hgstat_test_movie import (
    hgstat_ratings_dict__ratings,
    get_genres_distance_by_set2,
    check_rvalue__ratings_dict_by_Id,
    hgstat_get_vote_count_max,
)

#====================================
#====================================
#====================================
#---------------
# 데이터 읽어오기 
#---------------
# src: https://www.kaggle.com/rounakbanik/the-movies-dataset
# ==> archive.zip
# ==>     <DIR>          .
# ==>     <DIR>          ..
# ==>        189,917,659 credits.csv
# ==>          6,231,943 keywords.csv
# ==>            989,107 links.csv
# ==>            183,372 links_small.csv
# ==>         34,445,126 movies_metadata.csv
# ==>        709,550,327 ratings.csv
# ==>          2,438,266 ratings_small.csv
# ==>                7개 파일         943,755,800 바이트
#
# These files contain metadata for all 45,000 movies listed in the Full MovieLens Dataset. 
# The dataset consists of movies released on or before July 2017. 
# Data points include cast, crew, plot keywords, budget, revenue, posters, 
# release dates, languages, production companies, countries, TMDB vote counts and vote averages.
#
# This dataset also has files containing 26 million ratings from 270,000 users for all 45,000 movies. 
# Ratings are on a scale of 1-5 and have been obtained from the official GroupLens website.
#
#
# movies_metadata.csv: The main Movies Metadata file. Contains information on 45,000 movies featured in the Full MovieLens dataset. Features include posters, backdrops, budget, revenue, release dates, languages, production countries and companies.
# keywords.csv: Contains the movie plot keywords for our MovieLens movies. Available in the form of a stringified JSON Object.
# credits.csv: Consists of Cast and Crew Information for all our movies. Available in the form of a stringified JSON Object.
# links.csv: The file that contains the TMDB and IMDB IDs of all the movies featured in the Full MovieLens dataset.
# links_small.csv: Contains the TMDB and IMDB IDs of a small subset of 9,000 movies of the Full Dataset.
# ratings_small.csv: The subset of 100,000 ratings from 700 users on 9,000 movies.
# The Full MovieLens Dataset consisting of 26 million ratings and 750,000 tag applications from 270,000 users on all the 45,000 movies in this dataset can be accessed here
# 
# Acknowledgements
# This dataset is an ensemble of data collected from TMDB and GroupLens.
# The Movie Details, Credits and Keywords have been collected from the TMDB Open API. 
# This product uses the TMDb API but is not endorsed or certified by TMDb. 
# Their API also provides access to data on many additional movies, actors and actresses, 
# crew members, and TV shows. You can try it for yourself here.
#
# The Movie Links and Ratings have been obtained from the Official GroupLens website. 
#---------------

kaggle_filepath = '../ext-src/movie_dataset/kaggle/archive/'

#===================================
#===================================
def hgstat_metadata_kaggle(AllFlag=True, OverviewFlag=False, debugPrint=False):
    #---------------
    # format: movies_metadata
    #---------------
    # adult,belongs_to_collection,budget,genres,homepage,id,imdb_id,original_language,original_title,overview,popularity,poster_path,production_companies,production_countries,release_date,revenue,runtime,spoken_languages,status,tagline,title,video,vote_average,vote_count
    # False,"{'id': 10194, 'name': 'Toy Story Collection', 'poster_path': '/7G9915LfUQ2lVfwMEEhDsn3kT4B.jpg', 'backdrop_path': '/9FBwqcd9IRruEDUrTdcaafOMKUq.jpg'}",30000000,"[{'id': 16, 'name': 'Animation'}, {'id': 35, 'name': 'Comedy'}, {'id': 10751, 'name': 'Family'}]",http://toystory.disney.com/toy-story,862,tt0114709,en,Toy Story,"Led by Woody, Andy's toys live happily in his room until Andy's birthday brings Buzz Lightyear onto the scene. Afraid of losing his place in Andy's heart, Woody plots against Buzz. But when circumstances separate Buzz and Woody from their owner, the duo eventually learns to put aside their differences.",21.946943,/rhIRbceoE9lR4veEXuwCC2wARtG.jpg,"[{'name': 'Pixar Animation Studios', 'id': 3}]","[{'iso_3166_1': 'US', 'name': 'United States of America'}]",1995-10-30,373554033,81.0,"[{'iso_639_1': 'en', 'name': 'English'}]",Released,,Toy Story,False,7.7,5415
    # False,,65000000,"[{'id': 12, 'name': 'Adventure'}, {'id': 14, 'name': 'Fantasy'}, {'id': 10751, 'name': 'Family'}]",,8844,tt0113497,en,Jumanji,"When siblings Judy and Peter discover an enchanted board game that opens the door to a magical world, they unwittingly invite Alan -- an adult who's been trapped inside the game for 26 years -- into their living room. Alan's only hope for freedom is to finish the game, which proves risky as all three find themselves running from giant rhinoceroses, evil monkeys and other terrifying creatures.",17.015539,/vzmL6fP7aPKNKPRTFnZmiUfciyV.jpg,"[{'name': 'TriStar Pictures', 'id': 559}, {'name': 'Teitler Film', 'id': 2550}, {'name': 'Interscope Communications', 'id': 10201}]","[{'iso_3166_1': 'US', 'name': 'United States of America'}]",1995-12-15,262797249,104.0,"[{'iso_639_1': 'en', 'name': 'English'}, {'iso_639_1': 'fr', 'name': 'Français'}]",Released,Roll the dice and unleash the excitement!,Jumanji,False,6.9,2413
    #---------------
    import pandas as pd 
    csv_data = kaggle_filepath + "movies_metadata.csv"

    if(AllFlag == True):
        # 모든 항목(총:24)을 사용
        movies_metadata =  pd.read_csv(csv_data)

        if(debugPrint == True):
            print(movies_metadata)
            #---------------
            #= 출력결과 :  <movies_metadata.csv>
            #=       adult  ... vote_count
            #=0      False  ...     5415.0
            #=1      False  ...     2413.0
            #=2      False  ...       92.0
            #=3      False  ...       34.0
            #=4      False  ...      173.0
            #=...      ...  ...        ...
            #=45461  False  ...        1.0
            #=45462  False  ...        3.0
            #=45463  False  ...        6.0
            #=45464  False  ...        0.0
            #=45465  False  ...        0.0
            #=
            #=[45466 rows x 24 columns]
            #---------------
            #-----------------------------------------------
            #=print(movies_metadata.columns)
            #=print(f'movies_metadata.columns {(len(movies_metadata.columns.values))} :', movies_metadata.columns.values)
            #=print(movies_metadata.columns.values.tolist()) 
            #-----------------------------------------------
            #= Index(['adult', 'belongs_to_collection', 'budget', 'genres', 'homepage', 'id',
            #=   'imdb_id', 'original_language', 'original_title', 'overview',
            #=   'popularity', 'poster_path', 'production_companies',
            #=   'production_countries', 'release_date', 'revenue', 'runtime',
            #=   'spoken_languages', 'status', 'tagline', 'title', 'video',
            #=   'vote_average', 'vote_count'],
            #=  dtype='object')
            #=movies_metadata.columns (24) : ['adult' 'belongs_to_collection' 'budget' 'genres' 'homepage' 'id'
            #='imdb_id' 'original_language' 'original_title' 'overview' 'popularity'
            #='poster_path' 'production_companies' 'production_countries'
            #='release_date' 'revenue' 'runtime' 'spoken_languages' 'status' 'tagline'
            #='title' 'video' 'vote_average' 'vote_count']
            #=['adult', 'belongs_to_collection', 'budget', 'genres', 'homepage', 'id', 'imdb_id', 'original_language', 'original_title', 'overview', 'popularity', 'poster_path', 'production_companies', 'production_countries', 'release_date', 'revenue', 'runtime', 'spoken_languages', 'status', 'tagline', 'title', 'video', 'vote_average', 'vote_count']
            #-----------------------------------------------

    else:
        if(OverviewFlag == False): # {overview: 줄거리(짧은 문장)}만 읽을 것인가
            csv_option = ['id', 'imdb_id', 'original_title', 'overview', 'genres', 
                    'release_date', 'vote_average', 'vote_count', 'belongs_to_collection',
                    ]  # 총 9개 항목
        else:
            csv_option = ['id', 'overview'] # 줄거리만 사용
        movies_metadata = pd.read_csv(csv_data, usecols = csv_option)

        #---------------
        #=print(movies_metadata.columns)
        #=print(movies_metadata.columns.values)
        #=print(movies_metadata.columns.values.tolist())
        #---------------
        #= Index(['id', 'imdb_id', 'original_title'], dtype='object')
        #= ['id' 'imdb_id' 'original_title']
        #= ['id', 'imdb_id', 'original_title']
        #---------------

        if(debugPrint == True):
            print(movies_metadata)
            #---------------
            #= 출력결과 :  <movies_metadata.csv>
            #=            id    imdb_id               original_title
            #= 0         862  tt0114709                    Toy Story
            #= 1        8844  tt0113497                      Jumanji
            #= 2       15602  tt0113228             Grumpier Old Men
            #= 3       31357  tt0114885            Waiting to Exhale
            #= 4       11862  tt0113041  Father of the Bride Part II
            #= ...       ...        ...                          ...
            #= 45461  439050  tt6209470                      رگ خواب
            #= 45462  111109  tt2028550          Siglo ng Pagluluwal
            #= 45463   67758  tt0303758                     Betrayal
            #= 45464  227506  tt0008536          Satana likuyushchiy
            #= 45465  461257  tt6980792                     Queerama
            #= 
            #= [45466 rows x 3 columns]
            #---------------
    #
    return movies_metadata

def _hgstat_dataframe_kaggle_movies_meta_old(OverviewFlag=False):
    movies_metadata = hgstat_metadata_kaggle(AllFlag=False, OverviewFlag=OverviewFlag)
    return movies_metadata

def hgstat_links_kaggle():
    #---------------
    # format: links
    #---------------
    #---------------
    #-------------- 
    # {links}는 데이터가 많지 않아서 모두 로딩해도 된다.
    #-------------- 
    import pandas as pd 
    #=if(FullData != True):
    #=    csv_data = kaggle_filepath + "links_small.csv"
    csv_data = kaggle_filepath + "links.csv"
    links = pd.read_csv(csv_data) # ['movieId' 'imdbId' 'tmdbId']
    #=links = pd.read_csv(csv_data, usecols = ['movieId', 'imdbId', 'tmdbId']) # @1
    #=links = pd.read_csv(csv_data, usecols = [0,1,2]) # @2

    #=print(links.columns)
    #=print(links.columns.values)
    #=print(links.columns.values.tolist())
    #---------------
    #= Index(['movieId', 'imdbId', 'tmdbId'], dtype='object')
    #= ['movieId' 'imdbId' 'tmdbId']
    #= ['movieId', 'imdbId', 'tmdbId']
    #---------------

    #---------------
    #=print(links)
    #---------------
    #= 출력결과 :  <links_small.csv>
    #=       movieId   imdbId    tmdbId
    #= 0           1   114709     862.0
    #= 1           2   113497    8844.0
    #= 2           3   113228   15602.0
    #= 3           4   114885   31357.0
    #= 4           5   113041   11862.0
    #= ...       ...      ...       ...
    #= 9120   162672  3859980  402672.0
    #= 9121   163056  4262980  315011.0
    #= 9122   163949  2531318  391698.0
    #= 9123   164977    27660  137608.0
    #= 9124   164979  3447228  410803.0
    #= 
    #= [9125 rows x 3 columns]
    #---------------

    return links

def hgstat_dataframe_kaggle_movies_ratings(FullData=False, ReadRows=0):
    import pandas as pd 
    #---------------
    # format: ratings
    #---------------
    # userId,movieId,rating,timestamp
    # 1,110,1.0,1425941529
    # 1,147,4.5,1425942435
    # 1,858,5.0,1425941523
    #---------------
    if(FullData != True):
        csv_data = kaggle_filepath + "ratings_small.csv"
    else:
        csv_data = kaggle_filepath + "ratings.csv"
    #
    if(ReadRows > 0):
        #=ratings = pd.read_csv(csv_data)
        ratings = pd.read_csv(csv_data, nrows=ReadRows, usecols = ['userId','movieId','rating']) # @1
        #=ratings = pd.read_csv(csv_data, usecols = [0,1,2]) # @2
    else:
        #=ratings = pd.read_csv(csv_data)
        ratings = pd.read_csv(csv_data, usecols = ['userId','movieId','rating']) # @1
        #=ratings = pd.read_csv(csv_data, usecols = [0,1,2]) # @2

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

    #---------------
    #=print(ratings)
    #---------------
    #= 출력결과 :  <ratings_small.csv>
    #=         userId  movieId  rating
    #= 0            1       31     2.5
    #= 1            1     1029     3.0
    #= 2            1     1061     3.0
    #= 3            1     1129     2.0
    #= 4            1     1172     4.0
    #= ...        ...      ...     ...
    #= 99999      671     6268     2.5
    #= 100000     671     6269     4.0
    #= 100001     671     6365     4.0
    #= 100002     671     6385     2.5
    #= 100003     671     6565     3.5
    #= 
    #= [100004 rows x 3 columns]
    #---------------

    return ratings

def hgstat_dataframe_kaggle_movies_keywords():
    import pandas as pd 

    #---------------
    # format: keywords
    #---------------
    #= id,keywords
    #= 862,"[{'id': 931, 'name': 'jealousy'}, {'id': 4290, 'name': 'toy'}, {'id': 5202, 'name': 'boy'}, {'id': 6054, 'name': 'friendship'}, {'id': 9713, 'name': 'friends'}, {'id': 9823, 'name': 'rivalry'}, {'id': 165503, 'name': 'boy next door'}, {'id': 170722, 'name': 'new toy'}, {'id': 187065, 'name': 'toy comes to life'}]"
    #= 8844,"[{'id': 10090, 'name': 'board game'}, {'id': 10941, 'name': 'disappearance'}, {'id': 15101, 'name': ""based on children's book""}, {'id': 33467, 'name': 'new home'}, {'id': 158086, 'name': 'recluse'}, {'id': 158091, 'name': 'giant insect'}]"
    #---------------
    csv_data = kaggle_filepath + "keywords.csv"
    keywords = pd.read_csv(csv_data) # @0
    #=keywords = pd.read_csv(csv_data, usecols = ['id', 'keywords']) # @1
    #=keywords = pd.read_csv(csv_data, usecols = [0,1]) # @2

    #---------------
    #=print(keywords)
    #---------------
    #= 출력결과 :  <keywords.csv>
    #=           id                                           keywords
    #= 0         862  [{'id': 931, 'name': 'jealousy'}, {'id': 4290,...
    #= 1        8844  [{'id': 10090, 'name': 'board game'}, {'id': 1...
    #= 2       15602  [{'id': 1495, 'name': 'fishing'}, {'id': 12392...
    #= 3       31357  [{'id': 818, 'name': 'based on novel'}, {'id':...
    #= 4       11862  [{'id': 1009, 'name': 'baby'}, {'id': 1599, 'n...
    #= ...       ...                                                ...
    #= 46414  439050             [{'id': 10703, 'name': 'tragic love'}]
    #= 46415  111109  [{'id': 2679, 'name': 'artist'}, {'id': 14531,...
    #= 46416   67758                                                 []
    #= 46417  227506                                                 []
    #= 46418  461257                                                 []
    #= 
    #= [46419 rows x 2 columns]
    #---------------

    #=print(keywords.columns)
    #=print(keywords.columns.values)
    #=print(keywords.columns.values.tolist())
    #---------------
    #= Index(['id', 'keywords'], dtype='object')
    #= ['id' 'keywords']
    # =['id', 'keywords']
    #---------------

    return keywords

#===================================
#===================================
def hgstat_kaggle_movies_ratings_table(FullData=False):
    #---------------
    # format: ratings
    #---------------
    # userId,movieId,rating,timestamp
    # 1,110,1.0,1425941529
    # 1,147,4.5,1425942435
    # 1,858,5.0,1425941523
    #---------------

    ratings = hgstat_dataframe_kaggle_movies_ratings(FullData=FullData)

    # {dataFrame.pivot_table}은 데이터가 많으면 사용할 수 없다. (FullData == True)
    #=== type 1
    #=movie_table = ratings.pivot_table(index='userId', columns='movieId', values='rating')
    #=movie_table.fillna(0, inplace=True) # {NaN}을 '0'으로 바꿈
    #=== type 2
    movie_table = ratings.pivot_table(index='userId', 
        columns='movieId', values='rating', fill_value = 0) # 'NaN' 변경
    
    #---------------
    #=print(movie_table)
    #---------------
    #= 출력결과 :  <ratings_small.csv>
    #= movieId  1       2       3       4       ...  162376  162542  162672  163949
    #= userId                                   ...                                
    #= 1           0.0     0.0     0.0     0.0  ...     0.0       0       0       0
    #= 2           0.0     0.0     0.0     0.0  ...     0.0       0       0       0
    #= 3           0.0     0.0     0.0     0.0  ...     0.0       0       0       0
    #= 4           0.0     0.0     0.0     0.0  ...     0.0       0       0       0
    #= 5           0.0     0.0     4.0     0.0  ...     0.0       0       0       0
    #= ...         ...     ...     ...     ...  ...     ...     ...     ...     ...
    #= 667         0.0     0.0     0.0     0.0  ...     0.0       0       0       0
    #= 668         0.0     0.0     0.0     0.0  ...     0.0       0       0       0
    #= 669         0.0     0.0     0.0     0.0  ...     0.0       0       0       0
    #= 670         4.0     0.0     0.0     0.0  ...     0.0       0       0       0
    #= 671         5.0     0.0     0.0     0.0  ...     0.0       0       0       0
    #= 
    #= [671 rows x 9066 columns]
    #---------------

    return movie_table

def hgstat_kaggle_movies_ratings_lists(FullData=False):
    # {dataFrame.pivot_table}은  데이터가 많으면 사용할 수 없다. (FullData == True)
    movie_table = hgstat_kaggle_movies_ratings_table(FullData=FullData)
    movie_lists = movie_table.to_numpy()

    #---------------
    #= print(movie_table)
    #---------------
    #= movieId  1       2       3       4       ...  162376  162542  162672  163949
    #= userId                                   ...                                
    #= 1           0.0     0.0     0.0     0.0  ...     0.0       0       0       0
    #= 2           0.0     0.0     0.0     0.0  ...     0.0       0       0       0
    #= 3           0.0     0.0     0.0     0.0  ...     0.0       0       0       0
    #= 4           0.0     0.0     0.0     0.0  ...     0.0       0       0       0
    #= 5           0.0     0.0     4.0     0.0  ...     0.0       0       0       0
    #= ...         ...     ...     ...     ...  ...     ...     ...     ...     ...
    #= 667         0.0     0.0     0.0     0.0  ...     0.0       0       0       0
    #= 668         0.0     0.0     0.0     0.0  ...     0.0       0       0       0
    #= 669         0.0     0.0     0.0     0.0  ...     0.0       0       0       0
    #= 670         4.0     0.0     0.0     0.0  ...     0.0       0       0       0
    #= 671         5.0     0.0     0.0     0.0  ...     0.0       0       0       0
    #= 
    #= [671 rows x 9066 columns]
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
    
    return movie_lists, movie_table

def hgstat_kaggle_movies_keywords(debugPrint=False):
    #---------------
    # format: keywords
    #---------------
    #= id,keywords
    #= 862,"[{'id': 931, 'name': 'jealousy'}, {'id': 4290, 'name': 'toy'}, {'id': 5202, 'name': 'boy'}, {'id': 6054, 'name': 'friendship'}, {'id': 9713, 'name': 'friends'}, {'id': 9823, 'name': 'rivalry'}, {'id': 165503, 'name': 'boy next door'}, {'id': 170722, 'name': 'new toy'}, {'id': 187065, 'name': 'toy comes to life'}]"
    #= 8844,"[{'id': 10090, 'name': 'board game'}, {'id': 10941, 'name': 'disappearance'}, {'id': 15101, 'name': ""based on children's book""}, {'id': 33467, 'name': 'new home'}, {'id': 158086, 'name': 'recluse'}, {'id': 158091, 'name': 'giant insect'}]"
    #---------------
    keywords = hgstat_dataframe_kaggle_movies_keywords()

    #---------------
    #=print(keywords)
    #---------------
    #= 출력결과 :  <keywords.csv>
    #=           id                                           keywords
    #= 0         862  [{'id': 931, 'name': 'jealousy'}, {'id': 4290,...
    #= 1        8844  [{'id': 10090, 'name': 'board game'}, {'id': 1...
    #= 2       15602  [{'id': 1495, 'name': 'fishing'}, {'id': 12392...
    #= 3       31357  [{'id': 818, 'name': 'based on novel'}, {'id':...
    #= 4       11862  [{'id': 1009, 'name': 'baby'}, {'id': 1599, 'n...
    #= ...       ...                                                ...
    #= 46414  439050             [{'id': 10703, 'name': 'tragic love'}]
    #= 46415  111109  [{'id': 2679, 'name': 'artist'}, {'id': 14531,...
    #= 46416   67758                                                 []
    #= 46417  227506                                                 []
    #= 46418  461257                                                 []
    #= 
    #= [46419 rows x 2 columns]
    #---------------

    #=print(keywords.columns)
    #=print(keywords.columns.values)
    #=print(keywords.columns.values.tolist())
    #---------------
    #= Index(['id', 'keywords'], dtype='object')
    #= ['id' 'keywords']
    # =['id', 'keywords']
    #---------------

    if(debugPrint == True):
        print(f'키워드 목록: {len(keywords)}')
        print(f"순서\t고객ID\t키워드 목록")
    kwd_list_dict = {}
    kwd_dict = {}
    for li in range(len(keywords)):
        #
        meta_Id = keywords.iloc[li]['id']
        keywords_dict_list_str = keywords.iloc[li]['keywords']

        #=print ("type of object", type(keywords_dict_list_str)) 
        keywords_dict_list = eval(keywords_dict_list_str)
        #=if((li + 1) <= 10): # 임시로 '10'개까지만 출력
        #=    print(f"{li}\t{meta_Id}\t{len(keywords_dict_list)}\t{keywords_dict_list}")

        # keywords_dict_list format: [{'id': 931, 'name': 'jealousy'}, {'id': 4290, 'name': 'toy'}, ...]"
        kwd_dict_i = {}
        for ki, dict_i in enumerate(keywords_dict_list):
            #=print ("type of object", type(dict_i)) 
            #=print('dict_i:', dict_i)
            kwd_id = dict_i['id']
            kwd_name = dict_i['name']

            #
            kwd_dict_i[kwd_id] = kwd_name
            #
            kwd_dict[kwd_id] = kwd_name
        #
        #=print(kwd_dict_i.values())
        kwd_list_dict[meta_Id] = list(kwd_dict_i.values())

    if(debugPrint == True):
        print('kwd_dict:', len(kwd_dict))
        for ki, kwd_id in enumerate(kwd_dict):
            print(f'{ki}\t{kwd_id}\t{kwd_dict[kwd_id]}')
            if((ki + 1) >= 10):
                break
        print(), print(), print(), 

        print('kwd_list_dict:', len(kwd_list_dict))
        for ki, meta_id in enumerate(kwd_list_dict):
            print(f'{ki}\t{meta_id}\t{len(kwd_list_dict[meta_id])}\t{kwd_list_dict[meta_id]}')
            if((ki + 1) >= 10):
                break
        print(), print(), print(), 
    
    # kwd_list_dict format: {'meataId': [jealousy, toy, ...]}
    # kwd_dict format: {'kwdId': kwd, ...]}
    return kwd_list_dict, kwd_dict

def hgstat_kaggle_movies_datas(FullData=False):
    import pandas as pd 
    
    #====================================
    #====================================
    #---------------
    # format: movies_metadata
    #---------------
    # adult,belongs_to_collection,budget,genres,homepage,id,imdb_id,original_language,original_title,overview,popularity,poster_path,production_companies,production_countries,release_date,revenue,runtime,spoken_languages,status,tagline,title,video,vote_average,vote_count
    # False,"{'id': 10194, 'name': 'Toy Story Collection', 'poster_path': '/7G9915LfUQ2lVfwMEEhDsn3kT4B.jpg', 'backdrop_path': '/9FBwqcd9IRruEDUrTdcaafOMKUq.jpg'}",30000000,"[{'id': 16, 'name': 'Animation'}, {'id': 35, 'name': 'Comedy'}, {'id': 10751, 'name': 'Family'}]",http://toystory.disney.com/toy-story,862,tt0114709,en,Toy Story,"Led by Woody, Andy's toys live happily in his room until Andy's birthday brings Buzz Lightyear onto the scene. Afraid of losing his place in Andy's heart, Woody plots against Buzz. But when circumstances separate Buzz and Woody from their owner, the duo eventually learns to put aside their differences.",21.946943,/rhIRbceoE9lR4veEXuwCC2wARtG.jpg,"[{'name': 'Pixar Animation Studios', 'id': 3}]","[{'iso_3166_1': 'US', 'name': 'United States of America'}]",1995-10-30,373554033,81.0,"[{'iso_639_1': 'en', 'name': 'English'}]",Released,,Toy Story,False,7.7,5415
    # False,,65000000,"[{'id': 12, 'name': 'Adventure'}, {'id': 14, 'name': 'Fantasy'}, {'id': 10751, 'name': 'Family'}]",,8844,tt0113497,en,Jumanji,"When siblings Judy and Peter discover an enchanted board game that opens the door to a magical world, they unwittingly invite Alan -- an adult who's been trapped inside the game for 26 years -- into their living room. Alan's only hope for freedom is to finish the game, which proves risky as all three find themselves running from giant rhinoceroses, evil monkeys and other terrifying creatures.",17.015539,/vzmL6fP7aPKNKPRTFnZmiUfciyV.jpg,"[{'name': 'TriStar Pictures', 'id': 559}, {'name': 'Teitler Film', 'id': 2550}, {'name': 'Interscope Communications', 'id': 10201}]","[{'iso_3166_1': 'US', 'name': 'United States of America'}]",1995-12-15,262797249,104.0,"[{'iso_639_1': 'en', 'name': 'English'}, {'iso_639_1': 'fr', 'name': 'Français'}]",Released,Roll the dice and unleash the excitement!,Jumanji,False,6.9,2413
    #---------------

    movies_metadata = hgstat_metadata_kaggle(AllFlag=False)
    #=movies_metadata.sort_values(by=['id'])

    #---------------
    #=print(movies_metadata)
    #---------------
    #= 출력결과 :  <movies_metadata.csv>
    #=            id    imdb_id               original_title
    #= 0         862  tt0114709                    Toy Story
    #= 1        8844  tt0113497                      Jumanji
    #= 2       15602  tt0113228             Grumpier Old Men
    #= 3       31357  tt0114885            Waiting to Exhale
    #= 4       11862  tt0113041  Father of the Bride Part II
    #= ...       ...        ...                          ...
    #= 45461  439050  tt6209470                      رگ خواب
    #= 45462  111109  tt2028550          Siglo ng Pagluluwal
    #= 45463   67758  tt0303758                     Betrayal
    #= 45464  227506  tt0008536          Satana likuyushchiy
    #= 45465  461257  tt6980792                     Queerama
    #= 
    #= [45466 rows x 3 columns]
    #---------------


    #====================================
    #====================================
    #---------------
    # format: links
    #---------------
    # movieId,imdbId,tmdbId
    # 1,0114709,862
    # 2,0113497,8844
    # 3,0113228,15602
    #---------------

    links = hgstat_links_kaggle()
    #=links.sort_values(by=['movieId'])

    #---------------
    #=print(links)
    #---------------
    #= 출력결과 :  <links_small.csv>
    #=       movieId   imdbId    tmdbId
    #= 0           1   114709     862.0
    #= 1           2   113497    8844.0
    #= 2           3   113228   15602.0
    #= 3           4   114885   31357.0
    #= 4           5   113041   11862.0
    #= ...       ...      ...       ...
    #= 9120   162672  3859980  402672.0
    #= 9121   163056  4262980  315011.0
    #= 9122   163949  2531318  391698.0
    #= 9123   164977    27660  137608.0
    #= 9124   164979  3447228  410803.0
    #= 
    #= [9125 rows x 3 columns]
    #---------------

    #====================================
    #====================================
    #---------------
    # format: ratings
    #---------------
    # userId,movieId,rating,timestamp
    # 1,110,1.0,1425941529
    # 1,147,4.5,1425942435
    # 1,858,5.0,1425941523
    #---------------
    #=ratings = hgstat_dataframe_kaggle_movies_ratings(FullData=False)
    #=ratings.sort_values(by=['movieId'])

    #---------------
    #=print(ratings)
    #---------------
    #= 출력결과 :  <ratings_small.csv>
    #=         userId  movieId  rating
    #= 0            1       31     2.5
    #= 1            1     1029     3.0
    #= 2            1     1061     3.0
    #= 3            1     1129     2.0
    #= 4            1     1172     4.0
    #= ...        ...      ...     ...
    #= 99999      671     6268     2.5
    #= 100000     671     6269     4.0
    #= 100001     671     6365     4.0
    #= 100002     671     6385     2.5
    #= 100003     671     6565     3.5
    #= 
    #= [100004 rows x 3 columns]
    #---------------

    movie_lists, movie_table = hgstat_kaggle_movies_ratings_lists(FullData=FullData)
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
    #= 출력결과 :  <ratings_small.csv>
    #= movieId  1       2       3       4       ...  162376  162542  162672  163949
    #= userId                                   ...                                
    #= 1           0.0     0.0     0.0     0.0  ...     0.0       0       0       0
    #= 2           0.0     0.0     0.0     0.0  ...     0.0       0       0       0
    #= 3           0.0     0.0     0.0     0.0  ...     0.0       0       0       0
    #= 4           0.0     0.0     0.0     0.0  ...     0.0       0       0       0
    #= 5           0.0     0.0     4.0     0.0  ...     0.0       0       0       0
    #= ...         ...     ...     ...     ...  ...     ...     ...     ...     ...
    #= 667         0.0     0.0     0.0     0.0  ...     0.0       0       0       0
    #= 668         0.0     0.0     0.0     0.0  ...     0.0       0       0       0
    #= 669         0.0     0.0     0.0     0.0  ...     0.0       0       0       0
    #= 670         4.0     0.0     0.0     0.0  ...     0.0       0       0       0
    #= 671         5.0     0.0     0.0     0.0  ...     0.0       0       0       0
    #= 
    #= [671 rows x 9066 columns]
    #---------------

    #=print(movie_table.iloc[0])
    #=print(movie_table.columns)

    #
    return movies_metadata, links, movie_lists, movie_table


def hgstat_get_title_kaggle_by_movieId(movieId, links, movies_metadata):
    # movieId: ratins_list의 movieId
    #-----
    metadata_id = hgstat_get_metadataId_by_movieId(movieId, links)
    #=print(metadata_id)
    movie_title = hgstat_get_title_kaggle_by_metadataId(metadata_id, movies_metadata)
    return movie_title

def hgstat_get_title_kaggle_by_metadataId(metadataId, movies_metadata):
    # movieId: ratins_list의 movieId
    #-----
    movie_title = ''

    if('-' in metadataId): #= metadataId [19730]: 1997-08-20 <=== 이런 경우 있음.
        return movie_title # format error
    #
    try: # 중간에 비정상적인 데이터가 있을 수 있다.
        metadataId = int(metadataId) # float -> int : 862.0 -> 862
    except TypeError: # raise TypeError("cannot convert the series to " "{0}".format(str(converter)))
        #=print("TypeError: cannot convert the series to {", metadataId , "}.format(str(converter)))")
        #=print(links.iloc[links_movieId_inx])
        return movie_title # 내용 없는 제목으로 반환
    except ValueError: # raise ValueError("cannot convert float NaN to integer)
        #=print("ValueError: cannot convert float NaN to integer ")
        #=print(links.iloc[links_movieId_inx])
        return movie_title # 내용 없는 제목으로 반환
    
    #=print(metadataId)
    metadataId_str = str(metadataId) # int -> string
    #=print(metadataId_str)

    #=print('@5')
    #=print(movies_metadata[movies_metadata['id'] == metadataId_str])
    movies_find = movies_metadata[movies_metadata['id'] == metadataId_str]
    if(len(movies_find['original_title'].values) <= 0): # 제목이 없는 경우
        return movie_title
    movie_title = movies_find['original_title'].values[0]

    #=print(len(movie_title), ':', movie_title)

    #-----------
    #=print(f'[{movieId}], {movie_title}')

    return movie_title

def hgstat_get_genres_kaggle_by_metadataId(metadataId, movies_metadata):
    # movieId: ratins_list의 movieId
    #-----
    genres_list = []

    if('-' in metadataId): #= metadataId [19730]: 1997-08-20 <=== 이런 경우 있음.
        return genres_list        

    #
    try: # 중간에 비정상적인 데이터가 있을 수 있다.
        metadataId = int(metadataId) # float -> int : 862.0 -> 862
    except TypeError: # raise TypeError("cannot convert the series to " "{0}".format(str(converter)))
        #=print("TypeError: cannot convert the series to {", metadataId , "}.format(str(converter)))")
        #=print(links.iloc[links_movieId_inx])
        return genres_list # 내용 없는 것으로 반환
    except ValueError: # raise ValueError("cannot convert float NaN to integer)
        #=print("ValueError: cannot convert float NaN to integer ")
        #=print(links.iloc[links_movieId_inx])
        return genres_list # 내용 없는 것으로 반환
    
    #=print(metadataId)
    metadataId_str = str(metadataId) # int -> string
    #=print(metadataId_str)

    #=print('@5')
    #=print(movies_metadata[movies_metadata['id'] == metadataId_str])
    movies_find = movies_metadata[movies_metadata['id'] == metadataId_str]
    if(len(movies_find['genres'].values) <= 0): # 장르가 없는 경우
        return genres_list
    genres_kaggle = movies_find['genres'].values[0]

    # 장르 목록으로 변환
    GenreListDict = list(eval(genres_kaggle)) # format: [{'id': 16, 'name': 'Animation'}, {'id': 35, 'name': 'Comedy'}, {'id': 10751, 'name': 'Family'}]
    genres_list = [x['name'] for x in GenreListDict] # format: [{'id': 16, 'name': 'Animation'}, {'id': 35, 'name': 'Comedy'}, {'id': 10751, 'name': 'Family'}]

    #=print(len(genres_list), ':', genres_list)

    #-----------
    #=print(f'[{movieId}], {genres_list}')

    return genres_list

def hgstat_get_overview_kaggle_by_metadataId(metadataId, movies_metadata):
    # movieId: ratins_list의 movieId
    #-----
    movie_overview = ''

    if('-' in metadataId): #= metadataId [19730]: 1997-08-20 <=== 이런 경우 있음.
        return movie_overview        

    #
    try: # 중간에 비정상적인 데이터가 있을 수 있다.
        metadataId = int(metadataId) # float -> int : 862.0 -> 862
    except TypeError: # raise TypeError("cannot convert the series to " "{0}".format(str(converter)))
        #=print("TypeError: cannot convert the series to {", metadataId , "}.format(str(converter)))")
        #=print(links.iloc[links_movieId_inx])
        return movie_overview # 내용 없는 것으로 반환
    except ValueError: # raise ValueError("cannot convert float NaN to integer)
        #=print("ValueError: cannot convert float NaN to integer ")
        #=print(links.iloc[links_movieId_inx])
        return movie_overview # 내용 없는 것으로 반환
    
    #=print(metadataId)
    metadataId_str = str(metadataId) # int -> string
    #=print(metadataId_str)

    #=print('@5')
    #=print(movies_metadata[movies_metadata['id'] == metadataId_str])
    movies_find = movies_metadata[movies_metadata['id'] == metadataId_str]
    if(len(movies_find['overview'].values) <= 0): # 줄거리가 없는 경우
        return movie_overview
    movie_overview = movies_find['overview'].values[0]

    #=print(len(movie_overview), ':', movie_overview)

    #-----------
    #=print(f'[{movieId}], {movie_overview}')

    return movie_overview
    
def hgstat_get_kwd_list__kagmov_by_movieId(movieId, links, kwd_list_dict):
    # movieId: ratins_list의 movieId
    #
    kwd_list = []
    
    #
    #=print('@2')
    links_movieId_inx = links.index[links['movieId'] == movieId]
    #=print(links_movieId_inx)
    #=print(links.iloc[links_movieId_inx])
    
    #
    #=print('@3')
    metadata_id = links.iloc[links_movieId_inx]['tmdbId']
    #=print(metadata_id)
    
    try: # 중간에 비정상적인 데이터가 있을 수 있다.
        metadata_id = int(metadata_id) # float -> int : 862.0 -> 862
    except TypeError: # raise TypeError("cannot convert the series to " "{0}".format(str(converter)))
        #=print("TypeError: cannot convert the series to {", metadata_id , "}.format(str(converter)))")
        #=print(links.iloc[links_movieId_inx])
        return kwd_list # 내용 없이 반환
    except ValueError: # raise ValueError("cannot convert float NaN to integer)
        #=print("ValueError: cannot convert float NaN to integer ")
        #=print(links.iloc[links_movieId_inx])
        return kwd_list # 내용 없이 반환
    
    #=print(metadata_id)
    #=metadata_id = str(metadata_id) # int -> string
    #=print(metadata_id)

    #=print('@5')
    #=print(movies_metadata[movies_metadata['id'] == metadata_id])
    kwd_list = kwd_list_dict[metadata_id]
    #=print(len(kwd_list), ':', kwd_list)

    #-----------
    #=print(f'[{movieId}], {kwd_list}')

    return kwd_list

#=================================
#=================================
def hgstat_title_dict__kagmov(movies_metadata=None, links=None, debugPrint=False):
    #====================================
    #====================================
    #---------------
    # format: movies_metadata
    #---------------
    # adult,belongs_to_collection,budget,genres,homepage,id,imdb_id,original_language,original_title,overview,popularity,poster_path,production_companies,production_countries,release_date,revenue,runtime,spoken_languages,status,tagline,title,video,vote_average,vote_count
    # False,"{'id': 10194, 'name': 'Toy Story Collection', 'poster_path': '/7G9915LfUQ2lVfwMEEhDsn3kT4B.jpg', 'backdrop_path': '/9FBwqcd9IRruEDUrTdcaafOMKUq.jpg'}",30000000,"[{'id': 16, 'name': 'Animation'}, {'id': 35, 'name': 'Comedy'}, {'id': 10751, 'name': 'Family'}]",http://toystory.disney.com/toy-story,862,tt0114709,en,Toy Story,"Led by Woody, Andy's toys live happily in his room until Andy's birthday brings Buzz Lightyear onto the scene. Afraid of losing his place in Andy's heart, Woody plots against Buzz. But when circumstances separate Buzz and Woody from their owner, the duo eventually learns to put aside their differences.",21.946943,/rhIRbceoE9lR4veEXuwCC2wARtG.jpg,"[{'name': 'Pixar Animation Studios', 'id': 3}]","[{'iso_3166_1': 'US', 'name': 'United States of America'}]",1995-10-30,373554033,81.0,"[{'iso_639_1': 'en', 'name': 'English'}]",Released,,Toy Story,False,7.7,5415
    # False,,65000000,"[{'id': 12, 'name': 'Adventure'}, {'id': 14, 'name': 'Fantasy'}, {'id': 10751, 'name': 'Family'}]",,8844,tt0113497,en,Jumanji,"When siblings Judy and Peter discover an enchanted board game that opens the door to a magical world, they unwittingly invite Alan -- an adult who's been trapped inside the game for 26 years -- into their living room. Alan's only hope for freedom is to finish the game, which proves risky as all three find themselves running from giant rhinoceroses, evil monkeys and other terrifying creatures.",17.015539,/vzmL6fP7aPKNKPRTFnZmiUfciyV.jpg,"[{'name': 'TriStar Pictures', 'id': 559}, {'name': 'Teitler Film', 'id': 2550}, {'name': 'Interscope Communications', 'id': 10201}]","[{'iso_3166_1': 'US', 'name': 'United States of America'}]",1995-12-15,262797249,104.0,"[{'iso_639_1': 'en', 'name': 'English'}, {'iso_639_1': 'fr', 'name': 'Français'}]",Released,Roll the dice and unleash the excitement!,Jumanji,False,6.9,2413
    #---------------
    if(movies_metadata is None):
        movies_metadata = hgstat_metadata_kaggle(AllFlag=False)
        #=movies_metadata.sort_values(by=['id'])

    #---------------
    #=print(movies_metadata)
    #---------------
    #= 출력결과 :  <movies_metadata.csv>
    #=            id    imdb_id               original_title
    #= 0         862  tt0114709                    Toy Story
    #= 1        8844  tt0113497                      Jumanji
    #= 2       15602  tt0113228             Grumpier Old Men
    #= 3       31357  tt0114885            Waiting to Exhale
    #= 4       11862  tt0113041  Father of the Bride Part II
    #= ...       ...        ...                          ...
    #= 45461  439050  tt6209470                      رگ خواب
    #= 45462  111109  tt2028550          Siglo ng Pagluluwal
    #= 45463   67758  tt0303758                     Betrayal
    #= 45464  227506  tt0008536          Satana likuyushchiy
    #= 45465  461257  tt6980792                     Queerama
    #= 
    #= [45466 rows x 3 columns]
    #---------------
    #=            id  ...                                           overview
    #= 0         862  ...  Led by Woody, Andy's toys live happily in his ...
    #= 1        8844  ...  When siblings Judy and Peter discover an encha...
    #= 2       15602  ...  A family wedding reignites the ancient feud be...
    #= 3       31357  ...  Cheated on, mistreated and stepped on, the wom...
    #= 4       11862  ...  Just when George Banks has recovered from his ...
    #= ...       ...  ...                                                ...
    #= 45461  439050  ...        Rising and falling between a man and woman.
    #= 45462  111109  ...  An artist struggles to finish his work while a...
    #= 45463   67758  ...  When one of her hits goes wrong, a professiona...
    #= 45464  227506  ...  In a small town live two brothers, one a minis...
    #= 45465  461257  ...  50 years after decriminalisation of homosexual...
    #= 
    #= [45466 rows x 4 columns]
    #---------------

    if(links is None):
        links = hgstat_links_kaggle()
    #---------------
    #=print(links)
    #---------------
    #= 출력결과 :  <links_small.csv>
    #=       movieId   imdbId    tmdbId
    #= 0           1   114709     862.0
    #= 1           2   113497    8844.0
    #= 2           3   113228   15602.0
    #= 3           4   114885   31357.0
    #= 4           5   113041   11862.0
    #= ...       ...      ...       ...
    #= 9120   162672  3859980  402672.0
    #= 9121   163056  4262980  315011.0
    #= 9122   163949  2531318  391698.0
    #= 9123   164977    27660  137608.0
    #= 9124   164979  3447228  410803.0
    #= 
    #= [9125 rows x 3 columns]
    #---------------


    #============================
    #============================
    original_titles = movies_metadata['original_title'].tolist()
    if(debugPrint == True):
        print(f'original_titles: {len(original_titles)}')
        #=print(*original_titles, sep='\n')

    '''
    # 일부 출력해 본다.
    movie_num = len(original_titles)
    prt_num = 0
    prt_begin = 0
    prt_begin = 31
    prt_num = 10
    prt_num = 3
    for i in range(prt_begin, movie_num):
        title = original_titles[i]
        print(f"{i}: {title}")
        #
        if(prt_num > 0):
            if(i >= (prt_begin + prt_num -1)):
                break
    '''

    #
    title_dict = {}

    # <original_titles> 내용이 있는 것 중에서 사전 목록 생성
    for bi, title in enumerate(original_titles):
        #
        metadataId = movies_metadata.iloc[bi]['id']
        #=print(f'metadataId [{bi}]:', metadataId)
        movieId = hgstat_get_movieId_by_metadataId(metadataId, links)
        if(movieId == None): # 이런 경우도 있다.
            continue
        movieId = int(movieId)
        
        #
        if(isinstance(title, float)): # 'NaN' 내용이 없는 경우
            pass
        else:
            if(isinstance(title, float)): # {title} 값이 없는 경우
                #=print(f'{i}: (isinstance({title}, float)) ')
                pass
            else:
                #=print(f"{title}: {title}")
                title_dict[movieId] = title
    #==========
    return title_dict, movies_metadata

def hgstat_release_dict__kagmov(movies_metadata=None, links=None, debugPrint=False):
    #====================================
    #====================================
    #---------------
    # format: movies_metadata
    #---------------
    # adult,belongs_to_collection,budget,genres,homepage,id,imdb_id,original_language,original_title,overview,popularity,poster_path,production_companies,production_countries,release_date,revenue,runtime,spoken_languages,status,tagline,title,video,vote_average,vote_count
    # False,"{'id': 10194, 'name': 'Toy Story Collection', 'poster_path': '/7G9915LfUQ2lVfwMEEhDsn3kT4B.jpg', 'backdrop_path': '/9FBwqcd9IRruEDUrTdcaafOMKUq.jpg'}",30000000,"[{'id': 16, 'name': 'Animation'}, {'id': 35, 'name': 'Comedy'}, {'id': 10751, 'name': 'Family'}]",http://toystory.disney.com/toy-story,862,tt0114709,en,Toy Story,"Led by Woody, Andy's toys live happily in his room until Andy's birthday brings Buzz Lightyear onto the scene. Afraid of losing his place in Andy's heart, Woody plots against Buzz. But when circumstances separate Buzz and Woody from their owner, the duo eventually learns to put aside their differences.",21.946943,/rhIRbceoE9lR4veEXuwCC2wARtG.jpg,"[{'name': 'Pixar Animation Studios', 'id': 3}]","[{'iso_3166_1': 'US', 'name': 'United States of America'}]",1995-10-30,373554033,81.0,"[{'iso_639_1': 'en', 'name': 'English'}]",Released,,Toy Story,False,7.7,5415
    # False,,65000000,"[{'id': 12, 'name': 'Adventure'}, {'id': 14, 'name': 'Fantasy'}, {'id': 10751, 'name': 'Family'}]",,8844,tt0113497,en,Jumanji,"When siblings Judy and Peter discover an enchanted board game that opens the door to a magical world, they unwittingly invite Alan -- an adult who's been trapped inside the game for 26 years -- into their living room. Alan's only hope for freedom is to finish the game, which proves risky as all three find themselves running from giant rhinoceroses, evil monkeys and other terrifying creatures.",17.015539,/vzmL6fP7aPKNKPRTFnZmiUfciyV.jpg,"[{'name': 'TriStar Pictures', 'id': 559}, {'name': 'Teitler Film', 'id': 2550}, {'name': 'Interscope Communications', 'id': 10201}]","[{'iso_3166_1': 'US', 'name': 'United States of America'}]",1995-12-15,262797249,104.0,"[{'iso_639_1': 'en', 'name': 'English'}, {'iso_639_1': 'fr', 'name': 'Français'}]",Released,Roll the dice and unleash the excitement!,Jumanji,False,6.9,2413
    #---------------
    if(movies_metadata is None):
        movies_metadata = hgstat_metadata_kaggle(AllFlag=False)
        #=movies_metadata.sort_values(by=['id'])

    #---------------
    #=print(movies_metadata)
    #---------------
    #= 출력결과 :  <movies_metadata.csv>
    #=            id    imdb_id               original_title
    #= 0         862  tt0114709                    Toy Story
    #= 1        8844  tt0113497                      Jumanji
    #= 2       15602  tt0113228             Grumpier Old Men
    #= 3       31357  tt0114885            Waiting to Exhale
    #= 4       11862  tt0113041  Father of the Bride Part II
    #= ...       ...        ...                          ...
    #= 45461  439050  tt6209470                      رگ خواب
    #= 45462  111109  tt2028550          Siglo ng Pagluluwal
    #= 45463   67758  tt0303758                     Betrayal
    #= 45464  227506  tt0008536          Satana likuyushchiy
    #= 45465  461257  tt6980792                     Queerama
    #= 
    #= [45466 rows x 3 columns]
    #---------------
    #=            id  ...                                           overview
    #= 0         862  ...  Led by Woody, Andy's toys live happily in his ...
    #= 1        8844  ...  When siblings Judy and Peter discover an encha...
    #= 2       15602  ...  A family wedding reignites the ancient feud be...
    #= 3       31357  ...  Cheated on, mistreated and stepped on, the wom...
    #= 4       11862  ...  Just when George Banks has recovered from his ...
    #= ...       ...  ...                                                ...
    #= 45461  439050  ...        Rising and falling between a man and woman.
    #= 45462  111109  ...  An artist struggles to finish his work while a...
    #= 45463   67758  ...  When one of her hits goes wrong, a professiona...
    #= 45464  227506  ...  In a small town live two brothers, one a minis...
    #= 45465  461257  ...  50 years after decriminalisation of homosexual...
    #= 
    #= [45466 rows x 4 columns]
    #---------------

    if(links is None):
        links = hgstat_links_kaggle()
    #---------------
    #=print(links)
    #---------------
    #= 출력결과 :  <links_small.csv>
    #=       movieId   imdbId    tmdbId
    #= 0           1   114709     862.0
    #= 1           2   113497    8844.0
    #= 2           3   113228   15602.0
    #= 3           4   114885   31357.0
    #= 4           5   113041   11862.0
    #= ...       ...      ...       ...
    #= 9120   162672  3859980  402672.0
    #= 9121   163056  4262980  315011.0
    #= 9122   163949  2531318  391698.0
    #= 9123   164977    27660  137608.0
    #= 9124   164979  3447228  410803.0
    #= 
    #= [9125 rows x 3 columns]
    #---------------

    #============================
    #============================
    release_dates = movies_metadata['release_date'].tolist()
    if(debugPrint == True):
        print(f'release_dates: {len(release_dates)}')
        #=print(*release_dates, sep='\n')

    '''
    # 일부 출력해 본다.
    movie_num = len(release_dates)
    prt_num = 0
    prt_begin = 0
    prt_begin = 31
    prt_num = 10
    prt_num = 3
    for i in range(prt_begin, movie_num):
        release_date = release_dates[i]
        print(f"{i}: {release_date}")
        #
        if(prt_num > 0):
            if(i >= (prt_begin + prt_num -1)):
                break
    '''

    #
    release_dict = {}

    # <release_dates> 내용이 있는 것 중에서 사전 목록 생성
    for bi, release_date in enumerate(release_dates):
        #
        metadataId = movies_metadata.iloc[bi]['id']
        #=print(f'metadataId [{bi}]:', metadataId)
        movieId = hgstat_get_movieId_by_metadataId(metadataId, links)
        if(movieId == None): # 이런 경우도 있다.
            continue
        movieId = int(movieId)
        
        #
        if(isinstance(release_date, float)): # 'NaN' 내용이 없는 경우
            pass
        else:
            if(isinstance(release_date, float)): # {release_date} 값이 없는 경우
                #=print(f'{i}: (isinstance({release_date}, float)) ')
                pass
            else:
                #=print(f"{release_date}: {release_date}")
                release_dict[movieId] = release_date
    #==========
    return release_dict, movies_metadata

def hgstat_collection_dict__kagmov(movies_metadata=None, links=None, debugPrint=False):
    #====================================
    #====================================
    #---------------
    # format: movies_metadata
    #---------------
    # adult,belongs_to_collection,budget,genres,homepage,id,imdb_id,original_language,original_title,overview,popularity,poster_path,production_companies,production_countries,release_date,revenue,runtime,spoken_languages,status,tagline,title,video,vote_average,vote_count
    # False,"{'id': 10194, 'name': 'Toy Story Collection', 'poster_path': '/7G9915LfUQ2lVfwMEEhDsn3kT4B.jpg', 'backdrop_path': '/9FBwqcd9IRruEDUrTdcaafOMKUq.jpg'}",30000000,"[{'id': 16, 'name': 'Animation'}, {'id': 35, 'name': 'Comedy'}, {'id': 10751, 'name': 'Family'}]",http://toystory.disney.com/toy-story,862,tt0114709,en,Toy Story,"Led by Woody, Andy's toys live happily in his room until Andy's birthday brings Buzz Lightyear onto the scene. Afraid of losing his place in Andy's heart, Woody plots against Buzz. But when circumstances separate Buzz and Woody from their owner, the duo eventually learns to put aside their differences.",21.946943,/rhIRbceoE9lR4veEXuwCC2wARtG.jpg,"[{'name': 'Pixar Animation Studios', 'id': 3}]","[{'iso_3166_1': 'US', 'name': 'United States of America'}]",1995-10-30,373554033,81.0,"[{'iso_639_1': 'en', 'name': 'English'}]",Released,,Toy Story,False,7.7,5415
    # False,,65000000,"[{'id': 12, 'name': 'Adventure'}, {'id': 14, 'name': 'Fantasy'}, {'id': 10751, 'name': 'Family'}]",,8844,tt0113497,en,Jumanji,"When siblings Judy and Peter discover an enchanted board game that opens the door to a magical world, they unwittingly invite Alan -- an adult who's been trapped inside the game for 26 years -- into their living room. Alan's only hope for freedom is to finish the game, which proves risky as all three find themselves running from giant rhinoceroses, evil monkeys and other terrifying creatures.",17.015539,/vzmL6fP7aPKNKPRTFnZmiUfciyV.jpg,"[{'name': 'TriStar Pictures', 'id': 559}, {'name': 'Teitler Film', 'id': 2550}, {'name': 'Interscope Communications', 'id': 10201}]","[{'iso_3166_1': 'US', 'name': 'United States of America'}]",1995-12-15,262797249,104.0,"[{'iso_639_1': 'en', 'name': 'English'}, {'iso_639_1': 'fr', 'name': 'Français'}]",Released,Roll the dice and unleash the excitement!,Jumanji,False,6.9,2413
    #---------------
    if(movies_metadata is None):
        movies_metadata = hgstat_metadata_kaggle(AllFlag=False)
        #=movies_metadata.sort_values(by=['id'])

    #---------------
    #=print(movies_metadata)
    #---------------
    #= 출력결과 :  <movies_metadata.csv>
    #=            id    imdb_id               original_title
    #= 0         862  tt0114709                    Toy Story
    #= 1        8844  tt0113497                      Jumanji
    #= 2       15602  tt0113228             Grumpier Old Men
    #= 3       31357  tt0114885            Waiting to Exhale
    #= 4       11862  tt0113041  Father of the Bride Part II
    #= ...       ...        ...                          ...
    #= 45461  439050  tt6209470                      رگ خواب
    #= 45462  111109  tt2028550          Siglo ng Pagluluwal
    #= 45463   67758  tt0303758                     Betrayal
    #= 45464  227506  tt0008536          Satana likuyushchiy
    #= 45465  461257  tt6980792                     Queerama
    #= 
    #= [45466 rows x 3 columns]
    #---------------
    #=            id  ...                                           overview
    #= 0         862  ...  Led by Woody, Andy's toys live happily in his ...
    #= 1        8844  ...  When siblings Judy and Peter discover an encha...
    #= 2       15602  ...  A family wedding reignites the ancient feud be...
    #= 3       31357  ...  Cheated on, mistreated and stepped on, the wom...
    #= 4       11862  ...  Just when George Banks has recovered from his ...
    #= ...       ...  ...                                                ...
    #= 45461  439050  ...        Rising and falling between a man and woman.
    #= 45462  111109  ...  An artist struggles to finish his work while a...
    #= 45463   67758  ...  When one of her hits goes wrong, a professiona...
    #= 45464  227506  ...  In a small town live two brothers, one a minis...
    #= 45465  461257  ...  50 years after decriminalisation of homosexual...
    #= 
    #= [45466 rows x 4 columns]
    #---------------

    if(links is None):
        links = hgstat_links_kaggle()
    #---------------
    #=print(links)
    #---------------
    #= 출력결과 :  <links_small.csv>
    #=       movieId   imdbId    tmdbId
    #= 0           1   114709     862.0
    #= 1           2   113497    8844.0
    #= 2           3   113228   15602.0
    #= 3           4   114885   31357.0
    #= 4           5   113041   11862.0
    #= ...       ...      ...       ...
    #= 9120   162672  3859980  402672.0
    #= 9121   163056  4262980  315011.0
    #= 9122   163949  2531318  391698.0
    #= 9123   164977    27660  137608.0
    #= 9124   164979  3447228  410803.0
    #= 
    #= [9125 rows x 3 columns]
    #---------------

    #============================
    #============================
    belongs_to_collection = movies_metadata['belongs_to_collection'].tolist()
    if(debugPrint == True):
        print(f'belongs_to_collection: {len(belongs_to_collection)}')
        #=print(*belongs_to_collection, sep='\n')

    '''
    # 일부 출력해 본다.
    movie_num = len(belongs_to_collection)
    prt_num = 0
    prt_begin = 0
    prt_begin = 31
    prt_num = 10
    prt_num = 3
    for i in range(prt_begin, movie_num):
        collection = belongs_to_collection[i]
        print(f"{i}: {collection}")
        #
        if(prt_num > 0):
            if(i >= (prt_begin + prt_num -1)):
                break
    '''

    #
    collection_dict = {}
    belong_to_collection_dict = {}

    # <belongs_to_collection> 내용이 있는 것 중에서 컬렉션 사전 목록 생성
    for bi, item in enumerate(belongs_to_collection):
        #
        metadataId = movies_metadata.iloc[bi]['id']
        #=print(f'metadataId [{bi}]:', metadataId)
        movieId = hgstat_get_movieId_by_metadataId(metadataId, links)
        if(movieId == None): # 이런 경우도 있다.
            continue
        movieId = int(movieId)
        
        #
        if(isinstance(item, float)): # 'NaN' 내용이 없는 경우
            continue
        #
        collection_value = belongs_to_collection[bi]
        if(isinstance(collection_value, float)): # {collection} 값이 없는 경우
            #=print(f'{i}: (isinstance({collection}, float)) ')
            continue

        # format: {'id': 10194, 'name': 'Toy Story Collection', 'poster_path': '/7G9915LfUQ2lVfwMEEhDsn3kT4B.jpg', 'backdrop_path': '/9FBwqcd9IRruEDUrTdcaafOMKUq.jpg'}
        CollectionDict = eval(collection_value) # format: {'id': 10194, 'name': 'Toy Story Collection', 'poster_path': '/7G9915LfUQ2lVfwMEEhDsn3kT4B.jpg', 'backdrop_path': '/9FBwqcd9IRruEDUrTdcaafOMKUq.jpg'}
        CollectionID = CollectionDict['id']
        CollectionName = CollectionDict['name']
        #=print(f"{CollectionID}: {CollectionName}")

        CollectionName_Check = None
        try: # 중간에 비정상적인 데이터가 있을 수 있다.
            CollectionName_Check = collection_dict[CollectionID]
        except KeyError:#{KeyError:10194}발생, kag-mov와 mov-len 혼용할 때
            pass
        if(CollectionName_Check == None):
            collection_dict[CollectionID] = CollectionName
        #
        belong_to_collection_dict[movieId] = CollectionName
    #==========
    return belong_to_collection_dict, collection_dict

def hgstat_genres_dict__kagmov(movies_metadata=None, links=None, debugPrint=False):
    #====================================
    #====================================
    #---------------
    # format: movies_metadata
    #---------------
    # adult,belongs_to_collection,budget,genres,homepage,id,imdb_id,original_language,original_title,overview,popularity,poster_path,production_companies,production_countries,release_date,revenue,runtime,spoken_languages,status,tagline,title,video,vote_average,vote_count
    # False,"{'id': 10194, 'name': 'Toy Story Collection', 'poster_path': '/7G9915LfUQ2lVfwMEEhDsn3kT4B.jpg', 'backdrop_path': '/9FBwqcd9IRruEDUrTdcaafOMKUq.jpg'}",30000000,"[{'id': 16, 'name': 'Animation'}, {'id': 35, 'name': 'Comedy'}, {'id': 10751, 'name': 'Family'}]",http://toystory.disney.com/toy-story,862,tt0114709,en,Toy Story,"Led by Woody, Andy's toys live happily in his room until Andy's birthday brings Buzz Lightyear onto the scene. Afraid of losing his place in Andy's heart, Woody plots against Buzz. But when circumstances separate Buzz and Woody from their owner, the duo eventually learns to put aside their differences.",21.946943,/rhIRbceoE9lR4veEXuwCC2wARtG.jpg,"[{'name': 'Pixar Animation Studios', 'id': 3}]","[{'iso_3166_1': 'US', 'name': 'United States of America'}]",1995-10-30,373554033,81.0,"[{'iso_639_1': 'en', 'name': 'English'}]",Released,,Toy Story,False,7.7,5415
    # False,,65000000,"[{'id': 12, 'name': 'Adventure'}, {'id': 14, 'name': 'Fantasy'}, {'id': 10751, 'name': 'Family'}]",,8844,tt0113497,en,Jumanji,"When siblings Judy and Peter discover an enchanted board game that opens the door to a magical world, they unwittingly invite Alan -- an adult who's been trapped inside the game for 26 years -- into their living room. Alan's only hope for freedom is to finish the game, which proves risky as all three find themselves running from giant rhinoceroses, evil monkeys and other terrifying creatures.",17.015539,/vzmL6fP7aPKNKPRTFnZmiUfciyV.jpg,"[{'name': 'TriStar Pictures', 'id': 559}, {'name': 'Teitler Film', 'id': 2550}, {'name': 'Interscope Communications', 'id': 10201}]","[{'iso_3166_1': 'US', 'name': 'United States of America'}]",1995-12-15,262797249,104.0,"[{'iso_639_1': 'en', 'name': 'English'}, {'iso_639_1': 'fr', 'name': 'Français'}]",Released,Roll the dice and unleash the excitement!,Jumanji,False,6.9,2413
    #---------------
    if(movies_metadata is None):
        movies_metadata = hgstat_metadata_kaggle(AllFlag=False)
        #=movies_metadata.sort_values(by=['id'])

    #---------------
    #=print(movies_metadata)
    #---------------
    #= 출력결과 :  <movies_metadata.csv>
    #=            id    imdb_id               original_title
    #= 0         862  tt0114709                    Toy Story
    #= 1        8844  tt0113497                      Jumanji
    #= 2       15602  tt0113228             Grumpier Old Men
    #= 3       31357  tt0114885            Waiting to Exhale
    #= 4       11862  tt0113041  Father of the Bride Part II
    #= ...       ...        ...                          ...
    #= 45461  439050  tt6209470                      رگ خواب
    #= 45462  111109  tt2028550          Siglo ng Pagluluwal
    #= 45463   67758  tt0303758                     Betrayal
    #= 45464  227506  tt0008536          Satana likuyushchiy
    #= 45465  461257  tt6980792                     Queerama
    #= 
    #= [45466 rows x 3 columns]
    #---------------
    #=            id  ...                                           overview
    #= 0         862  ...  Led by Woody, Andy's toys live happily in his ...
    #= 1        8844  ...  When siblings Judy and Peter discover an encha...
    #= 2       15602  ...  A family wedding reignites the ancient feud be...
    #= 3       31357  ...  Cheated on, mistreated and stepped on, the wom...
    #= 4       11862  ...  Just when George Banks has recovered from his ...
    #= ...       ...  ...                                                ...
    #= 45461  439050  ...        Rising and falling between a man and woman.
    #= 45462  111109  ...  An artist struggles to finish his work while a...
    #= 45463   67758  ...  When one of her hits goes wrong, a professiona...
    #= 45464  227506  ...  In a small town live two brothers, one a minis...
    #= 45465  461257  ...  50 years after decriminalisation of homosexual...
    #= 
    #= [45466 rows x 4 columns]
    #---------------

    if(links is None):
        links = hgstat_links_kaggle()
    #---------------
    #=print(links)
    #---------------
    #= 출력결과 :  <links_small.csv>
    #=       movieId   imdbId    tmdbId
    #= 0           1   114709     862.0
    #= 1           2   113497    8844.0
    #= 2           3   113228   15602.0
    #= 3           4   114885   31357.0
    #= 4           5   113041   11862.0
    #= ...       ...      ...       ...
    #= 9120   162672  3859980  402672.0
    #= 9121   163056  4262980  315011.0
    #= 9122   163949  2531318  391698.0
    #= 9123   164977    27660  137608.0
    #= 9124   164979  3447228  410803.0
    #= 
    #= [9125 rows x 3 columns]
    #---------------

    #============================
    #============================
    genres_list = movies_metadata['genres'].tolist()
    if(debugPrint == True):
        print(f'genres_list: {len(genres_list)}')
        #=print(*genres_list, sep='\n')

    '''
    # 일부 출력해 본다.
    movie_num = len(genres_list)
    prt_num = 0
    prt_begin = 0
    prt_begin = 31
    prt_num = 10
    prt_num = 3
    for i in range(prt_begin, movie_num):
        genres = genres_list[i]
        print(f"{i}: {genres}")
        #
        if(prt_num > 0):
            if(i >= (prt_begin + prt_num -1)):
                break
    '''

    #
    genres_dict = {}

    # <release_dates> 내용이 있는 것 중에서 사전 목록 생성
    for bi, genres in enumerate(genres_list):
        #
        metadataId = movies_metadata.iloc[bi]['id']
        #=print(f'metadataId [{bi}]:', metadataId)
        movieId = hgstat_get_movieId_by_metadataId(metadataId, links)
        if(movieId == None): # 이런 경우도 있다.
            continue
        movieId = int(movieId)
        
        #
        if(isinstance(genres, float)): # 'NaN' 내용이 없는 경우
            pass
        else:
            if(isinstance(genres, float)): # {genres} 값이 없는 경우
                #=print(f'{i}: (isinstance({genres}, float)) ')
                pass
            else:
                #=print(f"{genres}: {genres}")
                # [genres]는 사전의 목록 형식의 문자열이므로 변환해야 한다.
                # format: [{'id': 16, 'name': 'Animation'}, {'id': 35, 'name': 'Comedy'}, {'id': 10751, 'name': 'Family'}]
                GenreListDict = list(eval(genres)) # format: [{'id': 16, 'name': 'Animation'}, {'id': 35, 'name': 'Comedy'}, {'id': 10751, 'name': 'Family'}]
                GenreList = [x['name'] for x in GenreListDict] # format: [{'id': 16, 'name': 'Animation'}, {'id': 35, 'name': 'Comedy'}, {'id': 10751, 'name': 'Family'}]
                #
                genres_dict[movieId] = GenreList
    #==========
    return genres_dict, movies_metadata

def hgstat_vote_average_dict__kagmov(movies_metadata=None, links=None, debugPrint=False):
    #====================================
    #====================================
    #---------------
    # format: movies_metadata
    #---------------
    # adult,belongs_to_collection,budget,genres,homepage,id,imdb_id,original_language,original_title,overview,popularity,poster_path,production_companies,production_countries,release_date,revenue,runtime,spoken_languages,status,tagline,title,video,vote_average,vote_count
    # False,"{'id': 10194, 'name': 'Toy Story Collection', 'poster_path': '/7G9915LfUQ2lVfwMEEhDsn3kT4B.jpg', 'backdrop_path': '/9FBwqcd9IRruEDUrTdcaafOMKUq.jpg'}",30000000,"[{'id': 16, 'name': 'Animation'}, {'id': 35, 'name': 'Comedy'}, {'id': 10751, 'name': 'Family'}]",http://toystory.disney.com/toy-story,862,tt0114709,en,Toy Story,"Led by Woody, Andy's toys live happily in his room until Andy's birthday brings Buzz Lightyear onto the scene. Afraid of losing his place in Andy's heart, Woody plots against Buzz. But when circumstances separate Buzz and Woody from their owner, the duo eventually learns to put aside their differences.",21.946943,/rhIRbceoE9lR4veEXuwCC2wARtG.jpg,"[{'name': 'Pixar Animation Studios', 'id': 3}]","[{'iso_3166_1': 'US', 'name': 'United States of America'}]",1995-10-30,373554033,81.0,"[{'iso_639_1': 'en', 'name': 'English'}]",Released,,Toy Story,False,7.7,5415
    # False,,65000000,"[{'id': 12, 'name': 'Adventure'}, {'id': 14, 'name': 'Fantasy'}, {'id': 10751, 'name': 'Family'}]",,8844,tt0113497,en,Jumanji,"When siblings Judy and Peter discover an enchanted board game that opens the door to a magical world, they unwittingly invite Alan -- an adult who's been trapped inside the game for 26 years -- into their living room. Alan's only hope for freedom is to finish the game, which proves risky as all three find themselves running from giant rhinoceroses, evil monkeys and other terrifying creatures.",17.015539,/vzmL6fP7aPKNKPRTFnZmiUfciyV.jpg,"[{'name': 'TriStar Pictures', 'id': 559}, {'name': 'Teitler Film', 'id': 2550}, {'name': 'Interscope Communications', 'id': 10201}]","[{'iso_3166_1': 'US', 'name': 'United States of America'}]",1995-12-15,262797249,104.0,"[{'iso_639_1': 'en', 'name': 'English'}, {'iso_639_1': 'fr', 'name': 'Français'}]",Released,Roll the dice and unleash the excitement!,Jumanji,False,6.9,2413
    #---------------
    if(movies_metadata is None):
        movies_metadata = hgstat_metadata_kaggle(AllFlag=False)
        #=movies_metadata.sort_values(by=['id'])

    #---------------
    #=print(movies_metadata)
    #---------------
    #= 출력결과 :  <movies_metadata.csv>
    #=            id    imdb_id               original_title
    #= 0         862  tt0114709                    Toy Story
    #= 1        8844  tt0113497                      Jumanji
    #= 2       15602  tt0113228             Grumpier Old Men
    #= 3       31357  tt0114885            Waiting to Exhale
    #= 4       11862  tt0113041  Father of the Bride Part II
    #= ...       ...        ...                          ...
    #= 45461  439050  tt6209470                      رگ خواب
    #= 45462  111109  tt2028550          Siglo ng Pagluluwal
    #= 45463   67758  tt0303758                     Betrayal
    #= 45464  227506  tt0008536          Satana likuyushchiy
    #= 45465  461257  tt6980792                     Queerama
    #= 
    #= [45466 rows x 3 columns]
    #---------------
    #=            id  ...                                           overview
    #= 0         862  ...  Led by Woody, Andy's toys live happily in his ...
    #= 1        8844  ...  When siblings Judy and Peter discover an encha...
    #= 2       15602  ...  A family wedding reignites the ancient feud be...
    #= 3       31357  ...  Cheated on, mistreated and stepped on, the wom...
    #= 4       11862  ...  Just when George Banks has recovered from his ...
    #= ...       ...  ...                                                ...
    #= 45461  439050  ...        Rising and falling between a man and woman.
    #= 45462  111109  ...  An artist struggles to finish his work while a...
    #= 45463   67758  ...  When one of her hits goes wrong, a professiona...
    #= 45464  227506  ...  In a small town live two brothers, one a minis...
    #= 45465  461257  ...  50 years after decriminalisation of homosexual...
    #= 
    #= [45466 rows x 4 columns]
    #---------------

    if(links is None):
        links = hgstat_links_kaggle()
    #---------------
    #=print(links)
    #---------------
    #= 출력결과 :  <links_small.csv>
    #=       movieId   imdbId    tmdbId
    #= 0           1   114709     862.0
    #= 1           2   113497    8844.0
    #= 2           3   113228   15602.0
    #= 3           4   114885   31357.0
    #= 4           5   113041   11862.0
    #= ...       ...      ...       ...
    #= 9120   162672  3859980  402672.0
    #= 9121   163056  4262980  315011.0
    #= 9122   163949  2531318  391698.0
    #= 9123   164977    27660  137608.0
    #= 9124   164979  3447228  410803.0
    #= 
    #= [9125 rows x 3 columns]
    #---------------


    #============================
    #============================
    vote_averages = movies_metadata['vote_average'].tolist()
    if(debugPrint == True):
        print(f'vote_averages: {len(vote_averages)}')
        #=print(*vote_averages, sep='\n')

    '''
    # 일부 출력해 본다.
    movie_num = len(vote_averages)
    prt_num = 0
    prt_begin = 0
    prt_begin = 31
    prt_num = 10
    prt_num = 3
    for i in range(prt_begin, movie_num):
        vote_average = vote_averages[i]
        print(f"{i}: {vote_average}")
        #
        if(prt_num > 0):
            if(i >= (prt_begin + prt_num -1)):
                break
    '''

    #
    import numpy
    vote_average_dict = {}

    # <vote_averages> 내용이 있는 것 중에서 사전 목록 생성
    for bi, vote_average in enumerate(vote_averages):
        #
        metadataId = movies_metadata.iloc[bi]['id']
        #=print(f'metadataId [{bi}]:', metadataId)
        movieId = hgstat_get_movieId_by_metadataId(metadataId, links)
        if(movieId == None): # 이런 경우도 있다.
            continue
        movieId = int(movieId)
        
        #
        if(isinstance(vote_average, float)):
            #=print(f"vote_average: {vote_average}")
            if(numpy.isnan(vote_average)): # nan 검사
                pass
            else:
                vote_average_dict[movieId] = vote_average
        else: # {vote_average} 없는 경우
            #=print(f'{i}: (isinstance({vote_average}, float)) ')
            pass
    #==========
    return vote_average_dict, movies_metadata

def hgstat_vote_count_dict__kagmov(movies_metadata=None, links=None, debugPrint=False):
    #====================================
    #====================================
    #---------------
    # format: movies_metadata
    #---------------
    # adult,belongs_to_collection,budget,genres,homepage,id,imdb_id,original_language,original_title,overview,popularity,poster_path,production_companies,production_countries,release_date,revenue,runtime,spoken_languages,status,tagline,title,video,vote_average,vote_count
    # False,"{'id': 10194, 'name': 'Toy Story Collection', 'poster_path': '/7G9915LfUQ2lVfwMEEhDsn3kT4B.jpg', 'backdrop_path': '/9FBwqcd9IRruEDUrTdcaafOMKUq.jpg'}",30000000,"[{'id': 16, 'name': 'Animation'}, {'id': 35, 'name': 'Comedy'}, {'id': 10751, 'name': 'Family'}]",http://toystory.disney.com/toy-story,862,tt0114709,en,Toy Story,"Led by Woody, Andy's toys live happily in his room until Andy's birthday brings Buzz Lightyear onto the scene. Afraid of losing his place in Andy's heart, Woody plots against Buzz. But when circumstances separate Buzz and Woody from their owner, the duo eventually learns to put aside their differences.",21.946943,/rhIRbceoE9lR4veEXuwCC2wARtG.jpg,"[{'name': 'Pixar Animation Studios', 'id': 3}]","[{'iso_3166_1': 'US', 'name': 'United States of America'}]",1995-10-30,373554033,81.0,"[{'iso_639_1': 'en', 'name': 'English'}]",Released,,Toy Story,False,7.7,5415
    # False,,65000000,"[{'id': 12, 'name': 'Adventure'}, {'id': 14, 'name': 'Fantasy'}, {'id': 10751, 'name': 'Family'}]",,8844,tt0113497,en,Jumanji,"When siblings Judy and Peter discover an enchanted board game that opens the door to a magical world, they unwittingly invite Alan -- an adult who's been trapped inside the game for 26 years -- into their living room. Alan's only hope for freedom is to finish the game, which proves risky as all three find themselves running from giant rhinoceroses, evil monkeys and other terrifying creatures.",17.015539,/vzmL6fP7aPKNKPRTFnZmiUfciyV.jpg,"[{'name': 'TriStar Pictures', 'id': 559}, {'name': 'Teitler Film', 'id': 2550}, {'name': 'Interscope Communications', 'id': 10201}]","[{'iso_3166_1': 'US', 'name': 'United States of America'}]",1995-12-15,262797249,104.0,"[{'iso_639_1': 'en', 'name': 'English'}, {'iso_639_1': 'fr', 'name': 'Français'}]",Released,Roll the dice and unleash the excitement!,Jumanji,False,6.9,2413
    #---------------
    if(movies_metadata is None):
        movies_metadata = hgstat_metadata_kaggle(AllFlag=False)
        #=movies_metadata.sort_values(by=['id'])

    #---------------
    #=print(movies_metadata)
    #---------------
    #= 출력결과 :  <movies_metadata.csv>
    #=            id    imdb_id               original_title
    #= 0         862  tt0114709                    Toy Story
    #= 1        8844  tt0113497                      Jumanji
    #= 2       15602  tt0113228             Grumpier Old Men
    #= 3       31357  tt0114885            Waiting to Exhale
    #= 4       11862  tt0113041  Father of the Bride Part II
    #= ...       ...        ...                          ...
    #= 45461  439050  tt6209470                      رگ خواب
    #= 45462  111109  tt2028550          Siglo ng Pagluluwal
    #= 45463   67758  tt0303758                     Betrayal
    #= 45464  227506  tt0008536          Satana likuyushchiy
    #= 45465  461257  tt6980792                     Queerama
    #= 
    #= [45466 rows x 3 columns]
    #---------------
    #=            id  ...                                           overview
    #= 0         862  ...  Led by Woody, Andy's toys live happily in his ...
    #= 1        8844  ...  When siblings Judy and Peter discover an encha...
    #= 2       15602  ...  A family wedding reignites the ancient feud be...
    #= 3       31357  ...  Cheated on, mistreated and stepped on, the wom...
    #= 4       11862  ...  Just when George Banks has recovered from his ...
    #= ...       ...  ...                                                ...
    #= 45461  439050  ...        Rising and falling between a man and woman.
    #= 45462  111109  ...  An artist struggles to finish his work while a...
    #= 45463   67758  ...  When one of her hits goes wrong, a professiona...
    #= 45464  227506  ...  In a small town live two brothers, one a minis...
    #= 45465  461257  ...  50 years after decriminalisation of homosexual...
    #= 
    #= [45466 rows x 4 columns]
    #---------------

    if(links is None):
        links = hgstat_links_kaggle()
    #---------------
    #=print(links)
    #---------------
    #= 출력결과 :  <links_small.csv>
    #=       movieId   imdbId    tmdbId
    #= 0           1   114709     862.0
    #= 1           2   113497    8844.0
    #= 2           3   113228   15602.0
    #= 3           4   114885   31357.0
    #= 4           5   113041   11862.0
    #= ...       ...      ...       ...
    #= 9120   162672  3859980  402672.0
    #= 9121   163056  4262980  315011.0
    #= 9122   163949  2531318  391698.0
    #= 9123   164977    27660  137608.0
    #= 9124   164979  3447228  410803.0
    #= 
    #= [9125 rows x 3 columns]
    #---------------


    #============================
    #============================
    vote_counts = movies_metadata['vote_count'].tolist()
    if(debugPrint == True):
        print(f'vote_counts: {len(vote_counts)}')
        #=print(*vote_counts, sep='\n')

    '''
    # 일부 출력해 본다.
    movie_num = len(vote_counts)
    prt_num = 0
    prt_begin = 0
    prt_begin = 31
    prt_num = 10
    prt_num = 3
    for i in range(prt_begin, movie_num):
        vote_count = vote_counts[i]
        print(f"{i}: {vote_count}")
        #
        if(prt_num > 0):
            if(i >= (prt_begin + prt_num -1)):
                break
    '''

    #
    vote_count_dict = {}

    # <vote_counts> 내용이 있는 것 중에서 사전 목록 생성
    for bi, vote_count in enumerate(vote_counts):
        #
        metadataId = movies_metadata.iloc[bi]['id']
        #=print(f'metadataId [{bi}]:', metadataId)
        movieId = hgstat_get_movieId_by_metadataId(metadataId, links)
        if(movieId == None): # 이런 경우도 있다.
            continue
        movieId = int(movieId)
        
        #
        if(vote_count != vote_count): # 'NaN' check
            #=print(f'{bi+1} [{movieId}]: {vote_count}')
            vote_count = 0
        else:
            if(isinstance(vote_count, float)):
                pass
            else: # {vote_count} 없는 경우
                #=print(f'{i}: (isinstance({vote_count}, float)) ')
                vote_count = 0
        #=print(f'{bi+1} [{movieId}] vote_count : {vote_count}')
        vote_count_dict[movieId] = int(vote_count)
    #==========
    return vote_count_dict, movies_metadata

def hgstat_overview_dict__kagmov(movies_metadata=None, links=None, debugPrint=False):
    #====================================
    #====================================
    #---------------
    # format: movies_metadata
    #---------------
    # adult,belongs_to_collection,budget,genres,homepage,id,imdb_id,original_language,original_title,overview,popularity,poster_path,production_companies,production_countries,release_date,revenue,runtime,spoken_languages,status,tagline,title,video,vote_average,vote_count
    # False,"{'id': 10194, 'name': 'Toy Story Collection', 'poster_path': '/7G9915LfUQ2lVfwMEEhDsn3kT4B.jpg', 'backdrop_path': '/9FBwqcd9IRruEDUrTdcaafOMKUq.jpg'}",30000000,"[{'id': 16, 'name': 'Animation'}, {'id': 35, 'name': 'Comedy'}, {'id': 10751, 'name': 'Family'}]",http://toystory.disney.com/toy-story,862,tt0114709,en,Toy Story,"Led by Woody, Andy's toys live happily in his room until Andy's birthday brings Buzz Lightyear onto the scene. Afraid of losing his place in Andy's heart, Woody plots against Buzz. But when circumstances separate Buzz and Woody from their owner, the duo eventually learns to put aside their differences.",21.946943,/rhIRbceoE9lR4veEXuwCC2wARtG.jpg,"[{'name': 'Pixar Animation Studios', 'id': 3}]","[{'iso_3166_1': 'US', 'name': 'United States of America'}]",1995-10-30,373554033,81.0,"[{'iso_639_1': 'en', 'name': 'English'}]",Released,,Toy Story,False,7.7,5415
    # False,,65000000,"[{'id': 12, 'name': 'Adventure'}, {'id': 14, 'name': 'Fantasy'}, {'id': 10751, 'name': 'Family'}]",,8844,tt0113497,en,Jumanji,"When siblings Judy and Peter discover an enchanted board game that opens the door to a magical world, they unwittingly invite Alan -- an adult who's been trapped inside the game for 26 years -- into their living room. Alan's only hope for freedom is to finish the game, which proves risky as all three find themselves running from giant rhinoceroses, evil monkeys and other terrifying creatures.",17.015539,/vzmL6fP7aPKNKPRTFnZmiUfciyV.jpg,"[{'name': 'TriStar Pictures', 'id': 559}, {'name': 'Teitler Film', 'id': 2550}, {'name': 'Interscope Communications', 'id': 10201}]","[{'iso_3166_1': 'US', 'name': 'United States of America'}]",1995-12-15,262797249,104.0,"[{'iso_639_1': 'en', 'name': 'English'}, {'iso_639_1': 'fr', 'name': 'Français'}]",Released,Roll the dice and unleash the excitement!,Jumanji,False,6.9,2413
    #---------------
    movies_metadata_work = movies_metadata
    if(movies_metadata is None):
        #=print('@@@ (movies_metadata is None)')
        # 줄거리를 읽으려면 {OverviewFlag=True}로 지정해야 한다.
        movies_metadata = hgstat_metadata_kaggle(AllFlag=False, OverviewFlag=True)
        #=movies_metadata.sort_values(by=['id'])
        movies_metadata_work = movies_metadata
    else: 
        # 외부에서 {movies_metadata} 변수가 있더라도 줄거리(overview) 항목이 있는지 확인
        if ('overview' in movies_metadata.columns):
            #=print("@@@ ('overview' in movies_metadata.columns)'")
            pass
        else:
            #=print("@@@ ('overview' not in movies_metadata.columns)")
            # 줄거리를 읽으려면 {OverviewFlag=True}로 지정해야 한다.
            movies_metadata_work = hgstat_metadata_kaggle(AllFlag=False, OverviewFlag=True)
    #=print('@@@ ', movies_metadata_work.columns)

    #---------------
    #=print(movies_metadata_work)
    #---------------
    #= 출력결과 :  <movies_metadata.csv>
    #=            id    imdb_id               original_title
    #= 0         862  tt0114709                    Toy Story
    #= 1        8844  tt0113497                      Jumanji
    #= 2       15602  tt0113228             Grumpier Old Men
    #= 3       31357  tt0114885            Waiting to Exhale
    #= 4       11862  tt0113041  Father of the Bride Part II
    #= ...       ...        ...                          ...
    #= 45461  439050  tt6209470                      رگ خواب
    #= 45462  111109  tt2028550          Siglo ng Pagluluwal
    #= 45463   67758  tt0303758                     Betrayal
    #= 45464  227506  tt0008536          Satana likuyushchiy
    #= 45465  461257  tt6980792                     Queerama
    #= 
    #= [45466 rows x 3 columns]
    #---------------
    #=            id  ...                                           overview
    #= 0         862  ...  Led by Woody, Andy's toys live happily in his ...
    #= 1        8844  ...  When siblings Judy and Peter discover an encha...
    #= 2       15602  ...  A family wedding reignites the ancient feud be...
    #= 3       31357  ...  Cheated on, mistreated and stepped on, the wom...
    #= 4       11862  ...  Just when George Banks has recovered from his ...
    #= ...       ...  ...                                                ...
    #= 45461  439050  ...        Rising and falling between a man and woman.
    #= 45462  111109  ...  An artist struggles to finish his work while a...
    #= 45463   67758  ...  When one of her hits goes wrong, a professiona...
    #= 45464  227506  ...  In a small town live two brothers, one a minis...
    #= 45465  461257  ...  50 years after decriminalisation of homosexual...
    #= 
    #= [45466 rows x 4 columns]
    #---------------

    if(links is None):
        links = hgstat_links_kaggle()
    #---------------
    #=print(links)
    #---------------
    #= 출력결과 :  <links_small.csv>
    #=       movieId   imdbId    tmdbId
    #= 0           1   114709     862.0
    #= 1           2   113497    8844.0
    #= 2           3   113228   15602.0
    #= 3           4   114885   31357.0
    #= 4           5   113041   11862.0
    #= ...       ...      ...       ...
    #= 9120   162672  3859980  402672.0
    #= 9121   163056  4262980  315011.0
    #= 9122   163949  2531318  391698.0
    #= 9123   164977    27660  137608.0
    #= 9124   164979  3447228  410803.0
    #= 
    #= [9125 rows x 3 columns]
    #---------------


    #============================
    #============================
    overview_list = movies_metadata_work['overview'].tolist()
    if(debugPrint == True):
        print(f'overview_list: {len(overview_list)}')
        #=print(*overview_list, sep='\n')

    '''
    # 일부 출력해 본다.
    movie_num = len(overview_list)
    prt_num = 0
    prt_begin = 0
    prt_begin = 31
    prt_num = 10
    prt_num = 3
    for i in range(prt_begin, movie_num):
        overview = overview_list[i]
        print(f"{i}: {overview_list}")
        #
        if(prt_num > 0):
            if(i >= (prt_begin + prt_num -1)):
                break
    '''

    #
    overview_dict = {}

    # <overview_list> 내용이 있는 것 중에서 사전 목록 생성
    for bi, overview in enumerate(overview_list):
        #
        metadataId = movies_metadata_work.iloc[bi]['id']
        #=print(f'metadataId [{bi}]:', metadataId)
        movieId = hgstat_get_movieId_by_metadataId(metadataId, links)
        if(movieId == None): # 이런 경우도 있다.
            continue
        movieId = int(movieId)
        
        #
        if(isinstance(overview, float)): # 'NaN' 내용이 없는 경우
            pass
        else:
            if(isinstance(overview, float)): # {title} 값이 없는 경우
                #=print(f'{i}: (isinstance({overview}, float)) ')
                pass
            else:
                #=print(f"{title}: {overview}")
                overview_dict[movieId] = overview
    #==========
    return overview_dict, movies_metadata_work

def hgstat_dicts__kagmov(debugPrint=False):
    #====================================
    #====================================
    #---------------
    # format: movies_metadata
    #---------------
    # adult,belongs_to_collection,budget,genres,homepage,id,imdb_id,original_language,original_title,overview,popularity,poster_path,production_companies,production_countries,release_date,revenue,runtime,spoken_languages,status,tagline,title,video,vote_average,vote_count
    # False,"{'id': 10194, 'name': 'Toy Story Collection', 'poster_path': '/7G9915LfUQ2lVfwMEEhDsn3kT4B.jpg', 'backdrop_path': '/9FBwqcd9IRruEDUrTdcaafOMKUq.jpg'}",30000000,"[{'id': 16, 'name': 'Animation'}, {'id': 35, 'name': 'Comedy'}, {'id': 10751, 'name': 'Family'}]",http://toystory.disney.com/toy-story,862,tt0114709,en,Toy Story,"Led by Woody, Andy's toys live happily in his room until Andy's birthday brings Buzz Lightyear onto the scene. Afraid of losing his place in Andy's heart, Woody plots against Buzz. But when circumstances separate Buzz and Woody from their owner, the duo eventually learns to put aside their differences.",21.946943,/rhIRbceoE9lR4veEXuwCC2wARtG.jpg,"[{'name': 'Pixar Animation Studios', 'id': 3}]","[{'iso_3166_1': 'US', 'name': 'United States of America'}]",1995-10-30,373554033,81.0,"[{'iso_639_1': 'en', 'name': 'English'}]",Released,,Toy Story,False,7.7,5415
    # False,,65000000,"[{'id': 12, 'name': 'Adventure'}, {'id': 14, 'name': 'Fantasy'}, {'id': 10751, 'name': 'Family'}]",,8844,tt0113497,en,Jumanji,"When siblings Judy and Peter discover an enchanted board game that opens the door to a magical world, they unwittingly invite Alan -- an adult who's been trapped inside the game for 26 years -- into their living room. Alan's only hope for freedom is to finish the game, which proves risky as all three find themselves running from giant rhinoceroses, evil monkeys and other terrifying creatures.",17.015539,/vzmL6fP7aPKNKPRTFnZmiUfciyV.jpg,"[{'name': 'TriStar Pictures', 'id': 559}, {'name': 'Teitler Film', 'id': 2550}, {'name': 'Interscope Communications', 'id': 10201}]","[{'iso_3166_1': 'US', 'name': 'United States of America'}]",1995-12-15,262797249,104.0,"[{'iso_639_1': 'en', 'name': 'English'}, {'iso_639_1': 'fr', 'name': 'Français'}]",Released,Roll the dice and unleash the excitement!,Jumanji,False,6.9,2413
    #---------------
    movies_metadata = hgstat_metadata_kaggle(AllFlag=False)
    #=movies_metadata.sort_values(by=['id'])

    #---------------
    #=print(movies_metadata)
    #---------------
    #= 출력결과 :  <movies_metadata.csv>
    #=            id    imdb_id               original_title
    #= 0         862  tt0114709                    Toy Story
    #= 1        8844  tt0113497                      Jumanji
    #= 2       15602  tt0113228             Grumpier Old Men
    #= 3       31357  tt0114885            Waiting to Exhale
    #= 4       11862  tt0113041  Father of the Bride Part II
    #= ...       ...        ...                          ...
    #= 45461  439050  tt6209470                      رگ خواب
    #= 45462  111109  tt2028550          Siglo ng Pagluluwal
    #= 45463   67758  tt0303758                     Betrayal
    #= 45464  227506  tt0008536          Satana likuyushchiy
    #= 45465  461257  tt6980792                     Queerama
    #= 
    #= [45466 rows x 3 columns]
    #---------------
    #=            id  ...                                           overview
    #= 0         862  ...  Led by Woody, Andy's toys live happily in his ...
    #= 1        8844  ...  When siblings Judy and Peter discover an encha...
    #= 2       15602  ...  A family wedding reignites the ancient feud be...
    #= 3       31357  ...  Cheated on, mistreated and stepped on, the wom...
    #= 4       11862  ...  Just when George Banks has recovered from his ...
    #= ...       ...  ...                                                ...
    #= 45461  439050  ...        Rising and falling between a man and woman.
    #= 45462  111109  ...  An artist struggles to finish his work while a...
    #= 45463   67758  ...  When one of her hits goes wrong, a professiona...
    #= 45464  227506  ...  In a small town live two brothers, one a minis...
    #= 45465  461257  ...  50 years after decriminalisation of homosexual...
    #= 
    #= [45466 rows x 4 columns]
    #---------------

    links = hgstat_links_kaggle()
    #---------------
    #=print(links)
    #---------------
    #= 출력결과 :  <links_small.csv>
    #=       movieId   imdbId    tmdbId
    #= 0           1   114709     862.0
    #= 1           2   113497    8844.0
    #= 2           3   113228   15602.0
    #= 3           4   114885   31357.0
    #= 4           5   113041   11862.0
    #= ...       ...      ...       ...
    #= 9120   162672  3859980  402672.0
    #= 9121   163056  4262980  315011.0
    #= 9122   163949  2531318  391698.0
    #= 9123   164977    27660  137608.0
    #= 9124   164979  3447228  410803.0
    #= 
    #= [9125 rows x 3 columns]
    #---------------
    title_dict, movies_metadata_ = hgstat_title_dict__kagmov(movies_metadata, links, debugPrint=debugPrint)
    release_dict, movies_metadata_ = hgstat_release_dict__kagmov(movies_metadata, links, debugPrint=debugPrint)
    belong_to_collection_dict, collection_dict = hgstat_collection_dict__kagmov(movies_metadata, links, debugPrint=debugPrint)
    genres_dict, movies_metadata_ = hgstat_genres_dict__kagmov(movies_metadata, links, debugPrint=debugPrint)
    #
    return title_dict, release_dict, belong_to_collection_dict, \
            collection_dict, genres_dict, movies_metadata

def hgstat_ratings_dict__kagmov(UserBase=True, FullData=False, ReadRows=0):
    #---------------
    # format: ratings
    #---------------
    # userId,movieId,rating,timestamp
    # 1,110,1.0,1425941529
    # 1,147,4.5,1425942435
    # 1,858,5.0,1425941523
    #---------------
    ratings = hgstat_dataframe_kaggle_movies_ratings(FullData, ReadRows)
    ratings_dict, userIdList, movieIdList = \
        hgstat_ratings_dict__ratings(ratings, UserBase=UserBase)

    #
    return ratings_dict, userIdList, movieIdList

#===================================
#===================================
def hgstat_print_movie_title__ratings_dict_by_userId(userId, ratings_dict, links, movies_metadata):
    print('============================')
    print('@@@ 영화 이름 출력 @@@')
    print('============================')
    print(f'userId: {userId}')
    ratings_tuple_list = ratings_dict[userId]
    base_movieId_list = [ratings_tuple[0] for ratings_tuple in ratings_tuple_list]

    # 사용자가 평점을 매긴 영화 제목 출력하기
    hgstat_print_title__kagmov_by_movieIds(base_movieId_list, links, movies_metadata)

def hgstat_print_title__kagmov_by_movieIds(movieId_list, links, movies_metadata, title=None):
    # print_title__kagmov_ratings_dict_by_movieIds() 함수와 기능이 거의 같다. 나중에 통합하자.
    if(title != None):
        print('============================')
        print(f'@@@ {title} @@@')
        print('============================')
    #
    print(f'userId_list: {len(movieId_list)}')

    # 영화 제목 출력하기
    for li, movieId in enumerate(movieId_list):
        movie_title = hgstat_get_title_kaggle_by_movieId(movieId, links, movies_metadata)
        if(len(movie_title) <= 0): # 제목이 없는 경우
            print(f'{li+1}\t{movieId}\t<<<영화 이름 없음>>>')
            continue
        print(f'{li+1}\t{movieId}\t{movie_title}')

def get_rvalue__ratings_dict_by_title(title, userIdList, movie_ratings_dict, 
    movies_metadata, links,
    debugPrint=False, ProcMod=0): 
    if(debugPrint == True):
        hgsysinc._print_function_name_(3)

    #---------------------
    #---------------------
    movieId = hgstat_get_movieId_metadata_by_title(movies_metadata, links, title)
    movieId = int(movieId) # 'str' 타입으로 바뀐 경우가 있다.

    if(debugPrint == True):
        print(f'{title} [{movieId}]: 상관계수 계산')
    rvalue_list = get_rvalue__ratings_dict_by_Id(movieId, userIdList, movie_ratings_dict, 
        debugPrint=debugPrint, ProcMod=ProcMod)
    if(len(rvalue_list) <= 0):
        return
    if(debugPrint == True):
        print(rvalue_list)
        print()

    #=rvalue_list : 상관계수가 큰 값부터 정렬된 상태
    return rvalue_list # rvalue_list format: [(keyId, r-value),...]

def check_rvalue__ratings_dict_by_title(title, movieIdList, userIdList, 
    movie_ratings_dict, movies_metadata, links,
    debugPrint=False, ProcMod=0): 
    #---------------------
    if(debugPrint == True):
        print(f'{title} : 상관계수 계산')

    #---------------------
    movieId = hgstat_get_movieId_metadata_by_title(movies_metadata, links, title)
    movieId = int(movieId) # 'str' 타입으로 바뀐 경우가 있다.

    check_rvalue__ratings_dict_by_Id(movieId, userIdList, movie_ratings_dict, 
    #=keyIdList=userIdList,
    keyIdList=movieIdList,
    debugPrint=debugPrint, ProcMod=ProcMod)

def print_title__kagmov_ratings_dict_by_movieIds(movieIds, links, movies_metadata):
    print('순서\t영화ID\t영화 이름')
    for li, movieId in enumerate(movieIds):
        movie_title = hgstat_get_title_kaggle_by_movieId(movieId, links, movies_metadata)
        if(len(movie_title) <= 0): # 제목이 없는 경우
            print(f'{li+1}\t{movieId}\t<<<영화 이름 없음>>>')
        else:
            print(f'{li+1}\t{movieId}\t{movie_title}')
    print(), print(), 

def check_reco_item__kagmov_ratings_dict_by_userId2(userId_b, userId_r, 
    ratings_dict, links, movies_metadata, debugPrint=False): 
    #
    if(debugPrint == True):
        hgsysinc._print_function_name_(3)

    #---------------------
    #---------------------
    # ratings_dict format: {'userId': [(movieId, rating_value), (),...]}
    #---------------------
    movie_list_b = hgstat_movie_list__ratings_dict(ratings_dict, userId_b)
    movie_list_r = hgstat_movie_list__ratings_dict(ratings_dict, userId_r)
    reco_movieId_list = find_reco__id_list(movie_list_b, movie_list_r, debugPrint=debugPrint)

    # 복사해서 사용(정렬할 때 원래 데이터 순서가 바뀌므로)
    movie_rating_r = ratings_dict[userId_r].copy() # 복사해서 사용(정렬할 때 원래 데이터 순서가 바뀌므로)
    movie_rating_r.sort(key=lambda r: -r[1]) # 튜플 2번째 값(rating_value) 큰 순서로 정렬

    #
    print(f'기준 고객ID: {userId_b}\t추천 고객ID: {userId_r}')
    print(f'추천 영화 수: {len(reco_movieId_list)}', end='\t')
    print('추천 영화(id) 목록:', reco_movieId_list)

    rinx = 0
    for rating_tuple in movie_rating_r:
        reco_movieId = rating_tuple[0]
        reco_rating = rating_tuple[1]
        if(reco_movieId not in reco_movieId_list):
            continue

        movie_title = hgstat_get_title_kaggle_by_movieId(reco_movieId, links, movies_metadata)
        if(len(movie_title) <= 0): # 제목이 없는 경우
            continue
    
        print(f'{rinx+1} ', end='')
        if(debugPrint == True):
            print(f'[{reco_movieId}] ', end='')
        print(f'({reco_rating}):', movie_title)
        rinx += 1
    if(len(reco_movieId_list) > 0): # 불필요한 줄바뀜 출력 방지
        print() 

#===================================
#===================================
def hgstat_get_metadataId_by_movieId(movieId, links):
    # movieId: ratins_list의 movieId
    #
    #=print('@2')
    links_movieId_inx = links.index[links['movieId'] == movieId]
    #=print(links_movieId_inx)
    #=print(links.iloc[links_movieId_inx])
    
    #
    #=print('@3')
    metadata_id = links.iloc[links_movieId_inx]['tmdbId']
    #=print(metadata_id)
    
    try: # 중간에 비정상적인 데이터가 있을 수 있다.
        metadata_id = int(metadata_id) # float -> int : 862.0 -> 862
    except TypeError: # raise TypeError("cannot convert the series to " "{0}".format(str(converter)))
        #=print("TypeError: cannot convert the series to {", metadata_id , "}.format(str(converter)))")
        #=print(links.iloc[links_movieId_inx])
        return None
    except ValueError: # raise ValueError("cannot convert float NaN to integer)
        #=print("ValueError: cannot convert float NaN to integer ")
        #=print(links.iloc[links_movieId_inx])
        return None
    #
    #=print(metadata_id)
    metadata_id = str(metadata_id) # int -> string
    #=print(metadata_id)
    return metadata_id

def hgstat_get_movieId_by_metadataId(metadataId, links):
    # movieId: ratins_list의 movieId
    #-----
    if('-' in metadataId): #= metadataId [19730]: 1997-08-20 <=== 이런 경우 있음.
        return None # format error
    metadataId = int(metadataId) # string -> int (아래에서 비교하려면)

    #
    #=print('@2')
    # links['tmdbId']가 {metadata}에서 {id}에 해당
    links_movieId_inx = links.index[links['tmdbId'] == metadataId]
    #=print(links_movieId_inx)
    #=print(links.iloc[links_movieId_inx])
    
    #
    #=print('@3')
    movieId = links.iloc[links_movieId_inx]['movieId']
    #=print(movieId)
    
    try: # 중간에 비정상적인 데이터가 있을 수 있다.
        movieId = int(movieId) # float -> int : 862.0 -> 862
    except TypeError: # raise TypeError("cannot convert the series to " "{0}".format(str(converter)))
        #=print("TypeError: cannot convert the series to {", movieId , "}.format(str(converter)))")
        #=print(links.iloc[links_movieId_inx])
        return None
    except ValueError: # raise ValueError("cannot convert float NaN to integer)
        #=print("ValueError: cannot convert float NaN to integer ")
        #=print(links.iloc[links_movieId_inx])
        return None
    
    #=print(movieId)
    movieId = str(movieId) # int -> string
    #=print(movieId)
    return movieId

def hgstat_get_title_movies_metadata_by_inx(movies_metadata, metadata_index):
    movies_title = movies_metadata.iloc[metadata_index]['original_title']
    return movies_title

def hgstat_get_story_movies_metadata(movies_metadata, metadata_index):
    movies_story = movies_metadata.iloc[metadata_index]['overview']
    return movies_story

def hgstat_get_movies_info_metadata_by_movieId(movies_metadata, links, movieId):
    # movieId: ratins_list의 movieId
    metadata_id = hgstat_get_metadataId_by_movieId(movieId, links)
    movie_info = movies_metadata.loc[movies_metadata['id'] == metadata_id]
    return movie_info

def hgstat_get_vote_movies_metadata_by_movieId(movies_metadata, links, movieId):
    # movieId: ratins_list의 movieId
    metadata_id = hgstat_get_metadataId_by_movieId(movieId, links)
    movie_info = movies_metadata.loc[movies_metadata['id'] == metadata_id]
    #=print(f'{movieId}: {movie_info}')
    if(movie_info.empty):
        vote_average = 0 # 정보가 없으므로 평점을 '0'으로 준다.
        return vote_average
    
    #=print(f'{movieId}: {movie_info.iloc[0]}')
    vote_average = movie_info.iloc[0]['vote_average']
    #=print(f"vote_average: {vote_average}")
    return vote_average

def hgstat_get_vote_dict_movies_metadata_by_movieIds(movies_metadata, links, movieIds):
    # movieId: ratins_list의 movieId
    vote_dict = {}
    for movieId in movieIds:
        vote = hgstat_get_vote_movies_metadata_by_movieId(movies_metadata, links, movieId)
        vote_dict[movieId] = vote
    return vote_dict

def hgstat_get_movies_info_metadata_by_title(movies_metadata, title):
    movie_info = movies_metadata.loc[movies_metadata['original_title'] == title]
    return movie_info

def hgstat_get_vote_movies_metadata_by_title(movies_metadata, title):
    movie_info = movies_metadata.loc[movies_metadata['original_title'] == title]
    #=print(f'{title}: {movie_info}')
    #=print(f'{title}: {movie_info.iloc[0]}')
    vote_average = movie_info.iloc[0]['vote_average']
    #=print(f"vote_average: {vote_average}")
    return vote_average

def hgstat_get_metadataId_by_title(movies_metadata, title):
    movie_info = movies_metadata.loc[movies_metadata['original_title'] == title]
    #=print(f'{title}: {movie_info}')
    #=print(f'{title}: {movie_info.iloc[0]}')
    metadata_id = movie_info.iloc[0]['id']
    #=print(f"metadata_id: {metadata_id}")
    metadata_id = int(metadata_id)
    return metadata_id

def hgstat_get_movieId_metadata_by_title(movies_metadata, links, title):
    movie_info = movies_metadata.loc[movies_metadata['original_title'] == title]
    #=print(f'{title}: {movie_info}')
    #=print(f'{title}: {movie_info.iloc[0]}')
    metadata_id = movie_info.iloc[0]['id']
    #=print(f"metadata_id: {metadata_id}")

    movieId = hgstat_get_movieId_by_metadataId(metadata_id, links)
    #=print(f"movieId: {movieId}")
    movieId = int(movieId)
    return movieId

def hgstat_get_vote_dict_movies_metadata_by_titles(movies_metadata, titles):
    vote_dict = {}
    for title in titles:
        vote = hgstat_get_vote_movies_metadata_by_title(movies_metadata, title)
        vote_dict[title] = vote
    return vote_dict

def hgstat_get_story_movies_metadata_by_title(movies_metadata, title):
    movie_info = movies_metadata.loc[movies_metadata['original_title'] == title]
    #=print(f'{title}: {movie_info}')
    #=print(f'{title}: {movie_info.iloc[0]}')
    overview = movie_info.iloc[0]['overview']
    #=print(f"overview: {overview}")

    return overview

#===================================
#===================================
def hgstat_get_collection_dict_list(belongs_to_collection, title_list=None, debugPrint=False):
    # <belongs_to_collection> 내용이 있는 것 중에서 컬력센 사전 목록 생성
    collectionDictList = {}
    for i, item in enumerate(belongs_to_collection):
        if(isinstance(item, float)): # 'NaN' 내용이 없는 경우
            pass
        else:
            #
            collection = belongs_to_collection[i]
            if(isinstance(collection, float)): # {collection}는 있는 값이 없는 경우
                #=print(f'{i}: (isinstance({collection}, float)) ', title_list[i])
                pass
            else:
                CollectionDict = eval(collection) # format: {'id': 10194, 'name': 'Toy Story Collection', 'poster_path': '/7G9915LfUQ2lVfwMEEhDsn3kT4B.jpg', 'backdrop_path': '/9FBwqcd9IRruEDUrTdcaafOMKUq.jpg'}
                CollectionName = CollectionDict['name']
                #=print(f"{i}: {CollectionName} @@ {title_list[i]}")

                title = ''
                if(title_list == None):  # {제목}이 없는 경우 - 배열 인덱스값만 전달
                    pass
                else:
                    title = title_list[i]
                #
                collectionItem = {i:title}
                if CollectionName in collectionDictList:
                    collectionDictItem = collectionDictList[CollectionName]
                    collectionDictItem.append(collectionItem)
                    #=print('collectionDictItem:', collectionDictItem)
                else:
                    collectionDictItem = []
                    collectionDictItem.append(collectionItem)
                    collectionDictList[CollectionName] = collectionDictItem

    #
    #=print(*collectionDictList, sep='\n')
    if(debugPrint == True):
        print(), print()
        print('# <collection> 목록 확인')
        for i, CollectionName in enumerate(collectionDictList):
            collectionDictItem = collectionDictList[CollectionName]
            print(f"[{i}] {CollectionName} : ({len(collectionDictItem)}){collectionDictItem}")
            #=print()
            #=if(i >= 10):
            #=    break
    #
    return collectionDictList

#---------------------
#---------------------
def hgstat_is_empty_overview(overview): # overview() 항목이 내용이 없는지 검사
    import numpy
    
    #
    if(isinstance(overview, float)):
        if(numpy.isnan(overview)): # nan 검사 (overview 필드에 'Nan'값이 있다.)
            return True
    else:
        no_overview_list = ['No Overview', 'No overview', 'no overview', 
                            'No Overview yet', 'No overview yet', 'no overview yet.', 
                            'Released', 'released', # 상영이 종료된 영화
                            ]
        if(overview in no_overview_list):
            return True
    return False

def hgstat_get_list_set__kaggle_movies(read_num=0, debugPrint=False):
    #====================================
    #====================================
    #---------------
    # format: movies_metadata
    #---------------
    # adult,belongs_to_collection,budget,genres,homepage,id,imdb_id,original_language,original_title,overview,popularity,poster_path,production_companies,production_countries,release_date,revenue,runtime,spoken_languages,status,tagline,title,video,vote_average,vote_count
    # False,"{'id': 10194, 'name': 'Toy Story Collection', 'poster_path': '/7G9915LfUQ2lVfwMEEhDsn3kT4B.jpg', 'backdrop_path': '/9FBwqcd9IRruEDUrTdcaafOMKUq.jpg'}",30000000,"[{'id': 16, 'name': 'Animation'}, {'id': 35, 'name': 'Comedy'}, {'id': 10751, 'name': 'Family'}]",http://toystory.disney.com/toy-story,862,tt0114709,en,Toy Story,"Led by Woody, Andy's toys live happily in his room until Andy's birthday brings Buzz Lightyear onto the scene. Afraid of losing his place in Andy's heart, Woody plots against Buzz. But when circumstances separate Buzz and Woody from their owner, the duo eventually learns to put aside their differences.",21.946943,/rhIRbceoE9lR4veEXuwCC2wARtG.jpg,"[{'name': 'Pixar Animation Studios', 'id': 3}]","[{'iso_3166_1': 'US', 'name': 'United States of America'}]",1995-10-30,373554033,81.0,"[{'iso_639_1': 'en', 'name': 'English'}]",Released,,Toy Story,False,7.7,5415
    # False,,65000000,"[{'id': 12, 'name': 'Adventure'}, {'id': 14, 'name': 'Fantasy'}, {'id': 10751, 'name': 'Family'}]",,8844,tt0113497,en,Jumanji,"When siblings Judy and Peter discover an enchanted board game that opens the door to a magical world, they unwittingly invite Alan -- an adult who's been trapped inside the game for 26 years -- into their living room. Alan's only hope for freedom is to finish the game, which proves risky as all three find themselves running from giant rhinoceroses, evil monkeys and other terrifying creatures.",17.015539,/vzmL6fP7aPKNKPRTFnZmiUfciyV.jpg,"[{'name': 'TriStar Pictures', 'id': 559}, {'name': 'Teitler Film', 'id': 2550}, {'name': 'Interscope Communications', 'id': 10201}]","[{'iso_3166_1': 'US', 'name': 'United States of America'}]",1995-12-15,262797249,104.0,"[{'iso_639_1': 'en', 'name': 'English'}, {'iso_639_1': 'fr', 'name': 'Français'}]",Released,Roll the dice and unleash the excitement!,Jumanji,False,6.9,2413
    #---------------

    movies_metadata = hgstat_metadata_kaggle(AllFlag=False)
    #=movies_metadata.sort_values(by=['id'])

    #---------------
    #=print(movies_metadata)
    #---------------
    #= 출력결과 :  <movies_metadata.csv>
    #=            id    imdb_id               original_title
    #= 0         862  tt0114709                    Toy Story
    #= 1        8844  tt0113497                      Jumanji
    #= 2       15602  tt0113228             Grumpier Old Men
    #= 3       31357  tt0114885            Waiting to Exhale
    #= 4       11862  tt0113041  Father of the Bride Part II
    #= ...       ...        ...                          ...
    #= 45461  439050  tt6209470                      رگ خواب
    #= 45462  111109  tt2028550          Siglo ng Pagluluwal
    #= 45463   67758  tt0303758                     Betrayal
    #= 45464  227506  tt0008536          Satana likuyushchiy
    #= 45465  461257  tt6980792                     Queerama
    #= 
    #= [45466 rows x 3 columns]
    #---------------
    #=            id  ...                                           overview
    #= 0         862  ...  Led by Woody, Andy's toys live happily in his ...
    #= 1        8844  ...  When siblings Judy and Peter discover an encha...
    #= 2       15602  ...  A family wedding reignites the ancient feud be...
    #= 3       31357  ...  Cheated on, mistreated and stepped on, the wom...
    #= 4       11862  ...  Just when George Banks has recovered from his ...
    #= ...       ...  ...                                                ...
    #= 45461  439050  ...        Rising and falling between a man and woman.
    #= 45462  111109  ...  An artist struggles to finish his work while a...
    #= 45463   67758  ...  When one of her hits goes wrong, a professiona...
    #= 45464  227506  ...  In a small town live two brothers, one a minis...
    #= 45465  461257  ...  50 years after decriminalisation of homosexual...
    #= 
    #= [45466 rows x 4 columns]
    #---------------


    #============================
    #============================
    overview_list = movies_metadata['overview'].tolist()
    title_list = movies_metadata['original_title'].tolist()
    release_date_list = movies_metadata['release_date'].tolist()
    genres_list = movies_metadata['genres'].tolist()
    vote_average_list = movies_metadata['vote_average'].tolist()
    vote_count_list = movies_metadata['vote_count'].tolist()
    belongs_to_collection = movies_metadata['belongs_to_collection'].tolist()
    metadataId_list = movies_metadata['id'].tolist()
    if(debugPrint == True):
        print(f'overview_list: {len(overview_list)} movies')
        #=print(*overview_list, sep='\n')

        print(f'title_list: {len(title_list)}')
        #=print(*title_list, sep='\n')

        print(f'release_date_list: {len(release_date_list)}')
        #=print(*release_date_list, sep='\n')

        print(f'genres_list: {len(genres_list)}')
        #=print(*genres_list, sep='\n')
        
        print(f'vote_average_list: {len(vote_average_list)}')
        #=print(*vote_average_list, sep='\n')

        print(f'vote_count_list: {len(vote_count_list)}')
        #=print(*vote_count_list, sep='\n')

        print(f'belongs_to_collection: {len(belongs_to_collection)}')
        #=print(*belongs_to_collection, sep='\n')

        print(f'metadataId_list: {len(metadataId_list)}')
        #=print(*metadataId_list, sep='\n')
        

    '''
    # 일부 출력해 본다.
    movie_num = len(overview_list)
    prt_num = 0
    prt_begin = 0
    prt_begin = 31
    prt_num = 10
    prt_num = 3
    for i in range(prt_begin, movie_num):
        story = overview_list[i]
        title = title_list[i]

        print(f"{i}: {title}")
        print(f'{story}')
        
        #
        if(prt_num > 0):
            if(i >= (prt_begin + prt_num -1)):
                break
    '''

    #============================
    #============================
    #============================
    # 일부 데이터는 불완전하다.
    # 32: Guillaumet, les ailes du courage
    # ===> 줄거리가 없다(nan)
    #============================
    if(debugPrint == True):
        print(), print(), print(), 
        print('줄거리가 없는 것을 제외')
    #
    import numpy

    movie_num = len(overview_list)
    del_num = 0
    del_list = []
    i = 0
    while(i < movie_num):
        story = overview_list[i]
        #=title = title_list[i]
        
        #
        emptyFlag = hgstat_is_empty_overview(story)
        if(emptyFlag == True):
            del_list.append(i)
            #=print(f'check nan [{i}]')

            # 데이터의 짝을 맞추기 위해서 관련된 인덱스는 모두 처리한다.
            del overview_list[i]
            del title_list[i]
            del release_date_list[i]
            del genres_list[i]
            del vote_average_list[i]
            del vote_count_list[i]
            del belongs_to_collection[i]
            del metadataId_list[i]

            #
            del_num += 1
            movie_num -= 1
            continue

        #
        i += 1

        #=print(f"{i}: {title}")
        #=print(f'{story}')

    if(debugPrint == True):
        #=print('del_num:', del_num)
        print('del_num:', len(del_list))
        #=print(del_list) # 양이 많을 경우를 위해서 막아둔다.
        print(f'overview_list: {len(overview_list)} movies')
        print(f'title_list: {len(title_list)}')
        print(f'release_date_list: {len(release_date_list)}')
        print(f'genres_list: {len(genres_list)}')
        print(f'vote_average_list: {len(vote_average_list)}')
        print(f'vote_count_list: {len(vote_count_list)}')
        print(f'belongs_to_collection: {len(belongs_to_collection)}')
        print(f'metadataId_list: {len(metadataId_list)}')
        
    #============================
    #============================
    #============================
    if(debugPrint == True):
        print(),print(),print()
        print('최종 선택된 데이터 통계')
    
    # 너무 많을 경우에 일부만 사용한다.
    movie_num = len(overview_list) # 모두 사용
    if(read_num > 0):
        movie_num = read_num

    #
    overview_list = overview_list[:movie_num]
    title_list = title_list[:movie_num]
    release_date_list = release_date_list[:movie_num]
    genres_list = genres_list[:movie_num]
    vote_average_list = vote_average_list[:movie_num]
    vote_count_list = vote_count_list[:movie_num]
    belongs_to_collection = belongs_to_collection[:movie_num]
    metadataId_list = metadataId_list[:movie_num]    

    if(debugPrint == True):
        print(f'overview_list: {len(overview_list)} movies')
        print(f'title_list: {len(title_list)} movies')
        print(f'release_date_list: {len(release_date_list)}')
        print(f'genres_list: {len(genres_list)}')
        print(f'vote_average_list: {len(vote_average_list)}')
        print(f'vote_count_list: {len(vote_count_list)}')
        print(f'belongs_to_collection: {len(belongs_to_collection)}')
        print(f'metadataId_list: {len(metadataId_list)}')

    #-----------
    #-----------
    #-----------
    import hgsysinc
    from hgwordlist import GetWordLists__TextList
    from hgeng_spell_rule import stoplist_eng_raw_min1
    #-----------
    # 줄거리(텍스트) 목록 불용어 처리
    #-----------
    stoplist = None
    stoplist = stoplist_eng_raw_min1
    #-----------
    #=overview_wordlists = GetWordLists__TextList(overview_list, ExcFilter=stoplist)
    overview_wordlists = GetWordLists__TextList(overview_list, 
        ExcFilter=stoplist, # 불용어 처리
        LowerCase = True, # 대문자는 소문자로 변환
        CliticsModify=True, # {~'s}, {~'t}, {~'d}는 {~}로 바꾼다.
        ExcChar1=True,  # 1글자보다 작은 것은 지운다.
        ExcNumber=True, # 숫자만 있는 것은 지운다.
        UnifySpellRule=True, # 철자 규칙으로 단일화(s 제거, es 변형, 's)
        )

    #============================
    #============================
    # 불용어 처리로 인하여 빈 목록이 있을 수 없다.
    #============================
    if(debugPrint == True):
        print(), print(), print(), 
        print('불용어 처리로 인하여 단어 목록이 없는 것을 제외')
    #
    movie_num = len(overview_wordlists)
    del_num = 0
    del_list = []
    i = 0
    while(i < movie_num):
        wordlist = overview_wordlists[i]

        #
        if(len(wordlist) <= 0):
            del_list.append(i)

            # 데이터의 짝을 맞추기 위해서 관련된 인덱스는 모두 처리한다.
            del overview_wordlists[i]
            del overview_list[i]
            del title_list[i]
            del release_date_list[i]
            del genres_list[i]
            del vote_average_list[i]
            del vote_count_list[i]
            del belongs_to_collection[i]
            del metadataId_list[i]

            #
            del_num += 1
            movie_num -= 1
            continue
        #
        i += 1

    if(debugPrint == True):
        #=print('del_num:', del_num)
        print('del_num:', len(del_list))
        #=print(del_list) # 양이 많을 경우를 위해서 막아둔다.
        print(f'overview_wordlists: {len(overview_wordlists)} movies')
        print(f'overview_list: {len(overview_list)}')
        print(f'title_list: {len(title_list)}')
        print(f'release_date_list: {len(release_date_list)}')
        print(f'genres_list: {len(genres_list)}')
        print(f'vote_average_list: {len(vote_average_list)}')
        print(f'vote_count_list: {len(vote_count_list)}')
        print(f'belongs_to_collection: {len(belongs_to_collection)}')
        print(f'metadataId_list: {len(metadataId_list)}')        

    #==========
    #==========
    return overview_wordlists, overview_list, title_list, \
            release_date_list, genres_list, vote_average_list, vote_count_list, \
            belongs_to_collection, metadataId_list

#===================================
#===================================
def hgstat_get_distance_pair__kaggke_movies(WordDict_Base, WordDict_Comp, CompInx=None,
    GenreSet_Base=None, GenreSet_Comp=None,  GenresRawMode=False,
    vote_average_comp=None, vote_count_comp=None, VoteCountMax=0,
    CollectionDict_Base=None, CollectionDict_Comp=None,
    ):
    #
    from hgdistance import GetWordDict_CosDistance

    #
    if(GenreSet_Base == None): # 밖에서 미리 만들어서 들어온 값이 없으면 여기서 만든다.
        GenreSet_Base = ()
    #
    if(CollectionDict_Base == None):
        CollectionDict_Base = {}

    #
    TotalDistance = 0
    CosDistance = GetWordDict_CosDistance(WordDict_Base, WordDict_Comp)
    #=print('[CosDistance]', round(CosDistance, 3))

    #-----------
    # 장르 거리 가중치
    #-----------
    GenreDistance = 1 # 거리는 작을수록 가깝기 때문에 최대로 먼 거리 '1' 로 지정
    if(GenreSet_Comp != None):
        GenreDistance, GenreIntersec = get_genres_distance_by_set2(GenreSet_Base, GenreSet_Comp, GenresRawMode=GenresRawMode)
        # 장르 거리를 재조정
        TotalDistance += GenreDistance

    #-----------
    # 평점 가중치
    #-----------
    vote_average = 0
    vote_count = 0
    vote_count_rate = 0 # 비율을 조정하지 않은 상태
    VotingDistance = 0 # 거리는 작을수록 가깝고 계산을 안했기 때문에 가장 가까운 거리 '0' 로 지정
    if(vote_average_comp != None):
        vote_average = vote_average_comp
        VotingDistance = 1 # 거리는 작을수록 가깝기 때문에 최대로 먼 거리 '1' 로 지정
        if(isinstance(vote_average, float)): # nan(NaN)(드물게 값이 없는 경우가 있다.)
            vote_average = 0
        else:
            vote_average_modify = (vote_average / 10) # {Voting: 10점 만점이라서 0~1 범위로 전환}

            # 평점 참여자 가중치
            if(vote_count_comp != None):
                vote_count = vote_count_comp
                if(isinstance(vote_count, float)): # nan(NaN)(드물게 값이 없는 경우가 있다.)
                    vote_count = 0
                else:
                    if(VoteCountMax > 0):
                        vote_count_rate = (vote_count / VoteCountMax)
                        vote_average_modify *= vote_count_rate # {투표 참여자 수}로 투표 거리 비율 조정
            #
            VotingDistance -= vote_average_modify
        # 평점 거리를 재조정
        TotalDistance += VotingDistance

    #-----------
    # 컬렉션 가중치
    #-----------
    CollectionName = ''
    CollectionDistance = None # 거리는 작을수록 가깝고 Collection 계산을 안했기 때문에 'None' 지정
    if(CollectionDict_Comp != None):
        # [belongs_to_collection]는 사전의 목록 형식의 문자열이므로 변환해야 한다.
        # format: {'id': 10194, 'name': 'Toy Story Collection', 'poster_path': '/7G9915LfUQ2lVfwMEEhDsn3kT4B.jpg', 'backdrop_path': '/9FBwqcd9IRruEDUrTdcaafOMKUq.jpg'}
        CollectionDistance = 1 # 거리는 작을수록 가깝기 때문에 최대로 먼 거리 '1' 로 지정
        if(isinstance(CollectionDict_Comp, float)): # nan(NaN)
            pass
        else:
            if(CollectionDict_Comp['name'] == CollectionDict_Base['name']):
                CollectionName = CollectionDict_Comp['name']
                CollectionDistance = 0 # {Collection}이 일치하므로 가장 가까운 거리값 '0'으로 세팅
        
        # 컬렉션 거리를 재조정
        TotalDistance += CollectionDistance

    #-----------
    #-----------
    TotalDistance += CosDistance
    Distance_Item = {
        'inx':CompInx, # {CompInx} 항목은 값이 'None'일 수도 있다.
        'distance':TotalDistance,
        'CosDistance':CosDistance,
        'genres': GenreSet_Comp,
        'GenreDistance': GenreDistance,
        'vote_average': vote_average,
        'vote_count': vote_count,
        'vote_count_rate': vote_count_rate,
        'VotingDistance': VotingDistance,
        'Collection': CollectionName,
        'CollectionDistance': CollectionDistance,
    }
    #=print(*DocDistance_Item, sep='\n') # 내용이 많을 경우에 출력하면 보기 힘듦.
    
    #
    return Distance_Item

def hgstat_get_distance2__kaggke_movies(WordDict_Base, BaseInx, WordDict_Comp, CompInx,
    GenreSet_Base=None, GenresList=None, GenresRawMode=False,
    VotingList=None, VoteCountList=None, VoteCountMax=0, 
    belongs_to_collection=None,
    ):
    #
    from hgdistance import GetWordDict_CosDistance

    #
    if(GenreSet_Base == None): # 밖에서 미리 만들어서 들어온 값이 없으면 여기서 만든다.
        GenreSet_Base = ()
    if(GenresList != None):
        Genre = GenresList[BaseInx]
        # [Genre]는 사전의 목록 형식의 문자열이므로 변환해야 한다.
        # format: [{'id': 16, 'name': 'Animation'}, {'id': 35, 'name': 'Comedy'}, {'id': 10751, 'name': 'Family'}]
        GenreListDict = list(eval(Genre)) # format: [{'id': 16, 'name': 'Animation'}, {'id': 35, 'name': 'Comedy'}, {'id': 10751, 'name': 'Family'}]
        GenreList = [x['name'] for x in GenreListDict] # format: [{'id': 16, 'name': 'Animation'}, {'id': 35, 'name': 'Comedy'}, {'id': 10751, 'name': 'Family'}]
        GenreSet_Base = set(GenreList)

    #
    CollectionName_Base = ''
    CollectionDict_Base = {}
    if(belongs_to_collection != None):
        Collection = belongs_to_collection[BaseInx]
        # [belongs_to_collection]는 사전의 목록 형식의 문자열이므로 변환해야 한다.
        # format: {'id': 10194, 'name': 'Toy Story Collection', 'poster_path': '/7G9915LfUQ2lVfwMEEhDsn3kT4B.jpg', 'backdrop_path': '/9FBwqcd9IRruEDUrTdcaafOMKUq.jpg'}
        if(isinstance(Collection, float)): # nan(NaN)
            pass
        else:
            CollectionDict_Base = eval(Collection) # format: {'id': 10194, 'name': 'Toy Story Collection', 'poster_path': '/7G9915LfUQ2lVfwMEEhDsn3kT4B.jpg', 'backdrop_path': '/9FBwqcd9IRruEDUrTdcaafOMKUq.jpg'}
            CollectionName_Base = CollectionDict_Base['name']

    #
    TotalDistance = 0
    CosDistance = GetWordDict_CosDistance(WordDict_Base, WordDict_Comp)
    #print('[', BaseInx, ':', WordDict_Comp, ']', round(CosDistance, 3))

    #-----------
    # 장르 거리 가중치
    #-----------
    GenreSet_Comp = set()
    GenreDistance = 1 # 거리는 작을수록 가깝기 때문에 최대로 먼 거리 '1' 로 지정
    if(GenresList != None):
        Genre = GenresList[CompInx]
        # [Genre]는 사전의 목록 형식의 문자열이므로 변환해야 한다.
        # format: [{'id': 16, 'name': 'Animation'}, {'id': 35, 'name': 'Comedy'}, {'id': 10751, 'name': 'Family'}]
        GenreListDict = list(eval(Genre)) # format: [{'id': 16, 'name': 'Animation'}, {'id': 35, 'name': 'Comedy'}, {'id': 10751, 'name': 'Family'}]
        GenreList = [x['name'] for x in GenreListDict] # format: [{'id': 16, 'name': 'Animation'}, {'id': 35, 'name': 'Comedy'}, {'id': 10751, 'name': 'Family'}]
        GenreSet_Comp = set(GenreList)
        GenreDistance, GenreIntersec = get_genres_distance_by_set2(GenreSet_Base, GenreSet_Comp, GenresRawMode=GenresRawMode)
        # 장르 거리를 재조정
        TotalDistance += GenreDistance

    #-----------
    # 평점 가중치
    #-----------
    vote_average = 0
    vote_count = 0
    vote_count_rate = 0 # 비율을 조정하지 않은 상태
    VotingDistance = 0 # 거리는 작을수록 가깝고 계산을 안했기 때문에 가장 가까운 거리 '0' 로 지정
    if(VotingList != None):
        VotingDistance = 1 # 거리는 작을수록 가깝기 때문에 최대로 먼 거리 '1' 로 지정
        vote_average = VotingList[CompInx]
        if(isinstance(vote_average, float)): # nan(NaN)(드물게 값이 없는 경우가 있다.)
            vote_average = 0
        else:
            vote_average_modify = (vote_average / 10) # {Voting: 10점 만점이라서 0~1 범위로 전환}

            # 평점 참여자 가중치
            if(VoteCountList != None):
                vote_count = VoteCountList[CompInx]
                if(isinstance(vote_count, float)): # nan 검사(드물게 값이 없는 경우가 있다.)
                    vote_count = 0
                else:
                    if(VoteCountMax > 0):
                        vote_count_rate = (vote_count / VoteCountMax)
                        vote_average_modify *= vote_count_rate # {투표 참여자 수}로 투표 거리 비율 조정
            #
            VotingDistance -= vote_average_modify
        # 평점 거리를 재조정
        TotalDistance += VotingDistance

    #-----------
    # 컬렉션 가중치
    #-----------
    CollectionName = ''
    CollectionDistance = None # 거리는 작을수록 가깝고 Collection 계산을 안했기 때문에 'None' 지정
    if(belongs_to_collection != None):
        Collection = belongs_to_collection[CompInx]
        # [belongs_to_collection]는 사전의 목록 형식의 문자열이므로 변환해야 한다.
        # format: {'id': 10194, 'name': 'Toy Story Collection', 'poster_path': '/7G9915LfUQ2lVfwMEEhDsn3kT4B.jpg', 'backdrop_path': '/9FBwqcd9IRruEDUrTdcaafOMKUq.jpg'}
        CollectionDistance = 1 # 거리는 작을수록 가깝기 때문에 최대로 먼 거리 '1' 로 지정
        #=print('Collection:', Collection)
        if(isinstance(Collection, float)): # nan(NaN)
            pass
        else:
            CollectionDict_Comp = eval(Collection) # format: {'id': 10194, 'name': 'Toy Story Collection', 'poster_path': '/7G9915LfUQ2lVfwMEEhDsn3kT4B.jpg', 'backdrop_path': '/9FBwqcd9IRruEDUrTdcaafOMKUq.jpg'}
            if(CollectionDict_Comp['name'] == CollectionDict_Base['name']):
                CollectionName = CollectionDict_Comp['name']
                CollectionDistance = 0 # {Collection}이 일치하므로 가장 가까운 거리값 '0'으로 세팅
        
        # 컬렉션 거리를 재조정
        TotalDistance += CollectionDistance

    #-----------
    #-----------
    TotalDistance += CosDistance
    DocDistance_Item = {
        'inx':CompInx,
        'distance':TotalDistance,
        'CosDistance':CosDistance,
        'genres': GenreSet_Comp,
        'GenreDistance': GenreDistance,
        'vote_average': vote_average,
        'vote_count': vote_count,
        'vote_count_rate': vote_count_rate,
        'VotingDistance': VotingDistance,
        'Collection': CollectionName,
        'CollectionDistance': CollectionDistance,
    }
    #=print(*DocDistance_Item, sep='\n') # 내용이 많을 경우에 출력하면 보기 힘듦.
    
    #
    return DocDistance_Item

def hgstat_get_distance_by_inx__kagmov(WordDicts, BaseInx, 
    GenresList=None, GenresRawMode=False, 
    VotingList=None, VoteCountList=None, VoteCountMax=0, 
    belongs_to_collection=None):
    #
    from hgdistance import GetWordDict_CosDistance
    
    #
    if(BaseInx >= len(WordDicts)):
        print("(BaseInx >= len(WordDicts))")
        print(f"({BaseInx} >= len(WordDicts))")
        assert False

    #
    GenreSet_Base = ()
    if(GenresList != None):
        Genre = GenresList[BaseInx]
        # [Genre]는 사전의 목록 형식의 문자열이므로 변환해야 한다.
        # format: [{'id': 16, 'name': 'Animation'}, {'id': 35, 'name': 'Comedy'}, {'id': 10751, 'name': 'Family'}]
        GenreListDict = list(eval(Genre)) # format: [{'id': 16, 'name': 'Animation'}, {'id': 35, 'name': 'Comedy'}, {'id': 10751, 'name': 'Family'}]
        GenreList = [x['name'] for x in GenreListDict] # format: [{'id': 16, 'name': 'Animation'}, {'id': 35, 'name': 'Comedy'}, {'id': 10751, 'name': 'Family'}]
        GenreSet_Base = set(GenreList)
    
    #
    CollectionName_Base = ''
    CollectionDict_Base = {}
    if(belongs_to_collection != None):
        Collection = belongs_to_collection[BaseInx]
        # [belongs_to_collection]는 사전의 목록 형식의 문자열이므로 변환해야 한다.
        # format: {'id': 10194, 'name': 'Toy Story Collection', 'poster_path': '/7G9915LfUQ2lVfwMEEhDsn3kT4B.jpg', 'backdrop_path': '/9FBwqcd9IRruEDUrTdcaafOMKUq.jpg'}
        if(isinstance(Collection, float)): # nan(NaN)
            pass
        else:
            CollectionDict_Base = eval(Collection) # format: {'id': 10194, 'name': 'Toy Story Collection', 'poster_path': '/7G9915LfUQ2lVfwMEEhDsn3kT4B.jpg', 'backdrop_path': '/9FBwqcd9IRruEDUrTdcaafOMKUq.jpg'}
            CollectionName_Base = CollectionDict_Base['name']
    

    #
    MovieDistances = []
    for j in range(0, len(WordDicts)):
        if(BaseInx == j):
            continue
        
        TotalDistance = 0
        CosDistance = GetWordDict_CosDistance(WordDicts[BaseInx], WordDicts[j])
        #print('[', BaseInx, ':', j, ']', round(CosDistance, 3))

        #-----------
        # 장르 가중치
        #-----------
        GenreSet_Comp = set()
        GenreDistance = 1 # 거리는 작을수록 가깝기 때문에 최대로 먼 거리 '1' 로 지정
        if(GenresList != None):
            Genre = GenresList[j]
            # [Genre]는 사전의 목록 형식의 문자열이므로 변환해야 한다.
            # format: [{'id': 16, 'name': 'Animation'}, {'id': 35, 'name': 'Comedy'}, {'id': 10751, 'name': 'Family'}]
            GenreListDict = list(eval(Genre)) # format: [{'id': 16, 'name': 'Animation'}, {'id': 35, 'name': 'Comedy'}, {'id': 10751, 'name': 'Family'}]
            GenreList = [x['name'] for x in GenreListDict] # format: [{'id': 16, 'name': 'Animation'}, {'id': 35, 'name': 'Comedy'}, {'id': 10751, 'name': 'Family'}]
            GenreSet_Comp = set(GenreList)
            GenreDistance, GenreIntersec = get_genres_distance_by_set2(GenreSet_Base, GenreSet_Comp, GenresRawMode=GenresRawMode)
            # 장르 거리를 재조정
            TotalDistance += GenreDistance

        #-----------
        # 평점 가중치
        #-----------
        vote_average = 0
        vote_count = 0
        vote_count_rate = 0 # 비율을 조정하지 않은 상태
        VotingDistance = 0 # 거리는 작을수록 가깝고 계산을 안했기 때문에 가장 가까운 거리 '0' 로 지정
        if(VotingList != None):
            VotingDistance = 1 # 거리는 작을수록 가깝기 때문에 최대로 먼 거리 '1' 로 지정
            vote_average = VotingList[j]
            vote_average_modify = (vote_average / 10) # {Voting: 10점 만점이라서 0~1 범위로 전환}

            # 평점 참여자 가중치
            if(VoteCountList != None):
                try: # 중간에 비정상적인 데이터가 있을 수 있다.
                    vote_count = int(VoteCountList[j])
                except ValueError: # raise ValueError("cannot convert float NaN to integer)
                    #=print("ValueError: cannot convert float NaN to integer ")
                    pass
                if(VoteCountMax > 0):
                    vote_count_rate = (vote_count / VoteCountMax)
                    vote_average_modify *= vote_count_rate # {투표 참여자 수}로 투표 거리 비율 조정
            #
            VotingDistance -= vote_average_modify

            # 평점 거리를 재조정
            TotalDistance += VotingDistance

        #-----------
        # 컬렉션 가중치
        #-----------
        CollectionName = ''
        CollectionDistance = None # 거리는 작을수록 가깝고 Collection 계산을 안했기 때문에 'None' 지정
        if(belongs_to_collection != None):
            Collection = belongs_to_collection[j]
            # [belongs_to_collection]는 사전의 목록 형식의 문자열이므로 변환해야 한다.
            # format: {'id': 10194, 'name': 'Toy Story Collection', 'poster_path': '/7G9915LfUQ2lVfwMEEhDsn3kT4B.jpg', 'backdrop_path': '/9FBwqcd9IRruEDUrTdcaafOMKUq.jpg'}
            CollectionDistance = 1 # 거리는 작을수록 가깝기 때문에 최대로 먼 거리 '1' 로 지정
            #=print('Collection:', Collection)
            if(isinstance(Collection, float)): # nan(NaN)
                pass
            else:
                CollectionDict_Comp = eval(Collection) # format: {'id': 10194, 'name': 'Toy Story Collection', 'poster_path': '/7G9915LfUQ2lVfwMEEhDsn3kT4B.jpg', 'backdrop_path': '/9FBwqcd9IRruEDUrTdcaafOMKUq.jpg'}
                if((len(CollectionDict_Comp['name'])) and (len(CollectionDict_Base) > 0)):
                    if(CollectionDict_Comp['name'] == CollectionDict_Base['name']):
                        CollectionName = CollectionDict_Comp['name']
                        CollectionDistance = 0 # {Collection}이 일치하므로 가장 가까운 거리값 '0'으로 세팅
            
            # 컬렉션 거리를 재조정
            TotalDistance += CollectionDistance

        #-----------
        #-----------
        TotalDistance += CosDistance
        DocDistance_j = {
            'inx':j,
            'distance':TotalDistance,
            'CosDistance':CosDistance,
            'genres': GenreSet_Comp,
            'GenreDistance': GenreDistance,
            'vote_average': vote_average,
            'vote_count': vote_count,
            'vote_count_rate': vote_count_rate,
            'VotingDistance': VotingDistance,
            'Collection': CollectionName,
            'CollectionDistance': CollectionDistance,
        }
        MovieDistances.append(DocDistance_j)
        #break
    
    # 정렬
    MovieDistances.sort(key = lambda item: (item['distance'])) # 거리(by low)
    #=print(*MovieDistances, sep='\n') # 내용이 많을 경우에 출력하면 보기 힘듦.
    
    #
    return MovieDistances

def hgstat_print_item__kaggle_movies(
    title, overview, release_date, genres, 
    vote_average = None, vote_count = None,
    CollectionDict = None,
    printShortFormat=False,
    ):
    #-----------------------
    # 영화 정보를 출력해본다.
    #-----------------------
    #=print(f'<doc-{FindInx}> : {Filelist[FindInx]}')
    story = overview
    Genre = genres
    #=print(f'{Genre}')
    # [Genre]는 사전의 목록 형식의 문자열이므로 변환해야 한다.
    # format: [{'id': 16, 'name': 'Animation'}, {'id': 35, 'name': 'Comedy'}, {'id': 10751, 'name': 'Family'}]
    GenreListDict = list(eval(Genre)) # format: [{'id': 16, 'name': 'Animation'}, {'id': 35, 'name': 'Comedy'}, {'id': 10751, 'name': 'Family'}]
    GenreList_Base = [x['name'] for x in GenreListDict] # format: [{'id': 16, 'name': 'Animation'}, {'id': 35, 'name': 'Comedy'}, {'id': 10751, 'name': 'Family'}]
    GenreList_Base = set(GenreList_Base)
    if(vote_average == None):
        vote_average = ''
    if(vote_count == None):
        vote_count = ''
    

    #=print(f'<doc-{FindInx}> ', end='')
    print(f'[{release_date}]: {title}')
    #=print(f'<doc-{FindInx}> :')
    #=PrintWordDictList(WordDictList_Find, PrintingNum=30, 
    #=    PrintIndex=True, OneLine=False, SimpleFormat=True, SortFlag=True)
    print(f"vote_average: {vote_average} ({vote_count})")
    if(printShortFormat == True):
        pass
    else:
        print(f'{GenreList_Base}')
        if(CollectionDict != None):
            print(f"{CollectionDict['name']}")
        print(f'{story}')
    #
    print()

def hgstat_print_info__kaggle_movies(WordDictList_Find,
    FindInx, title_list, overview_list, release_date_list, genres_list, 
    vote_average_list = None, vote_count_list = None,
    belongs_to_collection = None,
    printShortFormat=False,
    ):
    #-----
    import hgsysinc
    from hgbasic import PrintDictList_ByLine
    from hgwordlist import PrintWordDictList

    #-----------------------
    # 영화 정보를 출력해본다.
    #-----------------------
    #=print(f'<doc-{FindInx}> : {Filelist[FindInx]}')
    title = title_list[FindInx]
    story = overview_list[FindInx]
    release_date = release_date_list[FindInx]
    Genre = genres_list[FindInx] 
    #=print(f'{Genre}')
    # [Genre]는 사전의 목록 형식의 문자열이므로 변환해야 한다.
    # format: [{'id': 16, 'name': 'Animation'}, {'id': 35, 'name': 'Comedy'}, {'id': 10751, 'name': 'Family'}]
    GenreListDict = list(eval(Genre)) # format: [{'id': 16, 'name': 'Animation'}, {'id': 35, 'name': 'Comedy'}, {'id': 10751, 'name': 'Family'}]
    GenreList_Base = [x['name'] for x in GenreListDict] # format: [{'id': 16, 'name': 'Animation'}, {'id': 35, 'name': 'Comedy'}, {'id': 10751, 'name': 'Family'}]
    GenreList_Base = set(GenreList_Base)
    vote_average = ''
    if(vote_average_list != None):
        vote_average = vote_average_list[FindInx]
    vote_count = ''
    if(vote_count_list != None):
        vote_count = vote_count_list[FindInx]    
    wordlist_base_set = set([dic['word'] for dic in WordDictList_Find])

    CollectionName = ''
    if(belongs_to_collection != None):
        Collection = belongs_to_collection[FindInx]
        if(isinstance(Collection, float)): # nan(NaN)
            pass
        else:
            collection_Base = eval(Collection) # format: {'id': 10194, 'name': 'Toy Story Collection', 'poster_path': '/7G9915LfUQ2lVfwMEEhDsn3kT4B.jpg', 'backdrop_path': '/9FBwqcd9IRruEDUrTdcaafOMKUq.jpg'}
            CollectionName = collection_Base['name']

    #
    print(f'<doc-{FindInx}> [{release_date}]: {title}')
    #=print(f'<doc-{FindInx}> :')
    #=frist_doc_word_dict = WordDictList_Find
    #=PrintWordDictList(frist_doc_word_dict, PrintingNum=30, 
    #=    PrintIndex=True, OneLine=False, SimpleFormat=True, SortFlag=True)
    print(f"vote_average: {vote_average} ({vote_count})")
    if(len(CollectionName) > 0):
        print(f'Collection: {CollectionName}')
    if(len(GenreList_Base) > 0):
        print(f'Genre: {GenreList_Base}')

    if(printShortFormat == True):
        pass
    else:
        print(f'{story}')
    #
    print()

def hgstat_print_distanace_result__kaggle_movies(movie_distanace, WordDictList_Comp,
    title, overview, release_date, 
    wordlist_find_set, PrintCnt = None,
    debugPrint=False, printShortFormat=False,
    ):
    #-----
    import hgsysinc
    from hgbasic import PrintDictList_ByLine
    from hgwordlist import PrintWordDictList

    #-----------------------
    # 거리 정보를 출력해본다.
    #-----------------------
    first_docid = movie_distanace['inx']

    #
    story = overview
    Distanace = movie_distanace['distance']
    CosDistanace = movie_distanace['CosDistance']
    GenreList = movie_distanace['genres']
    vote_average = movie_distanace['vote_average']
    VotingDistance = movie_distanace['VotingDistance']
    vote_count = movie_distanace['vote_count']
    vote_count_rate = movie_distanace['vote_count_rate']
    collection = movie_distanace['Collection']
    CollectionDistance = movie_distanace['CollectionDistance']

    wordlist_comp_set = set([dic['word'] for dic in WordDictList_Comp])
    common_word_set = wordlist_find_set.intersection(wordlist_comp_set)
    common_wordnum = len(common_word_set)

    if(printShortFormat == True):
        print(f"{PrintCnt}\t ", end='')
        print(f"{first_docid}\t", end='')
        print('%0.4f\t' % Distanace, end='')
        print('%0.4f\t' % CosDistanace, end='')
        print(f"{vote_average}\t {vote_count}\t ", end='')
        print('%.3f\t' % vote_count_rate, end='')
        print('%.3f\t' % VotingDistance, end='')
        print(f'{collection}\t ', end='')
        if(CollectionDistance != None):
            print('%.3f\t' % CollectionDistance, end='')
        else:
            print('\t', end='')
    else:
        print()
        if(PrintCnt != None):
            print(f"[{PrintCnt}] ", end='')
        print(f"similar doc-inx: {first_docid} ", end='')
        print("(Distanace:", "%0.4f" % Distanace, ")")
        print("(CosDistanace:", "%0.4f" % CosDistanace, ")")
    #=print(f'[{simcnt}] similar file: {Filelist[first_docid]}')

    if(printShortFormat == True):
        print(f'{release_date}\t {common_wordnum}\t {title}', end='')
    else:
        if(PrintCnt != None):
            print(f"[{PrintCnt}] ", end='')
        print(f'similar doc [{release_date}]: {title}')
        print(f"{GenreList}:%.3f" % movie_distanace['GenreDistance'])
        print(f"vote_average: {vote_average}({vote_count}) (VotingDistance: %.3f)" %VotingDistance)
        print(f'({common_wordnum}) : {common_word_set}')
        if(len(collection) > 0):
            print(f'collection: {collection}:', end='')
            if(CollectionDistance != None):
                print("(", "%.4f" % CollectionDistance, ")")
            else:
                print()
        print(f'{story}')
    #
    print()

    if(debugPrint == True):
        if(printShortFormat == True):
            pass
        else:
            frist_doc_word_dict = WordDictList_Comp
            frist_doc_word_dict_some = frist_doc_word_dict[:30]
            frist_doc_word_list_some = [wdic_i['word'] for wdic_i in frist_doc_word_dict_some]
            print(frist_doc_word_list_some)

def hgstat_print_distanace_item__kaggle_movies(movie_distanace, WordDictList_Comp,
    title_list, overview_list, release_date_list, 
    wordlist_find_set, PrintCnt = None,
    debugPrint=False, printShortFormat=False,
    CosDistance2CosSimilarity=False, # 코사인 거리를 코사인 유사도로 출력
    ):
    #-----
    import hgsysinc
    from hgbasic import PrintDictList_ByLine
    from hgwordlist import PrintWordDictList

    #-----------------------
    # 거리 정보를 출력해본다.
    #-----------------------
    first_docid = movie_distanace['inx']

    #
    title = title_list[first_docid]
    story = overview_list[first_docid]
    release_date = release_date_list[first_docid]

    Distanace = movie_distanace['distance']
    CosDistanace = movie_distanace['CosDistance']
    CosSimilarity = 1 - CosDistanace
    GenreList = movie_distanace['genres']
    GenreDistance = movie_distanace['GenreDistance']
    vote_average = movie_distanace['vote_average']
    VotingDistance = movie_distanace['VotingDistance']
    vote_count = movie_distanace['vote_count']
    vote_count_rate = movie_distanace['vote_count_rate']
    collection = movie_distanace['Collection']
    CollectionDistance = movie_distanace['CollectionDistance']

    wordlist_comp_set = set([dic['word'] for dic in WordDictList_Comp])
    common_word_set = wordlist_find_set.intersection(wordlist_comp_set)
    common_wordnum = len(common_word_set)

    if(printShortFormat == True):
        print(f"{PrintCnt}\t ", end='')
        print(f"{first_docid}\t", end='')
        print('%0.3f\t' % Distanace, end='')
        if(CosDistance2CosSimilarity==True):
            print('%0.3f\t' % CosSimilarity, end='')
        else:
            print('%0.4f\t' % CosDistanace, end='')
        print('%.3f\t' % GenreDistance, end='')
        print(f"{vote_average}\t {vote_count}\t ", end='')
        print('%.3f\t' % vote_count_rate, end='')
        print('%.3f\t' % VotingDistance, end='')
        print(f'{collection}\t ', end='')
        if(CollectionDistance != None):
            print('%.3f\t' % CollectionDistance, end='')
        else:
            print('\t', end='')
    else:
        print()
        if(PrintCnt != None):
            print(f"[{PrintCnt}] ", end='')
        print(f"similar doc-inx: {first_docid} ", end='')
        print("(Distanace:", "%0.3f" % Distanace, ")")
        if(CosDistance2CosSimilarity == True):
            print("(Similarity:", "%0.3f" % CosSimilarity, ")")
        else:
            print("(CosDistanace:", "%0.3f" % CosDistanace, ")")
    #=print(f'[{simcnt}] similar file: {Filelist[first_docid]}')

    if(printShortFormat == True):
        print(f'{release_date}\t {common_wordnum}\t {title}', end='')
    else:
        if(PrintCnt != None):
            print(f"[{PrintCnt}] ", end='')
        print(f'similar doc [{release_date}]: {title}')
        print(f"{GenreList}:%.3f" % movie_distanace['GenreDistance'])
        print(f"vote_average: {vote_average}({vote_count}) (VotingDistance: %.3f)" %VotingDistance)
        print(f'({common_wordnum}) : {common_word_set}')
        if(len(collection) > 0):
            print(f'collection: {collection}:', end='')
            if(CollectionDistance != None):
                print("(", "%.4f" % CollectionDistance, ")")
            else:
                print()
        print(f'{story}')
    #
    print()

    if(debugPrint == True):
        if(printShortFormat == True):
            pass
        else:
            frist_doc_word_dict = WordDictList_Comp
            frist_doc_word_dict_some = frist_doc_word_dict[:30]
            frist_doc_word_list_some = [wdic_i['word'] for wdic_i in frist_doc_word_dict_some]
            print(frist_doc_word_list_some)

def hgstat_print_distanace_pair__kaggle_movies(DocDistance_Item, 
    WordDictList_Find, FindInx, title_find, overview_find, release_date_find, genres_find, 
    WordDictList_Comp, title_comp, overview_comp, release_date_comp, 
    vote_average_find = None, vote_count_find = None, 
    CollectionDict_Find = None,
    debugPrint=False, printShortFormat=False,
    ):
    #-----
    import hgsysinc
    from hgbasic import PrintDictList_ByLine
    from hgwordlist import PrintWordDictList

    print('==========================================================')
    #----------------
    # 문서를 비교 출력
    #----------------
    if(FindInx != None): # 값이 있을 때만 처리
        print(f'<doc-{FindInx}> ', end='')
    hgstat_print_item__kaggle_movies(title_find, overview_find, release_date_find, genres_find, 
        vote_average = vote_average_find, vote_count = vote_count_find,
        CollectionDict = CollectionDict_Find,
        printShortFormat=printShortFormat,
        )
    #
    wordlist_find_set = set([dic['word'] for dic in WordDictList_Find])

    # caption-print
    if(printShortFormat == True):
        print(f"order\t doc-inx\t distance\t cos-distance\t vote_average\t vote_count\t", end='')
        print(f'vote_count_rate\t vote_distance\t collection\t collection_dis\t', end='')
        print(f'release_date\t common_wordnum\t title\t', end='')
        print()

    #
    hgstat_print_distanace_result__kaggle_movies(DocDistance_Item, WordDictList_Comp,
        title_comp, overview_comp, release_date_comp, 
        wordlist_find_set, PrintCnt = None,
        debugPrint=debugPrint, printShortFormat=printShortFormat,
        )
    if(debugPrint == True):
        if(printShortFormat == True):
            pass
        else:
            # 검색 기준 문서의 단어 목록 전체 출력
            PrintWordDictList(WordDictList_Find, PrintingNum=0, PrintIndex=True, OneLine=True, SortFlag=True)

def hgstat_print_distanace_by_item__kaggle_movies(DocDistance_Item, WordDictList_Find,
    FindInx, WordDictList_Comp, title_list, overview_list, release_date_list, genres_list, 
    vote_average_list = None, vote_count_list = None, belongs_to_collection=None,
    debugPrint=False, printShortFormat=False,
    ):
    #-----
    import hgsysinc
    from hgbasic import PrintDictList_ByLine
    from hgwordlist import PrintWordDictList

    print('==========================================================')
    print('==========================================================')
    print('==========================================================')
    #----------------
    # 문서를 비교 출력
    #----------------
    hgstat_print_info__kaggle_movies(WordDictList_Find,
        FindInx, title_list, overview_list, release_date_list, genres_list, 
        vote_average_list = vote_average_list, vote_count_list = vote_count_list,
        belongs_to_collection=belongs_to_collection,
        printShortFormat=printShortFormat,
        )
    #
    wordlist_find_set = set([dic['word'] for dic in WordDictList_Find])

    # caption-print
    if(printShortFormat == True):
        print(f"order\t doc-inx\t distance\t cos-distance\t vote_average\t vote_count\t", end='')
        print(f'vote_count_rate\t vote_distance\t collection\t collection_dis\t', end='')
        print(f'release_date\t common_wordnum\t title\t', end='')
        print()

    #
    hgstat_print_distanace_item__kaggle_movies(DocDistance_Item, WordDictList_Comp,
        title_list, overview_list, release_date_list, genres_list, 
        wordlist_find_set, PrintCnt = None,
        debugPrint=debugPrint, printShortFormat=printShortFormat,
    )
    if(debugPrint == True):
        if(printShortFormat == True):
            pass
        else:
            # 검색 기준 문서의 단어 목록 전체 출력
            PrintWordDictList(WordDictList_Find, PrintingNum=0, PrintIndex=True, OneLine=True, SortFlag=True)

def hgstat_print_distanace__kaggle_movies2(DocDis_sort, WordDicts,
    FindInx, CompInx, title_list, overview_list, release_date_list, genres_list, 
    vote_average_list = None, vote_count_list = None, belongs_to_collection=None,
    debugPrint=False, printShortFormat=False,
    ):


    WordDictList_Find = WordDicts[FindInx]
    WordDictList_Comp = WordDicts[CompInx]
    DocDistance_Item = next(item for item in DocDis_sort if item['inx'] == CompInx)

    hgstat_print_distanace_by_item__kaggle_movies(DocDistance_Item, WordDictList_Find,
        FindInx, WordDictList_Comp, 
        title_list, overview_list, release_date_list, genres_list, 
        vote_average_list = vote_average_list, vote_count_list = vote_count_list,
        belongs_to_collection=belongs_to_collection,
        debugPrint=debugPrint, printShortFormat=printShortFormat,
    )

def hgstat_print_distanace__kaggle_movies(DocDis_sort, WordDicts,
    FindInx, title_list, overview_list, release_date_list, genres_list, 
    vote_average_list = None, vote_count_list = None,
    belongs_to_collection = None,
    RankNum=0, debugPrint=False, printShortFormat=False,
    CosDistance2CosSimilarity=False,
    ):
    #-----
    import hgsysinc
    from hgbasic import PrintDictList_ByLine
    from hgwordlist import PrintWordDictList

    print('==========================================================')
    print('==========================================================')
    print('==========================================================')
    #-----------------
    # 정렬된 내용을 출력
    #-----------------
    print_CosDistances = True
    print_CosDistances = False
    printNum = 0 # 모두 순위 출력
    if(RankNum > 0):
        printNum = RankNum
    if(print_CosDistances == True):
        PrintDictList_ByLine(DocDis_sort, Printnum=printNum)

    #-----------------------
    # 가장 가까운 문서를 출력해본다.
    #-----------------------
    WordDictList_Find = WordDicts[FindInx]
    hgstat_print_info__kaggle_movies(WordDictList_Find,
        FindInx, title_list, overview_list, release_date_list, genres_list, 
        vote_average_list = vote_average_list, vote_count_list = vote_count_list,
        belongs_to_collection = belongs_to_collection,
        printShortFormat=printShortFormat,
        )
    
    #
    wordlist_find_set = set([dic['word'] for dic in WordDictList_Find])

    # caption-print
    if(printShortFormat == True):
        print(f"order\t doc-inx\t distance\t cos-distance\t genre-distance\t vote_average\t vote_count\t", end='')
        print(f'vote_count_rate\t vote_distance\t collection\t collection_dis\t', end='')
        print(f'release_date\t common_wordnum\t title\t', end='')
        print()

    simcnt = 0
    for DocDis_i in DocDis_sort:
        first_docid = DocDis_i['inx']
        if(FindInx == first_docid): # 검사하는 문서와 같을 경우
            continue

        WordDictList_Comp = WordDicts[first_docid]
        hgstat_print_distanace_item__kaggle_movies(DocDis_i, WordDictList_Comp,
            title_list, overview_list, release_date_list, 
            wordlist_find_set, PrintCnt = simcnt,
            debugPrint=debugPrint, printShortFormat=printShortFormat,
            CosDistance2CosSimilarity=CosDistance2CosSimilarity,
        )
                
        #
        simcnt += 1
        if simcnt >= printNum:
            break

    if(debugPrint == True):
        if(printShortFormat == True):
            pass
        else:
            # 검색 기준 문서의 단어 목록 전체 출력
            PrintWordDictList(WordDictList_Find, PrintingNum=0, PrintIndex=True, OneLine=True, SortFlag=True)

def hgstat_get_set__metadata_by_title(movies_metadata, title, debugPrint=False):
    #-----------
    #-----------
    #-----------
    import hgsysinc
    from hgwordlist import GetWordList__Text6, GetWordDictList_WordList
    from hgeng_spell_rule import stoplist_eng_raw_min1

    #
    #=Info_Find = hgstat_get_movies_info_metadata_by_title(movies_metadata, title)
    #=print(Info_Find)
    
    movie_info = movies_metadata.loc[movies_metadata['original_title'] == title]
    #=print(f'{title}: {movie_info}')
    #=print(f'{title}: {movie_info.iloc[0]}')

    overview = movie_info.iloc[0]['overview']
    genres = movie_info.iloc[0]['genres']
    release_date = movie_info.iloc[0]['release_date']
    vote_average = movie_info.iloc[0]['vote_average']
    vote_count = movie_info.iloc[0]['vote_count']
    belongs_to_collection = movie_info.iloc[0]['belongs_to_collection']
    if(debugPrint == True):
        print(f"overview: {overview}")
        print(f"genres: {genres}")
        print(f"release_date: {release_date}")
        print(f"vote_average: {vote_average}")
        print(f"vote_count: {vote_count}")
        print(f"belongs_to_collection: {belongs_to_collection}")        

    #
    emptyFlag = hgstat_is_empty_overview(overview) # 줄거리가 없는지 확인
    if(emptyFlag == True):
        overview = ''
    
    #
    stoplist = stoplist_eng_raw_min1
    overview_wordlist = GetWordList__Text6(overview, 
            ExcFilter=stoplist, # 불용어 처리
            LowerCase=False, 
            CliticsModify=True, # {~'s}, {~'t}, {~'d}는 {~}로 바꾼다.
            ExcChar1=True,  # 1글자보다 작은 것은 지운다.
            ExcNumber=True, # 숫자만 있는 것은 지운다.
            )
    #print(overview_wordlist)
    if(len(overview_wordlist) <= 0):
        #=print('단어 목록(overview_wordlist)이 없습니다.')
        pass
    #
    overview_WordDictList = GetWordDictList_WordList(overview_wordlist, EraseNonKeyword=False)

    #
    return overview_WordDictList, overview, release_date, genres, \
            vote_average, vote_count, belongs_to_collection

def hgstat_recommend_movie__kaggle(WordDicts, FindInx, 
    title_list, overview_list, release_date_list, genres_list,
    vote_average_list = None, vote_count_list = None,
    belongs_to_collection=None,
    reco_type='genre+voting', RankNum=10, 
    debugPrint=False, printShortFormat = True):
    #---------------
    #---------------
    # debugPrint = True # 각 텍스트에 속한 사전(어휘 목록)을 출력
    # debugPrint = False # 각 텍스트에 속한 사전(어휘 목록)을 비롯하여 중간 내용 출력하지 않음
    #
    # printShortFormat = True # 간단하게 1줄로 출력(True:예)
    # printShortFormat = False # 간단하게 1줄로 출력(False:아님)
    #---------------
    #---------------

    print(), print(), print(), print(), print(), 
    if(reco_type == 'genre+voting'):
        print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        print('# 3) {장르+평점} 가중치 적용(장르 완전 일치) ')
        print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        SimDocInfo = hgstat_get_distance_by_inx__kagmov(WordDicts, FindInx, genres_list, 
            VotingList=vote_average_list)
        #=PrintSimDoc_CosDistance__ByInx(SimDocInfo, FindInx, RankNum=RankNum, debugPrint=debugPrint)
        hgstat_print_distanace__kaggle_movies(SimDocInfo, WordDicts,
            FindInx, title_list, overview_list, release_date_list, genres_list,
            vote_average_list = vote_average_list, vote_count_list = vote_count_list,
            RankNum=RankNum, debugPrint=debugPrint, printShortFormat=printShortFormat)
    elif(reco_type == 'genre+voting+count'):
        print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        print('# 4) {장르+(평점*평점참여자-참여자최댓값기준)} 가중치 적용(장르 완전 일치) ')
        print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        # 평점참여자 최댓값 구하기
        vote_count_max = hgstat_get_vote_count_max(vote_count_list)
        print('vote_count_max:', vote_count_max)

        SimDocInfo = hgstat_get_distance_by_inx__kagmov(WordDicts, FindInx, genres_list, 
            VotingList=vote_average_list, VoteCountList=vote_count_list, VoteCountMax=vote_count_max)
        hgstat_print_distanace__kaggle_movies(SimDocInfo, WordDicts,
            FindInx, title_list, overview_list, release_date_list, genres_list,
            vote_average_list = vote_average_list, vote_count_list = vote_count_list,
            RankNum=RankNum, debugPrint=debugPrint, printShortFormat=printShortFormat)

        #-----------------------------------
        # {평점참여자 최댓값}을 적용하면 어색한 요인이 발생한다.
        # {The Wrong Trousers:웰레스와 그로밋(전자바지 소동)}에서는 평점 참여자가 {266}명이라서 
        # {평점참여자 최댓값(vote_count_max)}이 {14075}에 비하면 작은 값이다.
        # {평점}을 {평점참여자 최댓값(vote_count_max)}으로 가중치를 적용하면 
        # 대중적으로 인기가 많은 픽사 영화는 {평점참여자}가 평균 5천명이 넘는다.
        # 그러면 {Monsters, Inc}, {Toy Story}, {Happy Feet Two}, {Inside Out} 등이 
        # 먼저 추천되고 {웰레스와 그로밋} 시리즈는 순위에서 볼 수 없다.
        # 마찬가지로 다른 시리즈 영화의 경우에는 일치하는 주제어가 적을수록 
        # {평점 가중치}에 영향을 받아서 시리즈보다 {평점 가중치}가 높은 유명한 영화가 추천된다.
        # {Toy Story} 시리즈의 경우에는 일치하는 주제어도 (상대적으로) 많고 
        # {평점 가중치}도 높아서 차이가 나지 않지만 ...
        #-----------------------------------
    elif(reco_type == 'genre+collection+voting+count'):
        print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        print('# 5) {장르+컬렉션+(평점*평점참여자-참여자최댓값기준)} 가중치 적용')
        print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        # 평점참여자 최댓값 구하기
        vote_count_max = hgstat_get_vote_count_max(vote_count_list)
        print('vote_count_max:', vote_count_max)

        SimDocInfo = hgstat_get_distance_by_inx__kagmov(WordDicts, FindInx, genres_list, 
            VotingList=vote_average_list, VoteCountList=vote_count_list, VoteCountMax=vote_count_max,
            belongs_to_collection=belongs_to_collection)
        hgstat_print_distanace__kaggle_movies(SimDocInfo, WordDicts,
            FindInx, title_list, overview_list, release_date_list, genres_list,
            vote_average_list = vote_average_list, vote_count_list = vote_count_list,
            belongs_to_collection=belongs_to_collection,
            RankNum=RankNum, debugPrint=debugPrint, printShortFormat=printShortFormat)

        #-----------------------------------
        # {컬렉션}을 적용하면 무조건 시리즈가 가장 먼저 추천된다.
        # {평점참여자 최댓값}을 적용했을 때보다 우선 순위가 높아져서 
        # {컬렉션} 시리즈물을 먼저 추천한 후에  {평점참여자 최댓값} 가중치를 적용한다.
        # 이렇게 {컬렉션}의 가중치를 높게 반영되도록 하면 일반적인 추천 사이트와 비슷한 느낌이 난다.
        #
        # {The Wrong Trousers:웰레스와 그로밋(전자바지 소동)}에서는 평점 참여자가 {266}명이라서 
        # {평점참여자 최댓값(vote_count_max)}이 {14075}에 비하면 작은 값이다.
        # {평점}을 {평점참여자 최댓값(vote_count_max)}으로 가중치를 적용하면 
        # 대중적으로 인기가 많은 픽사 영화는 {평점참여자}가 평균 5천명이 넘는다.
        # 그러면 {Monsters, Inc}, {Toy Story}, {Happy Feet Two}, {Inside Out} 등이 
        # 먼저 추천되고 {웰레스와 그로밋} 시리즈는 순위에서 볼 수 없었지만 
        # {컬렉션} 가중치를 반영하면 {웰레스와 그로밋} 시리즈가 가장 먼저 추천된다.
        # 마찬가지로 다른 시리즈 영화의 경우에는 {컬렉션} 가중치를 반영하면 
        # 시리즈물이 먼저 추천된다.
        #
        # {Toy Story} 시리즈의 경우에는 일치하는 주제어도 (상대적으로) 많고 
        # {평점 가중치}도 높을 뿐아서 {컬렉션} 가중치를 적용하지 않아도 먼저 추천된다.
        # {Toy Story}의 경우에는 {주제어 가중치, 장르 가중치, 평점 가중치, 컬렉션} 가중치가 모두 높아서 
        # 어떤 방식으로 계산해도 자연스러워 보인다.
        #-----------------------------------

    elif(reco_type == 'genre_low'):
        #---------------------
        # 이번 예제는 아래 부분은 필요 없어서 막는다. 실제 사용하기 어렵다. 알고리즘 평가용
        #---------------------
        #=print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        #=print('# {장르} 가중치 적용(장르 포함 일치) ')
        #=print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        #=SimDocInfo = hgstat_get_distance_by_inx__kagmov(WordDicts, FindInx, genres_list, VotingList=vote_average_list, GenresRawMode=True)
        #=#=PrintSimDoc_CosDistance__ByInx(SimDocInfo, FindInx, RankNum=RankNum, debugPrint=debugPrint)
        #=hgstat_print_distanace__kaggle_movies(SimDocInfo, WordDicts,
        #=    FindInx, title_list, overview_list, release_date_list, genres_list,
        #=    RankNum=RankNum, debugPrint=debugPrint, printShortFormat=printShortFormat)
        #---------------------
        #---------------------
        #---------------------
        pass
    elif(reco_type == 'genre'):
        print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        print('# 3) {장르} 가중치 적용(장르 완전 일치) ')
        print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        SimDocInfo = hgstat_get_distance_by_inx__kagmov(WordDicts, FindInx, genres_list)
        #=PrintSimDoc_CosDistance__ByInx(SimDocInfo, FindInx, RankNum=RankNum, debugPrint=debugPrint)
        hgstat_print_distanace__kaggle_movies(SimDocInfo, WordDicts,
            FindInx, title_list, overview_list, release_date_list, genres_list,
            RankNum=RankNum, debugPrint=debugPrint, printShortFormat=printShortFormat)
    else:
        print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        print('# 1) 가중치 적용 안 함')
        print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        print('reco_type:', reco_type)
        SimDocInfo = hgstat_get_distance_by_inx__kagmov(WordDicts, FindInx)
        #=PrintSimDoc_CosDistance__ByInx(SimDocInfo, FindInx, RankNum=RankNum, debugPrint=debugPrint)
        hgstat_print_distanace__kaggle_movies(SimDocInfo, WordDicts,
            FindInx, title_list, overview_list, release_date_list, genres_list,
            RankNum=RankNum, debugPrint=debugPrint, printShortFormat=printShortFormat)

#===============================
#===============================

#================================
#================================
def PrintSimDoc_CosDistance__ByInx(DocDis_sort, FindInx, 
    WordDicts, 
    metadataId_list, links, title_list, release_date_list, genres_list, overview_list,
    RankNum=10, 
    PrintEditMode=False, # 편집용 출력(True)
    debugPrint=False):
    #
    from hgbasic import PrintDictList_ByLine
    from hgwordlist import PrintWordDictList

    print('==========================================================')
    print('==========================================================')
    print('==========================================================')
    #-----------------
    # 정렬된 내용을 출력
    #-----------------
    print_CosDistances = True
    print_CosDistances = False
    printNum = 0 # 모두 순위 출력
    if(RankNum > 0):
        printNum = RankNum
    if(print_CosDistances == True):
        PrintDictList_ByLine(DocDis_sort, Printnum=printNum)

    #-----------------------
    # 기본 정보 출력
    #-----------------------
    metadataId_Find = metadataId_list[FindInx]
    movieId_Find = hgstat_get_movieId_by_metadataId(metadataId_Find, links)

    #=print(f'<doc-inx({FindInx})> : {Filelist[FindInx]}')
    title = title_list[FindInx]
    release_date = release_date_list[FindInx]
    release_date = release_date[:4] # 앞에 4자리 [연도]만 사용
    Genre = genres_list[FindInx] 
    #=print(f'{Genre}')
    # [Genre]는 사전의 목록 형식의 문자열이므로 변환해야 한다.
    # format: [{'id': 16, 'name': 'Animation'}, {'id': 35, 'name': 'Comedy'}, {'id': 10751, 'name': 'Family'}]
    GenreListDict = list(eval(Genre)) # format: [{'id': 16, 'name': 'Animation'}, {'id': 35, 'name': 'Comedy'}, {'id': 10751, 'name': 'Family'}]
    GenreList_Base = [x['name'] for x in GenreListDict] # format: [{'id': 16, 'name': 'Animation'}, {'id': 35, 'name': 'Comedy'}, {'id': 10751, 'name': 'Family'}]
    GenreList_Base = set(GenreList_Base)

    print(f'{title}(movieId:{movieId_Find}) : [{release_date}] {GenreList_Base}')
    #=print(f'<doc-{FindInx}> :')

    #
    printStory = True
    printStory = False
    if(printStory == True):
        story = overview_list[FindInx]
        print(f'{story}')
        print()

    # 단어 목록 출력
    WordDict_base = WordDicts[FindInx]
    #---
    #=PrintWordDictList(WordDict_base, PrintingNum=30, 
    #=    PrintIndex=True, OneLine=False, SimpleFormat=True, SortFlag=True)
    #---
    #print(WordDict_base)
    #---
    word_list_some = [wdic_i['word'] for wdic_i in WordDict_base]
    print(f'{len(word_list_some)} 단어: ', word_list_some)
    print()
    if(debugPrint == True):
        print(f'{len(word_list_some)} 단어: ', *word_list_some, sep=', ')
        print()

    #------------------
    #------------------
    #------------------
    if(PrintEditMode == False): # 편집용 출력(True)
        print('#-------------')
        print('# 추천 목록: (간편 출력)')
        print('#-------------')
        print(f"순위: (영화ID) 영화 제목 <코사인 거리(텍스트 거리)> [발표] (공통/전체){{공통 단어}}")
        simcnt = 0
        for DocDis_i in DocDis_sort:
            doc_inx = DocDis_i['inx']
            if(FindInx == doc_inx): # 검사하는 문서와 같을 경우(자기 자신은 제외)
                continue
            #
            metadataId = metadataId_list[doc_inx]
            movieId = hgstat_get_movieId_by_metadataId(metadataId, links)

            distance = DocDis_i['distance']
            #=GenreList = DocDis_i['genres'] # 밖에서 텍스트 유사도만 검사했기 때문에 장르는 없다.
            #=GenreDistance = DocDis_i['GenreDistance'] # 밖에서 텍스트 유사도만 검사했기 때문에 무조건 1

            title = title_list[doc_inx]
            release_date = release_date_list[doc_inx]
            release_date = release_date[:4] # 앞에 4자리 [연도]만 사용

            #=print(f'[{simcnt}] similar file: {Filelist[doc_inx]}')
            print(f'{simcnt+1}: [{movieId}] {title} ', end='')
            print(f'<%.3f> ' %(distance), end='')
            print(f'[{release_date}] ', end='')
            
            # 밖에서 텍스트 유사도만 검사했기 때문에 장르는 없다.
            #=if(len(GenreList) > 0):
            #=    print(f"{GenreDistance}\t{GenreList}")
            #=else:
            #=    print(f"{GenreDistance}\t{GenreList}")
            
            # 공통 단어수 / 전체 단어수
            WordDict_comp = WordDicts[doc_inx]
            wordset_base = set([word_i['word'] for word_i in WordDict_base])
            wordset_comp = set([word_i['word'] for word_i in WordDict_comp])
            wordset_common = wordset_base.intersection(wordset_comp)
            #=print(f'({len(wordset_common)}){wordset_common}')
            print(f'({len(wordset_common)} / {len(wordset_comp)})', end='')
            print(f'{wordset_common}')

            #
            simcnt += 1
            if simcnt >= printNum:
                break
    else:
        #-----------------------
        # 가장 가까운 문서를 출력해본다.
        #-----------------------
        print('# 추천 목록: (편집 코드)')
        print(f"순위\t영화 제목\t영화ID\t코사인 거리(텍스트 거리)\t발표\t공통 단어수\t전체 단어수\t공통 단어 목록")
        simcnt = 0
        for DocDis_i in DocDis_sort:
            doc_inx = DocDis_i['inx']
            if(FindInx == doc_inx): # 검사하는 문서와 같을 경우(자기 자신은 제외)
                continue
            #
            metadataId = metadataId_list[doc_inx]
            movieId = hgstat_get_movieId_by_metadataId(metadataId, links)

            distance = DocDis_i['distance']
            #=GenreList = DocDis_i['genres'] # 밖에서 텍스트 유사도만 검사했기 때문에 장르는 없다.
            #=GenreDistance = DocDis_i['GenreDistance'] # 밖에서 텍스트 유사도만 검사했기 때문에 무조건 1

            title = title_list[doc_inx]
            release_date = release_date_list[doc_inx]
            release_date = release_date[:4] # 앞에 4자리 [연도]만 사용

            #=print(f'[{simcnt}] similar file: {Filelist[doc_inx]}')
            print(f'{simcnt+1}\t{title}\t{movieId}\t', end='')
            print(f'%.3f\t' %(distance), end='')
            print(f'{release_date}\t', end='')
            
            # 밖에서 텍스트 유사도만 검사했기 때문에 장르는 없다.
            #=if(len(GenreList) > 0):
            #=    print(f"{GenreDistance}\t{GenreList}")
            #=else:
            #=    print(f"{GenreDistance}\t{GenreList}")
            
            # 공통 단어수/전체 단어수
            WordDict_comp = WordDicts[doc_inx]
            wordset_base = set([word_i['word'] for word_i in WordDict_base])
            wordset_comp = set([word_i['word'] for word_i in WordDict_comp])
            wordset_common = wordset_base.intersection(wordset_comp)
            print(f'{len(wordset_common)}\t', end='')
            print(f'{len(wordset_comp)}\t', end='')
            print(wordset_common)

            if(debugPrint == True):
                story = overview_list[doc_inx]
                print(f'{story}')

                word_dict_i = WordDicts[doc_inx]
                word_dict_some = word_dict_i[:30]
                word_list_some = [wdic_i['word'] for wdic_i in word_dict_some]
                print(word_list_some)
                print()
            #
            simcnt += 1
            if simcnt >= printNum:
                break

    if(debugPrint == True):
        # 검색 기준 문서의 단어 목록 전체 출력
        PrintWordDictList(WordDicts[FindInx], PrintingNum=0, PrintIndex=True, OneLine=True, SortFlag=True)


#================================
#================================
class HGTest(TestCase):
    def test_fun(self):
        hgsysinc._print_function_name_(3)
        from hgeng_spell_rule import stoplist_eng_raw_min1

        #
        print()

        print('stoplist:', len(stoplist_eng_raw_min1)) # 편집 코드
        
#---------------------
#---------------------
if __name__ == '__main__':
    main()

