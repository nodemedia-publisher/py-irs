from sort_base import dict1
# 정렬(sorted) 처리 예: dict
sort_dict1 = sorted(dict1)
print('dict1:', dict1)
print('sort_dict1:', type(sort_dict1), sort_dict1)

'''
처리 결과
===========================
dict1: {'장르': '소설', '저자': '허균', '시대': '조선', '제목': '홍길동'}
sort_dict1: <class 'list'> ['시대', '장르', '저자', '제목']
'''

