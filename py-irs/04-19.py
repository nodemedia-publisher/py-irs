# 컴프리헨션(comprehension) 처리 예:
from compre_base import kimchi_dict
# ㄱ)
kimchi_set_f = set()
for key in kimchi_dict:
    if(len(key) <= 3):
        kimchi_set_f.add(key)
print(f'ㄱ) kimchi_set_f ({len(kimchi_set_f)}):', kimchi_set_f)

# ㄴ)
kimchi_set_c = {key for key in kimchi_dict if(len(key) <= 3)}
print(f'ㄴ) kimchi_set_c ({len(kimchi_set_c)}):', kimchi_set_c)


'''
처리 결과:
=========================
ㄱ) kimchi_set_f (5): {'김치국', '김치독', '김치', '김치전', '김치맛'}
ㄴ) kimchi_set_c (5): {'김치국', '김치독', '김치', '김치전', '김치맛'}

'''
