import hgsysinc
from hgstat_test_movie import (
    hgstat_get_similarity_movie_by_movieId,
    hgstat_print_similarity_movie,
)
from hgstat_test_movielens import (
    hgstat_dicts_movielens,
    hgstat_ratings_dict__movlens,
)
#---------------------------
# 시작 연도를 제한하는 변수
#---------------------------
CutYearBelow = None # 시작 연도를 제한하지 않음.
#=CutYearBelow = 2015 # 2015년 이전(2014년 까지)은 사용하지 않는다.
#---------------------------
# {영화}를 기준으로 {사용자, 평점} 목록으로 읽는다.
#---------------------------
UserBase=False # {ratings_dict} 읽을 때 {영화}를 기준으로 {사용자, 평점} 목록으로 처리
movie_ratings_dict, userIdList, movieIdList = \
    hgstat_ratings_dict__movlens(UserBase=UserBase, CutYearBelow=CutYearBelow)

#======================
#======================
#=movieId = 1 # 첫 번째 영화() #= 1: Toy Story
#=movieId = 2 # 두 번째 영화() #= 2: Jumanji
#=movieId = 48 # Pocahontas (1995)
#=movieId = 364 # Lion King, The (1994)
#=movieId = 588 # Aladdin (1992)
#=movieId = 720 # Wallace & Gromit: The Best of Aardman Animation (1996)
#=movieId = 6377 # Finding Nemo
#=movieId = 356 # Forrest Gump (1994) <=== Pulp Fiction (1994)만 일치하고 나머지 어색
#=movieId = 648 # Mission: Impossible (1996) <=== 시리즈(콜렉션) 적용하지 않으면 매우 어색

#---------------------------
#----- 장르 완전 일치
#---------------------------
#--- (장르 완전 일치)를 적용하려면 장르에서 'IMAX'를 지우는 것이 좋다.
ModifyTilteYear = True # 'title'을 정확하게 찾으려면 이렇게 호출    
# 'Toy Story (1995)' --> 'Toy Story'와 '1995'로 분리

title_dict, genres_dict, movies_ = hgstat_dicts_movielens \
                (ModifyTilteYear=ModifyTilteYear, imax_exc=True)

#
from hgstat_test_kagmov import hgstat_collection_dict__kagmov
belong_to_collection_dict, collection_dict = hgstat_collection_dict__kagmov()

#
movieId = 648 # Mission: Impossible (1996) <= 시리즈(콜렉션) 적용하지 않으면 매우 어색

print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
print(f'# 영화 [{movieId}] +<장르+컬렉션> ')
print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
MovieSimilarity = hgstat_get_similarity_movie_by_movieId(
    movieId, movieIdList, userIdList, movie_ratings_dict, title_dict, 
    genres_dict=genres_dict, belong_to_collection_dict=belong_to_collection_dict,
    ProcMod=2500)

RankNum = 20 # 'Mission: Impossible(id:648)' 시리즈 출력 위해 20개로 늘림 
hgstat_print_similarity_movie(MovieSimilarity, movieId, title_dict, genres_dict, 
    belong_to_collection_dict=belong_to_collection_dict, RankNum=RankNum, 
    printShortFormat=True, # 간편 형식으로 출력
)


'''
처리 결과:

이 번에는 {평점} 가중치 + {장르} 가중치를 추가한 것이다.

==================

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# 영화 [648] +<장르+컬렉션> 
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
... 0.00
... 25.71
... 51.42
... 77.13
==========================================================
==========================================================
==========================================================
<648> : Mission: Impossible (1996)
Collection: Mission: Impossible Collection
Genre: {'Thriller', 'Adventure', 'Action', 'Mystery'}

순서	movieId	similarity	r-value	genre_sim	belong_to_collection	title
1	 45186	1.077	0.313	0.208	Mission: Impossible Collection	 0.556		 Mission: Impossible III (2006)
2	 3623	1.052	0.288	0.208	Mission: Impossible Collection	 0.556		 Mission: Impossible II (2000)
3	 91630	0.952	0.188	0.208	Mission: Impossible Collection	 0.556		 Mission: Impossible - Ghost Protocol (2011)
4	 111781	0.844	0.079	0.208	Mission: Impossible Collection	 0.556		 Mission: Impossible - Rogue Nation (2015)
5	 780	0.712	0.556	0.156	0.000		 Independence Day (a.k.a. ID4) (1996)
6	 733	0.656	0.447	0.208	0.000		 Rock, The (1996)
7	 736	0.635	0.478	0.156	0.000		 Twister (1996)
8	 10	0.629	0.420	0.208	0.000		 GoldenEye (1995)
9	 480	0.576	0.419	0.156	0.000		 Jurassic Park (1993)
10	 95	0.574	0.366	0.208	0.000		 Broken Arrow (1996)
11	 1552	0.560	0.352	0.208	0.000		 Con Air (1997)
12	 1370	0.544	0.336	0.208	0.000		 Die Hard 2 (1990)
13	 1722	0.541	0.333	0.208	0.000		 Tomorrow Never Dies (1997)
14	 494	0.539	0.330	0.208	0.000		 Executive Decision (1996)
15	 377	0.481	0.389	0.093	0.000		 Speed (1994)
16	 786	0.477	0.385	0.093	0.000		 Eraser (1996)
17	 3082	0.474	0.266	0.208	0.000		 World Is Not Enough, The (1999)
18	 2989	0.472	0.263	0.208	0.000		 For Your Eyes Only (1981)
19	 1610	0.471	0.262	0.208	0.000		 Hunt for Red October, The (1990)
20	 2949	0.469	0.261	0.208	0.000		 Dr. No (1962)



'''
