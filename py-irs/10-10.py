import hgsysinc
from hgchartype import get_script_list
print(*get_script_list("서울[seoul]"), sep='\n')
print('script_list len :', len(get_script_list("서울[seoul]")))


''''
처리 결과
=============================================
{'script': 'H', 'pos': 0, 'len': 2, 'string': '서울'}
{'script': 'I', 'pos': 2, 'len': 1, 'string': '['}
{'script': 'E', 'pos': 3, 'len': 5, 'string': 'seoul'}
{'script': 'I', 'pos': 8, 'len': 1, 'string': ']'}
script_list len : 4

'''
