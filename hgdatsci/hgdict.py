#------------------------
#------------------------
from typing import List
from collections import defaultdict

#----------
#----------
import hgsysinc
from hgwordlist import (
    GetWordLists__TextList,
    DeleteWordDictList_Filter,
    DeleteWordDictList_ByWordList,
    DeleteWordDictList_ByWordDictList, 
)

#----------
#---------- 아래용 코드는 사용하지 않지만 참고용으로 남겨둔다.
#=import importlib
#=exist_flag = importlib.util.find_spec("hgwordmatrix") is not None
#=if(exist_flag):
#    from hgwordmatrix_low import RunWordDicts_TFIDF
#----------
#----------

#-----
#-----
class HGDict():
    def __init__(self, WordList=None, FreqRate=False):
        self.freqrate = FreqRate # 빈도 비율
        self.dict = defaultdict(float)
        if(WordList != None):
            self.AddWordList(WordList, FreqRate)
            
    def AddWordList(self, WordList, FreqRate=False):
        #==print('WordList:', WordList)
        AddDictFreq__WordList(self.dict, WordList, FreqRate=FreqRate)
        #=print(self.dict)

    def SetWordList(self, WordList, FreqRate=False):
        #==print('WordList:', WordList)
        self.dict = defaultdict(float)
        AddDictFreq__WordList(self.dict, WordList, FreqRate=FreqRate)
        #=print(self.dict)

    def SetWordLists(self, WordLists, FreqRate=False, Averaging=1):
        #==print('WordList:', WordList)
        self.dict = defaultdict(float)
        for WordList in WordLists:
            AddDictFreq__WordList(self.dict, WordList, FreqRate=FreqRate)
        #=print(self.dict)
    
        if(Averaging > 1): # 평균값으로 변환(실제로는 나누기)
            self.CalcDictAvg(Averaging)
            #=print(self.dict)

    def DelWordList(self, WordList):
        #==print('WordList:', WordList)
        DelDictFreq__WordList(self.dict, WordList)
        #=print(self.dict)

    def SetDictFreq(self, DictFreq):
        #==print('DictFreq:', DictFreq)
        self.dict = defaultdict(float)
        AddDictFreq__DictFreq(self.dict, DictFreq)
        #=print(self.dict)

    def SetDictFreqs(self, DictFreqs, Averaging=1):
        #==print('DictFreqs:', DictFreqs)
        self.dict = defaultdict(float)
        for DictFreq in DictFreqs:
            AddDictFreq__DictFreq(self.dict, DictFreq)
        #=print(self.dict)
    
        if(Averaging > 1): # 평균값으로 변환(실제로는 나누기)
            self.CalcDictAvg(Averaging)
            #=print(self.dict)

    def GetVocabulary(self):
        #==print('self.dict:', self.dict)
        Vocabulary = set(self.dict.keys())
        #=print(Vocabulary)
        return Vocabulary
    
    def CalcDictAvg(self, Averaging): # Averaging값은 최소한 '2'이상
        assert Averaging >= 2, 'Error: (Averaging >= 2)' 
        for k in self.dict:
            self.dict[k] = self.dict[k] / Averaging
    
    def Sort(self, SortFilter='Key'):
        if(SortFilter == 'Key'):
            sort_dic = {key: val for key, val in sorted(self.dict.items(), key=lambda item: item[0])}
        else: # by value
            sort_dic = {key: val for key, val in sorted(self.dict.items(), key=lambda item: -item[1])} # by high value

    def Print(self, ShowMoreZero=False, RoundNum=0, SimpleFormat=False, 
        Printnum=None, ShowIndex=True, PrintFreqOrder=False, 
        OnlyKey=False, ExcFilter=None):
        # format: dict{'key':value}
        print()
        
        if(PrintFreqOrder == True):
            #= dict format: {key: val for key, val in sorted(self.diict.items(), key=lambda item: -item[1])}
            prt_dict = self.Sort(SortFilter='value') # by high-value
        else:
            prt_dict = self.Sort(SortFilter='key')
        
        inx = 0
        for key in prt_dict:
            printFlag = False
            if(ShowMoreZero == True): # '0'보다 큰 값만 출력
                if(key[1] > 0):
                    printFlag = True
            else: # 모두 출력
                printFlag = True

            if(ExcFilter != None): # 제외 목록에 있으면 출력하지 않는다.
                if(key[0] in ExcFilter):
                    printFlag = False
            #
            if(printFlag == True):
                if(SimpleFormat == True): # 줄바꿈을 하지 않는다.
                    print (f"'{key[0]}':", end='')
                    if(OnlyKey == True):
                        pass
                    else:
                        if(RoundNum != 0):
                            print (round(key[1], RoundNum), end='')
                        else:
                            print (f"{key[1]}", end='')
                else:
                    if(ShowIndex==True):
                        print((inx + 1), ':\t', end='')

                    print (f"'{key[0]}':", end='')
                    if(OnlyKey == True):
                        pass
                    else:
                        if(RoundNum != 0):
                            print (f'\t', round(key[1], RoundNum), end='')
                        else:
                            print (f'\t{key[1]}', end='')
                
                if(SimpleFormat == True):
                    print(', ', end='')
                else:
                    print()
                
                #
                inx += 1
                if ((Printnum != None) and (Printnum > 0)):
                    if inx >= Printnum:
                        break
        print()

#-----
#-----
def AddVocabularyDic_Word2(Vocabulary, Word):  
    '''# 샘플용 짧은 길이 간편 함수
    '''
    # format: {'word': 'our', 'freq': 1}
    Find = next((Item for Item in Vocabulary if Item['word'] == Word), None)
    if(Find == None):
        Vocabulary.append({'word':Word, 'freq':1})
    else:
        Find['freq'] += 1

def AddVocabularyDic_Word4(Vocabulary, Word, Freq, DocID):  
    '''# 샘플용 짧은 길이 간편 함수
    '''
    # format: {'word': 'our', 'freq': 1, 'doc':{13: 1, 27: 1, 30: 1, 47: 1}}
    Find = next((Item for Item in Vocabulary if Item['word'] == Word), None)
    if(Find == None):
        Vocabulary.append({'word':Word, 'freq':Freq, 'doc':{DocID:Freq}})
    else:
        Find['freq'] += Freq
        Find['doc'].update({DocID:Freq})

#=============================
#=============================
#===== dict-freq-area
#===== mini-simple-code for sample(example)
#=============================
#=============================
def MakeDictFreq__WordList(WordList): # 샘플용 짧은 길이 간편 함수
    '''# 샘플용 짧은 길이 간편 함수
    '''
    DictFreq = defaultdict(int)
    for word in WordList:
        DictFreq[word] += 1
    return DictFreq

def MakeDictFreq__WordLists(WordLists, Vocabulary=None):  # 샘플용 짧은 길이 간편 함수
    '''# 샘플용 짧은 길이 간편 함수
    '''
    #=print('WordLists:', WordLists)
    DictFreq = defaultdict(int)
    for WordList in WordLists:
        AddDictFreq__WordList(DictFreq, WordList, Vocabulary=Vocabulary)
    #=print(DictFreq)
    return dict(DictFreq)

def MakeDictFreq__EngTextList(TextList): # 샘플용 짧은 길이 간편 함수
    '''# 샘플용 짧은 길이 간편 함수
    '''
    import re
    DictFreq = defaultdict(int)
    for Text in TextList:
        Text = Text.lower() # 소문자 변환
        WordList = re.findall("[a-z]+", Text)
        for Word in WordList:
            DictFreq[Word] += 1
    return DictFreq

def MakeDictFreqList__EngTextList(TextList): # 샘플용 짧은 길이 간편 함수
    '''# 샘플용 짧은 길이 간편 함수
    '''
    import re
    DictFreqList = {}
    for doc_i, Text in enumerate(TextList):
        Text = Text.lower() # 소문자 변환
        WordList = re.findall("[a-z]+", Text) # string -> word list
        DictFreq = MakeDictFreq__WordList(WordList)

        for word, freq in DictFreq.items():
            # foramt: {'word': {13: 1, 27: 1, 30: 1, 47: 1}}
            DocFreq = {doc_i: freq}
            if(word in DictFreqList):
                DocFreqList = DictFreqList[word]
                DocFreqList.update(DocFreq)
            else:
                DictFreqList[word] = DocFreq
    return DictFreqList

def MakeListDictFreq2__EngTextList(TextList): # 샘플용 짧은 길이 간편 함수
    '''# 샘플용 짧은 길이 간편 함수
    '''
    import re
    Vocabulary = []
    for doc_i, text in enumerate(TextList):
        text = text.lower() # 소문자 변환
        WordList = re.findall("[a-z]+", text)

        for Word_c in WordList: # format: {'word': 'our', 'freq': 1}
            AddVocabularyDic_Word2(Vocabulary, Word_c)
    return Vocabulary

def MakeListDictFreq4__EngTextList(TextList): # 샘플용 짧은 길이 간편 함수
    '''# 샘플용 짧은 길이 간편 함수
    '''
    import re
    Vocabulary = []
    for doc_i, text in enumerate(TextList):
        text = text.lower() # 소문자 변환
        WordList = re.findall("[a-z]+", text)
        DictFreq = MakeDictFreq__WordList(WordList)

        # format: {'word': 'our', 'freq': 1, 'doc':{13: 1, 27: 1, 30: 1, 47: 1}}
        for Word_c, Freq in DictFreq.items():
            AddVocabularyDic_Word4(Vocabulary, Word_c, Freq, doc_i)
    return Vocabulary

def MakeDictFreqList__TextList(TextList): # 샘플용 짧은 길이 간편 함수
    '''# 샘플용 짧은 길이 간편 함수
    '''
    DictFreqList = {}
    for doc_i, Text in enumerate(TextList):
        Text = Text.lower() # 소문자 변환
        WordList = Text.split()
        DictFreq = MakeDictFreq__WordList(WordList)

        for word, freq in DictFreq.items():
            # foramt: {'word': {13: 1, 27: 1, 30: 1, 47: 1}}
            DocFreq = {doc_i: freq}
            if(word in DictFreqList):
                DocFreqList = DictFreqList[word]
                DocFreqList.update(DocFreq)
            else:
                DictFreqList[word] = DocFreq
    return DictFreqList

def PrintDictFreq(DictFreq, PrintNum=0, LeadingString='', PrintGuide=False, SortFlag=True):
    if(PrintGuide == True):
        print('\n---By abc Order ---')
    #-----    
    # DictFreq {key:value} === {word:freq}
    #-----
    if (SortFlag == True):
        dict__worker = sorted(DictFreq.items(), key=lambda item: item[0]) # by key: a->z
    else:
        dict__worker = DictFreq.items()
    dict_num = len(dict__worker)
    for i, dic in enumerate(dict__worker):
        print(LeadingString, end='')
        print(f'{i}, {dic[0]}: {dic[1]}') # format: [('that', 13),...]
        if(PrintNum > 0):
            if((i + 1) >= PrintNum):
                break
    if(PrintNum > 0): 
        # 맨 끝에서 일부 출력
        print('...')
        print('...')
        for i, dic in enumerate(dict__worker):
            if(i >= (dict_num - PrintNum)):
                print(f'{i}, {dic[0]}: {dic[1]}') # format: [('that', 13),...]
    print(), print()

#=============================
#=============================
#===== dict-freq-area
#=============================
#=============================
def GetDictFreq_Char__String(String, FreqRate=False):
    '''문자열을 글자 단위로 빈도 사전으로 변환'''
    #==print('String:', String)
    if(FreqRate == True): # 빈도 비율
        DictFreq = defaultdict(float)
    else:
        DictFreq = defaultdict(int)

    CharNum = len(String)
    for c in String:
        if(FreqRate == True):  # 빈도 비율
            curVal = 1.0 / CharNum
        else:
            curVal = 1
        DictFreq[c] += curVal
    #=print(DictFreq)
    #
    return dict(DictFreq)

def GetDictFreq__WordList(WordList, 
    FreqRate=False, 
    SortFlag=False, 
    FreqOrderFlag=False,
    Vocabulary=None,
    ):
    #==print('WordList:', WordList)

    if(FreqRate == True): # 빈도 비율
        DictFreq = defaultdict(float)
    else:
        DictFreq = defaultdict(int)

    AddDictFreq__WordList(DictFreq, WordList, 
            FreqRate=FreqRate, Vocabulary=Vocabulary)
    #=print(DictFreq)

    #
    if(SortFlag == True):
        if(FreqOrderFlag == True):
            DictFreq_Sort = dict(sorted(DictFreq.items(), key=lambda item: -item[1])) # by high freq
        else:
            DictFreq_Sort = dict(sorted(DictFreq.items(), key=lambda item: item[0])) # by abc
        DictFreq = DictFreq_Sort
        return DictFreq
    else:
        return dict(DictFreq)


def AddDictFreq__DictFreq(DictFreqBase, DictFreqNew):
    #==print('DictFreqNew:', DictFreqNew)

    for word in DictFreqNew:
        if(word in DictFreqBase):
            DictFreqBase[word] += DictFreqNew[word]
        else:
            DictFreqBase[word] = DictFreqNew[word]
    #=print(DictFreqBase)

def AddDictFreq__WordList(DictFreq, WordList, FreqRate=False, Vocabulary=None):
    '''Vocabulary: 어휘집(단어 목록)에 있는 단어만 처리
    '''
    #==print('WordList:', WordList)

    WordNum = len(WordList)
    for word in WordList:
        #
        if(Vocabulary != None): # {어휘집}이 있으면 여기에 있는 것만 허용
            if(word not in Vocabulary):
                continue
        #
        if(FreqRate == True):  # 빈도 비율
            curVal = 1.0 / WordNum
        else:
            curVal = 1
        if(word not in DictFreq): # 어휘가 없으면 생성해줌
            if(FreqRate == True):  # 빈도 비율
                DictFreq[word] = 0.0
            else:
                DictFreq[word] = 0
        DictFreq[word] += curVal
    
    #=print(DictFreq)

def DelDictFreq__WordList(DictFreq, WordList, DelType='not'):
    #==print('WordList:', WordList)
    if(DelType == 'match'): 
        for word in DictFreq:
            if(word in DictFreq):
                DictFreq.pop(word)
    else: # DelType == 'not'
        #-----
        # {WordList}에 속한 것은 남겨두고 일치하지 않은 것만 지우지 않는다.
        #-----
        # code error: dictionary changed size during iteration
        for word in list(DictFreq.keys()): # 사전{DictFreq}에서 받아서 지우면 안 됨.
            if(word not in WordList):
                pass
            else:
                #=print('del:', word)
                DictFreq.pop(word)
    #=print(DictFreq)

def DelDictFreqs__WordList(DictFreqs, WordList):
    #==print('WordList:', WordList)
    for DictFreq_c in DictFreqs:
        DelDictFreq__WordList(DictFreq_c, WordList)

def DelDictFreq__DictFreq(DictFreq, DictFreq_Filter):
    #==print('WordList:', WordList)
    for word in DictFreq_Filter:
        if(word in DictFreq):
            DictFreq.pop(word)
    #=print(DictFreq)

def DelDictFreqs__DictFreq(DictFreqs, DictFreq_Filter):
    #==print('WordList:', WordList)
    for DictFreq_c in DictFreqs:
        DelDictFreq__DictFreq(DictFreq_c, DictFreq_Filter)

def DelDictFreq__WordDict(DictFreq, WordDict, DelType='not'):
    #==print('WordDict:', WordDict)
    if(DelType == 'match'): 
        #-----
        # {WordDict}에 속한 것만 지운다.
        #-----
        for word_c in WordDict:
            if(word_c['word'] in DictFreq):
                #=print('del:', word_c)
                DictFreq.pop(word_c['word'])
    else: # DelType == 'not'
        #-----
        # {WordDict}에 속한 것은 남겨두고 일치하지 않은 것만 지우지 않는다.
        #-----
        #=print(WordDict[0]) # for check-format
        DictFreq_keys = list(DictFreq.keys())
        #=print(DictFreq_keys)
        for dic_k in DictFreq_keys:
            find_topic = next((word_c for word_c in WordDict if word_c['word'] == dic_k), False)
            if(find_topic == False): 
                #=print('del:', dic_k)
                DictFreq.pop(dic_k)
    #=print(DictFreq)

def DelDictFreqs__WordDict(DictFreqs, WordDict, DelType='not'):
    #==print('WordDict:', WordDict)
    for DictFreq_c in DictFreqs:
        #=print('[before] DictFreq_c:', len(DictFreq_c))
        DelDictFreq__WordDict(DictFreq_c, WordDict, DelType=DelType)
        #=print('[after] DictFreq_c:', len(DictFreq_c))

def GetDictFreq__WordLists(WordLists, FreqRate=False, Vocabulary=None):
    #=print('WordLists:', WordLists)

    if(FreqRate == True): # 빈도 비율
        DictFreq = defaultdict(float)
    else:
        DictFreq = defaultdict(int)

    for WordList in WordLists:
        AddDictFreq__WordList(DictFreq, WordList, FreqRate=FreqRate, Vocabulary=Vocabulary)

    #=print(DictFreq)
    return dict(DictFreq)

def GetDictFreqs__WordLists(WordLists, FreqRate=False, Vocabulary=None):
    '''Vocabulary: 어휘집(단어 목록)에 있는 단어만 처리
    '''
    #=print('WordLists:', WordLists)

    DictFreqLists = []
    for WordList in WordLists:
        DictFreq = GetDictFreq__WordList(WordList, FreqRate=FreqRate, Vocabulary=Vocabulary)
        DictFreqLists.append(DictFreq) # dict()

    #=print(DictFreqLists)
    return DictFreqLists # dict()

def GetDictFreq__DictFreqs(DictFreqs):
    #=print('DictFreqs:', DictFreqs)
    DictFreq_New = defaultdict(float)
    for DictFreq_i in DictFreqs:
        AddDictFreq__DictFreq(DictFreq_New, DictFreq_i)
    #=print(DictFreq_New)
    return dict(DictFreq_New)

def GetDictFreq__WordDictList(WordDictList, FreqRate=False):
    #=print('WordDictList:', WordDictList)

    if(FreqRate == True): # 빈도 비율
        DictFreq = defaultdict(float)
    else:
        DictFreq = defaultdict(int)

    for WordDict in WordDictList:
        DictFreq[WordDict['word']] = WordDict['freq']

    #=print(DictFreq)
    return dict(DictFreq)

def GetDictFreqs__WordDictLists(WordDictLists, FreqRate=False):
    #=print('WordDictLists:', WordDictLists)

    DictFreqs = []
    for WordDictList in WordDictLists:
        DictFreq = GetDictFreq__WordDictList(WordDictList, FreqRate=FreqRate)
        DictFreqs.append(DictFreq) # dict()

    #=print(DictFreqs)
    return DictFreqs # dict()

def GetDictFreq__TextList(TextList, 
    FreqRate=False,
    Vocabulary=None,
    LowerCase=False,
    ExcFilter=None,
    CliticsModify=False, 
    ExcChar1=False, 
    ExcNumber=False,
    UnifySpellRule=False,
    PrintProcState=False, 
    ): 
    '''
    FreqRate:   빈도를 최댓값에 대한 비율로 처리
    Vocabulary: 어휘집(Vocabulary:단어 목록)에 있는 단어만 처리
    ExcFilter:  목록에 있는 단어 제외(stopword)
    CliticsModify: 접어(Clitics) 분리 # {~'s}, {~'t}, {~'d}는 {~}로 바꾼다.
    ExcChar1:   1글자 단어는 제외(영어는 이래되 되지만 한글을 이렇게 하면 안 된다.)
    ExcNumber:  숫자는 제외
    UnifySpellRule: # 철자 규칙으로 단일화(s 제거, es 변형, 's)
    PrintProcState: 진행 상태 출력(텍스트 목록이 많을 경우 오래 걸릴 때 출력 필요)
    '''
    WordLists = GetWordLists__TextList(TextList, ExcFilter=ExcFilter, LowerCase=LowerCase,
                    CliticsModify=CliticsModify, ExcChar1=ExcChar1, ExcNumber=ExcNumber,
                    UnifySpellRule=UnifySpellRule, PrintProcState=PrintProcState)
    DictFreq = GetDictFreq__WordLists(WordLists, 
                    FreqRate=FreqRate, Vocabulary=Vocabulary)
    return DictFreq

def GetDictFreqs__TextList(TextList, 
    FreqRate=False,
    Vocabulary=None,
    LowerCase=False,
    ExcFilter=None,
    CliticsModify=False, 
    ExcChar1=False, 
    ExcNumber=False,
    UnifySpellRule=False,
    PrintProcState=False, 
    ): 
    '''
    FreqRate:   빈도를 최댓값에 대한 비율로 처리
    Vocabulary: 어휘집(Vocabulary:단어 목록)에 있는 단어만 처리
    ExcFilter:  목록에 있는 단어 제외(stopword)
    CliticsModify: 접어(Clitics) 분리 # {~'s}, {~'t}, {~'d}는 {~}로 바꾼다.
    ExcChar1:   1글자 단어는 제외(영어는 이래되 되지만 한글을 이렇게 하면 안 된다.)
    ExcNumber:  숫자는 제외
    UnifySpellRule: # 철자 규칙으로 단일화(s 제거, es 변형, 's)
    PrintProcState: 진행 상태 출력(텍스트 목록이 많을 경우 오래 걸릴 때 출력 필요)
    '''
    WordLists = GetWordLists__TextList(TextList, ExcFilter=ExcFilter, LowerCase=LowerCase,
                    CliticsModify=CliticsModify, ExcChar1=ExcChar1, ExcNumber=ExcNumber,
                    UnifySpellRule=UnifySpellRule, PrintProcState=PrintProcState)
    DictFreqs = GetDictFreqs__WordLists(WordLists, FreqRate=FreqRate, Vocabulary=Vocabulary)
    return DictFreqs

def GetDictFreq_Product(DictFreqBase, DictFreqComp):
    '''빈도 사전의 내적(Product) 계산'''
    #=print('DictFreqBase:', DictFreqBase)
    #=print('DictFreqComp:', DictFreqComp)
    ##----------
    Product = 0
    ProductCnt = 0
    for key, base_val in DictFreqBase.items():
        comp_val = DictFreqComp.get(key, 0)
        #=print(f'{key}: {base_val}, {comp_val}')
        if((base_val > 0) and (comp_val > 0)):
            mul_c = base_val * comp_val
            #=print('mul_c:', mul_c)
            Product += mul_c
            ProductCnt += 1
    #
    return Product, ProductCnt

def TransDictFreq_By_DictFreq(DictFreq_Work, DictFreq_Filter):
    #---
    #=print('DictFreqWork:', DictFreqBase)
    #=print('DictFreqFilter:', DictFreqComp)
    #---
    DictFreq_Trans = {}
    for word in DictFreq_Work:
        wordvalue = DictFreq_Filter.get(word, None)
        #=print(f'{word}: {wordvalue}')
        if(wordvalue is not None):
            DictFreq_Trans[word] = wordvalue
    #
    return DictFreq_Trans

def TransDictFreq__WordList(DictFreq, WordList, TransType='match'):
    #==print('WordList:', WordList)
    
    DictFreq_Trans = {}
    if(TransType == 'match'): # 일치하는 것만 새로 만든다.
        for word in DictFreq:
            if(word in DictFreq):
                DictFreq_Trans[word] = DictFreq[word]
    else: # TransType == 'not'
        # {WordList}에 속한 것은 제외하고 새로 만든다.
        for word in DictFreq:
            if(word not in WordList):
                DictFreq_Trans[word] = DictFreq[word]
    #=print(DictFreq_Trans)
    return DictFreq_Trans

#=============================
#=============================
#===== Vocabulary-area
#=============================
#=============================
def GetVocabulary__WordList(WordList, SortFlag=True):
    '''return Vocabulary: set()
    '''
    #==print('WordList:', WordList)
    Vocabulary = set(Word for Word in WordList)
    #=print(Vocabulary)
    if(SortFlag == True):
        Vocabulary = set(sorted(Vocabulary))
    #=print(Vocabulary)
    return Vocabulary

def GetVocabulary__WordLists(WordLists, SortFlag=True):
    '''return Vocabulary: set()
    '''
    #==print('WordLists:', WordLists)
    Vocabulary = set(Word for WordList in WordLists for Word in WordList)
    #=print(Vocabulary)
    if(SortFlag == True):
        Vocabulary = set(sorted(Vocabulary))
    return Vocabulary

def GetVocabulary__DictFreq(DictFreq, SortFlag=True):
    '''return Vocabulary: set()
    '''
    #==print('DictFreq:', DictFreq)
    Vocabulary = set(Word for Word in DictFreq)
    #=print(Vocabulary)
    if(SortFlag == True):
        Vocabulary = set(sorted(Vocabulary))
    #=print(Vocabulary)
    return Vocabulary

def GetVocabulary__DictFreqs(DictFreqs, SortFlag=True):
    '''return Vocabulary: set()
    '''
    #==print('DictFreqs:', DictFreqs)
    Vocabulary = set(Word for DictFreq in DictFreqs for Word in DictFreq)
    #=print(Vocabulary)
    if(SortFlag == True):
        Vocabulary = set(sorted(Vocabulary))
    return Vocabulary

#=============================
#=============================
#===== word-dict-area
#=============================
#=============================
def MakeWordDict__DictFreq(DictFreq):
    #=print('DictFreq:', DictFreq)
    #=DictFreq_len = len(DictFreq)
    WordDict = []
    for df_wd in DictFreq:
        WordDict.append({'word': df_wd, 'freq': DictFreq[df_wd]})
    return WordDict

def MakeWordDicts__DictFreqs(DictFreqs):
    #=DictFreqs_len = len(DictFreqs)
    #print ('len :', DictFreqs_len)
    WordDicts = []
    for df in DictFreqs:
        WordDict = MakeWordDict__DictFreq(df)
        WordDicts.append(WordDict)
    return WordDicts

def DeleteWordDicts_Freq(WordDicts, DelFreq=1, DelType='same'):
    WordDicts_len = len(WordDicts)
    #print ('len :', WordDicts_len)

    for d in range(0, WordDicts_len):
        WordDict_c = WordDicts[d]
        print('del before:', len(WordDict_c))
        DeleteWordDictList_Filter(WordDict_c, FilterFreq=DelFreq, FreqType=DelType)
        print('del after:', len(WordDict_c))

def DeleteWordDicts_ByWordList(WordDicts, WordList_Filter, DelType='match'):
    WordDicts_len = len(WordDicts)
    #print ('len :', WordDicts_len)

    for c in range(0, WordDicts_len):
        WordDict_c = WordDicts[c]
        #print('[dict', (c + 1), ']', 'del before:', len(WordDict_c))
        DeleteWordDictList_ByWordList(WordDict_c, WordList_Filter, DelType=DelType)
        #print('[dict', (c + 1), ']', 'del after:', len(WordDict_c))
    #print()

def DeleteWordDicts_ByWordDict(WordDicts, WordDict_Filter, DelType='match'):
    WordDicts_len = len(WordDicts)
    #print ('len :', WordDicts_len)

    for c in range(0, WordDicts_len):
        WordDict_c = WordDicts[c]
        #print('[dict', (c + 1), ']', 'del before:', len(WordDict_c))
        DeleteWordDictList_ByWordDictList(WordDict_c, WordDict_Filter, DelType=DelType)
        #print('[dict', (c + 1), ']', 'del after:', len(WordDict_c))
    #print()

#================================
#================================
#================================
def load_dictfreq_eng_textfile(filename, encoding='utf-8', SortFlag=True, toLower=True):
    from hgwordfile import ReadTxtFile
    import re

    booktext = ReadTxtFile(filename, encoding=encoding)
    if(toLower == True):
        booktext = booktext.lower() # 대문자롤 소문자로 통합하기 위해서 소문자 변환

    #
    DictFreq = defaultdict(int)
    WordList = re.findall("[a-z]+", booktext)
    for Word in WordList:
        DictFreq[Word] += 1

    if SortFlag == True: # sort by a->z
        dict_by_keys = sorted(DictFreq.items(), key=lambda item: item[0]) # by key:->z
        Vocabulary_AZ = {dic[0]:dic[1] for dic in dict_by_keys} 
        #print(*Vocabulary_AZ, sep='\n')
        return Vocabulary_AZ
    else:
        return DictFreq


#================================
#================================
#================================
from unittest import TestCase, main
class HGTest(TestCase):
    #================================
    #================================
    #================================
    def setUp(self):
        self.a = 'test setup'

    def _testrun(self):
        print('testrun: ok')

    #================================
    #================================
    #================================
    WordList1 = ['감자', '가리비', '가나다', '가다',
                '개나리', '거짓말', '감자', 
                '거짓말',
                '고양이', '구름', '감자',
    ]
    WordList2 = ['감자', '가리비', 
                '거짓말', '감자', 
                '고양이', '구름', 
                '나무', '노랑', '높이'
    ]
    WordList3 = ['가나다', '가다',
                '개나리', '거짓말', '감자', 
                '구름', '감자',
                '다랑어', '다리', '대나무',
                '도무지', '빨리'
    ]
    WordLists = [WordList1, WordList2, WordList3]

    def _test_aa(self):
        print('\n\n#--- test Vocabulary__WordList')
        print('WordList1:', self.WordList1)
        voca = GetVocabulary__WordList(self.WordList1)
        print('Vocabulary:', voca)

        print('\n\n#--- test DictFreq__WordList')
        DictFreq = GetDictFreq__WordList(self.WordList1)
        print(DictFreq)

        DictFreq = GetDictFreq__WordList(self.WordList1, FreqRate=True)
        print(DictFreq)

        print('\n\n#--- test Vocabulary__WordLists')
        print('WordLists:', self.WordLists)
        voca = GetVocabulary__WordLists(self.WordLists)
        print('Vocabulary[', len(voca),']:', voca)
        


        print()
        print()
        print('\n\n#--- test HGDict() WordList')
        hgdic = HGDict(self.WordList1)
        print('hgdict.dict:', hgdic.dict, '(', sum(hgdic.dict.values()), ')')

        hgdic = HGDict()
        hgdic.AddWordList(self.WordList1)
        print('hgdict.dict:', hgdic.dict, '(', sum(hgdic.dict.values()), ')')
        print('Vocabulary[', len(hgdic.GetVocabulary()),']:', hgdic.GetVocabulary())

        hgdic.SetWordList(self.WordList2)
        print('hgdict.dict:', hgdic.dict, '(', sum(hgdic.dict.values()), ')')
        print('Vocabulary[', len(hgdic.GetVocabulary()),']:', hgdic.GetVocabulary())


        print('\n\n#--- test HGDict() WordLists')
        hgdic = HGDict()
        hgdic.SetWordLists(self.WordLists)
        print('hgdict.dict:', hgdic.dict, '(', sum(hgdic.dict.values()), ')')
        print('Vocabulary[', len(hgdic.GetVocabulary()),']:', hgdic.GetVocabulary())

        #===
        print('test: ok')

    def test_cc(self):
        DictFreq = GetDictFreq__WordList(self.WordList1)
        print('DictFreq:', DictFreq)
        Vocabulary = GetVocabulary__DictFreq(DictFreq, SortFlag=True)
        print('Vocabulary:', Vocabulary)

        DictFreqs = GetDictFreqs__WordLists(self.WordLists)
        print('DictFreqs:', DictFreqs)
        Vocabulary = GetVocabulary__DictFreqs(DictFreqs, SortFlag=True)
        print('Vocabulary:', Vocabulary)

if __name__ == '__main__':
    main()



