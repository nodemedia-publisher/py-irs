import hgsysinc
from hgkbd import HGTransString2EngString
from hgtest import load_dictfreq_kbs_2009, load_dictfreq_kbs_01_16
#-----------------------------
#-----------------------------
#=print('reading texts')
# foramt: {'word': 1}
DictFreqList = load_dictfreq_kbs_2009()
#=DictFreqList = load_dictfreq_kbs_01_16()
print('Dict Num:', len(DictFreqList))
#=WordNum = sum(DictFreqList[dic] for dic in DictFreqList)
#=print('Word Num:', WordNum)

#@@@@@@@@@@@@@@@@@@@@
#@@@ 먼저 검색어 사전을 탐색하지 않고 곧 바로 한영 변환한 후에 검색어 사전 탐색
#@@@@@@@@@@@@@@@@@@@@
##----------
##----------
#=FindWord = '듄' # ebs <== (2009년에는 없다)
#=FindWord = 'eogksalsrnr' # 대한민국 <== 없다
FindWord = 'ㅏㅠㄴ' # kbs
#=FindWord = 'ㅓㅠㄴ' # jbs (사전에 없는 영문단어를 한글로 입력해본다.)
#=FindWord = 'ㅂㅈㄷㄳ' # qwert (사전에 없으며 의미없는 영문단어를 한글로 입력해본다.)
EngKBDCharString = HGTransString2EngString(FindWord) # 한글을 영문자로 변환
if EngKBDCharString in DictFreqList:
    print(f'[{FindWord} -> {EngKBDCharString}]:{DictFreqList[EngKBDCharString]} 회')
else:
    print(f'[{EngKBDCharString}] 검색어가 없습니다.')

"""
처리 결과:
===========================================
@@@ [KBS 9시 뉴스] @@@
@@@ @@@ [토큰처리] -  {주제어}
file: ..\testtext\hgdatsci\_kbs_2009_\2009.가나순_WordList.txt
----------------------
Dict Num: 99989
[ㅏㅠㄴ -> kbs] : 41 회
---------------------- 아래는 (DebugPrint == True)
Dict Num: 99989
한글 음절 -> 영문자:
[ㅏㅠㄴ -> kbs] : 41 회

"""
