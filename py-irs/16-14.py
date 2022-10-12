import hgsysinc
from hgunicode import hgGetChoJungJongString
from hgtest import load_dictfreq_kbs_2009
from hgtest import load_dictfreq_kbs_01_16
from hgfind import HGTrie
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
    Jamo3String = hgGetChoJungJongString(CurWord, 
        jamo=True, CompatibleJamo2ChoJungJong=True) #. [한글] -> [초중종 자모]
    #=TrieTest.InsertWord(CurWord, Weight=WordFreq) # RealWord=? 사용하지 않는 버전
    TrieTest.InsertNode(Jamo3String, RealWord=CurWord, Weight=WordFreq)
#=TrieTest.PrintTrie()
#-----------------------------
#-----------------------------
# 트라이 추천(Suggestion)
FindWord = '만ㄷ' #  단어
FindWord_Jamo3 = hgGetChoJungJongString(FindWord, 
    jamo=True, CompatibleJamo2ChoJungJong=True) # [한글] -> [초중종 자모]
print(f'{FindWord}:{FindWord_Jamo3}')

SugList = TrieTest.FindWord(FindWord_Jamo3) 
#=print(len(SugList), ':', SugList)
print(), print(f'<{FindWord}(<==={FindWord_Jamo3})> Suggest {len(SugList)}:')
print(*SugList[:10], sep='\n') # 10 단어만 출력
print()


'''
출력 결과:
========================================
이 예제는 [KBS 9시 뉴스 16년치] 사전 목록을 사용한다.

한글 음절로 된 단어를 초중종 자모로 변환하여 트라이를 생성한다.
========================================
만ㄷ:만ᄃ

<만ㄷ(<===만ᄃ)> Suggest 110:
{'word': '만다', 'realword': '만다', 'weight': 1}
{'word': '만다나오', 'realword': '만다나오', 'weight': 1}
{'word': '만다라', 'realword': '만다라', 'weight': 2}
{'word': '만다라톡신', 'realword': '만다라톡신', 'weight': 1}
{'word': '만다린', 'realword': '만다린', 'weight': 1}
{'word': '만다섬', 'realword': '만다섬', 'weight': 1}
{'word': '만다이', 'realword': '만다이', 'weight': 1}
{'word': '만단', 'realword': '만단', 'weight': 4}
{'word': '만단위', 'realword': '만단위', 'weight': 1}
{'word': '만달러', 'realword': '만달러', 'weight': 163}


'''


