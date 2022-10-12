#-----------------------------
#-----------------------------
import hgsysinc
from hgtest import load_dictfreq_Anne_of_Green_Gables

#-----------------------------
#-----------------------------
# 이상한 나라의 앨리스
#=Vocabulary = load_dictfreq_Alice_Adventures() # 이상한 나라의 앨리스

# 빨강 머리 앤
Vocabulary = load_dictfreq_Anne_of_Green_Gables() # 빨강 머리 앤
print('word num:', len(Vocabulary))

#===================
#===================
print('# 접두사 일치 단어 목록')
find = 'lov'
print('# ㄱ) for loop')
wordlist_for = []
for word in Vocabulary:
    if word.startswith(find):
        wordlist_for.append(word)
print(f'ㄱ) wordlist_for ({len(wordlist_for)}):', wordlist_for)
print()

print('# ㄴ) comprehension')
wordlist_com = [word for word in Vocabulary if word.startswith(find)]
print(f'ㄴ) wordlist_com ({len(wordlist_com)}):', wordlist_com)
print()



'''
출력 결과:
==================================
word num: 7427
# 접두사 일치 단어 목록
ㄱ) wordlist_for (11): ['love', 'loved', 'lovelier', 'loveliest', 'loveliness', 'lovely', 'lovemaking', 'lover', 'lovers', 'loves', 'loving']

# ㄴ) comprehension
ㄴ) wordlist_com (11): ['love', 'loved', 'lovelier', 'loveliest', 'loveliness', 'lovely', 'lovemaking', 'lover', 'lovers', 'loves', 'loving']

'''
