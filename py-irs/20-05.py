import hgsysinc
from hgstat_test_movie import print_rvalue_movie__ratings_dict_by_movieId
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
#----------------
ModifyTilteYear = True # 'title'을 정확하게 찾으려면 이렇게 호출
# 'Toy Story (1995)' --> 'Toy Story'와 '(1995)'로 분리

title_dict, genres_dict_, movies_ = \
    hgstat_dicts_movielens(ModifyTilteYear=ModifyTilteYear)
print('title_dict:', len(title_dict))
#=print(f'genres_dict [{len(genres_dict_)}]:')
#---------------
#---------------
print('# {영화ID}로 영화 정보 출력하기(상관계수 높은 순서로 )')
movieId = 1 # {Toy Story}
print_rvalue_movie__ratings_dict_by_movieId(movieId, 
    movieIdList, userIdList, movie_ratings_dict, title_dict=title_dict, 
    PrintNum = 10, # 어떤 영화는 목록이 50개 정도 필요하다. (10개는 부족)
    debugPrint=False, ProcMod=2500)
   

'''
처리 결과:
=============================================
title_dict: 9742
# {영화ID}로 영화 정보 출력하기(상관계수 높은 순서로 )
... 0.00
... 25.71
... 51.42
... 77.13
(1) Toy Story (1995): 상관계수에 의한 영화 추천
순서    영화ID  상관계수        고객수  평점 평균       영화 이름
1       3114    0.462   97      3.861   Toy Story 2 (1999)
2       1265    0.362   143     3.944   Groundhog Day (1993)
3       780     0.358   202     3.446   Independence Day (a.k.a. ID4) (1996)   
4       1073    0.357   119     3.874   Willy Wonka & the Chocolate Factory (1971)
5       648     0.353   162     3.537   Mission: Impossible (1996)
6       788     0.350   82      2.732   Nutty Professor, The (1996)
7       2355    0.345   92      3.516   Bug's Life, A (1998)
8       364     0.344   172     3.942   Lion King, The (1994)
9       34      0.341   128     3.652   Babe (1995)
10      4886    0.331   132     3.871   Monsters, Inc. (2001)


'''
