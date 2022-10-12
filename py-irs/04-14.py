from sort_base import dict1
# 정렬(sorted) 처리 예: dict
# ㄱ) 
sort_keys = sorted(dict1.keys())
sort_dict_keys = {}
for key in sort_keys:
    sort_dict_keys[key] = dict1[key]
print('ㄱ) sort_dict_keys:', sort_dict_keys)

# ㄴ)
sort_items = sorted(dict1.items()) # (key, value)
sort_dict_items = {}
for key, value in sort_items:
    sort_dict_items[key] = value
print('ㄴ) sort_dict_items:', sort_dict_items)

# ㄷ)
sort_dict_items = {}
for item in sort_items:
    key = item[0]
    value = item[1]
    sort_dict_items[key] = value
print('ㄷ) sort_dict_items:', sort_dict_items)

# ㄹ)
sort_dict_items = dict(sorted(dict1.items())) # (key, value)
print('ㄹ) sort_dict_items:', sort_dict_items)


'''
처리 결과
===========================
ㄱ) sort_dict_keys: {'시대': '조선', '장르': '소설', '저자': '허균', '제목': '홍길동'}
ㄴ) sort_dict_items: {'시대': '조선', '장르': '소설', '저자': '허균', '제목': '홍길동'}
ㄷ) sort_dict_items: {'시대': '조선', '장르': '소설', '저자': '허균', '제목': '홍길동'}
ㄹ) sort_dict_items: {'시대': '조선', '장르': '소설', '저자': '허균', '제목': '홍길동'}

'''

