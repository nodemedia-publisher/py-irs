# 컴프리헨션(comprehension) 처리 예:
from compre_base import dict_lov1
# by rev-value (key, value)
dict_sort_list = sorted(dict_lov1.items(), key=lambda item:-item[1]) # by rev-value

# ㄱ)
dict_sort_d = dict(dict_sort_list)
print('ㄱ) dict_sort_d:', dict_sort_d)

# ㄴ)
dict_sort_f = {}
for key, value in dict_sort_list:
    dict_sort_f[key] = value
print('ㄴ) dict_sort_f:', dict_sort_f)

# ㄷ)
dict_sort_c1 = {key:value for key, value in dict_sort_list}
print('ㄷ) dict_sort_c1:', dict_sort_c1)

# ㄹ) 
dict_sort_c2 = {key:value for key, value in 
        sorted(dict_lov1.items(), key=lambda item:-item[1])} # by rev-value
print('ㄹ) dict_sort_c2:', dict_sort_c2) 



'''
처리 결과:
=========================
ㄱ) dict_sort_d: {'love': 71, 'lovely': 64, 'loved': 15, 'lover': 13, 'loveliest': 9, 'loving': 7, 'lovers': 5, 'loveliness': 4, 'lovelier': 1, 'lovemaking': 1, 'loves': 1}
ㄴ) dict_sort_f: {'love': 71, 'lovely': 64, 'loved': 15, 'lover': 13, 'loveliest': 9, 'loving': 7, 'lovers': 5, 'loveliness': 4, 'lovelier': 1, 'lovemaking': 1, 'loves': 1}
ㄷ) dict_sort_c1: {'love': 71, 'lovely': 64, 'loved': 15, 'lover': 13, 'loveliest': 9, 'loving': 7, 'lovers': 5, 'loveliness': 4, 'lovelier': 1, 'lovemaking': 1, 'loves': 1}
ㄹ) dict_sort_c2: {'love': 71, 'lovely': 64, 'loved': 15, 'lover': 13, 'loveliest': 9, 'loving': 7, 'lovers': 5, 'loveliness': 4, 'lovelier': 1, 'lovemaking': 1, 'loves': 1}

'''
