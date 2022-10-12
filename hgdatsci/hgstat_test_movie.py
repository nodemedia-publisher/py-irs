#---
#---
from unittest import TestCase, main
#=from math import nan
#=from numpy.core.numeric import NaN
from numpy.lib.function_base import average

import hgsysinc
from hgstat import hgCoefficient_low

from hgstat_test import find_reco__id_list

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

#=================================
#=================================
def hgstat_ratings_dict__ratings(ratings, UserBase=True, CutYearBelow=None):
    #---------------
    # format: ratings
    #---------------
    # userId,movieId,rating,timestamp
    # 1,1,4.0,964982703
    # 1,3,4.0,964981247
    # 1,6,4.0,964982224
    #---------------
    ratings_dict = {}
    userIdList = []
    movieIdList = []

    list_num = len(ratings)
    for i in range(list_num):
        #=print(f"ratings_i ({len(ratings.iloc[i])}): {ratings.iloc[i]}")
        userId = ratings.iloc[i, 0]
        movieId = ratings.iloc[i, 1]
        rating_val = ratings.iloc[i, 2]
        time_val = None
        if(len(ratings.iloc[i]) > 3):
            time_val = ratings.iloc[i, 3]
        
        #
        if(CutYearBelow != None): # 지정 연도보다 과거는 등록하지 않는다.
            if(time_val != None):
                from datetime import datetime
            
                #=time_val = 845553938 # fromtimestamp(845553938) ==> 1996-10-17 21:05:38
                datetime_v  = datetime.fromtimestamp(time_val)
                #=print(f'{i+1} {datetime_v.year}: {datetime_v}')
                time_val = int(datetime_v.year) # 연도만 사용
                if(time_val < CutYearBelow):
                    continue

        #
        if(UserBase == True): # key:userId
            #---------------
            # userId 기준(키)으로 (movieId, 평점) 목록 생성
            # ratings_dict format: {'userId': [(movieId, rating_value), (),...]}
            #---------------
            # {
            # 1: [(31, 2.5), (1029, 3.0), (1061, 3.0), ... , 
            # 2: [(10, 4.0), (17, 5.0), (39, 5.0), (47, 4.0), ... , 
            # 3: [(60, 3.0), (110, 4.0), (247, 3.5), (267, 3.0), ... , 
            # }
            #---------------
            if(userId in ratings_dict):
                value = ratings_dict[userId]
            else:
                value = []
                ratings_dict[userId] = value
            value.append((movieId, rating_val)) # (movieId, rating_val)
        else: # key:movieId
            #---------------
            # movieId 기준(키)으로 (userId, 평점) 목록 생성
            # ratings_dict format: {'movieId': [(userId, rating_value), (),...]}
            #---------------
            # {
            # 1: [(31, 2.5), (1029, 3.0), (1061, 3.0), ... , 
            # 2: [(10, 4.0), (17, 5.0), (39, 5.0), (47, 4.0), ... , 
            # 3: [(60, 3.0), (110, 4.0), (247, 3.5), (267, 3.0), ... , 
            # }
            #---------------
            if(movieId in ratings_dict):
                value = ratings_dict[movieId]
            else:
                value = []
                ratings_dict[movieId] = value
            value.append((userId, rating_val)) # (userId, rating_val)
        #
        if(userId not in userIdList):
            userIdList.append(userId) # 사용자 목록에 사용자 추가
        #
        if(movieId not in movieIdList):
            movieIdList.append(movieId) # 영화 목록에 영화 추가

    # sort: userIdList, movieIdList
    userIdList.sort()
    movieIdList.sort()
    # (UserBase:False)일 경우 {key:movieId}로 정렬을 다시 해줘야 한다.
    # (UserBase:True)일 경우에는 정렬할 필요가 없지만 
    # 데이터가 반드시 순서대로 구성된다는 보장이 없으므로 무조건 정렬하는 것이 안전하다.
    ratings_dict_sort = sorted(ratings_dict.items()) 
    #=ratings_dict = {key:val for key, val in ratings_dict_sort}
    ratings_dict = dict(ratings_dict_sort)

    #
    return ratings_dict, userIdList, movieIdList

def hgstat_time_dict__ratings(ratings, UserBase=True, TimeYearMode=True, CutYearBelow=None):
    #---------------
    from datetime import datetime

    #---------------
    # format: ratings
    #---------------
    # userId,movieId,rating,timestamp
    # 1,1,4.0,964982703
    # 1,3,4.0,964981247
    # 1,6,4.0,964982224
    #---------------
    time_dict = {}
    userIdList = []
    movieIdList = []

    list_num = len(ratings)
    for i in range(list_num):
        #=print(f"ratings_i: {ratings.iloc[i]}")
        userId = ratings.iloc[i, 0]
        movieId = ratings.iloc[i, 1]
        #=rating_val = ratings.iloc[i, 2]
        time_val = ratings.iloc[i, 3]

        if(TimeYearMode == True): # 연도만 사용
            #=time_val = 845553938 # fromtimestamp(845553938) ==> 1996-10-17 21:05:38
            datetime_v  = datetime.fromtimestamp(time_val)
            #=print(f'{i+1} {datetime_v.year}: {datetime_v}')
            time_val = int(datetime_v.year) # 연도만 사용

            #
            if(CutYearBelow != None): # 지정 연도보다 과거는 등록하지 않는다.
                if(time_val < CutYearBelow):
                    continue        
        #
        if(UserBase == True): # key:userId
            #---------------
            # userId 기준(키)으로 (movieId, 평점) 목록 생성
            # time_dict format: {'userId': [(movieId, time_value), (),...]}
            #---------------
            # {
            # 1: [(1, 2000), (5, 1996), (7, 2005), ... , 
            # }
            #---------------
            if(userId in time_dict):
                value = time_dict[userId]
            else:
                value = []
                time_dict[userId] = value
            value.append((movieId, time_val)) # (movieId, time_val)
        else: # key:movieId
            #---------------
            # movieId 기준(키)으로 (userId, 평점) 목록 생성
            # time_dict format: {'movieId': [(userId, time_value), (),...]}
            #---------------
            # {
            # 1: [(1, 2000), (5, 1996), (7, 2005), ... , 
            # }
            if(movieId in time_dict):
                value = time_dict[movieId]
            else:
                value = []
                time_dict[movieId] = value
            value.append((userId, time_val)) # (userId, time_val)
        #
        if(userId not in userIdList):
            userIdList.append(userId) # 사용자 목록에 사용자 추가
        #
        if(movieId not in movieIdList):
            movieIdList.append(movieId) # 영화 목록에 영화 추가

    # sort: userIdList, movieIdList
    userIdList.sort()
    movieIdList.sort()
    # (UserBase:False)일 경우 {key:movieId}로 정렬을 다시 해줘야 한다.
    # (UserBase:True)일 경우에는 정렬할 필요가 없지만 
    # 데이터가 반드시 순서대로 구성된다는 보장이 없으므로 무조건 정렬하는 것이 안전하다.
    time_dict_sort = sorted(time_dict.items()) 
    time_dict = {key:val for key, val in time_dict_sort}

    #
    return time_dict, userIdList, movieIdList

def hgstat_print_ratings_dict(ratings_dict, prt_begin = 0, prt_num = 0, UserBase=True):
    print(),print(),
    print(f'ratings_dict: {len(ratings_dict)}')
    if(UserBase==True):
        print("index\t고객ID\t영화수\t영화 평점 목록(영화ID, 평점)")
        #-----
        # ratings_dict format: {'userId': [(movieId, rating_value), (),...]}
        #-----
        for i, userId in enumerate(ratings_dict):
            if((prt_begin > 0) and (i < prt_begin)):
                continue
            #
            user_ratings_list = ratings_dict[userId]
            print(f"{i}\t{userId}\t{len(user_ratings_list)}\t{user_ratings_list}")
            #
            if((prt_num > 0) and (i >= (prt_begin + prt_num -1))):
                break
    else:
        print("index\t영화ID\t영화수\t영화 평점 목록(고객ID, 평점)")
        #-----
        # ratings_dict format: {'movieId': [(userId, rating_value), (),...]}
        #-----
        for i, movieId in enumerate(ratings_dict):
            if((prt_begin > 0) and (i < prt_begin)):
                continue
            #
            movie_ratings_list = ratings_dict[movieId]
            print(f"{i}\t{movieId}\t{len(movie_ratings_list)}\t{movie_ratings_list}")
            #
            if((prt_num > 0) and (i >= (prt_begin + prt_num -1))):
                break

def hgstat_ratings_list__ratings_dict(ratings_dict, keyId):
    #-----
    # ratings_dict format1: {'userId': [(movieId, rating_value), (),...]}
    # ratings_dict format2: {'movieId': [(userId, rating_value), (),...]}
    #-----
    user_ratings_list = ratings_dict[keyId]
    #=print(f"{keyId} {len(user_ratings_list)} :{user_ratings_list}")

    cur_ratings_list = [rtuple[1] for rtuple in user_ratings_list]
    #-print(f'cur_ratings_list({len(cur_ratings_list)}):', cur_ratings_list)
    return cur_ratings_list

def hgstat_movie_list__ratings_dict(ratings_dict, keyId):
    #-----
    # ratings_dict format1: {'userId': [(movieId, rating_value), (),...]}
    # ratings_dict format2: {'movieId': [(userId, rating_value), (),...]}
    #-----
    keyId_ratings_list = ratings_dict[keyId]
    #=print(f"{keyId} {len(keyId_ratings_list)} :{keyId_ratings_list}")

    ratings_id_list = [rtuple[0] for rtuple in keyId_ratings_list]
    #-print(f'ratings_id_list({len(ratings_id_list)}):', ratings_id_list)
    return ratings_id_list

def hgstat_print_ratings_dict_summary(ratings_dict, prt_begin = 0, prt_num = 0):
    print(),print(),
    print(f'ratings_dict: {len(ratings_dict)}')
    #-----
    # ratings_dict format0: {'keyId': [(valueId, rating_value), (),...]}
    # ratings_dict format1: {'userId': [(movieId, rating_value), (),...]}
    # ratings_dict format2: {'movieId': [(userId, rating_value), (),...]}
    #-----
    ratings_lists = []
    ratings_count_lists = []
    for i, keyId in enumerate(ratings_dict):
        if(prt_begin > 0):
            if(i < prt_begin):
                continue
        #
        cur_ratings_list = hgstat_ratings_list__ratings_dict(ratings_dict, keyId)
        ratings_lists.append(cur_ratings_list)
        ratings_count_lists.append(len(cur_ratings_list))
        
        #
        if(prt_num > 0):
            if(i >= (prt_begin + prt_num -1)):
                break
    #
    stat_max = max(ratings_count_lists)
    stat_min = min(ratings_count_lists)
    stat_avg = average(ratings_count_lists)

    #
    print()
    print('통계 요약')
    print('max rating num:', stat_max)
    print('min rating num:', stat_min)
    print('average rating num: %.3f' %stat_avg)

    return ratings_lists, ratings_count_lists, stat_max, stat_min, stat_avg

def hgstat_comp_rating_id_list__ratings_dict_by_keyId(ratings_dict, keyId_b, keyId_c,
    debugPrint=False):
    # {keyId: userId or movieId}
    #
    rating_id_list_b = hgstat_movie_list__ratings_dict(ratings_dict, keyId_b)
    rating_id_list_c = hgstat_movie_list__ratings_dict(ratings_dict, keyId_c)
    if(debugPrint == True):
        print(), print()
        print('#---------------')
        print('# 평점 목록 비교')
        print(f"{keyId_b} : {len(rating_id_list_b)}")
        print(f"{keyId_c} : {len(rating_id_list_c)}")
        print(f"{keyId_b} ^ {keyId_c}")
        print('#---------------')

    #
    rating_id_list_b_set = set(rating_id_list_b)
    rating_id_list_c_set = set(rating_id_list_c)

    movie_common = rating_id_list_c_set.intersection(rating_id_list_b_set)
    movie_common_list = list(movie_common)
    movie_common_list.sort()

    if(debugPrint == True):
        print(), print()
        print(f"common ({len(movie_common_list)}):")
        print(f"{movie_common_list}")

    #
    movie_only_c = rating_id_list_c_set.difference(rating_id_list_b_set)
    movie_only_list_2 = list(movie_only_c)
    movie_only_list_2.sort()

    if(debugPrint == True):
        print(), print()
        print(f"movie_only_list_2 ({len(movie_only_list_2)}):")
        print(f"{movie_only_list_2}")

    #
    movie_only_b = rating_id_list_b_set.difference(rating_id_list_c_set)
    movie_only_list_1 = list(movie_only_b)
    movie_only_list_1.sort()

    if(debugPrint == True):
        print(), print()
        print(f"movie_only_list_1 ({len(movie_only_list_1)}):")
        print(f"{movie_only_list_1}")

    #
    return movie_common_list, movie_only_list_1, movie_only_list_2

def hgstat_avg_rating__ratings_dict_by_movieId(movieId, ratings_dict):
    ratings_tuple_list = ratings_dict[movieId]
    ratings_list = [ratings_tuple[1] for ratings_tuple in ratings_tuple_list]
    avg_rating = average(ratings_list)
    #=print(f'movieId [{movieId}] avg_rating: {avg_rating}')
    return avg_rating

def hgstat_avg_rating_dict__ratings_dict(ratings_dict):
    avg_ratings_dict = {}
    for movieId in ratings_dict:
        #=ratings_tuple_list = ratings_dict[movieId]
        avg_rating = hgstat_avg_rating__ratings_dict_by_movieId(movieId, ratings_dict)
        avg_ratings_dict[movieId] = avg_rating
    return avg_ratings_dict

def hgstat_count_rating_dict__ratings_dict(ratings_dict):
    count_ratings_dict = {}
    for ri, movieId in enumerate(ratings_dict):
        ratings_tuple_list = ratings_dict[movieId]
        count_ratings_dict[movieId] = len(ratings_tuple_list)
    return count_ratings_dict

def get_rvalue__ratings_dict_by_Id(keyId, ratingIdList, ratings_dict, 
    debugPrint=False, ProcMod=0): 
    if(debugPrint == True):
        hgsysinc._print_function_name_(3)

    #---------------------
    #---------------------
    # {keyId}에 대한 평점 벡터 구하기
    ratings_tuple_list = ratings_dict[keyId]
    ratings_vector = hgstat_vector__ratings_dict(ratings_tuple_list, ratingIdList)

    #-------------------------------
    # 아래 방식은 사용하지 않는다.
    # 목록의 일부를 지우면 다른 곳에서 index 순서가 달라져서 
    # 논리적인 일관성이 없어진다. 삭제된 상태를 감안해서 
    # {keyId_inx}를 재계산하여 출력하면 문제가 없지만 
    # 여기서 출력된 {keyId_inx}값은
    # 원래 {keyId_inx}값과는 다르기 때문에 논리적인 혼선이 발생한다.
    # 이러한 혼선이 발생하지 않도록 아래 방법은 사용하지 않고
    # 대신에 hgRValue_Lists() 출력 결과에서 {keyId_inx} 부분을 
    # 제외시킨다. 그러면 이 함수에서 출력된 {keyId_inx} 것이 
    # 외부에서 출력된 것과 논리적으로 일치한다.
    #-------------------------------
    #=# 지정한 고객keyId를 제외한 나머지로 데이터 목록을 구성
    #=#=print(f'ratings_dict ({len(ratings_dict)}):')
    #=#=print(f'keyIdList ({len(keyIdList)}):')
    #=keyId_inx = keyIdList.index(keyId)
    #=ratings_dict.remove(keyId, baselist)
    #=keyIdList.remove(keyId)
    #=#=print(f'ratings_dict ({len(ratings_dict)}):') # 삭제되었나 확인
    #=#=print(f'keyIdList ({len(keyIdList)}):') # 삭제되었나 확인
    #-------------------------------

    #---------------------
    #---------------------
    if(debugPrint == True):
        print(f'ID: {keyId}, 상관계수 계산')
    # {keyId}의 {평점 벡터}로 전체 평점 데이터와의 상관계수 구하기
    rvalue_list = hgstat_RValueLists__ratings_dict(ratings_vector, 
                    ratings_dict, ratingIdList, ProcMod=ProcMod) # ProcMod=50: 50번마다 상태 출력
    if(len(rvalue_list) <= 0):
        return rvalue_list
    if(debugPrint == True):
        print(rvalue_list)
        print()

    #---------------------
    # 비교 대상에서 자기 자신을 삭제 # rvalue_list format: [(keyId, r-value),...]
    #---------------------
    rvalue_list_pure = [rv_tuple for rv_tuple in rvalue_list if rv_tuple[0] != keyId]
    #=print('rvalue_list_pure:', rvalue_list_pure)

    #
    if(debugPrint == True):
        # ratings_dict 없이 출력
        print_rvalue_list__ratings_dict(rvalue_list_pure, 
            ratingIdList, title='rvalue_list (by r-value order):') # ratings_dict 없이 출력
        #-----
        #=# ratings_dict 포함해서 출력({ratings_dict} 데이터가 많으면 화면을 꽉 채워서 함부로 호출하면 안 된다.)
        #=print_rvalue_list__ratings_dict(rvalue_list_pure, ratingIdList, ratings_dict,
        #-----

    #-------------------------------
    # 아래 방식은 사용하지 않는다.
    # 목록의 일부를 지우면 다른 곳에서 index 순서가 달라져서 
    # 논리적인 일관성이 없어진다. 삭제된 상태를 감안해서 
    # {keyId_inx}를 재계산하여 출력하면 문제가 없지만 
    # 여기서 출력된 {keyId_inx}값은
    # 원래 {keyId_inx}값과는 다르기 때문에 논리적인 혼선이 발생한다.
    # 이러한 혼선이 발생하지 않도록 아래 방법은 사용하지 않고
    # 대신에 hgRValue_Lists() 출력 결과에서 {keyId_inx} 부분을 
    # 제외시킨다. 그러면 이 함수에서 출력된 {keyId_inx} 것이 
    # 외부에서 출력된 것과 논리적으로 일치한다.
    #=#-------------------------------
    #=#---------------------
    #=#---------------------
    #=# 다음 작업을 위해서 삭제한 것을 데이터 목록을 삽입하여 복원
    #=ratings_dict.insert(keyId_inx, keyId, baselist)
    #=keyIdList.insert(keyId_inx, keyId)
    #-------------------------------

    #=rvalue_list_pure(rvalue_list) : 상관계수가 큰 값부터 정렬된 상태
    return rvalue_list_pure # rvalue_list_pure format: [(keyId, r-value),...]

def check_rvalue__ratings_dict_by_Id(keyId, ratingIdList, ratings_dict, 
    keyIdList=None,
    debugPrint=False, ProcMod=0): 
    if(debugPrint == True):
        hgsysinc._print_function_name_(3)

    #---------------------
    #---------------------
    print(f'ID: {keyId}, 상관계수 계산')
    rvalue_list = get_rvalue__ratings_dict_by_Id(keyId, ratingIdList, ratings_dict, 
        debugPrint=debugPrint, ProcMod=ProcMod)
    if(len(rvalue_list) <= 0):
        print(f'ID: {keyId}, 상관계수 계산 [결과 없음]')
        return

    #
    #=rvalue_list : 상관계수가 큰 값부터 정렬된 상태
    if(debugPrint == False): # get_rvalue__ratings_dict_by_Id()에서 출력하지 않았기 때문에 여기서 출력
        # ratings_dict 없이 출력
        print_rvalue_list__ratings_dict(rvalue_list, 
            ratingIdList, title='rvalue_list (by r-value order):') # ratings_dict 없이 출력
    if(debugPrint == True):
        # ratings_dict 포함해서 출력
        print_rvalue_list__ratings_dict(rvalue_list, ratingIdList, ratings_dict, title='rvalue_list (by r-value order):')

    # 아래에서 {inx} 순으로 정렬(sort)하기 전에 최댓값과 최솟값을 받아둔다.
    rvalue_list_max = rvalue_list[0]
    rvalue_list_min = rvalue_list[len(rvalue_list) - 1]

    if(debugPrint == True):
        # sort : inx 순으로 정렬(hgRValue_Lists()함수는 r_value[1] 큰 값 순서로 정렬된 상태)
        rvalue_list.sort(key=lambda x : x[0]) # {format: (keyId, r-value)}
        # ratings_dict 없이 출력
        print_rvalue_list__ratings_dict(rvalue_list, ratingIdList, title='rvalue_list (by keyId order):')
        # ratings_dict 포함해서 출력
        print_rvalue_list__ratings_dict(rvalue_list, ratingIdList, ratings_dict, title='rvalue_list (by keyId order):')

    max_keyId = rvalue_list_max[0] # format: (keyId, r-value)
    min_keyId = rvalue_list_min[0] # format: (keyId, r-value)
    print('상관계수 최댓값:[keyId:%i] %.4f' %(max_keyId, rvalue_list_max[1]))
    print('상관계수 최솟값:[keyId:%i] %.4f' %(min_keyId, rvalue_list_min[1]))

    if(debugPrint == True):
        if(keyIdList != None):
            max_keyId_inx = keyIdList.index(max_keyId)
            min_keyId_inx = keyIdList.index(min_keyId)
            print('상관계수 최댓값:[keyId_inx:%i] %.4f' %(max_keyId_inx, rvalue_list_max[1]))
            print('상관계수 최솟값:[keyId_inx:%i] %.4f' %(min_keyId_inx, rvalue_list_min[1]))
            '''
            try: # 캐글 데이터에서는 값이 없는 경우 있음
                max_keyId_inx = keyIdList.index(max_keyId)
            except ValueError: # raise ValueError: 3114 is not in list
                max_keyId_inx = None # 내용 없이 처리
            if(max_keyId_inx != None):
                print('상관계수 최댓값:[keyId_inx:%i] %.4f' %(max_keyId_inx, rvalue_list_max[1]))
            else:
                print('상관계수 최댓값:[keyId_inx: is not in list] [ID:%i]' %(max_keyId))

            try: # 캐글 데이터에서는 값이 없는 경우 있음
                min_keyId_inx = keyIdList.index(min_keyId)
            except ValueError: # raise ValueError: 3114 is not in list
                min_keyId_inx = None # 내용 없이 처리
            if(min_keyId_inx != None):
                print('상관계수 최솟값:[keyId_inx:%i] %.4f' %(min_keyId_inx, rvalue_list_min[1]))
            else:
                print('상관계수 최솟값:[keyId_inx: is not in list] [ID:%i]' %(min_keyId))
            '''

def print_avg_rating__ratings_dict_by_movieIds(movieIds, movie_ratings_dict):
    print('순서\t영화ID\t평점 평균')
    for li, movieId in enumerate(movieIds):
        avg_rating = hgstat_avg_rating__ratings_dict_by_movieId(movieId, movie_ratings_dict)
        print(f'{li+1}\t{movieId}\t', end='')
        print('%.3f' %avg_rating)
    print(), print(), 

def print_rvalue_list__ratings_dict(rvalue_list, IdList=None, ratings_dict=None, 
    PrintNum=30, title=None):
    if(title != None):
        print(title)
    print('순서\tID\t상관계수', end='')
    if(ratings_dict != None):
        print('\t항목수', end='')
        if(IdList != None):
            print('\t평점 리스트', end='')
    print()

    for ri, rvalue_tuple in enumerate(rvalue_list): # format: [(Id, r-value),...]
        Id = rvalue_tuple[0]
        r_value = rvalue_tuple[1]

        print(f'{ri+1}', end='')
        print(f'\t{Id}', end='')
        print(f'\t%.3f' %(r_value), end='')

        if(ratings_dict != None):
            ratings_tuple_list = ratings_dict[Id]
            item_num = len(ratings_tuple_list)
            print(f'\t{item_num}', end='')
            if(IdList != None):
                ratings_vector = hgstat_vector__ratings_dict(ratings_tuple_list, IdList)
                print(f'\t{ratings_vector}', end='')
        print()

        #
        if((ri + 1) >= PrintNum):
            break            
    print()

def hgstat_RValueLists__ratings_dict(base_ratings_vector, ratings_dict, IdList, 
    workNum=0, debugPrint=False, ProcMod=0):
    # 평점 사전으로부터 상관계수 목록 생성
    rvalue_list = []
    for i, keyId in enumerate(ratings_dict):
        ratings_tuple_list = ratings_dict[keyId]
        comp_ratings_vector = hgstat_vector__ratings_dict(ratings_tuple_list, IdList)
        r_value = hgCoefficient_low(base_ratings_vector, comp_ratings_vector, 
                                    debugPrint=debugPrint)
        if(debugPrint==True):
            #=print('anova:', anova)
            print(f'({i})[{keyId}] 상관계수(r): %.4f' % r_value)
        rvalue_list.append((keyId, r_value)) # format: (Id, r-value)
        #
        if(workNum > 0):
            if(i >= (workNum - 1)):
                break
        # 진행 상태 출력
        if(ProcMod > 0):
            modval = i % ProcMod
            if(modval == 0):
                perval = (i / len(ratings_dict)) * 100
                print('... %.2f' % perval)

    # 정렬: rvalue_list format [(Id, r_value),...]
    rvalue_list.sort(key=lambda r: -r[1]) # 튜플 2번째 값(r-value), 큰 값 순서로 정렬
    #
    return rvalue_list # format: [(Id, r-value), ...]

def hgstat_vector__ratings_dict(ratings_tuple_list, IdList):
    # 튜플로 된 평점 목록을 벡터화
    # {IdList}는 {userId}이거나 아니면 {movieId}
    IdList_num = len(IdList)
    ratings_vector = [0 for r in range(IdList_num)] # 개수만큼 생성

    for ratings_tuple in ratings_tuple_list:
        keyId = ratings_tuple[0]
        rating = float(ratings_tuple[1])

        keyIdId_inx = IdList.index(keyId)
        ratings_vector[keyIdId_inx] = rating
    #
    return ratings_vector

#===================================
#===================================
def hgstat_get_vote_count_max(vote_count_list):
    # 평점참여자 최댓값 구하기
    from numpy import isnan
    #=print()
    vote_count_max = 0
    for vc in vote_count_list:
        if(isinstance(vc, float)):
            if(isnan(vc)): # nan 검사
                continue

        if(vote_count_max < int(vc)):
            vote_count_max = int(vc)
    #=print('vote_count_max:', vote_count_max)
    return vote_count_max

#---------------------
#---------------------
def get_genres_distance_by_set2(GenreSet_Base, GenreSet_Comp, GenresRawMode=False):
    #----------
    # 장르 거리
    #----------
    #=GenreDistance = 0 # 거리는 작을수록 가깝고 장르 계산을 안했기 때문에 가장 가까운 거리 '0' 로 지정
    GenreDistance = 1 # 거리는 작을수록 가깝기 때문에 최대로 먼 거리 '1' 로 지정
    GenreIntersec = set()
    if((len(GenreSet_Comp) > 0) and (len(GenreSet_Base) > 0)):
        GenreIntersec = GenreSet_Comp.intersection(GenreSet_Base)
        if(GenresRawMode != False): # == True
            # 비교 대상의 장르가 기준보다 많을 경우에 
            # 장르는 기준과 비슷하지만 다른 장르를 포함하고 있기 때문에 
            # 더 어색한 것을 먼저 보여준다.
            GenreSet_BaseRate = len(GenreIntersec) / len(GenreSet_Base) # 공통된 장르의 비율
            GenreValRate = GenreSet_BaseRate
        else:
            # 완전 일치하는 비율
            GenreSet_CompRate = len(GenreIntersec) / len(GenreSet_Comp) # 공통된 장르의 비율
            GenreSet_BaseRate = len(GenreIntersec) / len(GenreSet_Base) # 공통된 장르의 비율
            GenreValRate = GenreSet_CompRate * GenreSet_BaseRate
        #
        GenreDistance -= GenreValRate
    # 
    return GenreDistance, GenreIntersec

#===============================
#===============================
def get_genres_similarity_by_set2(GenreSet_Base,GenreSet_Comp,GenresRawMode=False):
    #-----------
    # 장르 유사도 계산
    #-----------
    GenreSimilarity = 0 # 유사도가 클수록 비슷하기 때문에 최소 유사도 '0'으로 초기화
    GenreIntersec = set()
    if((len(GenreSet_Comp) > 0) and (len(GenreSet_Base) > 0)):
        GenreIntersec = GenreSet_Comp.intersection(GenreSet_Base)
        if(GenresRawMode == True): # 포함 일치
            #-----
            # 비교 대상의 장르가 기준보다 많을 경우에 
            # 장르는 기준(base)과 비슷하지만 다른 장르를 포함하고 있기 때문에 
            # 더 어색한 것을 먼저 보여준다.
            #-----
            # 공통 장르 비율
            GenreSet_BaseRate = len(GenreIntersec) / len(GenreSet_Base)# 공통 장르 비율
            GenreValRate = GenreSet_BaseRate
        else:
            # 완전 일치하는 비율
            GenreSet_CompRate = len(GenreIntersec) /len(GenreSet_Comp)#공통 장르 비율
            GenreSet_BaseRate = len(GenreIntersec) / len(GenreSet_Base)# 공통 장르 비율
            GenreValRate = GenreSet_CompRate * GenreSet_BaseRate
        #
        GenreSimilarity = GenreValRate
    #
    return GenreSimilarity, GenreIntersec

def hgstat_get_similarity_movie_by_movieId(movieId, movieIdList, userIdList, 
    movie_ratings_dict, title_dict=None, genres_dict=None, GenresRawMode=False, 
    debugPrint=False, ProcMod=2500,
    avg_ratings_dict=None, count_ratings_dict=None, rating_count_max=0, 
    belong_to_collection_dict=None):
    if(debugPrint == True):
        hgsysinc._print_function_name_(3)

    #
    if(debugPrint == True):
        print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
    #---------------------
    #---------------------
    if(debugPrint == True):
        print(f'[{movieId}] : 상관계수 계산')
    # 전체 평점 데이터를 대상으로 상관계수 측정
    rvalue_list = get_rvalue__ratings_dict_by_Id(movieId, userIdList, movie_ratings_dict, 
        debugPrint=debugPrint, ProcMod=ProcMod)
    if(len(rvalue_list) <= 0):
        return
    #=rvalue_list : 상관계수가 큰 값부터 정렬된 상태

    if(debugPrint == True):
        # ratings_dict 포함해서 출력
        print_rvalue_list__ratings_dict(rvalue_list, userIdList, movie_ratings_dict, title='rvalue_list (by r-value order):')

    if(debugPrint == True):
        # 
        rvalue_list_max = rvalue_list[0]
        rvalue_list_min = rvalue_list[len(rvalue_list) - 1]
        max_movieId = rvalue_list_max[0]
        min_movieId = rvalue_list_min[0]
        print('상관계수 최댓값:[movieId:%i] %.4f' %(max_movieId, rvalue_list_max[1]))
        print('상관계수 최솟값:[movieId:%i] %.4f' %(min_movieId, rvalue_list_min[1]))

        max_movieId_inx = movieIdList.index(max_movieId)
        min_movieId_inx = movieIdList.index(min_movieId)
        print('상관계수 최댓값:[movieId_inx:%i] %.4f' %(max_movieId_inx, rvalue_list_max[1]))
        print('상관계수 최솟값:[movieId_inx:%i] %.4f' %(min_movieId_inx, rvalue_list_min[1]))

    #---------------------
    #---------------------
    #
    GenreSet_Base = set()
    if(genres_dict != None):
        GenreSet_Base = set(genres_dict[movieId]) # 영화(movieId) 장르 집합
    
    CollectionName_Base = ''
    if(belong_to_collection_dict != None):
        CollectionName_Base = belong_to_collection_dict[movieId] # 영화(movieId) 시리즈

    r_value_max = 0 # 상관계수가 클수록 비슷하기 때문에 최솟값 '0'으로 초기화
    MovieSimilarity = []
    for ri, rvalue_tuple in enumerate(rvalue_list): # format: [(Id, r-value),...]
        TotalSimilarity = 0

        #-----
        rval_movieId = int(rvalue_tuple[0]) # movieId
        r_value = rvalue_tuple[1] # 상관계수
        if(r_value_max < r_value): # 상관계수 최댓값 구하기
            r_value_max = r_value
            #=print('r_value_max:', r_value_max)

        #-----
        if(title_dict != None): # {movie_title}은 여기 말고 아래서 사용하는 곳이 없다.
            movie_title = '<<<영화 이름 없음>>>'
            try: # 중간에 비정상적인 데이터가 있을 수 있다.
                movie_title = title_dict[rval_movieId]
            except KeyError: # {463}은 {KeyError} 발생, kag-mov와 mov-len 혼용할 때 발생
                pass
            except IndexError: # IndexError: tuple index out of range
                print ('IndexError: [movieId]', rval_movieId)
                pass
            if(len(movie_title) <= 0): # 제목이 없는 경우
                movie_title = '<<<영화 이름 없음>>>'

        #=ratings_tuple_list = movie_ratings_dict[rval_movieId]
        #=avg_rating = hgstat_avg_rating__ratings_dict_by_movieId \
        #=                (rval_movieId, movie_ratings_dict)

        #-----------
        # 장르 유사도 가중치
        #-----------
        GenreSet_Comp = set()
        GenreSimilarity = None
        if(genres_dict != None):
            # 유사도가 클수록 비슷하기 때문에 최소 유사도 '0'
            try: # 중간에 비정상적인 데이터가 있을 수 있다.
                GenreSet_Comp = set(genres_dict[rval_movieId])
            except KeyError: # {KeyError:463} 발생, kag-mov와 mov-len 혼용할 때 발생
                pass
            GenreSimilarity, GenreIntersec = get_genres_similarity_by_set2 \
                    (GenreSet_Base, GenreSet_Comp, GenresRawMode=GenresRawMode)
            # 장르 유사도 재조정(상관계수 범위 이내로 줄임)
            GenreSimilarity *= r_value_max

            GenreAlpha = 0.5 # 장르는 절반(1/2)만 반영한다.
            GenreSimilarity *= GenreAlpha

            # 장르 가중치 반영
            TotalSimilarity += GenreSimilarity

        #-----------
        # 평점 가중치
        #-----------
        vote_average = None
        vote_count = None
        vote_count_rate = None
        VotingSimilarity = None
        if(avg_ratings_dict != None):
            try: # 중간에 비정상적인 데이터가 있을 수 있다.
                vote_average = avg_ratings_dict[rval_movieId]
                vote_average_modify = (vote_average / 5) # rating_value: 5점이라서 0~1로 변환
            except KeyError: # {KeyError: 720} 발생, {kag-mov}는 값이 없는 경우
                vote_average_modify = 0

            # 평점 참여자 가중치
            if(count_ratings_dict != None):
                try: # 중간에 비정상적인 데이터가 있을 수 있다.
                    vote_count = count_ratings_dict[rval_movieId]
                except KeyError: # {KeyError: 720} 발생, {kag-mov}는 값이 없는 경우
                    vote_count = 0

                if(rating_count_max > 0):
                    vote_count_rate = (vote_count / rating_count_max)
                    vote_average_modify *= vote_count_rate # {투표 참여자 수}로 투표 비율 조정
            #
            VotingSimilarity = vote_average_modify

            #---------------
            # 평점 가중치 재조정(상관계수보다 크면 왜곡되므로 상관계수 범위 이내로 줄임)
            VotingSimilarity *= r_value_max

            #=VotingAlpha = 0.5 # 평점 평균은 절반(1/2)만 반영한다.
            #=VotingAlpha = 0.3 # 평점 평균은 절반(1/3)만 반영한다.
            #=VotingAlpha = 0.15 # 평점 평균은 절반(15/100)만 반영한다.
            VotingAlpha = 0.1 # 평점 평균은 절반(1/10)만 반영한다.
            VotingSimilarity *= VotingAlpha

            # 평점 가중치 반영
            TotalSimilarity += VotingSimilarity

        #-----------
        # 컬렉션(시리즈) 가중치
        #-----------
        CollectionName = None
        CollectionSimilarity = None # Collection 계산을 안했기 때문에 'None' 지정
        if(belong_to_collection_dict != None):
            CollectionSimilarity = 0 # 유사도가 클수록 비슷하기 때문에 최소 유사도 '0'
            CollectionName_Comp = ''
            try: # 중간에 비정상적인 데이터가 있을 수 있다.
                CollectionName_Comp = belong_to_collection_dict[rval_movieId]
            except KeyError: # {KeyError: 2355} 발생, kag-mov와 mov-len 혼용할 때 발생
                pass
            #=print('CollectionName_Comp:', CollectionName_Comp)
            if(CollectionName_Comp == CollectionName_Base):
                CollectionName = CollectionName_Comp
                CollectionSimilarity = 1 # {Collection}이 일치하므로 가장 유사한 '1'로 세팅
            
            # Collection:가중치 재조정(상관계수보다 크면 왜곡되므로 상관계수 범위 이내 줄임
            CollectionSimilarity *= r_value_max
            # 컬렉션 가중치 반영
            TotalSimilarity += CollectionSimilarity

        #-----------
        #-----------
        TotalSimilarity += r_value
        MovieSimilarity_j = {
            'movieId': rval_movieId, # 영화ID
            'similarity': TotalSimilarity, # 전체 유사도
            'r_value': r_value, # 상관계수
            'genres': GenreSet_Comp, # 비교 영화 장르
            'GenreSimilarity': GenreSimilarity, # 비교 장르 유사도
            'vote_average': vote_average,
            'vote_count': vote_count,
            'vote_count_rate': vote_count_rate,
            'VotingSimilarity': VotingSimilarity,
            'Collection': CollectionName, # 시리즈
            'CollectionSimilarity': CollectionSimilarity, # 시리즈 유사도
        }
        MovieSimilarity.append(MovieSimilarity_j)
        #break

    # 유사도를 기준으로 정렬
    MovieSimilarity.sort(key = lambda item: -(item['similarity'])) # 유사도(by high)
    #=print(*MovieSimilarity, sep='\n') # 내용이 많을 경우에 출력하면 보기 힘듦.
    
    #
    return MovieSimilarity

def hgstat_print_movie_info_by_movieId(
    Find_movieId, title_dict, genres_dict, 
    release_dict=None,
    avg_ratings_dict=None, count_ratings_dict=None,
    belong_to_collection_dict = None,
    debugPrint=False,
    ):
    #-----------------------
    # 영화 정보를 출력해본다.
    #-----------------------
    #=print(f'Find_movieId: {Find_movieId}')
    title = ''
    if(title_dict != None):
        title = title_dict[Find_movieId]
    release_date = ''
    if(release_dict != None):
        release_date = release_dict[Find_movieId]
    GenreList_Base = set()
    if(genres_dict != None):
        GenreList_Base = set(genres_dict[Find_movieId])
    vote_count = None
    if(count_ratings_dict != None):
        vote_count = count_ratings_dict[Find_movieId]    

    CollectionName = ''
    if(belong_to_collection_dict != None):
        CollectionName = belong_to_collection_dict[Find_movieId]
    #
    print(f'<{Find_movieId}> ', end='')
    if(release_dict != None):
        print(f'[{release_date}]', end='')
    print(f': {title}')
    if(avg_ratings_dict != None):
        vote_average = avg_ratings_dict[Find_movieId]
        print(f'vote_average: %.3f' % vote_average, end='')
        if(vote_count != None):
            print(f'({vote_count})', end='')
        print()
    if(belong_to_collection_dict != None):
        print(f'Collection: {CollectionName}')
    if(len(GenreList_Base) > 0):
        print(f'Genre: {GenreList_Base}')
    print()

def hgstat_print_similarity_movie(MovieSimilarity, 
    Find_movieId, title_dict=None, genres_dict=None, 
    release_dict=None,
    avg_ratings_dict=None, count_ratings_dict=None,
    belong_to_collection_dict = None,
    RankNum=10, debugPrint=False, printShortFormat=False,
    ):
    print('==========================================================')
    print('==========================================================')
    print('==========================================================')
    #-----------------
    # 정렬된 내용을 출력
    #-----------------
    print_Similarity = True
    print_Similarity = False
    printNum = 0 # 모두 순위 출력
    if(RankNum > 0):
        printNum = RankNum
    if(print_Similarity == True):
        #-----
        import hgsysinc
        from hgbasic import PrintDictList_ByLine
        PrintDictList_ByLine(MovieSimilarity, Printnum=printNum)

    #-----------------------
    # 가장 가까운 문서를 출력해본다.
    #-----------------------
    hgstat_print_movie_info_by_movieId(Find_movieId, title_dict, genres_dict, 
        release_dict,
        avg_ratings_dict=avg_ratings_dict, count_ratings_dict=count_ratings_dict,
        belong_to_collection_dict = belong_to_collection_dict)
    
    # caption-print
    if(printShortFormat == True):
        caption_list = ['순서', 'movieId', 'similarity', 'r-value']
        print(*caption_list, sep='\t', end='\t')
        if(genres_dict != None):
            print('genre_sim', end='\t')
        if(avg_ratings_dict != None):
            print('vote_average', end='\t')
            if(count_ratings_dict != None):
                pass
            else:
                print('vote_sim', end='\t')
        if(count_ratings_dict != None):
            print('count_ratings\t', end='\t')
            print('vote_count_rate\t', end='\t')
            print('vote_sim', end='\t')
        if(belong_to_collection_dict != None):
            print('belong_to_collection', end='\t')
        if(release_dict != None):
            print('release_date', end='\t')
        print('title')

    for simcnt, Similarity_i in enumerate(MovieSimilarity):
        simcnt += 1
        movieId = Similarity_i['movieId']
        if(Find_movieId == movieId): # 검사하는 문서와 같을 경우
            continue

        hgstat_print_similarity_movie_item(Similarity_i, title_dict, 
            release_dict=release_dict,
            PrintCnt = simcnt,
            debugPrint=debugPrint, printShortFormat=printShortFormat,
        )
        #
        if simcnt >= printNum:
            break

def hgstat_print_similarity_movie_item(movie_similarity, title_dict,
    release_dict=None,
    PrintCnt = None,
    debugPrint=False, printShortFormat=False,
    ):
    #-----------------------
    # 유사도 정보를 출력해본다.
    #-----------------------
    movieId = movie_similarity['movieId']

    #
    title = ''
    if(title_dict != None):
        title = title_dict[movieId]
    release_date = ''
    if(release_dict != None):
        release_date = release_dict[movieId]
    Similarity = movie_similarity['similarity']
    RValue = movie_similarity['r_value']
    GenreSet = movie_similarity['genres']
    GenreSimilarity = movie_similarity['GenreSimilarity']

    vote_average = movie_similarity['vote_average']
    VotingSimilarity = movie_similarity['VotingSimilarity']

    vote_count = movie_similarity['vote_count']
    vote_count_rate = movie_similarity['vote_count_rate']

    collection = movie_similarity['Collection']
    CollectionSimilarity = movie_similarity['CollectionSimilarity']

    if(printShortFormat == True):
        print(f"{PrintCnt}\t ", end='')
        print(f"{movieId}\t", end='')
        print('%0.3f\t' % Similarity, end='')
        print('%0.3f\t' % RValue, end='')
        if(GenreSimilarity != None):
            print('%0.3f\t' % GenreSimilarity, end='')
        if(vote_average != None):
            print('%0.2f\t' % vote_average, end='')
        if(vote_count != None):
            print(f'{vote_count}\t', end='')
        if(vote_count_rate != None):
            print('%.3f\t' % vote_count_rate, end='')
        if(VotingSimilarity != None):
            print('%.3f\t' % VotingSimilarity, end='')
        if(collection != None):
            print(f'{collection}\t ', end='')
        if(CollectionSimilarity != None):
            print('%.3f\t' % CollectionSimilarity, end='')
        #=else:
        #=    print('\t', end='')
    else:
        print()
        if(PrintCnt != None):
            print(f"[{PrintCnt}] ", end='')
        print(f"similar movieId: {movieId} ", end='')
        print("(Similarity:", "%0.3f" % Similarity, ")")
        print("(RValue:", "%0.3f" % RValue, ")")

    if(printShortFormat == True):
        print(f'{release_date}\t {title}', end='')
    else:
        if(PrintCnt != None):
            print(f"[{PrintCnt}] ", end='')
        print(f'similar movie [{release_date}]: {title}')
        if(len(GenreSet) > 0):
            print(f"{GenreSet}:%.3f" % movie_similarity['GenreSimilarity'])
        if(vote_average != None):
            print(f'vote_average: %.3f' % vote_average)
        if(vote_count != None):
            print('vote_count:', vote_count)
        if(VotingSimilarity != None):
            print('(VotingSimilarity: %.3f' % VotingSimilarity)
        if(collection != None):
            print(f'collection: {collection}:', end='')
        if(CollectionSimilarity != None):
            print("(", "%.3f" % CollectionSimilarity, ")")
        else:
            print()
    #
    print()

def get_GenresRawMode_name(GenresRawMode):
    if(GenresRawMode==True):
        return '장르 포함 일치' # 비교 기준의 장르를 얼마나 포함했나
    else:
        return '장르 완전 일치' # 비교 기준과 대상이 동시에 얼마나 포함했나

def print_genres_similarity_by_movieId(FindMovieId, GenreSimilarityDict, genres_dict, 
    title_dict=None, movie_ratings_dict=None, printNum=10):
    
    print(f'영화 [{FindMovieId}]: {genres_dict[FindMovieId]}')
    
    print('순서\t영화ID\t장르 유사도', end='')
    if(movie_ratings_dict != None):
        print('\t평점 평균', end='')
        print('\t평점 수', end='')
    print('\t장르 수\t장르 목록', end='')
    if(title_dict is not None):
        print(f'\t영화이름', end='')
    print()

    for li, movieId in enumerate (GenreSimilarityDict):
        genres = genres_dict[movieId]
        GenreSimilarity = GenreSimilarityDict[movieId]

        #-----
        print(f'{li+1}', end='')
        print(f'\t{movieId}', end='')
        print(f'\t%.2f' %(GenreSimilarity), end='')

        if(movie_ratings_dict != None):
            avg_rating = hgstat_avg_rating__ratings_dict_by_movieId \
                            (movieId, movie_ratings_dict)
            print(f'\t%.2f' %(avg_rating), end='')
            print(f'\t{len(movie_ratings_dict[movieId])}', end='')

        print(f'\t{len(genres)}', end='')
        print(f'\t{genres}', end='')
    
        if(title_dict is not None):
            title = title_dict[movieId]
            print(f'\t{title}', end='')

        print()
        
        if((li + 1) >= printNum):
            break
    print(), print(), 

def hgstat_genres_similarity_at_all_by_movieId(movieId, genres_dict, GenresRawMode=False):
    #-----------
    # 장르 유사도 계산
    #-----------
    GenreSet_Base = set(genres_dict[movieId])
    GenreSimilarityDict = {}
    for movieId_c in genres_dict:
        if(movieId_c == movieId): # 비교 기준(자기 자신)은 제외
            continue
        GenreSet_Comp = set(genres_dict[movieId_c])
        GenreSimilarity, GenreIntersec = get_genres_similarity_by_set2(GenreSet_Base, 
                            GenreSet_Comp, GenresRawMode=GenresRawMode)
        GenreSimilarityDict[movieId_c] = GenreSimilarity # format: {movieId:GenreSimilarity}
    #
    return GenreSimilarityDict # format: {movieId:GenreSimilarity}

def hgstat_get_genres_similarity_by_movieId2 \
    (movieId_b, movieId_c, genres_dict, GenresRawMode=False):
    #-----------
    # 장르 유사도 계산
    #-----------
    #=if(movieId_c == movieId_b): # 비교 기준(자기 자신)은 제외
    #=    assert False, "(movieId_c == movieId_b): # 비교 기준(자기 자신)은 제외"
    GenreSet_Base = set(genres_dict[movieId_b])
    GenreSet_Comp = set(genres_dict[movieId_c])
    GenreSimilarity, GenreIntersec = get_genres_similarity_by_set2 \
            (GenreSet_Base, GenreSet_Comp, GenresRawMode=GenresRawMode)
    return GenreSimilarity, GenreIntersec

def hgstat_genres_similarity_at_movieIds_by_movieId(movieId, 
    movieIds, genres_dict, GenresRawMode=False):
    #-----------
    # 장르 유사도 계산
    #-----------
    GenreSet_Base = set(genres_dict[movieId])
    GenreSimilarityDict = {}
    for movieId_c in movieIds:
        if(movieId_c == movieId): # 비교 기준(자기 자신)은 제외
            continue
        GenreSet_Comp = set(genres_dict[movieId_c])
        GenreSimilarity, GenreIntersec = get_genres_similarity_by_set2(GenreSet_Base, 
                            GenreSet_Comp, GenresRawMode=GenresRawMode)
        # format: {movieId:GenreSimilarity}
        GenreSimilarityDict[movieId_c] = GenreSimilarity # format: {movieId:GenreSimilarity}
    # format: {movieId:GenreSimilarity}
    return GenreSimilarityDict # format: {movieId:GenreSimilarity}

def print_genres_count_dict(GenresCountDict, genres_dict, 
    FindMovieId=None, title_dict=None, movie_ratings_dict=None, printNum=10):
    if(FindMovieId != None):
        print(f'영화 [{FindMovieId}]: {genres_dict[FindMovieId]}')
    
    print('순서\t영화ID\t계산 수', end='')
    if(movie_ratings_dict != None):
        print('\t평점 평균', end='')
        print('\t평점 수', end='')
    print('\t장르 수\t장르 목록', end='')
    if(title_dict != None):
        print(f'\t영화이름', end='')
    print()

    for li, movieId in enumerate (GenresCountDict):
        genres = genres_dict[movieId]
        GenresCount = GenresCountDict[movieId]

        #-----
        print(f'{li+1}', end='')
        print(f'\t{movieId}', end='')
        print(f'\t{len(GenresCount)}', end='')

        if(movie_ratings_dict != None):
            avg_rating = hgstat_avg_rating__ratings_dict_by_movieId \
                            (movieId, movie_ratings_dict)
            print(f'\t%.2f' %(avg_rating), end='')
            print(f'\t{len(movie_ratings_dict[movieId])}', end='')

        print(f'\t{len(genres)}', end='')
        print(f'\t{genres}', end='')
    
        if(title_dict != None):
            title = title_dict[movieId]
            print(f'\t{title}', end='')

        print()
        
        if((li + 1) >= printNum):
            break
    print(), print(), 

def hgstat_genres_count_at_all_by_movieId(movieId, genres_dict, CommonMode=True):
    GenreSet_Base = set(genres_dict[movieId])
    GenreCountDict = {}
    for movieId_c in genres_dict:
        if(movieId_c == movieId): # 비교 기준(자기 자신)은 제외
            continue
        GenreSet_Comp = set(genres_dict[movieId_c])
        if(CommonMode==True): # == True
            GenreOp = GenreSet_Comp.intersection(GenreSet_Base)
        else:
            GenreOp = GenreSet_Comp.difference(GenreSet_Base)
        # 
        GenreCountDict[movieId_c] = GenreOp # format: {movieId:GenreSet}
    #
    return GenreCountDict # format: {movieId:GenreSet}

def hgstat_genres_count_at_movieIds_by_movieId(movieId, movieIds, genres_dict, CommonMode=True):
    GenreSet_Base = set(genres_dict[movieId])
    GenresCountDict = {}
    for movieId_c in movieIds:
        if(movieId_c == movieId): # 비교 기준(자기 자신)은 제외
            continue
        GenreSet_Comp = set(genres_dict[movieId_c])
        if(CommonMode==True): # == True
            GenreOp = GenreSet_Comp.intersection(GenreSet_Base)
        else:
            GenreOp = GenreSet_Comp.difference(GenreSet_Base)
        # 
        GenresCountDict[movieId_c] = GenreOp # format: {movieId:GenreSet}
    #
    return GenresCountDict # format: {movieId:GenreSet}

def check_reco_item__ratings_dict_by_userId2(userId_b, userId_r, ratings_dict, title_dict, 
    debugPrint=False): 
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

    # 복사해서 사용(정렬할 때 원래 데이터 순서가 바뀌지 않도록)
    movie_rating_r = ratings_dict[userId_r].copy() # 복사해서 사용(정렬할 때 원래 데이터 순서가 바뀌지 않도록)
    movie_rating_r.sort(key=lambda r: -r[1]) # 튜플 2번째 값(rating_value) 큰 순서로 정렬

    #
    print(f'기준 고객ID: {userId_b}\t추천 고객ID: {userId_r}')
    print(f'추천 영화 수: {len(reco_movieId_list)}', end='\t')
    print('추천 영화(id) 목록:', reco_movieId_list)

    no_title_num = 0
    rinx = 0
    for rating_tuple in movie_rating_r:
        reco_movieId = rating_tuple[0]
        reco_rating = rating_tuple[1]
        if(reco_movieId not in reco_movieId_list):
            continue

        try: # 중간에 비정상적인 데이터가 있을 수 있다.
            movie_title = title_dict[reco_movieId]
        except KeyError: # {KeyError: 447} 발생, kag-mov와 mov-len 혼용할 때 발생, 아님 없는 경우 있음
            if(debugPrint == True):
                print(f'no tilte: reco_movieId [{reco_movieId}]')
            movie_title = ''
            no_title_num +=1
        if(len(movie_title) <= 0): # 제목이 없는 경우
            continue

        print(f'{rinx+1} ', end='')
        if(debugPrint == True):
            print(f'[{reco_movieId}] ', end='')
        print(f'({reco_rating}):', movie_title)
        rinx += 1
    if(len(reco_movieId_list) > 0): # 불필요한 줄바뀜 출력 방지
        print() 
    if(debugPrint == True):
        print(f'no tilte movie: {no_title_num}')

def print_title__ratings_dict_by_movieIds(movieIds, title_dict):
    print('순서\t영화ID\t영화 이름')
    for li, movieId in enumerate(movieIds):
        movie_title = title_dict[movieId]
        if(len(movie_title) <= 0): # 제목이 없는 경우
            print(f'{li+1}\t{movieId}\t<<<영화 이름 없음>>>')
        else:
            print(f'{li+1}\t{movieId}\t{movie_title}')
    print(), print(), 

def hgstat_print_title__ratings_dict_by_userId(userId, ratings_dict, title_dict):
    print('============================')
    print('@@@ 영화 이름 출력 @@@')
    print('============================')
    print(f'userId: {userId}')
    ratings_tuple_list = ratings_dict[userId]
    base_movieId_list = [ratings_tuple[0] for ratings_tuple in ratings_tuple_list]

    # 사용자가 평점을 매긴 영화 제목 출력하기
    hgstat_print_title_by_movieIds(base_movieId_list, title_dict)

def hgstat_print_title_by_movieIds(movieId_list, title_dict, title=None):
    # print_title__ratings_dict_by_movieIds() 함수와 기능이 거의 같다. 나중에 통합하자.
    if(title != None):
        print('============================')
        print(f'@@@ {title} @@@')
        print('============================')
    #
    print(f'userId_list: {len(movieId_list)}')

    # 영화 제목 출력하기
    for li, movieId in enumerate(movieId_list):
        movie_title = title_dict[movieId]
        if(len(movie_title) <= 0): # 제목이 없는 경우
            print(f'{li+1}\t{movieId}\t<<<영화 이름 없음>>>')
            continue
        print(f'{li+1}\t{movieId}\t{movie_title}')

def print_title_vote_by_movieIds(movieId_list, movie_ratings_dict, title_dict, 
    SortByVote=False, caption=None):
    if(caption != None):
        print('============================')
        print(f'@@@ {caption} @@@')
        print('============================')
    #
    print(f'userId_list: {len(movieId_list)}')

    # 영화 {평점 평균+제목} 출력하기
    print('순서\t영화ID\t고객수\t평점 평균\t영화 이름')
    VoteSortDict = {}
    for li, movieId in enumerate(movieId_list):
        avg_rating = hgstat_avg_rating__ratings_dict_by_movieId \
                        (movieId, movie_ratings_dict)
        #-----
        if(SortByVote == True): # 평균 평점으로 정렬
            VoteSortDict[movieId] = avg_rating
        else: # 평균 평점으로 정렬하지 않을 때 출력
            movie_title = title_dict[movieId]
            if(len(movie_title) <= 0): # 제목이 없는 경우
                print(f'{li+1}\t{movieId}\t<<<영화 이름 없음>>>')
                continue
            ratings_tuple_list = movie_ratings_dict[movieId]
            rating_num = len(ratings_tuple_list)

            print(f'{li+1}', end='')
            print(f'\t{movieId}', end='')
            print(f'\t{rating_num}', end='')
            print(f'\t%.3f' %(avg_rating), end='')
            print(f'\t{movie_title}')

    if(SortByVote == True): # 평균 평점으로 정렬
        VoteSortDict = dict(sorted(VoteSortDict.items(), key=lambda item: -item[1]))
        for li, movieId in enumerate(VoteSortDict):
            movie_title = title_dict[movieId]
            if(len(movie_title) <= 0): # 제목이 없는 경우
                print(f'{li+1}\t{movieId}\t<<<영화 이름 없음>>>')
                continue

            avg_rating = hgstat_avg_rating__ratings_dict_by_movieId \
                            (movieId, movie_ratings_dict)
            ratings_tuple_list = movie_ratings_dict[movieId]
            rating_num = len(ratings_tuple_list)

            #-----
            print(f'{li+1}', end='')
            print(f'\t{movieId}', end='')
            print(f'\t{rating_num}', end='')
            print(f'\t%.3f' %(avg_rating), end='')
            print(f'\t{movie_title}')
    #
    print(),print(),print(),

def print_rvalue_movie__ratings_dict_by_movieId(movieId, movieIdList, userIdList, 
    movie_ratings_dict, title_dict, PrintNum = 10, 
    debugPrint=False, ProcMod=0):
    if(debugPrint == True):
        hgsysinc._print_function_name_(3)

    if(debugPrint == True):
        print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
    #---------------------
    #---------------------
    if(debugPrint == True):
        print(f'[{movieId}] : 상관계수 계산')
    rvalue_list = get_rvalue__ratings_dict_by_Id(movieId, userIdList, movie_ratings_dict, 
        debugPrint=debugPrint, ProcMod=ProcMod)
    if(len(rvalue_list) <= 0):
        return
    #=rvalue_list : 상관계수가 큰 값부터 정렬된 상태

    if(debugPrint == True):
        # ratings_dict 포함해서 출력
        print_rvalue_list__ratings_dict(rvalue_list, userIdList, movie_ratings_dict, title='rvalue_list (by r-value order):')

    if(debugPrint == True):
        # 
        rvalue_list_max = rvalue_list[0]
        rvalue_list_min = rvalue_list[len(rvalue_list) - 1]
        max_movieId = rvalue_list_max[0]
        min_movieId = rvalue_list_min[0]
        print('상관계수 최댓값:[movieId:%i] %.4f' %(max_movieId, rvalue_list_max[1]))
        print('상관계수 최솟값:[movieId:%i] %.4f' %(min_movieId, rvalue_list_min[1]))

        max_movieId_inx = movieIdList.index(max_movieId)
        min_movieId_inx = movieIdList.index(min_movieId)
        print('상관계수 최댓값:[movieId_inx:%i] %.4f' %(max_movieId_inx, rvalue_list_max[1]))
        print('상관계수 최솟값:[movieId_inx:%i] %.4f' %(min_movieId_inx, rvalue_list_min[1]))

    #---------------------
    #---------------------
    movie_title = title_dict[movieId]
    print(f'({movieId}) {movie_title}: 상관계수에 의한 영화 추천')
    print('순서\t영화ID\t상관계수\t고객수\t평점 평균\t영화 제목')
    for ri, rvalue_tuple in enumerate(rvalue_list): # format: [(Id, r-value),...]
        #-----
        rval_movieId = rvalue_tuple[0] # movieId
        r_value = rvalue_tuple[1]

        #-----
        movie_title = title_dict[rval_movieId]
        if(len(movie_title) <= 0): # 제목이 없는 경우
            movie_title = '<<<영화 제목 없음>>>'

        ratings_tuple_list = movie_ratings_dict[rval_movieId]
        avg_rating = hgstat_avg_rating__ratings_dict_by_movieId \
                        (rval_movieId, movie_ratings_dict)
        #-----
        print(f'{ri+1}', end='')
        print(f'\t{rval_movieId}', end='')
        print(f'\t%.3f' %(r_value), end='')
        print(f'\t{len(ratings_tuple_list)}', end='')
        print(f'\t%.3f' %(avg_rating), end='')
        print(f'\t{movie_title}')

        #
        if((ri + 1) >= PrintNum):
            break            
    print(), print()

def hgstat_recommend_movie__by_movieId(
    movieId, movieIdList, userIdList, 
    movie_ratings_dict, title_dict, genres_dict=None, GenresRawMode=False, 
    avg_ratings_dict=None, count_ratings_dict=None, rating_count_max=0, 
    belong_to_collection_dict=None,
    reco_type='genre+voting', RankNum=10, 
    debugPrint=False, printShortFormat = True, ProcMod=2500,
    ):
    #---------------
    #---------------
    # debugPrint = True # 중간 내용 출력
    # debugPrint = False # 중간 내용 출력하지 않음
    #
    # printShortFormat = True # 간단하게 1줄로 출력(True:예)
    # printShortFormat = False # 간단하게 1줄로 출력(False:아님)
    #---------------
    #---------------
    print(), print(), print(), print(), print(), 
    if(reco_type == 'genre+voting'):
        print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        #=GenresRawMode=True # 포함 일치
        GenresRawMode = False # 완전 일치
        print(f'# 23) 영화 [{movieId}] +<장르+평점> ({get_GenresRawMode_name(GenresRawMode)}) ')
        print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')

        MovieSimilarity = hgstat_get_similarity_movie_by_movieId(
            movieId, movieIdList, userIdList, movie_ratings_dict, title_dict, 
            genres_dict=genres_dict, avg_ratings_dict=avg_ratings_dict, 
            GenresRawMode=GenresRawMode,
            debugPrint=debugPrint, ProcMod=1500)
        hgstat_print_similarity_movie(MovieSimilarity, 
            movieId, title_dict, genres_dict, 
            avg_ratings_dict=avg_ratings_dict, count_ratings_dict=None,
            belong_to_collection_dict = None,
            RankNum=RankNum, debugPrint=debugPrint, printShortFormat=printShortFormat,
        )
    elif(reco_type == 'genre+voting+count'):
        print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        #=GenresRawMode = True # 포함 일치
        GenresRawMode = False # 완전 일치
        print(f'# 24) 영화 [{movieId}] +<장르+(평점*평점참여자-참여자최댓값)> ({get_GenresRawMode_name(GenresRawMode)}) ')
        print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        # 평점참여자 최댓값 구하기
        rating_count_max = max(count_ratings_dict.values())
        print('rating_count_max:', rating_count_max)

        MovieSimilarity = hgstat_get_similarity_movie_by_movieId(
            movieId, movieIdList, userIdList, movie_ratings_dict, title_dict, 
            genres_dict=genres_dict, avg_ratings_dict=avg_ratings_dict, 
            count_ratings_dict=count_ratings_dict, rating_count_max=rating_count_max,
            GenresRawMode=GenresRawMode,
            debugPrint=debugPrint, ProcMod=1500)
        hgstat_print_similarity_movie(MovieSimilarity, 
            movieId, title_dict, genres_dict, 
            avg_ratings_dict=avg_ratings_dict, count_ratings_dict=count_ratings_dict,
            belong_to_collection_dict = None,
            RankNum=RankNum, debugPrint=debugPrint, printShortFormat=printShortFormat,
        )

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
        pass # 구현하지 않았다. 아래 코드는 kaggle_movie 방식이다.
        #=print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        #=print('# 5) {장르+컬렉션+(평점*평점참여자-참여자최댓값기준)} 가중치 적용')
        #=print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        #=# 평점참여자 최댓값 구하기
        #=vote_count_max = hgstat_get_vote_count_max(vote_count_list)
        #=print('vote_count_max:', vote_count_max)
        #=
        #=SimDocInfo = hgstat_get_distance_by_inx__kagmov(WordDicts, FindInx, genres_list, 
        #=    VotingList=vote_average_list, VoteCountList=vote_count_list, VoteCountMax=vote_count_max,
        #=    belong_to_collection_dict=belong_to_collection_dict)
        #=hgstat_print_distanace__kaggle_movies(SimDocInfo, WordDicts,
        #=    FindInx, title_list, overview_list, release_date_list, genres_list,
        #=    vote_average_list = vote_average_list, vote_count_list = vote_count_list,
        #=    belong_to_collection_dict=belong_to_collection_dict,
        #=    RankNum=RankNum, debugPrint=debugPrint, printShortFormat=printShortFormat)

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
        print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        GenresRawMode = True # 포함 일치
        #=GenresRawMode = False # 완전 일치
        print(f'# 12) 영화 [{movieId}] +<장르> 유사도 적용({get_GenresRawMode_name(GenresRawMode)}) ')
        print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        MovieSimilarity = hgstat_get_similarity_movie_by_movieId(
            movieId, movieIdList, userIdList, movie_ratings_dict, title_dict, 
            genres_dict=genres_dict, 
            GenresRawMode=GenresRawMode, 
            debugPrint=debugPrint, ProcMod=1500)
        hgstat_print_similarity_movie(MovieSimilarity, 
            movieId, title_dict, genres_dict, 
            avg_ratings_dict = None, count_ratings_dict = None,
            belong_to_collection_dict = None,
            RankNum=RankNum, debugPrint=debugPrint, printShortFormat=printShortFormat,
        )
    elif(reco_type == 'genre'):
        print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        #=GenresRawMode=True # 포함 일치
        GenresRawMode = False # 완전 일치
        print(f'# 22) 영화 [{movieId}] +<장르> 유사도 적용({get_GenresRawMode_name(GenresRawMode)}) ')
        print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')

        MovieSimilarity = hgstat_get_similarity_movie_by_movieId(
            movieId, movieIdList, userIdList, movie_ratings_dict, title_dict, 
            genres_dict=genres_dict, 
            GenresRawMode=GenresRawMode, 
            debugPrint=debugPrint, ProcMod=1500)
        hgstat_print_similarity_movie(MovieSimilarity, 
            movieId, title_dict, genres_dict, 
            avg_ratings_dict=None, count_ratings_dict=None,
            belong_to_collection_dict = None,
            RankNum=RankNum, debugPrint=debugPrint, printShortFormat=printShortFormat,
        )
    else:
        print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        print(f'# 11) 영화 [{movieId}] 가중치 적용 안 함 - 상관계수만 적용')
        print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        #-------------------
        #=print_rvalue_movie__ratings_dict_by_movieId(movieId, movieIdList, userIdList, 
        #=    movie_ratings_dict, title_dict, PrintNum = RankNum, 
        #=    debugPrint=debugPrint, ProcMod=900)
        #-------------------
        MovieSimilarity = hgstat_get_similarity_movie_by_movieId(
            movieId, movieIdList, userIdList, movie_ratings_dict, title_dict, 
            debugPrint=debugPrint, ProcMod=1500)
        hgstat_print_similarity_movie(MovieSimilarity, 
            movieId, title_dict, genres_dict = None, 
            avg_ratings_dict = None, count_ratings_dict = None,
            belong_to_collection_dict = None,
            RankNum=RankNum, debugPrint=debugPrint, printShortFormat=printShortFormat,
        )



#================================
#================================
class HGTest(TestCase):
    def test_fun(self):
        hgsysinc._print_function_name_(3)

        #
        print()


#---------------------
#---------------------
if __name__ == '__main__':
    main()

