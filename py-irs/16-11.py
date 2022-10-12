import hgsysinc
from hgtest import load_dictfreq_kbs_2009
from hgtest import load_dictfreq_kbs_01_16
from hgfind import HGTrie, WeightSuggestList_SameWeight, __Hng_2_Jamo__
from hgkbd import HGTransString2KBDJamo
#---------------
#---------------
#=print('reading texts')
#=Vocabulary = load_dictfreq_kbs_2009() # [KBS 9시 뉴스: 2009년]
Vocabulary = load_dictfreq_kbs_01_16() # [KBS 9시 뉴스: 16년치(2001~2016)]
#=print('Dict Num:', len(Vocabulary))
#=print('Word Num:', sum([Vocabulary[dic] for dic in Vocabulary]))
#=print(Vocabulary)
#-----------------------------
#-----------------------------
# 트라이 생성: 어휘 사전을 트라이로 변환
TrieTest = HGTrie() 
#=TrieTest.MakeTrie__DictFreq(Vocabulary) # 이 함수는 이미 NGram과 한영 변환이 적용되니까 예제에서는 사용 안 함.
for CurWord in Vocabulary:
    WordFreq = Vocabulary[CurWord]
    KBDCharString = HGTransString2KBDJamo(CurWord) # 한글 음절->두벌식 자모 변환
    #=TrieTest.InsertWord(CurWord, Weight=WordFreq) # RealWord=? 사용하지 않는 버전
    TrieTest.InsertNode(KBDCharString, RealWord=CurWord, Weight=WordFreq)
#=TrieTest.PrintTrie()
#-----------------------------
#-----------------------------
# 트라이 추천(Suggestion)
FindWord = '한국방송'
FindWord_KBDjamo = HGTransString2KBDJamo(FindWord) # 한글 음절->두벌식 자모 변환
SugList = TrieTest.FindWord(FindWord_KBDjamo)
#=print(len(SugList), ':', SugList)

SugList_Sort = sorted(SugList, key=lambda item: -item['weight']) # by high
#=print(len(SugList_Sort), ':', SugList_Sort)
print(f'<{FindWord}(<==={FindWord_KBDjamo})> Suggest {len(SugList_Sort)}:')
#=print(f'<{FindWord}> Suggest {len(SugList_Sort)}:')
print(*SugList_Sort[:12], sep='\n') # 12개까지 출력

#-----------------------------
#----------------------------- 
# 지정한 추천 개수 초과 검사
SuggestNum = 10
if(len(SugList_Sort) > SuggestNum): # 추천 단어 초과
    # 맨 끝쪽에 가중치(빈도)가 같은 단어가 여럿이 있는 경우 - 2차 가중치 처리
    #=print('len(SugList_Sort):', len(SugList_Sort))
    #-----
    #=WeightSuggestList_SameWeight(FindWord, SugList_Sort, SuggestNum) # {FindWord} 한글 음절이라서 계산 틀림.
    #-----
    # 한글: 두벌식(키보드) 자모로 처리(TrieTest에 등록할 때 두벌식으로 했기 때문)
    WeightSuggestList_SameWeight(FindWord_KBDjamo, 
        SugList_Sort, SuggestNum, HngFmt=__Hng_2_Jamo__) 

    # {SuggestNum}을 초과한 것은 삭제
    #= SugList_Sort = SugList_Sort[:SuggestNum] # 외부에서 넘어올 때는 직접 전달하면 함수 밖에서 사라진다.
    while(True):
        if(len(SugList_Sort) > SuggestNum):
            #=print('SugList_Sort[-1]:', SugList_Sort[-1])
            del SugList_Sort[-1]
        else:
            break
    #=print('len(SugList_Sort):', len(SugList_Sort))
print(f'<{FindWord}(<==={FindWord_KBDjamo})> Suggest {len(SugList_Sort)}:')
#=print(f'<{FindWord}> Suggest {len(SugList_Sort)}:')
#=print(*SugList_Sort, sep='\n') # 모두 출력

for i, x in enumerate(SugList_Sort):
    print(f"{i+1}, {x['realword']}({x['weight']})")




'''
출력 결과:
=============================================
이 예제는 [KBS 9시 뉴스 16년치] 사전 목록을 사용한다.

한글 음절로 된 단어를 두벌식 자모로 변환하여 트라이를 생성한다.
=============================================

<한국방송(<===ㅎㅏㄴㄱㅜㄱㅂㅏㅇㅅㅗㅇ)> Suggest 17:
{'word': 'ㅎㅏㄴㄱㅜㄱㅂㅏㅇㅅㅗㅇㅎㅕㅂㅎㅗㅣ', 'realword': '한국방송협회', 'weight': 67}
{'word': 'ㅎㅏㄴㄱㅜㄱㅂㅏㅇㅅㅗㅇㄷㅐㅅㅏㅇ', 'realword': '한국방송대상', 'weight': 25}
{'word': 'ㅎㅏㄴㄱㅜㄱㅂㅏㅇㅅㅗㅇㄱㅣㅈㅏㅋㅡㄹㄹㅓㅂ', 'realword': '한국방송기자클럽', 'weight': 22}
{'word': 'ㅎㅏㄴㄱㅜㄱㅂㅏㅇㅅㅗㅇㄱㅗㅏㅇㄱㅗㄱㅗㅇㅅㅏ', 'realword': '한국방송광고공사', 'weight': 19}
{'word': 'ㅎㅏㄴㄱㅜㄱㅂㅏㅇㅅㅗㅇㅎㅕㅂㅎㅗㅣㅈㅏㅇ', 'realword': '한국방송협회장', 'weight': 13}
{'word': 'ㅎㅏㄴㄱㅜㄱㅂㅏㅇㅅㅗㅇㅎㅏㄱㅎㅗㅣ', 'realword': '한국방송학회', 'weight': 12}
{'word': 'ㅎㅏㄴㄱㅜㄱㅂㅏㅇㅅㅗㅇㄱㅗㅇㅅㅏ', 'realword': '한국방송공사', 'weight': 11}
{'word': 'ㅎㅏㄴㄱㅜㄱㅂㅏㅇㅅㅗㅇㅇㅕㅇㅅㅏㅇㅅㅏㄴㅇㅓㅂㅈㅣㄴㅎㅡㅇㅇㅜㅓㄴ', 'realword': '한국방송영상산업진흥원', 'weight': 8}
{'word': 'ㅎㅏㄴㄱㅜㄱㅂㅏㅇㅅㅗㅇㄱㅗㅏㅇㄱㅗㅈㅣㄴㅎㅡㅇㄱㅗㅇㅅㅏ', 'realword': '한국방송광고진흥공사', 'weight': 7}
{'word': 'ㅎㅏㄴㄱㅜㄱㅂㅏㅇㅅㅗㅇㅋㅏㅁㅔㄹㅏㄱㅣㅈㅏㅎㅕㅂㅎㅗㅣ', 'realword': '한국방송카메라기자협회', 'weight': 7}
{'word': 'ㅎㅏㄴㄱㅜㄱㅂㅏㅇㅅㅗㅇㅌㅗㅇㅅㅣㄴㄷㅐㅎㅏㄱㄱㅛ', 'realword': '한국방송통신대학교', 'weight': 7}
{'word': 'ㅎㅏㄴㄱㅜㄱㅂㅏㅇㅅㅗㅇㅌㅗㅇㅅㅣㄴㄷㅐㅎㅏㄱ', 'realword': '한국방송통신대학', 'weight': 4}
<한국방송(<===ㅎㅏㄴㄱㅜㄱㅂㅏㅇㅅㅗㅇ)> Suggest 10:
1, 한국방송협회(67)
2, 한국방송대상(25)
3, 한국방송기자클럽(22)
4, 한국방송광고공사(19)
5, 한국방송협회장(13)
6, 한국방송학회(12)
7, 한국방송공사(11)
8, 한국방송영상산업진흥원(8)
9, 한국방송통신대학교(7)
10, 한국방송카메라기자협회(7)

'''




