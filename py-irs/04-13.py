from sort_base import dict1
# 정렬(sorted) 처리 예: dict
# ㄱ) 
sort_keys = sorted(dict1.keys())
print('ㄱ) sort_keys:', sort_keys)
print('ㄱ) sorted(dict1):', sorted(dict1))
# ㄴ)
sort_values = sorted(dict1.values())
print('ㄴ) sort_values:', sort_values)
# ㄷ) 
sort_items = sorted(dict1.items()) # (key, value)
print('ㄷ) sort_items:', sort_items)


'''
처리 결과
===========================
ㄱ) sort_keys: ['시대', '장르', '저자', '제목']
ㄱ) sorted(dict1): ['시대', '장르', '저자', '제목']
ㄴ) sort_values: ['소설', '조선', '허균', '홍길동']
ㄷ) sort_items: [('시대', '조선'), ('장르', '소설'), ('저자', '허균'), ('제목', '홍길동')]

'''

