import hgsysinc
from hgbasic import PrintDict_ByLine
from hgtest import load_textlist_gutenberg
from hgcrawl import get_gutenberg_text_folder
#-----
from hgdict_low import AddDictFreq__Word
#-----------
# gutenberg porject: https://www.gutenberg.org/
guten_pathname = get_gutenberg_text_folder()
text_list = load_textlist_gutenberg(guten_pathname)
print(len(text_list), 'files')
#-----------
print('reading text...', guten_pathname)
PrintProcState = True # 진행 상태 출력(텍스트 목록이 많을 경우 오래 걸릴 때 출력 필요)

#-----
# re.findall("[\w]+", string) 방식은 접어(예:can't)를 분리하기 때문에 
# 온전한 접어(예:can't) 형태는 오지 않는 문제가 있다.
# 접어(예:can't)를 처리하기 위해 작은따옴표 {'}를 추가한 
# re.findall("[\w']+", string) 방식으로 처리
#-----
# 1. 대문자를 소문자로 변환
# 2. 토큰 분리
#-----
import re
DictFreq = dict()
for ti, text in enumerate(text_list):
    # 1. 대문자를 소문자로 변환
    text = text.lower() # 대문자를 소문자로 변경

    # 2. 토큰 분리
    WordList = re.findall("[\w']+", text)
    for word in WordList:
        AddDictFreq__Word(DictFreq, word)
    if(PrintProcState == True):
        print(f'[{ti}] make wordlist...')
#    
print(f'DictFreq [{len(DictFreq)}]:')
print()

# 정렬(sort): 코드 오름차순(일반적인 사전 순서)
DictFreq_Sort = dict(sorted(DictFreq.items(), key=lambda item: item[0])) # by abc
DictFreq = DictFreq_Sort
#
PrintDict_ByLine(DictFreq, ShowIndex=True, Printnum=30)


"""
처리 결과:
--------------
[64246] 단어
==========================
43 files
reading text... ./../ext-src/data/gutenberg/text/
[0] make wordlist...
[1] make wordlist...
[2] make wordlist...
...
[41] make wordlist...
[42] make wordlist...
DictFreq [64246]:

0 :0 :  1
1 :00 : 8
2 :000 :        284
3 :0009m :      1
...
28 :0091m :     1
29 :0093m :     1

"""
