import hgsysinc
from hgbasic import PrintDict_ByLine
from hgtest import load_textlist_gutenberg
from hgdict_low import AddDictFreq__Word, UpdateDictfreq__Wordlist
from hgcrawl import get_gutenberg_text_folder
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
# 3-1. 양 끝에 문자('_') 제거: {_now then_ _common_}
# 3-2. 중간에 문자('_') 분리: {gentle_men  woman_kind 1_st  21_st  30_th}
# 3-3. 철자 규칙으로 단일화(s 제거, es 변형, 's)
# 4. 불용어 필터링: 접어(예:can't)를 제외한 나머지 작은따옴표를 포함한 단어(예: b'lieve, b'long)
# 5. 어휘 빈도 사전 저장
#-----
import re
DictFreq = dict()
for ti, text in enumerate(text_list):
    # 1. 대문자를 소문자로 변환
    text = text.lower() # 대문자를 소문자로 변경

    # 2. 토큰 분리
    #=WordList = re.findall("[\w]+", text)
    WordList = re.findall("[\w']+", text)
    for word in WordList:
        # 3-1) 양 끝에 문자('_') 제거: {_now then_ _common_}
        # 3-2) 중간에 문자('_') 분리: {gentle_men  woman_kind 1_st  21_st  30_th}
        divlist = word.split('_')
        if(len(divlist) > 0): # 분리된 단어 목록이 있는 경우
            # 3-3. 철자 규칙으로 단일화(s 제거, es 변형, 's)
            UpdateDictfreq__Wordlist(DictFreq, divlist, WordSuifx=True)
        else:
            # 3-3. 철자 규칙으로 단일화(s 제거, es 변형, 's)
            AddDictFreq__Word(DictFreq, word, WordSuifx=True)
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
print()

#-----
# 5. 어휘 빈도 사전 저장
#-----
#-----------
run_mode = "" # 코드 순서
#=run_mode = "_by_freq" # 빈도 순서

if(len(run_mode) > 0):
    # 빈도순 정렬
    FreqOrderFlag = True
    #=FreqOrderFlag = False
    print('sorting dictionary...')
    if(FreqOrderFlag == True):
        DictFreq_Sort = dict(sorted(DictFreq.items(), key=lambda item: (-item[1], item[0]))) # by high freq, abc
    else:
        DictFreq_Sort = dict(sorted(DictFreq.items(), key=lambda item: item[0])) # by abc
    DictFreq = DictFreq_Sort

#-----
# 어휘 빈도 사전 저장 
#-----
#
encoding='utf-8' 
#=encoding='euc-kr' # 표준완성형이라서 범위를 벗어난 통합완성형 코드가 있으면 오류 발생하여 읽지 못한다.
#=encoding='cp949'

# writing
save_file = guten_pathname + '/gutenberg_wordfreq' + run_mode + '.tpx'
print('dictionary writing:', save_file)
file = open(save_file, "w", encoding=encoding)
for word_cnt, word in enumerate(DictFreq):
    freq = DictFreq[word]
    tx_line = word + '\t' + str(freq) + '\n'
    wr_num = file.write(tx_line)
    # temp
    #=if(di > 5):
    #=    break
#
file.close()

#
word_cnt += 1
print(f'word_cnt:', word_cnt)


'''
처리 결과:
==================
[53847] 단어 = [61112](=[64246] - [3134]) - [7265]
접미사 삭제하면 [7265]단어가 줄어둠

[61112] 단어 = [64246] - [3134]
문자('_') 제거 및 분리하면 [3134] 단어가 줄어듦
==================
43 files
reading text... ./../ext-src/data/gutenberg/text
[0] make wordlist...
[1] make wordlist...
[2] make wordlist...
:
[41] make wordlist...
[42] make wordlist...
DictFreq [53847]:

0 :0 :  1
1 :00 : 8
2 :000 :        284
3 :0009m :      1
:
28 :0091m :     1
29 :0093m :     1


dictionary writing: ./../ext-src/data/gutenberg/text/gutenberg_wordfreq.tpx
word_cnt: 53847

'''

