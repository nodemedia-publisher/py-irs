import hgsysinc
from hgstat_test_movie import (
    hgstat_get_similarity_movie_by_movieId,
    hgstat_print_similarity_movie,
    get_GenresRawMode_name,
)
from hgstat_test_movielens import (
    hgstat_dicts_movielens,
    hgstat_ratings_dict__movlens,
)
#---------------------------
# {영화}를 기준으로 {사용자, 평점} 목록으로 읽는다.
#---------------------------
UserBase=False # {ratings_dict} 읽을 때 {영화}를 기준으로 {사용자, 평점} 목록으로 처리
movie_ratings_dict, userIdList, movieIdList = \
    hgstat_ratings_dict__movlens(UserBase=UserBase)

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

#---
#=printShortFormat=True  # 간단하게 1줄로 출력(True:예)
#=GenresRawMode=True # 포함 일치
GenresRawMode = False # 완전 일치

movieId = 1 # 첫 번째 영화() #= 1: Toy Story

print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
print(f'영화 [{movieId}] +<장르> 유사도 적용({get_GenresRawMode_name(GenresRawMode)}) ')
print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
MovieSimilarity = hgstat_get_similarity_movie_by_movieId(
    movieId, movieIdList, userIdList, movie_ratings_dict, 
    title_dict = title_dict, 
    genres_dict=genres_dict, GenresRawMode=GenresRawMode, 
    ProcMod=2500)
hgstat_print_similarity_movie(MovieSimilarity, 
    movieId, title_dict, genres_dict, printShortFormat=True)



'''

이번에는 {평점} 가중치를 추가한 것이다.

=============================================

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
영화 [1] +<장르> 유사도 적용(장르 완전 일치) 
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
... 0.00
... 25.71
... 51.42
... 77.13
==========================================================
==========================================================
==========================================================
<1> : Toy Story (1995)
Genre: {'Animation', 'Fantasy', 'Adventure', 'Comedy', 'Children'}

순서	movieId	similarity	r-value	genre_sim	title
1	 3114	0.693	0.462	0.231		 Toy Story 2 (1999)
2	 4886	0.562	0.331	0.231		 Monsters, Inc. (2001)
3	 78499	0.547	0.316	0.231		 Toy Story 3 (2010)
4	 2355	0.530	0.345	0.185		 Bug's Life, A (1998)
5	 4306	0.521	0.329	0.192		 Shrek (2001)
6	 2294	0.495	0.264	0.231		 Antz (1998)
7	 673	0.479	0.286	0.192		 Space Jam (1996)
8	 6377	0.478	0.293	0.185		 Finding Nemo (2003)
9	 2054	0.476	0.329	0.148		 Honey, I Shrunk the Kids (1989)
10	 588	0.464	0.317	0.148		 Aladdin (1992)


'''
