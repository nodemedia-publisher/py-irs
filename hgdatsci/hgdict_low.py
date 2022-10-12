#----------
#----------
import hgsysinc

#-----
# re.findall("[\w]+", string) 방식은 접어(예:can't)를 분리하기 때문에 
# 온전한 접어(예:can't) 형태는 오지 않는 문제가 있다.
# 접어(예:can't)를 처리하기 위해 작은따옴표 {'}를 추가한 
# re.findall("[\w']+", string) 방식으로 처리
#-----
def AddDictFreq__Word(DictFreq, word, WordSuifx=False):
    #---
    # 단어 앞(prefix)과 뒤(suffix)에서 불필요한 기호 문자 삭제: {'}
    #---
    _del_fix_chars_ = "'" # 영문자 토큰 합성 글자: quatation
    word = word.strip(_del_fix_chars_)
    if(word == ''): # 내용이 없는 경우
        return
    #---
    if(WordSuifx == True):
        from hgwordlist import GetBasicForm__suiffx_s
        # add-3) 철자 규칙으로 단일화(s 제거, es 변형, 's)
        basicform = GetBasicForm__suiffx_s(word)
        if(len(basicform) > 0): # 기본형으로 바꾼 경우
            word = basicform
    #---
    if(word not in DictFreq):
        DictFreq[word] = 1
    else:
        DictFreq[word] += 1

def UpdateDictfreq__Wordlist(DictFreq, WordList, WordSuifx=False):
    for word in WordList:
        AddDictFreq__Word(DictFreq, word, WordSuifx=WordSuifx)

def TransDictfreq__Stoplist(DictFreq, Stoplist): # 불용어 제거
    DelNum = 0
    for stopword in Stoplist:
        if stopword in DictFreq:
            DictFreq.pop(stopword)
            DelNum += 1
            # 아래는 임시 확인용
            #=if(stopword.isalnum() == False): # {알파벳+숫자}가 아닌 글자를 포함한 단어
            #=    print(word)
    #=print('del word num:', DelNum)
    #=print('DictFreq:', len(DictFreq))
    #
    return DelNum
