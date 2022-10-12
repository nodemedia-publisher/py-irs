import hgsysinc
from hgstat import (
    hgAnova_List, hgRValue_Lists, hgNonZeroCount, hgCoefficient_low,
)

#----------------
#----------------
def hgstat_GetMovieList(moviedata, debug=False):
    #----------------
    # format:
    # movie_rate = {'user1':{'movie_name1': rate_value(number)}, ...}
    #----------------
    if moviedata == None:
        from hgstat_test_data_fake import movie_rates_ex1, movie_rates_ex2
        #=moviedata = movie_rates_ex1
        moviedata = movie_rates_ex2

    #
    #=print('moviedata:', moviedata)
    key_list = moviedata.keys()
    if(debug == True):
        print(key_list)

    person_list = []
    movie_list = []
    score_list = []
    for person in key_list:
        person_list.append(person)

        person_data = moviedata[person]
        #=print(person_data)
        #=print()

        movie_list_person = person_data.keys()
        if(debug == True):
            print(movie_list_person)
        for movie in movie_list_person:
            #=print(movie)
            movie_data = person_data[movie]
            #=print(movie_data)
            if movie not in movie_list:
                movie_list.append(movie)
            if movie_data not in score_list:
                score_list.append(movie_data)

    if(debug == True):
        print()
        print(f'person list({len(person_list)}):', person_list)
        print(f'movie list({len(movie_list)}):', movie_list)
        print(f'score list({len(score_list)}):', score_list)
    return person_list, movie_list, score_list

def hgstat_MakeMovieTable_4_Reco(moviedata, debug=False):
    #----------------
    # format:
    # movie_rate = {'user1':{'movie_name1': rate_value(number)}, ...}
    #----------------
    if moviedata == None:
        from hgstat_test_data_fake import movie_rates_ex1, movie_rates_ex2
        #=moviedata = movie_rates_ex1
        moviedata = movie_rates_ex2

    #
    person_list, movie_list, score_list = hgstat_GetMovieList(moviedata)
    if(debug == True):
        print(f'person list({len(person_list)}):', person_list)
        print(f'movie list({len(movie_list)}):', movie_list)
        print(f'score list({len(score_list)}):', score_list)
        print()

    movie_table = [[]] * len(person_list)
    for person in person_list:
        movie_id_list = [0 for a in range(0,len(movie_list))]

        #=print('person:', person)
        person_data = moviedata[person]
        #=print(person_data)
        #=print()

        movie_list_person = person_data.keys()
        for movie in movie_list_person:
            #=print(movie)
            movie_data = person_data[movie]
            #=print(movie_data)
            if movie in movie_list:
                movie_index = movie_list.index(movie)
                movie_id_list[movie_index] = movie_data

        person_index = person_list.index(person)
        movie_table[person_index] = movie_id_list

    if(debug == True):
        print()
        print(f'movie table({len(movie_table)}):', movie_table)

    return movie_table, person_list, movie_list, score_list

#----------------
#----------------

#================================
#================================
def get_database_buydatas(buydatas):
    #---------------------
    # buydatas format:
    #---------------------
    # buydata_111 = {'고객ID':111, '구입목록': ['C언어', '파이썬', '자료구조', '파일처리', '운영체제', '논리회로', '데이터베이스', '인공지능', '네트워크', '영상처리','정보검색', 'Window 프로그래밍', 'iOS 프로그래밍', '자바 프로그래밍']}
    # buydata_112 = {'고객ID':112, '구입목록': ['C언어', '파이썬', '자료구조', '파일처리',]}
    # buydatas = [buydata_111, buydata_112, ...]
    #---------------------

    #
    person_id_list = [item['고객ID'] for item in buydatas]
    buy_item_lists = [item['구입목록'] for item in buydatas]

    #
    item_list = []
    for list in buy_item_lists:
        for item in list:
            if item not in item_list:
                item_list.append(item)
    #
    person_id_list_by_item_key = {item:[] for item in item_list}
    for item in item_list:
        for pinx, buylist in enumerate(buy_item_lists):
            if item in buylist:
                buy_item_list_by_item = person_id_list_by_item_key[item]
                buy_item_list_by_item.append(person_id_list[pinx])
    #=print('person_id_list_by_item_key:', person_id_list_by_item_key)

    #----------
    # format:
    #----------
    # person_id_list = [111, 112, 113, 114, 115, 116, 117, 118, 119, 131, 132, 133, 134, 135, 211, 212, 213, 221, 222, 311, 312]
    # buy_item_lists = [
    #   ['C언어', '파이썬', '자료구조', '파일처리', '운영체제', '논리회로', '데이터베이스', '인공지능', '네트워크', '영상처리','정보검색', 'Window 프로그래밍', 'iOS 프로그래밍', '자바 프로그래밍'],
    #   ['C언어', '파이썬', '자료구조', '파일처리',],
    # ]
    # item_list = ['C언어', '파이썬', '자료구조', '파일처리', '운영체제', '논리회로', '데이터베이스', '인공지능', '네트워크', '영상처리', '정보검색', 'Window 프로그래밍', 'iOS 프로그래밍', '자바 프로그래밍', '언어학', '형태론', '통사론', '음성학', '의미론', '표준국어문법', '심리언어학', '신경언어학', '언어병리학', '교육학', '교육행정', '교육심리', '교육상담', '교육철학']
    # person_id_list_by_item_key = {
    #   'C언어': [111, 112, 113, 114, 115, 116, 117, 118, 135],
    #   '파이썬': [111, 112, 113, 117, 118, 119, 131, 132, 133, 134, 135],
    # }
    #----------
    return person_id_list, buy_item_lists, item_list, person_id_list_by_item_key

def print_itemlist_by_inxlist(item_list, inx_list):
        print(f'항목 수: {len(inx_list)}', end='\t')
        print('항목(inx) 목록:', inx_list)
        for ri, inx in enumerate(inx_list):
            print(f'{ri+1}:', item_list[inx], end='\t')
        if(len(inx_list) > 0): # 불필요한 줄바뀜 출력 방지
            print() 

def print_rvalue_list(rvalue_list, ID_list=None, datalists=None, title=None,
    mod_val=0):
    if(title != None):
        print(title)
    if(mod_val <= 0): # 한 줄에 항목 1개를 출력할 때
        print('순서\t', end='')
    print('인덱스', end='')
    if(ID_list != None):
        print('\tID', end='')
    print('\t상관계수', end='')
    if(datalists != None):
        print('\t항목수\t상태 리스트', end='')
    print()

    for prinx, rvalue_tuple in enumerate(rvalue_list): # format: [(index, r-value),...]
        pid_index = rvalue_tuple[0]
        r_value = rvalue_tuple[1]
        
        #
        pr_str = ""

        if(mod_val <= 0): # 한 줄에 항목 1개를 출력할 때
            pr_str += f'{prinx + 1}\t'

        pr_str += f'{pid_index}'
        if(ID_list != None):
            id_name = ID_list[pid_index]
            pr_str += f'\t{id_name}'

        pr_str += f'\t%.3f' %(r_value)

        if(datalists != None):
            cur_list = datalists[pid_index]
            item_num = hgNonZeroCount(cur_list)
            pr_str += f'\t{item_num}\t{cur_list}'
            
        #---
        if(mod_val <= 0): # 한 줄에 항목 1개를 출력할 때
            print(pr_str)
        else:
            if((prinx % mod_val) == 1):
                print(pr_str)
            else:
                print(pr_str, end='\t')
    #
    print()

def check_rvalue__datalists(item_name, item_list, datalists, 
    debugPrint=False): 
    if(debugPrint == True):
        hgsysinc._print_function_name_(3)

    #---------------------
    #---------------------
    if(item_name not in item_list):
        print(f'{item_name} : 목록에 없습니다.')
        return
    item_index = item_list.index(item_name) # 상품('파이썬') 인덱스
    baselist = datalists[item_index]
    
    #-------------------------------
    # 아래 방식은 사용하지 않는다.
    # 목록의 일부를 지우면 다른 곳에서 index 순서가 달라져서 
    # 논리적인 일관성이 없어진다. 삭제된 상태를 감안해서 
    # {item_index}를 재계산하여 출력하면 문제가 없지만 
    # 여기서 출력된 {item_index}값은
    # 원래 {item_index}값과는 다르기 때문에 논리적인 혼선이 발생한다.
    # 이러한 혼선이 발생하지 않도록 아래 방법은 사용하지 않고
    # 대신에 hgRValue_Lists() 출력 결과에서 {item_index} 부분을 
    # 제외시킨다. 그러면 이 함수에서 출력된 {item_index}가 
    # 외부에서 출력된 것과 논리적으로 일치한다.
    #-------------------------------
    #=# 지정한 상품(item_name)을 제외한 나머지로 데이터 목록을 구성
    #=#=print(f'datalists ({len(datalists)}):')
    #=#=print(f'item_list ({len(item_list)}):')
    #=datalists.remove(baselist)
    #=item_list.remove(item_name)
    #=#=print(f'datalists ({len(datalists)}):') # 삭제되었나 확인
    #=#=print(f'item_list ({len(item_list)}):') # 삭제되었나 확인
    #-------------------------------

    #---------------------
    #---------------------
    print(f'{item_name}: 상관계수')
    rvalue_list = hgRValue_Lists(baselist, datalists)
    if(len(rvalue_list) <= 0):
        return rvalue_list
    if(debugPrint == True):
        print(rvalue_list)
        print()

    #---------------------
    # 비교 대상에서 자기 자신을 삭제
    #---------------------
    # rvalue_list format: [(index, r-value),...]
    rvalue_list_pure = [rv_tuple for rv_tuple in rvalue_list if rv_tuple[0] != item_index]
    #=print('rvalue_list_pure:', rvalue_list_pure)

    # 최댓값과 최솟값: (아래에서 {inx} 순으로 정렬(sort)하기 전에 처리)
    rvalue_list_max = rvalue_list_pure[0]
    rvalue_list_min = rvalue_list_pure[len(rvalue_list_pure) - 1]

    if(debugPrint == True):
        # sort : inx 순으로 정렬(hgRValue_Lists()함수는 r_value[1] 큰 값 순서로 정렬된 상태)
        rvalue_list_pure.sort(key=lambda x : x[0]) # {format: (index, r_value)}
        # datalists 없이 출력
        print_rvalue_list(rvalue_list_pure, item_list, title='rvalue_list (by item order):')
        # datalists 포함해서 출력
        print_rvalue_list(rvalue_list_pure, item_list, datalists, title='rvalue_list (by item order):')

    #=print('상관계수 최솟값:[%i] %.3f' %(rvalue_list_min[0], rvalue_list_min[1]))
    #=print('상관계수 최댓값:[%i] %.3f' %(rvalue_list_max[0], rvalue_list_max[1]))

    item_max = item_list[rvalue_list_max[0]]
    item_min = item_list[rvalue_list_min[0]]
    print(f'상관계수 최댓값:[{item_max}] %.3f' %(rvalue_list_max[1]))
    print(f'상관계수 최솟값:[{item_min}] %.3f' %(rvalue_list_min[1]))
    print()

    #-------------------------------
    # 아래 방식은 사용하지 않는다.
    # 목록의 일부를 지우면 다른 곳에서 index 순서가 달라져서 
    # 논리적인 일관성이 없어진다. 삭제된 상태를 감안해서 
    # {item_index}를 재계산하여 출력하면 문제가 없지만 
    # 여기서 출력된 {item_index}값은
    # 원래 {item_index}값과는 다르기 때문에 논리적인 혼선이 발생한다.
    # 이러한 혼선이 발생하지 않도록 아래 방법은 사용하지 않고
    # 대신에 hgRValue_Lists() 출력 결과에서 {item_index} 부분을 
    # 제외시킨다. 그러면 이 함수에서 출력된 {item_index}가 
    # 외부에서 출력된 것과 논리적으로 일치한다.
    #=#-------------------------------
    #=#---------------------
    #=#---------------------
    #=# 다음 작업을 위해서 삭제한 것을 데이터 목록을 삽입하여 복원
    #=datalists.insert(item_index, baselist)
    #=item_list.insert(item_index, item_name)
    #-------------------------------
    #
    return rvalue_list_pure

def find_reco_inx__statelist(baselist, recolist, item_list=None, debugPrint=False):
    # {recolist} 상태 목록과 비교하여 {baselist}에 없는 항목의 {inx}를 찾는다.
    if(len(baselist) != len(recolist)):
        assert False, '(len(baselist) != len(recolist))'
        
    if(debugPrint == True):
        hgsysinc._print_function_name_(3)

        #---------------------
        #---------------------
        print([i for i in range(len(baselist))])
        print(f'baselist ({hgNonZeroCount(baselist)}/{len(baselist)}):', baselist) # 상태 [0,0,1,1,0]
        print(f'recolist ({hgNonZeroCount(recolist)}/{len(recolist)}):', recolist) # 상태 [0,0,1,0,1]
        print()

    #
    reco_item_inx_list = []
    for inx, base_state in enumerate(baselist):
        reco_state = recolist[inx]
        if(reco_state > 0): # '0': 무효 상태(구매하지 않은 상태)
            if(base_state != reco_state): # 동시에 구매한 것을 제외하고 없는 항목만
                reco_item_inx_list.append(inx)
                #=print('추천 항목 inx:', inx)
    if(debugPrint == True):
        print_itemlist_by_inxlist(item_list, reco_item_inx_list)
    #
    return reco_item_inx_list

def find_reco__id_list(baselist, recolist, debugPrint=False):
    # {recolist} id 목록과 비교하여 {baselist}에 없는 {id}를 찾는다.
    if(debugPrint == True):
        hgsysinc._print_function_name_(3)
        #---------------------
        #---------------------
        print(f'baselist ({len(baselist)}):', baselist) # 상태 [0,0,1,1,0]
        print(f'recolist ({len(recolist)}):', recolist) # 상태 [0,0,1,0,1]
        print()

    #
    find_reco_id_list = []
    for inx, reco_id in enumerate(recolist):
        if(reco_id not in baselist):
            find_reco_id_list.append(reco_id)
            #=print('추천 항목 id:', reco_id)
    #
    return find_reco_id_list

def find_real_max_rvalue__RValueList(baselist, datalists, R_ValueList, SortFlag=False, debugPrint=False):
    #--------------------------------------------
    # {R_ValueList}는 상관계수가 큰 값부터 정렬되어 있는데 
    # 맨 앞에서부터 (자신을 제외하고) 무조건 상관계수가 큰 것을 선택하면 
    # 이 방식의 경우에 선택된 고객의 상품이 찾는 사람보다 적은 경우가 있다.
    # 이럴 경우에는 추천할 상품이 없으므로 
    # 실제로 추천할 상품이 있는 (첫 번째) 추천 인덱스를 찾아야 한다.
    #--------------------------------------------
    if(SortFlag == True): # 만약 정렬하라고 하면 최댓값을 구하기 위해서 정렬해준다.
        R_ValueList.sort(key=lambda x : -x[1]) # 큰 값 기준 정렬>>format:(index,value)
    else: # 외부에서 정렬된 상태일 때는 이쪽으로
        pass

    for rvalue_tuple in R_ValueList:
        if(debugPrint == True):
            print('rvalue_tuple:', rvalue_tuple)
        item_index = rvalue_tuple[0] # format: (index, r_value)
        recolist = datalists[item_index]
        reco_item_inx_list = find_reco_inx__statelist(baselist, recolist) # 여기서는 결과만 받을 거니까 {debugPrint}를 커지 않는다.
        if(len(reco_item_inx_list) > 0): # 추천 상품이 있는 경우
            return rvalue_tuple
    return None

def check_recommend_person_simple(baselist, datalists, baselist_person_id=None, buy_item_list=None, buy_person_list=None,
    debugPrint=False,
    ):
    if(debugPrint == True):
        hgsysinc._print_function_name_(3)

        #---------------------
        #---------------------
        print(f'baselist:', baselist)
        print(f'{len(datalists)}:')
        print(*datalists, sep='\n')
        print()

    #=rvalue_list = hgRValue_Lists(baselist, datalists, debug=True)
    rvalue_list = hgRValue_Lists(baselist, datalists)
    if(len(rvalue_list) <= 0):
        return None
    if(debugPrint == True):
        print(rvalue_list)
        print()
    
    if(baselist_person_id != None):
        #---------------------
        # 비교 대상에서 자기 자신을 삭제
        #---------------------
        # rvalue_list format: [(index, r-value),...]
        person_id_inx = buy_person_list.index(baselist_person_id)
        rvalue_list_control = [rv_tuple for rv_tuple in rvalue_list if rv_tuple[0] == person_id_inx]
        #=print('rvalue_list_control:', rvalue_list_control)
        if(len(rvalue_list_control) >= 1):
            rvalue_list.remove(rvalue_list_control[0])
    
    if(debugPrint == True):
        # datalists 포함해서 출력
        print_rvalue_list(rvalue_list, buy_person_list, datalists, title='rvalue_list (by r-value order):')
        # datalists 없이 출력
        print_rvalue_list(rvalue_list, buy_person_list, title='rvalue_list (by r-value order):')

    # 아래에서 {inx} 순으로 정렬(sort)하기 전에 최댓값과 최솟값을 받아둔다.
    rvalue_list_max = rvalue_list[0]

    if(debugPrint == True):
        # sort : inx 순으로 정렬
        rvalue_list.sort(key=lambda x : x[0]) # {format: (index, r_value)}

        # datalists 포함해서 출력
        print_rvalue_list(rvalue_list, buy_person_list, datalists, title='rvalue_list (by person-id order):')
        # datalists 없이 출력
        print_rvalue_list(rvalue_list, buy_person_list, title='rvalue_list (by person-id order):')

    if(debugPrint == True):
        rvalue_list_min = rvalue_list[len(rvalue_list) - 1]
        print('상관계수 최댓값:[%i] %.4f' %(rvalue_list_max[0], rvalue_list_max[1]))
        print('상관계수 최솟값:[%i] %.4f' %(rvalue_list_min[0], rvalue_list_min[1]))

    if(debugPrint == True):
        if(buy_person_list != None):
            person_id_max = buy_person_list[rvalue_list_max[0]]
            print('상관계수 최댓값:[고객ID:%i] %.4f' %(person_id_max, rvalue_list_max[1]))

    #
    max_list = datalists[rvalue_list_max[0]]
    reco_item_inx_list = find_reco_inx__statelist(baselist, max_list, buy_item_list, debugPrint=debugPrint)

    #
    reco_index = rvalue_list_max[0]
    r_value = rvalue_list_max[1]
    #
    return (reco_index, r_value, reco_item_inx_list) # (추천고객ID, 추천 상관계수, 추천 상품 인덱스 목록)

def check_recommend_person_real(baselist, datalists, baselist_person_id=None, buy_item_list=None, buy_person_list=None,
    debugPrint=False,
    ):
    if(debugPrint == True):
        hgsysinc._print_function_name_(3)

        #---------------------
        #---------------------
        print(f'baselist:', baselist)
        print(f'{len(datalists)}:')
        print(*datalists, sep='\n')
        print()

    #=rvalue_list = hgRValue_Lists(baselist, datalists, debug=True)
    rvalue_list = hgRValue_Lists(baselist, datalists)
    if(len(rvalue_list) <= 0):
        return None
    if(debugPrint == True):
        print(rvalue_list)
        print()

    if(baselist_person_id != None):
        #---------------------
        # 비교 대상에서 자기 자신을 삭제
        #---------------------
        # rvalue_list format: [(index, r-value),...]
        person_id_inx = buy_person_list.index(baselist_person_id)
        rvalue_list_control = [rv_tuple for rv_tuple in rvalue_list if rv_tuple[0] == person_id_inx]
        #=print('rvalue_list_control:', rvalue_list_control)
        if(len(rvalue_list_control) >= 1):
            rvalue_list.remove(rvalue_list_control[0])

    if(debugPrint == True):
        # datalists 포함해서 출력
        print_rvalue_list(rvalue_list, buy_person_list, datalists, title='rvalue_list (by r-value order):')
        # datalists 없이 출력
        print_rvalue_list(rvalue_list, buy_person_list, title='rvalue_list (by r-value order):')

    #--------------------------------------------
    # 아래에서 {inx} 순으로 정렬(sort)하기 전에 최댓값과 최솟값을 받아둔다.
    #--------------------------------------------
    # 아래 방식의 경우에는 (자신을 제외하고) 무조건 상관계수가 큰 것을 선택하는데 
    # 이 방식의 경우에 선택된 고객의 상품이 찾는 사람보다 적은 경우가 있다.
    # 이럴 경우에는 추천할 상품이 없으므르 
    # 실제로 추천할 상품이 있는 (첫 번째) 추천 인덱스를 찾아야 한다.
    #--------------------------------------------
    #=rvalue_list_max = rvalue_list[0]
    #--------------------------------------------
    rvalue_list_max = find_real_max_rvalue__RValueList(baselist, datalists, rvalue_list, debugPrint=debugPrint)
    if(rvalue_list_max == None):
        #=if(buy_item_list != None):
        #=    print(f'추천 상품 수: 없음', end='\t')
        #=    print('추천 상품 목록: 없음')
        return (None, None, None) # (추천고객ID, 추천 상관계수, 추천 상품 인덱스 목록)
    # rvalue_list_max: (index, r_value)

    if(debugPrint == True):
        # sort : inx 순으로 정렬
        rvalue_list.sort(key=lambda x : x[0]) # {format: (index, r_value)}

        # datalists 포함해서 출력
        print_rvalue_list(rvalue_list, buy_person_list, datalists, title='rvalue_list (by person-id order):')
        # datalists 없이 출력
        print_rvalue_list(rvalue_list, buy_person_list, title='rvalue_list (by person-id order):')

    if(debugPrint == True):
        rvalue_list_min = rvalue_list[len(rvalue_list) - 1]
        print('상관계수 최댓값:[%i] %.4f' %(rvalue_list_max[0], rvalue_list_max[1]))
        print('상관계수 최솟값:[%i] %.4f' %(rvalue_list_min[0], rvalue_list_min[1]))

    if(debugPrint == True):
        if(buy_person_list != None):
            person_id_max = buy_person_list[rvalue_list_max[0]]
            print('상관계수 최댓값:[고객ID:%i] %.4f' %(person_id_max, rvalue_list_max[1]))

    #
    max_list = datalists[rvalue_list_max[0]]
    reco_item_inx_list = find_reco_inx__statelist(baselist, max_list, buy_item_list, debugPrint=debugPrint)

    #
    reco_index = rvalue_list_max[0]
    r_value = rvalue_list_max[1]
    #
    return (reco_index, r_value, reco_item_inx_list) # (추천고객ID, 추천 상관계수, 추천 상품 인덱스 목록)

def print_selling_info__person_id_list(item_selling_lists, buy_item_list, 
    person_id_list_by_item_key=None, title=None, sortByName=False, PrintNum=0):
    print('-------------------------------------')
    if(title != None):
        print(f'--- {title} ---')
    print('-------------------------------------')

    # caption
    print('순서', end='')
    print('\t항목[index]', end='')
    print(f'\t빈도', end='')
    if(person_id_list_by_item_key != None):
        print(f'\t구매자 목록', end='')
    print()

    item_tuple3_list = []
    for cnt, item_tuple in enumerate(item_selling_lists):
        item_inx = item_tuple[0]
        item_count = item_tuple[1]
        
        item = buy_item_list[item_inx]
        
        if(sortByName == True):
            item_tuple3_list.append((item_inx, item, item_count))
        else:
            print(f'{cnt+1}', end='')
            print(f'\t{item}[{item_inx}]', end='')
            print(f'\t{item_count}', end='')

            if(person_id_list_by_item_key != None):
                buy_person_list = person_id_list_by_item_key[item]
                print('\t', end='')
                print(buy_person_list, end='')
            print()
        #
        if(PrintNum > 0):
            if((cnt + 1) >= PrintNum):
                break

    if(sortByName == True): # 항목 이름으로 정렬
        # sort : 항목 이름으로 정렬
        item_tuple3_list.sort(key=lambda x : x[1]) # {format: (index, item, count)}
        for cnt, item_tuple in enumerate(item_tuple3_list):
            item_inx = item_tuple[0]
            #=item = buy_item_list[item_inx]
            item = item_tuple[1]
            item_count = item_tuple[2]
            
            print(f'{cnt+1}', end='')
            print(f'\t{buy_item_list[item_inx]}[{item_inx}]', end='')
            print(f'\t{item_count}', end='')
            if(person_id_list_by_item_key != None):
                buy_person_list = person_id_list_by_item_key[item]
                print('\t', end='')
                print(buy_person_list, end='')
            print()

    print()
    print()

def find_recommend_item_by_item(buy_item, person_id_list, 
    buy_item_lists, item_list, person_id_list_by_item_key, 
    debugPrint=False,
    ):
    if(debugPrint == True):
        hgsysinc._print_function_name_(3)
    #---------------------
    #---------------------
    # 검색 '상품' 구매한 사람 목록
    #=buy_item = 'C언어'
    person_id_list_at_item = person_id_list_by_item_key[buy_item]
    if(debugPrint == True):
        print('#----------')
        print('# 상품 추천')
        print('#----------')
        print(f'[{buy_item}] 상품을 구매한 사람-id 목록 ({len(person_id_list_at_item)}):', person_id_list_at_item)

    # 연관 상품: 구매한 사람들이 구매한 모든 상품 목록 <== 검색 '상품' 구매한 사람 목록
    buylist_set = set()
    for person_id in person_id_list_at_item:
        person_id_inx = person_id_list.index(person_id)
        buy_item_list_at_person = buy_item_lists[person_id_inx]
        #
        buylist_set.update(buy_item_list_at_person)
    buylist_set.remove(buy_item) # {검색한 항목}은 제외
    if(debugPrint == True):
        print(f'[{buy_item}] 상품과 동시에 구매한 상품 ({len(buylist_set)}):', buylist_set)
    
    if(debugPrint == True):
        buylist_by_name = list(buylist_set)
        buylist_by_name.sort()
        print(f'[{buy_item}] 상품과 동시에 구매한 상품(이름 순서) ({len(buylist_by_name)}):', buylist_by_name)

    # 검색 '상품'과 연관된 모든 상품의 판매량 데이터 구하기
    item_reco_list = [] # fromat: [(index, count),...]
    for item in buylist_set:
        item_inx = item_list.index(item)
        person_id_list_at_item = person_id_list_by_item_key[item]
        item_count = len(person_id_list_at_item)
        # 
        item_reco_list.append((item_inx, item_count)) # find_item_tuple: [(0, 9)]
    
    #-----------------------
    # sort : 많이 팔린 순서로
    #-----------------------
    item_reco_list.sort(key=lambda x : -x[1]) # 높은 값 순서로 정렬 format:(index, count)
    if(debugPrint == True):
        print(f'(inner check) item_reco_list ({len(item_reco_list)}):', item_reco_list)
        print_selling_info__person_id_list(item_reco_list, item_list, 
            person_id_list_by_item_key, title='추천 목록 [많이 팔린 순서]')

        print_selling_info__person_id_list(item_reco_list, item_list, 
            person_id_list_by_item_key, title='추천 목록 [이름 순서]', sortByName=True)
        print(), print()
    
    # 
    return item_reco_list # item_reco_list fromat: [(index, count),...]

def check_reco_item_by_person_id2(base_person_id, reco_person_id, 
    datalists, buy_person_list, buy_item_list, debugPrint=False): 
    if(debugPrint == True):
        hgsysinc._print_function_name_(3)

    #---------------------
    #---------------------
    base_person_id_inx = buy_person_list.index(base_person_id)
    baselist = datalists[base_person_id_inx]

    reco_person_id_inx = buy_person_list.index(reco_person_id)
    recolist = datalists[reco_person_id_inx]

    #
    print(f'기준 고객ID: {base_person_id}\t추천 고객ID: {reco_person_id}')

    reco_item_inx_list = find_reco_inx__statelist(baselist, recolist, buy_item_list, debugPrint=debugPrint)
    if(debugPrint == True): # find_reco_inx__statelist()에서 내부 출력(debugPrint == True)했으면 pass
        pass
    else:
        # find_reco_inx__statelist()에서 내부 출력(debugPrint == True)하지 않으면 출력
        print(f'추천 상품 수: {len(reco_item_inx_list)}', end='\t')
        print('추천 상품(inx) 목록:', reco_item_inx_list)

        for ri, reco_inx in enumerate(reco_item_inx_list):
            print(f'{ri+1}:', buy_item_list[reco_inx], end='\t')
        if(len(reco_item_inx_list) > 0): # 불필요한 줄바뀜 출력 방지
            print() 

def check_rvalue__datalists_by_person(person_id, buy_person_list, datalists, 
    debugPrint=False): 
    if(debugPrint == True):
        hgsysinc._print_function_name_(3)

    #---------------------
    #---------------------
    if(person_id not in buy_person_list):
        print(f'{person_id} : 고객 목록에 없습니다.')
        return
    person_id_inx = buy_person_list.index(person_id)
    baselist = datalists[person_id_inx]

    #-------------------------------
    # 아래 방식은 사용하지 않는다.
    # 목록의 일부를 지우면 다른 곳에서 index 순서가 달라져서 
    # 논리적인 일관성이 없어진다. 삭제된 상태를 감안해서 
    # {person_id_inx}를 재계산하여 출력하면 문제가 없지만 
    # 여기서 출력된 {person_id_inx}값은
    # 원래 {person_id_inx}값과는 다르기 때문에 논리적인 혼선이 발생한다.
    # 이러한 혼선이 발생하지 않도록 아래 방법은 사용하지 않고
    # 대신에 hgRValue_Lists() 출력 결과에서 {person_id_inx} 부분을 
    # 제외시킨다. 그러면 이 함수에서 출력된 {person_id_inx} 것이 
    # 외부에서 출력된 것과 논리적으로 일치한다.
    #-------------------------------
    #=# 지정한 고객id를 제외한 나머지로 데이터 목록을 구성
    #=#=print(f'datalists ({len(datalists)}):')
    #=#=print(f'buy_person_list ({len(buy_person_list)}):')
    #=datalists.remove(baselist)
    #=buy_person_list.remove(person_id)
    #=#=print(f'datalists ({len(datalists)}):') # 삭제되었나 확인
    #=#=print(f'buy_person_list ({len(buy_person_list)}):') # 삭제되었나 확인
    #-------------------------------

    #---------------------
    #---------------------
    print(f'고객ID: {person_id}, 상관계수 계산')
    rvalue_list = hgRValue_Lists(baselist, datalists)
    if(len(rvalue_list) <= 0):
        return
    if(debugPrint == True):
        print(rvalue_list)
        print()

    #---------------------
    # 비교 대상에서 자기 자신을 삭제
    #---------------------
    # rvalue_list format: [(index, r-value),...]
    rvalue_list_pure = [rv_tuple for rv_tuple in rvalue_list if rv_tuple[0] != person_id_inx]
    #=print('rvalue_list_pure:', rvalue_list_pure)

    #
    #=rvalue_list_pure(rvalue_list) : 상관계수가 큰 값부터 정렬된 상태
    # datalists 없이 출력
    print_rvalue_list(rvalue_list_pure,buy_person_list, title='rvalue_list (by r-value order):')
    if(debugPrint == True):
        # datalists 포함해서 출력
        print_rvalue_list(rvalue_list_pure, buy_person_list, datalists, title='rvalue_list (by r-value order):')

    # 최댓값과 최솟값: (아래에서 {inx} 순으로 정렬(sort)하기 전에 처리)
    rvalue_list_max = rvalue_list_pure[0]
    rvalue_list_min = rvalue_list_pure[len(rvalue_list_pure) - 1]

    if(debugPrint == True):
        # sort : inx 순으로 정렬(hgRValue_Lists()함수는 r_value[1] 큰 값 순서로 정렬된 상태)
        rvalue_list_pure.sort(key=lambda x : x[0]) # {format: (index, r_value)}
        # datalists 없이 출력
        print_rvalue_list(rvalue_list_pure, buy_person_list, title='rvalue_list (by person-id order):')
        # datalists 포함해서 출력
        print_rvalue_list(rvalue_list_pure, buy_person_list, datalists, title='rvalue_list (by person-id order):')

    print('상관계수 최댓값:[%i] %.3f' %(rvalue_list_max[0], rvalue_list_max[1]))
    print('상관계수 최솟값:[%i] %.3f' %(rvalue_list_min[0], rvalue_list_min[1]))

    person_id_max = buy_person_list[rvalue_list_max[0]]
    print('상관계수 최댓값:[고객ID:%i] %.3f' %(person_id_max, rvalue_list_max[1]))

    #-------------------------------
    # 아래 방식은 사용하지 않는다.
    # 목록의 일부를 지우면 다른 곳에서 index 순서가 달라져서 
    # 논리적인 일관성이 없어진다. 삭제된 상태를 감안해서 
    # {person_id_inx}를 재계산하여 출력하면 문제가 없지만 
    # 여기서 출력된 {person_id_inx}값은
    # 원래 {person_id_inx}값과는 다르기 때문에 논리적인 혼선이 발생한다.
    # 이러한 혼선이 발생하지 않도록 아래 방법은 사용하지 않고
    # 대신에 hgRValue_Lists() 출력 결과에서 {person_id_inx} 부분을 
    # 제외시킨다. 그러면 이 함수에서 출력된 {person_id_inx} 것이 
    # 외부에서 출력된 것과 논리적으로 일치한다.
    #=#-------------------------------
    #=#---------------------
    #=#---------------------
    #=# 다음 작업을 위해서 삭제한 것을 데이터 목록을 삽입하여 복원
    #=datalists.insert(person_id_inx, baselist)
    #=buy_person_list.insert(person_id_inx, person_id)
    #-------------------------------

def check_reco_item_simple_by_person_id(person_id, buy_person_list, datalists, buy_item_list,
    debugPrint=True): 
    hgsysinc._print_function_name_(3)

    #---------------------
    #---------------------
    person_id_inx = buy_person_list.index(person_id)
    baselist = datalists[person_id_inx]

    #-------------------------------
    # 아래 방식은 사용하지 않는다.
    # 목록의 일부를 지우면 다른 곳에서 index 순서가 달라져서 
    # 논리적인 일관성이 없어진다. 삭제된 상태를 감안해서 
    # {person_id_inx}를 재계산하여 출력하면 문제가 없지만 
    # 여기서 출력된 {person_id_inx}값은
    # 원래 {person_id_inx}값과는 다르기 때문에 논리적인 혼선이 발생한다.
    # 이러한 혼선이 발생하지 않도록 아래 방법은 사용하지 않고
    # 대신에 hgRValue_Lists() 출력 결과에서 {person_id_inx} 부분을 
    # 제외시킨다. 그러면 이 함수에서 출력된 {person_id_inx} 것이 
    # 외부에서 출력된 것과 논리적으로 일치한다.
    #-------------------------------
    #=# 지정한 고객id를 제외한 나머지로 데이터 목록을 구성
    #=#=print(f'datalists ({len(datalists)}):')
    #=#=print(f'buy_person_list ({len(buy_person_list)}):')
    #=datalists.remove(baselist)
    #=buy_person_list.remove(person_id)
    #=#=print(f'datalists ({len(datalists)}):') # 삭제되었나 확인
    #=#=print(f'buy_person_list ({len(buy_person_list)}):') # 삭제되었나 확인
    #-------------------------------

    #
    print(f'고객ID: {person_id}, 상관계수 탐색')
    recommend_person_info = check_recommend_person_simple(baselist, datalists, person_id, buy_item_list, buy_person_list, debugPrint=debugPrint)
    #= recommend_person_info # format: (reco_index, r_value, reco_item_inx_list)

    #---------------------
    #---------------------
    if(debugPrint == False): # debugPrint(상태 출력) 꺼진 상태면 앞에서 출력하지 않았기 때문에 여기서 출력
        #= recommend_person_info # format: (reco_index, r_value, reco_item_inx_list)
        reco_index = recommend_person_info[0]
        r_value = recommend_person_info[1]
        reco_item_inx_list = recommend_person_info[2]

        #
        person_id_inx_reco = buy_person_list[reco_index]
        print('상관계수 최댓값:[고객ID:%i] %.4f' %(person_id_inx_reco, r_value))

        #
        print_itemlist_by_inxlist(buy_item_list, reco_item_inx_list)

    #-------------------------------
    # 아래 방식은 사용하지 않는다.
    # 목록의 일부를 지우면 다른 곳에서 index 순서가 달라져서 
    # 논리적인 일관성이 없어진다. 삭제된 상태를 감안해서 
    # {person_id_inx}를 재계산하여 출력하면 문제가 없지만 
    # 여기서 출력된 {person_id_inx}값은
    # 원래 {person_id_inx}값과는 다르기 때문에 논리적인 혼선이 발생한다.
    # 이러한 혼선이 발생하지 않도록 아래 방법은 사용하지 않고
    # 대신에 hgRValue_Lists() 출력 결과에서 {person_id_inx} 부분을 
    # 제외시킨다. 그러면 이 함수에서 출력된 {person_id_inx} 것이 
    # 외부에서 출력된 것과 논리적으로 일치한다.
    #=#-------------------------------
    #=#---------------------
    #=#---------------------
    #=# 다음 작업을 위해서 삭제한 것을 데이터 목록을 삽입하여 복원
    #=datalists.insert(person_id_inx, baselist)
    #=buy_person_list.insert(person_id_inx, person_id)
    #-------------------------------

    #
    return recommend_person_info

def check_reco_item_real_by_person_id(person_id, buy_person_list, datalists, buy_item_list,
    debugPrint=True): 
    hgsysinc._print_function_name_(3)

    #---------------------
    #---------------------
    person_id_inx = buy_person_list.index(person_id)
    baselist = datalists[person_id_inx]

    #-------------------------------
    # 아래 방식은 사용하지 않는다.
    # 목록의 일부를 지우면 다른 곳에서 index 순서가 달라져서 
    # 논리적인 일관성이 없어진다. 삭제된 상태를 감안해서 
    # {person_id_inx}를 재계산하여 출력하면 문제가 없지만 
    # 여기서 출력된 {person_id_inx}값은
    # 원래 {person_id_inx}값과는 다르기 때문에 논리적인 혼선이 발생한다.
    # 이러한 혼선이 발생하지 않도록 아래 방법은 사용하지 않고
    # 대신에 hgRValue_Lists() 출력 결과에서 {person_id_inx} 부분을 
    # 제외시킨다. 그러면 이 함수에서 출력된 {person_id_inx} 것이 
    # 외부에서 출력된 것과 논리적으로 일치한다.
    #-------------------------------
    #=# 지정한 고객id를 제외한 나머지로 데이터 목록을 구성
    #=#=print(f'datalists ({len(datalists)}):')
    #=#=print(f'buy_person_list ({len(buy_person_list)}):')
    #=datalists.remove(baselist)
    #=buy_person_list.remove(person_id)
    #=#=print(f'datalists ({len(datalists)}):') # 삭제되었나 확인
    #=#=print(f'buy_person_list ({len(buy_person_list)}):') # 삭제되었나 확인
    #-------------------------------

    #
    print(f'고객ID: {person_id}, 상관계수 탐색')
    recommend_person_info = check_recommend_person_real(baselist, datalists, person_id, buy_item_list, buy_person_list, debugPrint=debugPrint)
    #= recommend_person_info # format: (reco_index, r_value, reco_item_inx_list)

    #---------------------
    #---------------------
    if(debugPrint == False): # debugPrint(상태 출력) 꺼진 상태면 앞에서 출력하지 않았기 때문에 여기서 출력
        #= recommend_person_info # format: (reco_index, r_value, reco_item_inx_list)
        reco_index = recommend_person_info[0]
        r_value = recommend_person_info[1]
        reco_item_inx_list = recommend_person_info[2]

        #
        person_id_inx_reco = buy_person_list[reco_index]
        print('상관계수 최댓값:[고객ID:%i] %.4f' %(person_id_inx_reco, r_value))

        #
        print_itemlist_by_inxlist(buy_item_list, reco_item_inx_list)

    #-------------------------------
    # 아래 방식은 사용하지 않는다.
    # 목록의 일부를 지우면 다른 곳에서 index 순서가 달라져서 
    # 논리적인 일관성이 없어진다. 삭제된 상태를 감안해서 
    # {person_id_inx}를 재계산하여 출력하면 문제가 없지만 
    # 여기서 출력된 {person_id_inx}값은
    # 원래 {person_id_inx}값과는 다르기 때문에 논리적인 혼선이 발생한다.
    # 이러한 혼선이 발생하지 않도록 아래 방법은 사용하지 않고
    # 대신에 hgRValue_Lists() 출력 결과에서 {person_id_inx} 부분을 
    # 제외시킨다. 그러면 이 함수에서 출력된 {person_id_inx} 것이 
    # 외부에서 출력된 것과 논리적으로 일치한다.
    #=#-------------------------------
    #=#---------------------
    #=#---------------------
    #=# 다음 작업을 위해서 삭제한 것을 데이터 목록을 삽입하여 복원
    #=datalists.insert(person_id_inx, baselist)
    #=buy_person_list.insert(person_id_inx, person_id)
    #-------------------------------

    #
    return recommend_person_info

#================================
#================================
from unittest import TestCase, main

class HGTest(TestCase):
    def _test_funstat(self):
        hgsysinc._print_function_name_()

        #
        from hgstat_test_data_reff import weightlist, heightlist
        #
        print(weightlist)
        print(heightlist)
        print()

        #
        #=r_value, R2, TSS, SSE, SSR, slope, spare, avg1, avg2 = hgAnova_List(weightlist, heightlist, True)
        r_value, R2, TSS, SSE, SSR, slope, spare, avg1, avg2 = hgAnova_List(weightlist, heightlist)
        print('slope:', slope, 'spare:', spare)
        print('avg1:', avg1, 'avg2:', avg2)

        print('회귀제곱합(SSR):', SSR, '오차제곱합(SSE):', SSE, '총변동(TSS):', TSS)
        print('결정계수(R2):', R2)
        print('상관계수(r):', r_value)

#---------------------
#---------------------
if __name__ == '__main__':
    main()

