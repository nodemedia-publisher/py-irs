import hgsysinc
from hgstat_test_movielens import hgstat_ratings_movielens
#---------------
# format: ratings
#---------------
# userId,movieId,rating,timestamp
# 1,1,4.0,964982703
# 1,3,4.0,964981247
# 1,6,4.0,964982224
#---------------
ratings = hgstat_ratings_movielens() # movielens 평점 데이터 읽어오기 
print(ratings)


'''
처리 결과:
==================
        userId  movieId  rating   timestamp
0            1        1     4.0   964982703
1            1        3     4.0   964981247
2            1        6     4.0   964982224
3            1       47     5.0   964983815
4            1       50     5.0   964982931
...        ...      ...     ...         ...
100831     610   166534     4.0  1493848402
100832     610   168248     5.0  1493850091
100833     610   168250     5.0  1494273047
100834     610   168252     5.0  1493846352
100835     610   170875     3.0  1493846415

[100836 rows x 4 columns]

'''
