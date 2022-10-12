import hgsysinc
from hgtest import load_dictfreq_kbs_2009, load_dictfreq_kbs_01_16
from hgfind import HGTrie, __Hng_AsItIs__, __Hng_2_Jamo__
from hgkbd import HGTransString2KBDJamo, HGGetJaumMoum__EngString
#-----------------------
#-----------------------
#=print('reading texts')
#=Vocabulary = load_dictfreq_kbs_2009() # [KBS 9시 뉴스: 2009년]
Vocabulary = load_dictfreq_kbs_01_16()# [KBS 9시 뉴스: 16년치(2001~2016)]
#=print('Dict Num:', len(Vocabulary))
#=print('Word Num:', sum([Vocabulary[dic] for dic in Vocabulary]))
#=print(Vocabulary)
#-----------------------------
#-----------------------------
# 트라이 생성: 어휘 사전을 트라이로 변환
TrieTest = HGTrie() 
#=# 편집 코드 조정
#=TrieTest.Opt_Hng_Fmt = __Hng_AsItIs__ # 한글: 변형없이 그대로 처리(음절)(기본값은 __Hng_2_Jamo__[한글=>두벌식자모])
#=TrieTest.MakeTrie__DictFreq(Vocabulary) # 이 함수는 이미 NGram과 한영 변환이 적용되니까 예제에서는 사용 안 함.
for CurWord in Vocabulary:
    WordFreq = Vocabulary[CurWord]
    CurWord_Low = CurWord.lower() # 소문자 변환
    KBDCharString = HGTransString2KBDJamo(CurWord_Low) # 한글->두벌식 자모
    TrieTest.InsertNode(KBDCharString, RealWord=CurWord, Weight=WordFreq)
#=TrieTest.PrintTrie()

#-----------------------------
#-----------------------------
# 트라이 추천(Suggestion)
FindWord = 'skt' # '낫' 한영 둘다 가능성
SugList_Eng = TrieTest.GetSuggestion(FindWord)
print(f'<{FindWord}> Suggest {len(SugList_Eng)}:')
print(*SugList_Eng, sep='\n')
print(), print()

#------
# 영문자 -> 두벌식 자모
#------
FindWord_KBDjamo = HGGetJaumMoum__EngString(FindWord)#'낫'(영문자->두벌식 자모)
SugList_Jamo = TrieTest.GetSuggestion(FindWord_KBDjamo)
print(f'<{FindWord}(<=={FindWord_KBDjamo})> Suggest {len(SugList_Jamo)}:')
print(*SugList_Jamo, sep='\n')
print()

print('#------')
print('# 각 추천 목록 통합')
print('#------')
# 위에서 트라이를 두벌식 자모로 변환했기 때문에 여기서 한글(__Hng_2_Jamo__) 옵션 지정
Merge_Suggest = []
TrieTest.ImportSuggestion(FindWord, 
            Merge_Suggest, SugList_Eng, HngFmt=__Hng_2_Jamo__) # 위에서 두벌식 자모로 변환했기 때문에 여기서 한글(__Hng_2_Jamo__) 옵션 지정
TrieTest.ImportSuggestion(FindWord_KBDjamo, 
            Merge_Suggest, SugList_Jamo, HngFmt=__Hng_2_Jamo__) # 위에서 두벌식 자모로 변환했기 때문에 여기서 한글(__Hng_2_Jamo__) 옵션 지정
for i, dic in enumerate(Merge_Suggest):
    print(f"{i+1}, {dic['realword']}({dic['weight']})")
print()

print('#------')
print('# 통합 추천 목록 정렬')
print('#------')
SugList_Sort = sorted(Merge_Suggest, key=lambda item: -item['weight']) # by high
for i, dic in enumerate(SugList_Sort):
    print(f"{i+1}, {dic['realword']}({dic['weight']})")



'''
출력 결과:

이 예제는 [KBS 9시 뉴스: 2009년]과 [KBS 9시 뉴스: 16년치] 사전 목록을 사용한다.

1. 'skt' 추천 결과
2. (영한 변환 후) '낫' 추천결과
3. 'skt' 추천 결과와 '낫' 추천결과를 합쳐서 정렬

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@ 16년치 KBS 9시 뉴스
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

<skt> Suggest 2:
{'word': 'skt', 'realword': 'SKT', 'weight': 84}
{'word': 'sktㄱㅡㄹㅜㅂ', 'realword': 'SKT그룹', 'weight': 1}



<skt(<==ㄴㅏㅅ)> Suggest 10:
{'word': 'ㄴㅏㅅㅓㄷㅏ', 'realword': '나서다', 'weight': 33781}
{'word': 'ㄴㅏㅅㅏ', 'realword': '나사', 'weight': 280}
{'word': 'ㄴㅏㅅㅣㄹㅣㅇㅑ', 'realword': '나시리야', 'weight': 94}
{'word': 'ㄴㅏㅅㅡㄷㅏㄱ', 'realword': '나스닥', 'weight': 89}
{'word': 'ㄴㅏㅅㅡㄷㅏㄱㅈㅣㅅㅜ', 'realword': '나스닥지수', 'weight': 46}
{'word': 'ㄴㅏㅅ', 'realword': '낫', 'weight': 34}
{'word': 'ㄴㅏㅅㅓㄴ', 'realword': '나선', 'weight': 27}
{'word': 'ㄴㅏㅅㅏㅁㅗㅅ', 'realword': '나사못', 'weight': 25}
{'word': 'ㄴㅏㅅㅓㄴㅎㅕㅇ', 'realword': '나선형', 'weight': 17}
{'word': 'ㄴㅏㅅㅡㄷㅏㄱㅅㅣㅈㅏㅇ', 'realword': '나스닥시장', 'weight': 15}

#------
# 각 추천 목록 통합
#------
1, SKT(84)
2, SKT그룹(1)
3, 나서다(33781)
4, 나사(280)
5, 나시리야(94)
6, 나스닥(89)
7, 나스닥지수(46)
8, 낫(34)
9, 나선(27)
10, 나사못(25)
11, 나선형(17)
12, 나스닥시장(15)

#------
# 통합 추천 목록 정렬
#------
1, 나서다(33781)
2, 나사(280)
3, 나시리야(94)
4, 나스닥(89)
5, SKT(84)
6, 나스닥지수(46)
7, 낫(34)
8, 나선(27)
9, 나사못(25)
10, 나선형(17)
11, 나스닥시장(15)
12, SKT그룹(1)

-----------------------------------



'''




