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
#=Vocabulary = load_dictfreq_Anne_of_Green_Gables()
print('word num:', len(Vocabulary))

#===================
#===================
print('# 접미사 일치 단어 목록')
find = 'ment'
print('# ㄱ) for loop')
wordlist_for = []
for word in Vocabulary:
    if word.endswith(find): # 접미사 일치
        if len(word) >= 10: # 10글자 이상
            wordlist_for.append(word)
print(f'ㄱ) wordlist_for ({len(wordlist_for)}):', wordlist_for)
print()

print('# ㄴ) comprehension')
wordlist_com = [word for word in Vocabulary if word.endswith(find) if len(word) >= 10]
print(f'ㄴ) wordlist_com ({len(wordlist_com)}):', wordlist_com)
print()


'''
출력 결과:
==================================
word num: 7427
# 접미사 일치 단어 목록
# ㄱ) for loop
ㄱ) wordlist_for (29): ['abandonment', 'accomplishment', 'achievement', 'arrangement', 'astonishment', 'bewilderment', 'commandment', 'commencement', 'compliment', 'department', 'deportment', 'development', 'disappointment', 'discouragement', 'embarrassment', 'enchantment', 'encouragement', 'engagement', 'excitement', 'experiment', 'fulfillment', 'government', 'imprisonment', 'improvement', 'parliament', 'presentiment', 'punishment', 'resentment', 'settlement']

# ㄴ) comprehension
ㄴ) wordlist_com (29): ['abandonment', 'accomplishment', 'achievement', 'arrangement', 'astonishment', 'bewilderment', 'commandment', 'commencement', 'compliment', 'department', 'deportment', 'development', 'disappointment', 'discouragement', 'embarrassment', 'enchantment', 'encouragement', 'engagement', 'excitement', 'experiment', 'fulfillment', 'government', 'imprisonment', 'improvement', 'parliament', 'presentiment', 'punishment', 'resentment', 'settlement']


'''
