import hgsysinc
from hgchartype import get_script_list
# 하이브리 글자 타입
print(*get_script_list("중앙亞  한미FTA  비타민A  워싱턴DC"), sep='\n')
print('len:', len("중앙亞  한미FTA  비타민A  워싱턴DC"))


'''
처리 결과
=============================================
{'script': 'H', 'pos': 0, 'len': 2, 'string': '중앙'}
{'script': 'C', 'pos': 2, 'len': 1, 'string': '亞'}
{'script': 'S', 'pos': 3, 'len': 2, 'string': '  '}
{'script': 'H', 'pos': 5, 'len': 2, 'string': '한미'}
{'script': 'E', 'pos': 7, 'len': 3, 'string': 'FTA'}
{'script': 'S', 'pos': 10, 'len': 2, 'string': '  '}
{'script': 'H', 'pos': 12, 'len': 3, 'string': '비타민'}
{'script': 'E', 'pos': 15, 'len': 1, 'string': 'A'}
{'script': 'S', 'pos': 16, 'len': 2, 'string': '  '}
{'script': 'H', 'pos': 18, 'len': 3, 'string': '워싱턴'}
{'script': 'E', 'pos': 21, 'len': 2, 'string': 'DC'}
len: 23
'''

