import hgsysinc
from hgstat_test_movie import check_rvalue__ratings_dict_by_Id
from hgstat_test_movielens import hgstat_ratings_dict__movlens
#---------------------------
# {영화}를 기준으로 {사용자, 평점} 목록으로 읽는다.
#---------------------------
UserBase=False # {ratings_dict} 읽을 때 {영화}를 기준으로 {사용자, 평점} 목록으로 처리
movie_ratings_dict, userIdList, movieIdList = \
    hgstat_ratings_dict__movlens(UserBase=UserBase)
print(f'ratings_dict: {len(movie_ratings_dict)}')
#---------------
#---------------
print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
print('@@@ 영화ID(movieId) ')
print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
# 데이터 목록에서 'Toy Story' 제외한 나머지 상관계수 계산
movieId = movieIdList[0] # movieIdList[0]('Toy Story')
check_rvalue__ratings_dict_by_Id(movieId, userIdList, movie_ratings_dict, 
    ProcMod=2500) # ProcMod=2500: 2500번마다 상태 출력


'''
처리 결과: 
=============================================
ratings_dict: 9724
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@ 영화ID(movieId)
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
ID: 1, 상관계수 계산
... 0.00
... 25.71
... 51.42
... 77.13
rvalue_list (by r-value order):
순서    ID      상관계수
1       3114    0.462
2       1265    0.362
3       780     0.358
4       1073    0.357
5       648     0.353
6       788     0.350
7       2355    0.345
8       364     0.344
9       34      0.341
10      4886    0.331
11      1270    0.330
12      4306    0.329
13      2054    0.329
14      480     0.328
15      1210    0.323
16      1136    0.322
17      588     0.317
18      595     0.316
19      78499   0.316
20      1291    0.315
21      2115    0.309
22      1580    0.309
23      260     0.304
24      367     0.304
25      2716    0.303
26      1517    0.300
27      2081    0.298
28      1307    0.297
29      2918    0.296
30      1028    0.295

상관계수 최댓값:[keyId:3114] 0.4618
상관계수 최솟값:[keyId:55908] -0.0811


'''
