# 컴프리헨션(comprehension) 처리 예:

wordlist101 = ['조사', '다람쥐', '흙', '값', '형태', '여덟', '체언', '갈매기', '하와이', '용언']

tuple1 = ('조사', '흙', '값', '형태', '여덟', '하와이', '체언', '기러기', '용언')

set1 = {'조사', '흙', '값', '형태', '여덟', '하와이', '체언', '기러기', '용언'}
set11 = {'김치맛', '김치비빔국수', '김치축제', '김치국', '김치제조업체', '김치담그기', '김치업체', 
    '김치독', '김치냉장고', '김치파동', '김치시장', '김치유산균', '김치찌게', '김치코너', '김치찌개', 
    '김치전', '김치볶음밥', '김치', '김치공장', '김치지수', '김치양념', '김치전골',
}
#@@@ 아래는 임시로 출력한 것
#=print(*set11, sep='\n')
#=for item in set11:
#=    print(f"'{item}':{kimchi_dict[item]},")

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#@@@@@ {kimchi_dict} 변수는 {sort_base.py}와 {compre_base.py}에 
#@@@@@ 동시에 선언되었으므로 변경할 경우에 신경 써야 한다.
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# '김치'로 시작하는 단어 빈도 사전
kimchi_dict ={'김치지수':2, '김치냉장고':82, '김치유산균':16, '김치국':1, '김치전':3, 
    '김치제조업체':13, '김치':1578, '김치볶음밥':9, '김치찌게':5, '김치업체':12,
    '김치전골':1, '김치비빔국수':1, '김치파동':38, '김치찌개':38, '김치축제':5, '김치공장':40, 
    '김치독':3, '김치맛':28, '김치시장':15, '김치담그기':18, '김치양념':5, '김치코너':2,
}
#@@@ 아래는 임시로 출력한 것
#=print(*kimchi_dict, sep='\n')
#=for key in kimchi_dict:
#=    print(f'{key}', end=', ')


# 'lov'로 시작하는 단어 빈도 목록
dict_lov = {'love': 71, 'loved': 15, 'lovelier': 1, 'loveliest': 9, 'loveliness': 4, 'lovely': 64, 'lovemaking': 1, 'lover': 13, 'lovers': 5, 'loves': 1, 'loving': 7}

#=set_lov = set(dict_lov.keys())
#=print(set_lov)
set_lov = {'loves', 'lovelier', 'loveliness', 'lovers', 'lover', 'loveliest', 'love', 'loving', 'loved', 'lovely', 'lovemaking'}

#=dict_lov1 = {word:dict_lov[word] for word in set_lov}
#=print(dict_lov1) # 정렬되지 않은 상태
dict_lov1 = {'lovelier': 1, 'lovers': 5, 'loving': 7, 'lover': 13, 'lovely': 64, 'lovemaking': 1, 'loved': 15, 'loveliness': 4, 'loves': 1, 'love': 71, 'loveliest': 9}

#=kimchi_list = [key for key in kimchi_dict]
#=print(kimchi_list)
kimchi_list = ['김치지수', '김치냉장고', '김치유산균', '김치국', '김치전', '김치제조업체', '김치', '김치볶음밥', '김치찌게', '김치업체', '김치전골', '김치비빔국수', '김치파동', '김치찌개', '김치축제', '김치공장', '김치독', '김치맛', '김치시장', '김치담그기', '김치양념', '김치코너']
