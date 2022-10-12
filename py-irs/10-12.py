import hgsysinc
from hgchartype import HGGetToken
# 하이브리 글자 타입
print(*HGGetToken("중앙亞  한미FTA  비타민A  워싱턴DC"), sep='\n')

'''
처리 결과
=============================================
{'script': 'HC', 'pos': 0, 'len': 3, 'string': '중앙亞', 'ending': {'script': 'C', 'pos': 2, 'len': 1, 'string': '亞'}}
{'script': 'S', 'pos': 3, 'len': 2, 'string': '  '}
{'script': 'HE', 'pos': 5, 'len': 5, 'string': '한미FTA', 'ending': {'script': 'E', 'pos': 7, 'len': 3, 'string': 'FTA'}}
{'script': 'S', 'pos': 10, 'len': 2, 'string': '  '}
{'script': 'HE', 'pos': 12, 'len': 4, 'string': '비타민A', 'ending': {'script': 'E', 'pos': 15, 'len': 1, 'string': 'A'}}
{'script': 'S', 'pos': 16, 'len': 2, 'string': '  '}
{'script': 'HE', 'pos': 18, 'len': 5, 'string': '워싱턴DC', 'ending': {'script': 'E', 'pos': 21, 'len': 2, 'string': 'DC'}}

'''

