import hgsysinc
from hgworddistance import MakeStringNGram
from hgkbd import HGTransString2KBDJamo
from hgtest_ext_kbs import load_kbs_16_and_trans_ngram
#-----------------------
#-----------------------
ngram_k = 5
Vocabulary, NGramVocabulary = load_kbs_16_and_trans_ngram(NGram=ngram_k)
#-----------------------------
#-----------------------------
#=ngram_k = 5
FindWord = '란국' # '한국'의 철자 오류 입력
FindWord_KBDjamo = HGTransString2KBDJamo(FindWord) # 두벌식 자모로 변환
FindNGram = MakeStringNGram(FindWord_KBDjamo, NGram=ngram_k, MoreThan=True)

print(f'@@@ 순서 : 두벌식 자모 : 길이 : 포함된 어휘수 @@@')
for NGramDicNum, dic_f in enumerate(FindNGram):
    NGramDicVocabulary = NGramVocabulary.get(dic_f)
    if(NGramDicVocabulary == None): # n-gram에 속하는 단어가 없는 경우
        NGramDicVocabularyNum = 0
    else: 
        NGramDicVocabularyNum = len(NGramDicVocabulary)
    print(f'{NGramDicNum+1} : {dic_f} : {len(dic_f)} : {NGramDicVocabularyNum}')


'''
출력 결과:
-----------------------------------
이 예제는 [KBS 9시 뉴스(16년치)] 사전 목록을 사용한다.
[KBS 9시 뉴스(16년치)] 사전을 N그램(N=5) 사전으로 변환하여 N그램 추천

Dict Num: 413165
NGram Dict Num: 4125348

@@@ 순서 : 두벌식 자모 : 길이 : 포함된 어휘수 @@@
1 : ㄹㅏㄴㄱㅜ : 5 : 7
2 : ㄹㅏㄴㄱㅜㄱ : 6 : 3
3 : ㅏㄴㄱㅜㄱ : 5 : 1127


'''




