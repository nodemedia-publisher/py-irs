#---
#---
import hgsysinc
from hgstat_test import (
    find_real_max_rvalue__RValueList, find_reco_inx__statelist,
    find_recommend_item_by_item, print_selling_info__person_id_list,
)

#----------------
#----------------
def print_recommend_item_by_item(datalists, buy_item_list=None, 
    rvalue_limit = None, reco_num = 0, print_item_index=False,
    debugPrint=False):
    '''
    datalists: 이진화 상품 목록(각 상품에 대한 구매 고객은 이진 상태 목록)
    buy_item_list: 상품 목록
    rvalue_limit: 상관계수가 {rvalue_limit}보다 작으면 출력 안 함.
    reco_num: {reco_num}만큼만 출력, {reco_num=0} 모두 출력
    '''
    #-----
    # 이 함수는 전체 상품 목록을 대상을 
    # 상품을 기준으로 상관계수를 계산하여 상품을 추천한다.
    #-----
    from hgstat import hgRValueLists_Lists
    #-----
    if(debugPrint == True):
        hgsysinc._print_function_name_(3)
        #---------------------
        #---------------------
        print(f'{len(datalists)}:')
        print(*datalists, sep='\n')
        print()

    # 상관계수 계산
    SortFlag = False # 아래 hgRValueLists_Lists() 호출할 때 순차 출력을 위해서 정렬 안함
    #---
    #=SortFlag = True
    #=RValueLists = hgRValueLists_Lists(datalists, SortFlag=SortFlag, debug=True)
    #=RValueLists = hgRValueLists_Lists(datalists, SortFlag=SortFlag)
    #---
    RValueLists = hgRValueLists_Lists(datalists, SortFlag=SortFlag)
    #=print(*RValueLists, sep='\n')

    for item_inx, R_ValueList in enumerate(RValueLists):
        if(debugPrint == True):
            print('-------------------------------------')
            print('-------------------------------------')
            for j, r_value in enumerate(R_ValueList):
                index = r_value[0]
                value = r_value[1]
                if(value != None):
                    print(f'{index}:%.3f \t' % value, end='')
            print()

        # 만약 정렬하지 않았다면 최댓값을 구하기 위해서 정렬해야 한다.
        if(SortFlag == False):
            R_ValueList.sort(key=lambda x : -x[1]) # 큰 값 기준 정렬: format (index,value)
        #
        print(f'{buy_item_list[item_inx]}', end='')
        if(print_item_index == True):
            print(f'[{item_inx}]', end='')
        print(f' >> ', end='')
            
        print_num = 0 # 출력된 개수
        for ri, rvalue_item in enumerate(R_ValueList):
            r_index = rvalue_item[0] # format: [index, r_value]
            r_value = rvalue_item[1] # format: [index, r_value]
            if(item_inx == r_index): # 자기 자신은 제외하고
                continue

            # 상관계수 최젓값 적용
            if(rvalue_limit != None): # 상관계수 최젓값 적용
                if(r_value < rvalue_limit):
                    continue
            #
            print(f'{buy_item_list[r_index]}(', end='')
            if(print_item_index == True):
                print(f'{r_index}, ', end='')
            print('%.3f), ' %(r_value), end='')
            
            # 추천 개수 적용
            print_num += 1
            if(reco_num > 0): # 추천 개수 적용
                if(print_num >= reco_num):
                    break
        #
        if(reco_num <= 0): # 추천 개수 적용하지 않는 경우: 모두 출력
            print() # 모두 출력하면 항목이 많아서 구분하기 좋게 1줄 더 출력
        print()

def print_recommend_item_by_item_sell(buy_item, person_id_list, 
    buy_item_lists, item_list, person_id_list_by_item_key,
    printEditVer=False, debugPrint=False):
    #-----
    # 이 함수는 특정 상품을 구매한 고객의 구매 목록을 모두 모아서 
    # 판매량을 기준으로 추천하는 것으로 상관계수를 사용하지 않은 
    # 매우 단순하면서도 직관적인 방식이다.
    # 알고리즘을 전개할 때 도입을 위한 목적으로 만든 함수이며 
    # 실제 추천은 이 함수를 사용하지 않는다.
    #-----
    # 상품 추천 1
    #=buy_item = 'C언어'
    #=buy_item = '파이썬'

    if(debugPrint == True):
        hgsysinc._print_function_name_(3)

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

    if(debugPrint == True):
        print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
    
    if(debugPrint == True):
        print('#----------------------')
        print('# find_recommend_item_by_item() 내부 출력')
        print('#----------------------')
        # item_reco_list fromat: [(index, count),...]
        item_reco_list = find_recommend_item_by_item(buy_item, person_id_list, 
            buy_item_lists, item_list, person_id_list_by_item_key, debugPrint=True)
        print('# find_recommend_item_by_item() 끝내고 ...')
        print(),

    print('#----------------------')
    print('# 출력(구매자 목록 제외)')
    print('#----------------------')
    # item_reco_list fromat: [(index, count),...]
    item_reco_list = find_recommend_item_by_item(buy_item, person_id_list, 
        buy_item_lists, item_list, person_id_list_by_item_key)

    print_selling_info__person_id_list(item_reco_list, item_list, 
        title='추천 목록 [많이 팔린 순서]')

    print_selling_info__person_id_list(item_reco_list, item_list, 
        title='추천 목록 [이름 순서]', sortByName=True)


    if(printEditVer == True):
        print(), print()
        print('#----------')
        print('# 편집 코드')
        print('#----------')

        print('#----------------------')
        print('# 출력(구매자 목록 포함)')
        print('#----------------------')
        # item_reco_list fromat: [(index, count),...]
        item_reco_list = find_recommend_item_by_item(buy_item, person_id_list, 
            buy_item_lists, item_list, person_id_list_by_item_key)

        print_selling_info__person_id_list(item_reco_list, item_list, 
            person_id_list_by_item_key, title='추천 목록 [많이 팔린 순서]')

        print_selling_info__person_id_list(item_reco_list, item_list, 
            person_id_list_by_item_key, title='추천 목록 [이름 순서]', sortByName=True)

        print(), print()

def print_recommend_report_simple(datalists, buy_person_list=None, buy_item_list=None, 
    TableModePrint=False,
    debugPrint=False):
    #-----
    # 이 함수는 전체 고객을 대상으로 고객별 상관계수를 계산한 후 
    # 구매 성향이 비슷한 고객을 찾아서 고객별로 아직 구매하지 않은 상품을 추천한다.
    #-----
    from hgstat import hgRValueLists_Lists

    if(debugPrint == True):
        hgsysinc._print_function_name_(3)
        #---------------------
        #---------------------
        print(f'{len(datalists)}:')
        print(*datalists, sep='\n')
        print()

    # 상관계수 계산
    SortFlag = False # 아래 hgRValueLists_Lists() 호출할 때 순차 출력을 위해서 정렬 안함
    #=SortFlag = True
    #=RValueLists = hgRValueLists_Lists(datalists, SortFlag=SortFlag, debug=True)
    #=RValueLists = hgRValueLists_Lists(datalists, SortFlag=SortFlag)
    RValueLists = hgRValueLists_Lists(datalists, SortFlag=SortFlag)
    #=print(*RValueLists, sep='\n')
    
    if(TableModePrint == True):
        titles = ['base-pid', 'reco-pid', '상관계수', '추천상품수', '추천 상품 목록(ID)', '추천 상품 목록']
        print(*titles, sep='\t')

    for i, R_ValueList in enumerate(RValueLists):
        if(debugPrint == True):
            print('-------------------------------------')
            print('-------------------------------------')
            for j, r_value in enumerate(R_ValueList):
                index = r_value[0]
                value = r_value[1]
                if(value != None):
                    print(f'{index}:%.3f \t' % value, end='')
            print()

        # 만약 정렬하지 않았다면 최댓값을 구하기 위해서 정렬해야 한다.
        if(SortFlag == False):
            R_ValueList.sort(key=lambda x : -x[1]) # 큰 값 기준 정렬: format (index,value)
        #
        max_value = R_ValueList[0][1] # format: [index, r_value]
        max_index = R_ValueList[0][0] # format: [index, r_value]
        if(i == max_index): # 자기 자신은 제외하고 그 다음(2번째) 상관계수 큰 값을 선택
            max_value = R_ValueList[1][1] # format: [index, r_value]
            max_index = R_ValueList[1][0] # format: [index, r_value]

        if(debugPrint == True):
            r_listnum = len(R_ValueList)
            min_index = R_ValueList[r_listnum-1][0] # format: (index, r_value)
            min_value = R_ValueList[r_listnum-1][1] # format: (index, r_value)
            print('상관계수 최댓값:[%i] %.3f' %(max_index, max_value))
            print('상관계수 최솟값:[%i] %.3f' %(min_index, min_value))

        if(buy_person_list != None):
            if(TableModePrint == True):
                print(f'{buy_person_list[i]}[{i}]', end='\t')
                print(f'{buy_person_list[max_index]}[{max_index}]', end='\t')
                print('%.3f' %(max_value), end='\t') # {상관계수}
            else:
                print(f'{buy_person_list[i]}[{i}] >> ', end='')
                print(f'{buy_person_list[max_index]}[{max_index}] : ', end='')
                print('상관계수(%.3f)' %(max_value))
            
        if(buy_item_list != None): # 고객별 추천 상품 찾기
            baselist = datalists[i] # 현재 기준 고객 상품
            recolist = datalists[max_index] # 상관계수 최댓값 고객 상품
            reco_item_inx_list = find_reco_inx__statelist(baselist, recolist, buy_item_list, debugPrint=debugPrint)
            if(debugPrint == True):
                pass # (debugPrint == True)이면 find_reco_inx__statelist()에서 출력하니까 여기서는 생략
            else:
                if(TableModePrint == True):
                    print(f'{len(reco_item_inx_list)}', end='\t') # {추천 상품 수}
                    print(reco_item_inx_list, end='\t') # {추천 상품 목록}
                    for ri, reco_inx in enumerate(reco_item_inx_list):
                        print(f'{ri+1}:', buy_item_list[reco_inx], end=', ')
                    print() 
                else:
                    print(f'추천 상품 수: {len(reco_item_inx_list)}', end='\t')
                    print('추천 상품 목록:', reco_item_inx_list)
                    for ri, reco_inx in enumerate(reco_item_inx_list):
                        print(f'{ri+1}:', buy_item_list[reco_inx], end='\t')
                    if(len(reco_item_inx_list) > 0): # 불필요한 줄바뀜 출력 방지
                        print() 
        if(debugPrint == True):
            print()
        if(TableModePrint == True):
            pass
        else:
            print()

def print_recommend_report_real(datalists, buy_person_list=None, buy_item_list=None, 
    TableModePrint=False, 
    debugPrint=False,
    ):
    from hgstat import hgRValueLists_Lists

    if(debugPrint == True):
        hgsysinc._print_function_name_(3)
        #---------------------
        #---------------------
        print(f'datalists ({len(datalists)}):')
        print(*datalists, sep='\n')
        print()

    # 상관계수 계산
    SortFlag = False # 아래 hgRValueLists_Lists() 호출할 때 순차 출력을 위해서 정렬 안함
    #=SortFlag = True
    #=RValueLists = hgRValueLists_Lists(datalists, SortFlag=SortFlag, debug=True)
    #=RValueLists = hgRValueLists_Lists(datalists, SortFlag=SortFlag)
    RValueLists = hgRValueLists_Lists(datalists, SortFlag=SortFlag)
    #=print(*RValueLists, sep='\n')

    if(TableModePrint == True):
        titles = ['base-pid', 'reco-pid', '상관계수', '추천상품수', '추천 상품 목록(ID)', '추천 상품 목록']
        print(*titles, sep='\t')

    for i, R_ValueList in enumerate(RValueLists):
        if(debugPrint == True):
            print('-------------------------------------')
            print('-------------------------------------')
            for j, r_value in enumerate(R_ValueList):
                index = r_value[0] # format: (index, r_value)
                value = r_value[1] # format: (index, r_value)
                if(value != None):
                    print(f'{index}:%.3f \t' % value, end='')
            print()

        # 만약 정렬하지 않았다면 최댓값을 구하기 위해서 정렬해야 한다.
        if(SortFlag == False):
            R_ValueList.sort(key=lambda x : -x[1]) # 큰 값 기준 정렬: format(index,value)

        #--------------------------------------------
        # 아래 방식의 경우에는 (자신을 제외하고) 무조건 상관계수가 큰 것을 선택하는데 
        # 이 방식의 경우에 선택된 고객의 상품이 찾는 사람보다 적은 경우가 있다.
        # 이럴 경우에는 추천할 상품이 없게 되므르 
        # 실제로 추천할 상품이 있는 (첫 번째) 추천 인덱스를 찾아야 한다.
        #--------------------------------------------
        #=max_index = R_ValueList[0][0] # format: (index, r_value)
        #=max_value = R_ValueList[0][1] # format: (index, r_value)
        #=if(i == max_index): # 자기 자신은 제외, 그 다음(2번째) 상관계수 큰 값을 선택
        #=    max_index = R_ValueList[1][0] # format: (index, r_value)
        #=    max_value = R_ValueList[1][1] # format: (index, r_value)
        #--------------------------------------------
        #---
        baselist = datalists[i]
        real_max_rvalue=find_real_max_rvalue__RValueList(baselist,datalists,R_ValueList, debugPrint=debugPrint)
        if(real_max_rvalue == None):
            if(buy_item_list != None):
                print(f'추천 상품 수: 없음', end='\t')
                print('추천 상품 목록: 없음')
            continue
        #
        max_index = real_max_rvalue[0] # format: (index, r_value)
        max_value = real_max_rvalue[1] # format: (index, r_value)
        
        if(debugPrint == True):
            r_listnum = len(R_ValueList)
            min_index = R_ValueList[r_listnum-1][0] # format: (index, r_value)
            min_value = R_ValueList[r_listnum-1][1] # format: (index, r_value)
            print('상관계수 최댓값:[%i] %.3f' %(max_index, max_value))
            print('상관계수 최솟값:[%i] %.3f' %(min_index, min_value))

        if(buy_person_list != None):
            if(TableModePrint == True):
                print(f'{buy_person_list[i]}[{i}]', end='\t')
                print(f'{buy_person_list[max_index]}[{max_index}]', end='\t')
                print('%.3f' %(max_value), end='\t') # {상관계수}
            else:
                print(f'{buy_person_list[i]}[{i}] >> ', end='')
                print(f'{buy_person_list[max_index]}[{max_index}] : ', end='')
                print('상관계수(%.3f)' %(max_value))

        if(buy_item_list != None): # 고객별 추천 상품 찾기
            recolist = datalists[max_index] # 상관계수 최댓값 고객 상품
            reco_item_inx_list = find_reco_inx__statelist(baselist, recolist, buy_item_list, debugPrint=debugPrint)
            if(debugPrint == True):
                pass # (debugPrint == True)이면 find_reco_inx__statelist()에서 출력하니까 여기서는 생략
            else:
                if(TableModePrint == True):
                    print(f'{len(reco_item_inx_list)}', end='\t') # {추천 상품 수}
                    print(reco_item_inx_list, end='\t') # {추천 상품 목록}
                    for ri, reco_inx in enumerate(reco_item_inx_list):
                        print(f'{ri+1}:', buy_item_list[reco_inx], end=', ')
                    print() 
                else:
                    print(f'추천 상품 수: {len(reco_item_inx_list)}', end='\t')
                    print('추천 상품 목록:', reco_item_inx_list)
                    for ri, reco_inx in enumerate(reco_item_inx_list):
                        print(f'{ri+1}:', buy_item_list[reco_inx], end='\t')
                    if(len(reco_item_inx_list) > 0): # 불필요한 줄바뀜 출력 방지
                        print() 
        #
        if(debugPrint == True):
            print()
        if(TableModePrint == True):
            pass
        else:
            print()

def print_report_item_sell_by_datalists(datalists, buy_item_list):
    from hgstat import hgTranspose_Lists, hgNonZeroCount

    # 고객별 상품(상태) 목록을 상품별 고객 목록으로 변환(전치:transpose)
    item_lists_by_person = hgTranspose_Lists(datalists) #상품별 구입 고객 목록(판매 실적)

    print('-------------------------------------')
    print('--------------row list----------------')
    print('-------------------------------------')
    print(f'item_lists_by_person ({len(item_lists_by_person)}):')
    print(*item_lists_by_person, sep='\n')
    print()
    print()
    print()

    print('상품 인덱스 순서')
    print('순서\t상품인덱스\t상품명\t고객 수\t고객 목록')

    item_count_list = []
    for item_inx, row in enumerate(item_lists_by_person):
        non_zero_item_num = hgNonZeroCount(row)
        print(f'{item_inx+1}\t{item_inx}\t{buy_item_list[item_inx]}\t{non_zero_item_num}\t{row}')
        
        #
        BuyItem = buy_item_list[item_inx]
        BuyCount = hgNonZeroCount(item_lists_by_person[item_inx])
        item_count_list.append((item_inx, BuyCount, BuyItem)) 
    print()
    
    # 판매 순으로 정렬해서 다시 출력
    # format : [(item_inx, BuyCount, BuyItem),...]
    item_count_list.sort(key=lambda rc: -rc[1]) # 튜플 2번째 값, 큰 값 순서로 정렬(구매수)

    print('판매 실적 순서')
    print('순서\t상품인덱스\t상품명\t고객 수\t고객 목록')
    for ri, item in enumerate(item_count_list):
        item_inx = item[0]
        BuyCount = item[1]
        BuyItem = item[2]
        PersonList_by_Item = item_lists_by_person[item_inx]
        print(f'{ri+1}\t{BuyItem}\t{item_inx}\t{BuyCount}\t{PersonList_by_Item}')
    print()
    print()

def print_recommend_report__RValueLists_by_sell(RValueLists, datalists, 
    buy_item_list, buy_person_list, printType=0, debugPrint=False):
    from hgstat import hgTranspose_Lists, hgNonZeroCount

    # 고객별 상품(상태) 목록을 상품별 고객 목록으로 변환(전치:transpose)
    item_lists_by_person = hgTranspose_Lists(datalists) #상품별 구입 고객 목록(판매 실적)
    if(debugPrint == True):
        print_report_item_sell_by_datalists(datalists, buy_item_list)

    #
    if(printType == 1):
        print('고객ID(고객ID inx)\t추천 고객ID(고객ID inx)\t상관계수\t상품 수\t추천 상품 목록')
    elif(printType == 2):
        print('고객ID\t추천 고객ID\t상관계수\t상품 수\t추천 상품 목록')
    else:    
        print('고객ID\t고객ID inx\t추천 고객ID\t추천 고객ID inx\t상관계수\t상품 수\t추천 상품 목록')

    for i, R_ValueList in enumerate(RValueLists):
        # 만약 정렬하지 않았다면 최댓값을 구하기 위해서 정렬해야 한다.
        R_ValueList.sort(key=lambda x : -x[1]) # 높은 값을 기준으로 정렬

        #---
        baselist = datalists[i]
        real_max_rvalue=find_real_max_rvalue__RValueList(baselist,datalists,R_ValueList, debugPrint=False) # 여기서는 debugPrint=False
        if(real_max_rvalue == None):
            if(buy_item_list != None):
                print(f'추천 상품 수: 없음', end='\t')
                print('추천 상품 목록: 없음')
            continue
        #
        max_index = real_max_rvalue[0] # format: (index, r_value)
        max_value = real_max_rvalue[1] # format: (index, r_value)

        #
        baselist = datalists[i]
        recolist = datalists[max_index]
        if(buy_person_list != None):
            if(printType == 1):
                #=print('고객ID(고객ID inx)\t추천 고객ID(고객ID inx)\t상관계수 최댓값\t상품 수\t추천 상품 목록')
                print(f'{buy_person_list[i]}({i})', end='\t')
                print(f'{buy_person_list[max_index]}({max_index})', end='\t')
                print('%.3f' %(max_value), end='\t')
            elif(printType == 2):
                #=print('고객ID\t추천 고객ID\t상관계수 최댓값\t상품 수\t추천 상품 목록')
                print(f'{buy_person_list[i]}', end='\t')
                print(f'{buy_person_list[max_index]}', end='\t')
                print('%.3f' %(max_value), end='\t')
            else:    
                #=print('고객ID\t고객ID inx\t추천 고객ID\t추천 고객ID inx\t상관계수 최댓값\t상품 수\t추천 상품 목록')
                print(f'{buy_person_list[i]}\t{i}', end='\t')
                print(f'{buy_person_list[max_index]}\t{max_index}', end='\t')
                print('%.3f' %(max_value), end='\t')


        if(buy_item_list != None):
            #=reco_item_inx_list=find_reco_inx__statelist(baselist,recolist,buy_item_list, debugPrint=True)
            reco_item_inx_list=find_reco_inx__statelist(baselist,recolist,buy_item_list)
            item_count_list = []
            for item_inx in reco_item_inx_list:
                BuyItem = buy_item_list[item_inx]
                BuyCount = hgNonZeroCount(item_lists_by_person[item_inx])
                item_count_list.append((item_inx, BuyCount, BuyItem)) 

            # format : [(reco_item_inx, BuyCount, BuyItem),...]
            item_count_list.sort(key=lambda rc: -rc[1]) # 튜플 2번째 값, 큰 값 순서로 정렬(구매수)

            # 판매 순위로 정렬된 상품을 출력
            print(f'{len(item_count_list)}', end='\t')
            #=print('추천 상품 목록:', item_count_list)
            for ri, item in enumerate(item_count_list):
                print(f'{ri+1}:{item[2]}', end=', ') # 상품명: 튜플 2번째 값
            if(len(item_count_list) > 0): # 불필요한 줄바뀜 출력 방지
                print() 
    #
    print()        
    print()

def print_recommend_report_by_sell(datalists, 
    buy_item_by_person_inx_list, # 상품 목록(각 항목은 구매 고객 index 목록)
    buy_person_list=None, buy_item_list=None, 
    TableModePrint=False, 
    debugPrint=False,
    ):
    from hgstat import hgRValueLists_Lists
    
    if(debugPrint == True):
        hgsysinc._print_function_name_(3)
        #---------------------
        #---------------------
        print(f'{len(datalists)}:')
        print(*datalists, sep='\n')
        print()

    if(debugPrint == True):
        print_report_item_sell_by_datalists(datalists, buy_item_list)

    # 상관계수 계산
    SortFlag = False # 아래 hgRValueLists_Lists() 호출할 때 순차 출력을 위해서 정렬 안함
    #---
    #=SortFlag = True
    #=RValueLists = hgRValueLists_Lists(datalists, SortFlag=SortFlag, debug=True)
    #=RValueLists = hgRValueLists_Lists(datalists, SortFlag=SortFlag)
    #---
    RValueLists = hgRValueLists_Lists(datalists, SortFlag=SortFlag)
    #=print(*RValueLists, sep='\n')

    if(TableModePrint == True):
        titles = ['base-pid', 'reco-pid', '상관계수', '추천상품수', '추천 상품 목록']
        print(*titles, sep='\t')

    for i, R_ValueList in enumerate(RValueLists):
        if(debugPrint == True):
            print('-------------------------------------')
            print('-------------------------------------')
            for j, r_value in enumerate(R_ValueList):
                index = r_value[0]
                value = r_value[1]
                if(value != None):
                    print(f'{index}:%.3f \t' % value, end='')
            print()

        # 만약 정렬하지 않았다면 최댓값을 구하기 위해서 정렬해야 한다.
        if(SortFlag == False):
            R_ValueList.sort(key=lambda x : -x[1]) # 높은 값을 기준으로 정렬

        #--------------------------------------------
        # 아래 방식의 경우에는 (자신을 제외하고) 무조건 상관계수가 큰 것을 선택하는데 
        # 이 방식의 경우에 선택된 고객의 상품이 찾는 사람보다 적은 경우가 있다.
        # 이럴 경우에는 추천할 상품이 없게 되므르 
        # 실제로 추천할 상품이 있는 (첫 번째) 추천 인덱스를 찾아야 한다.
        #--------------------------------------------
        #=max_index = R_ValueList[0][0] # format: (index, r_value)
        #=max_value = R_ValueList[0][1] # format: (index, r_value)
        #=if(i == max_index): # 자기 자신은 제외, 그 다음(2번째) 상관계수 큰 값을 선택
        #=    max_index = R_ValueList[1][0] # format: (index, r_value)
        #=    max_value = R_ValueList[1][1] # format: (index, r_value)
        #--------------------------------------------
        baselist = datalists[i]
        real_max_rvalue=find_real_max_rvalue__RValueList(baselist,datalists,R_ValueList, debugPrint=debugPrint)
        if(real_max_rvalue == None):
            if(buy_item_list != None):
                print(f'추천 상품 수: 없음', end='\t')
                print('추천 상품 목록: 없음')
            continue
        #
        max_index = real_max_rvalue[0] # format: (index, r_value)
        max_value = real_max_rvalue[1] # format: (index, r_value)

        #
        if(debugPrint == True):
            r_listnum = len(R_ValueList)
            min_index = R_ValueList[r_listnum-1][0] # format: (index, r_value)
            min_value = R_ValueList[r_listnum-1][1] # format: (index, r_value)
            print('상관계수 최댓값:[%i] %.3f' %(max_index, max_value))
            print('상관계수 최솟값:[%i] %.3f' %(min_index, min_value))
            print()

        #
        baselist = datalists[i]
        recolist = datalists[max_index]
        if(debugPrint == True):
            print(f'기준값[{i}] ({len(baselist)}) :', baselist)
            print(f'추천값[{max_index}] ({len(recolist)}) :', recolist)

        if(buy_person_list != None):
            if(TableModePrint == True):
                print(f'{buy_person_list[i]}[{i}]', end='\t')
                print(f'{buy_person_list[max_index]}[{max_index}]', end='\t')
                print('%.3f' %(max_value), end='\t') # {상관계수}
            else:
                print(f'{buy_person_list[i]}[{i}] >> ', end='')
                print(f'{buy_person_list[max_index]}[{max_index}] : ', end='')
                print('상관계수(%.3f)' %(max_value))

        if(buy_item_list != None):
            # 추천 상품 판매량 목록을 구한 후에 정렬
            #=reco_item_inx_list=find_reco_inx__statelist(baselist,recolist,buy_item_list, debugPrint=True)
            reco_item_inx_list = find_reco_inx__statelist(baselist, recolist, buy_item_list)
            item_count_list = [] # 상품 판매량 목록
            for item_inx in reco_item_inx_list:
                BuyItem = buy_item_list[item_inx]
                BuyCount = len(buy_item_by_person_inx_list[BuyItem])
                item_count_list.append((item_inx, BuyCount, BuyItem)) 

            # format : [(reco_item_inx, BuyCount, BuyItem),...]
            item_count_list.sort(key=lambda rc: -rc[1]) # 튜플 2번째 값, 큰 값 순서로 정렬(구매수)

            # 판매 순위로 정렬된 상품을 출력
            if(TableModePrint == True):
                print(f'{len(item_count_list)}', end='\t') # {추천 상품 수}
                #=print(item_count_list, end='\t') # {추천 상품 목록}
                #='추천 상품 목록:'
                for ri, item in enumerate(item_count_list):
                    print(f'{ri+1}:{item[2]}', end=', ') # 상품명: 튜플 2번째 값
                print() 
            else:
                print(f'추천 상품 수: {len(item_count_list)}', end='\t')
                #=print('추천 상품 목록:', item_count_list)
                print('추천 상품 목록:')
                if(debugPrint == True):
                    print(*item_count_list, sep='\n')
                for ri, item in enumerate(item_count_list):
                    print(f'{ri+1}:{item[2]}', end='\t') # 상품명: 튜플 [2]번째 값
                if(len(item_count_list) > 0): # 불필요한 줄바뀜 출력 방지
                    print() 
        #
        if(debugPrint == True):
            print()
        if(TableModePrint == True):
            pass
        else:
            print()

    if(debugPrint == True):
        print('-------------------------')
        print('# 편집 코드')
        print('-------------------------')
        #=print('고객ID(고객ID inx)\t추천 고객ID(고객ID inx)\t상관계수 최댓값\t상품 수\t추천 상품 목록')
        print_recommend_report__RValueLists_by_sell(RValueLists, datalists, 
            buy_item_list, buy_person_list, printType=1)

        print('-------------------------')
        print('# 편집 코드 - 추가로 다른 버전')
        print('-------------------------')
        #=print('고객ID\t추천 고객ID\t상관계수 최댓값\t상품 수\t추천 상품 목록')
        print_recommend_report__RValueLists_by_sell(RValueLists, datalists, 
            buy_item_list, buy_person_list, printType=2)

        print('-------------------------')
        print('# 편집 코드 - 또 추가로 다른 버전')
        print('-------------------------')
        #=print('고객ID\t고객ID inx\t추천 고객ID\t추천 고객ID inx\t상관계수 최댓값\t상품 수\t추천 상품 목록')
        print_recommend_report__RValueLists_by_sell(RValueLists, datalists, 
            buy_item_list, buy_person_list, printType=0)


#================================
#================================
from unittest import TestCase, main

class HGTest(TestCase):
    def test_funstat(self):
        hgsysinc._print_function_name_()

        #
        print()

#---------------------
#---------------------
if __name__ == '__main__':
    main()

