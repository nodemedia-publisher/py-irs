from hgbasic import get_backword_string
from hgbasic import PrintDictList_ByLine
from hgchartype import HGGetToken

from hgchartype import (
    get_keyword_type_num__scripts, HGGetKeywordList,
    get_scripts, get_script_list,
    HGTokenize,
)

#-----
def GetToken_File(filename, encoding='utf-8', PrintTextFlag = False):
    TokenList = []

    if filename.is_file():
        if filename.exists():pass
        else: return TokenList
    else:
        print("file not found: %s" %filename)
        return TokenList

    file = open(filename, 'r', encoding=encoding)
    while True:
        line = file.readline()
        if not line: 
            break
        if(PrintTextFlag == True): 
            print(line)
        word_tok = HGGetToken(line)
        if(word_tok != None): 
            TokenList.extend(word_tok)
    file.close()
    return TokenList

def GetKeywordList_File(filename, encoding='utf-8', PrintTextFlag = False):
    # old: GetWordTok_File
    from pathlib import Path
    #===
    KeywordList = []
    filename = Path(filename)
    if filename.is_file():
        if filename.exists():pass
        else: return KeywordList
    else:
        print("file not found: %s" %filename)
        return KeywordList

    file = open(filename, 'r', encoding=encoding)
    while True:
        line = file.readline()
        if not line:
            break
        if(PrintTextFlag == True):
            print(line)
        word_tok = HGGetKeywordList(line)
        if(word_tok != None):
            KeywordList.extend(word_tok)
    file.close()
    return KeywordList

def PrintWordList(WordList, FilterLen = 0, FilterCharType = None, OneLine=False, PrintIndex=False, BackwardFlag=False):
    if(WordList == None): return
    
    wordlist_len = len(WordList)
    FilterCnt = 0
    for i in range(0, wordlist_len):
        Word = WordList[i]
        wordlen = len(Word)
    
        # filter
        if(FilterLen > 0):
            if(FilterLen != wordlen):
                continue
        if(FilterCharType != None):
            WordCharType = get_scripts(Word)
            if(len(FilterCharType) == 1):
                if(FilterCharType != WordCharType):
                    continue
            #else:
            #    if(FilterCharType == 'keyword'):
            #        if(get_keyword_type_num__scripts(WordCharType) >= 1)
            #        continue
        FilterCnt += 1
        
        if(OneLine == True):
            pass
        else:
            if(FilterCnt == 1):
                print("[", end='')
            elif(FilterCnt > 1):
                print(", ", end='')
            print("'", end='')

        if(PrintIndex == True):
            print('%i: ' %FilterCnt, end='')

        #
        if(BackwardFlag == True):
            backword = get_backword_string(Word)
            print(backword, end='')
        else:
            print(Word, end='')

        #        
        if(OneLine == True):
            print('')
        else:
            print("'", end='')

    if(OneLine == False):
        if(wordlist_len > 0):
            if(FilterCnt > 0):
                print("]", end='')
    print("")

def GetWordDictList_WordList(WordList, 
    EraseNonKeyword=False, LowerCasifyFlag=False):
    WordDictList = []
    if(WordList == None): 
        return WordDictList
    #
    if(LowerCasifyFlag == True): # ???????????? ??????
        WordList_lower = [word.lower() for word in WordList]
        WordList_Sort = sorted(WordList_lower)
    else:
        WordList_Sort = sorted(WordList)
    #PrintWordList(WordList_Sort, PrintIndex=True)
    #PrintWordList(WordList_Sort, OneLine=True, PrintIndex=True)
    #print ('')

    #==============================================
    ## WordItem = {
    ##     'word': '', 
    ##     'freq':0, 
    ##     'len': 0, 
    ##     'script_num':0
    ## }
    #==============================================

    PreWord = None
    for word in WordList_Sort:
        ###print('word-len :', len(word))
        #
        if(EraseNonKeyword == True):
            char_type_string = get_scripts(word)            
            if(get_keyword_type_num__scripts(char_type_string) <= 0):
                continue
        #
        addflag = False
        if(PreWord == None):
            addflag = True
        else:
            if(PreWord['word'] == word):
                PreWord['freq'] += 1
            else:
                addflag = True
        if(addflag == True):
            string_char_type_list = get_script_list(word)
            #print('string_char_type_list: ', string_char_type_list)
            wordlen = len(word)
            script_num = len(string_char_type_list)
            WordItem = {'word': word, 'freq':1, 'len': wordlen, 'script_num':script_num}
            WordDictList.append(WordItem)
            PreWord = WordItem
        
    return WordDictList

def GetWordDictLists_WordLists(WordLists, EraseNonKeyword=False, LowerCasifyFlag=False):
    #=print(WordLists)
    WordDictLists = []
    for WordList in WordLists:
        WordDictList = GetWordDictList_WordList(WordList, 
            EraseNonKeyword=EraseNonKeyword, LowerCasifyFlag=LowerCasifyFlag)
        WordDictLists.append(WordDictList)
    return WordDictLists

def GetWordDictList_String(string, EraseNonKeyword=False, LowerCasifyFlag=False):
    WordDictList = []
    if(string == None): return WordDictList

    #KeywordList = string.split()
    KeywordList = HGGetKeywordList(string)
    #print (KeywordList)

    WordDictList = GetWordDictList_WordList(KeywordList, 
        EraseNonKeyword=EraseNonKeyword, LowerCasifyFlag=LowerCasifyFlag)
    #print(WordDictList)

    return WordDictList

def GetWordDictList_File(filename, encoding='utf-8', 
    PrintTextFlag = False, EraseNonKeyword=False, LowerCasifyFlag=False):
    KeywordList = GetKeywordList_File(filename, encoding, PrintTextFlag)
    WordDictList = GetWordDictList_WordList(KeywordList, 
        EraseNonKeyword=EraseNonKeyword, LowerCasifyFlag=LowerCasifyFlag)
    return WordDictList

def GetWordDictItem_String(WordDictItem, OneLine = False, 
    PrintingIndex = -1, BackwardFlag = False, SimpleFormat=False,
    TotalWordFreq=0):
    WordDictItem_String = ''

    if(WordDictItem == None): WordDictItem_String

    # {'word': '????????????????????????', 'freq': 1, 'len': 8, 'script_num':WordCharType}
    # 1: {'word': '????????????????????????', 'freq': 1, 'len': 8, 'script_num':WordCharType}

    disp_word = WordDictItem['word']
    if(BackwardFlag == True):
        disp_word = get_backword_string(WordDictItem['word'])

    #
    if(SimpleFormat == True):
        if(PrintingIndex > -1):
            print('%i:\t' %PrintingIndex, end='')

        WordDictItem_String += disp_word
        WordDictItem_String += "\t"
        WordDictItem_String += str(WordDictItem['freq'])

        if(TotalWordFreq > 0): # ?????? ?????? ????????? ????????? ????????? ???????????? ??????
            WordFreq = int(WordDictItem['freq'])
            WordRate = WordFreq / TotalWordFreq
            WordRatePer = WordRate * 100

            WordDictItem_String += "\t"
            WordDictItem_String += str('%.1f' % WordRatePer)
    else:
        if(PrintingIndex > -1):
            print('%i: ' %PrintingIndex, end='')

        #
        WordDictItem_String += "{"
    
        #
        WordDictItem_String += "'word': '"
        WordDictItem_String += disp_word
        WordDictItem_String += "'"
    
        #
        WordDictItem_String += ", 'freq': "
        WordDictItem_String += str(WordDictItem['freq'])

        #
        if(TotalWordFreq > 0): # ?????? ?????? ????????? ????????? ????????? ???????????? ??????
            WordFreq = int(WordDictItem['freq'])
            WordRate = WordFreq / TotalWordFreq
            WordRatePer = WordRate * 100

            WordDictItem_String += ", 'rate': "
            WordDictItem_String += str('%.1f' % WordRatePer)
    
        #
        WordDictItem_String += ", 'len': "
        WordDictItem_String += str(WordDictItem['len'])

        #
        WordDictItem_String += ", 'script_num': "
        WordDictItem_String += str(WordDictItem['script_num'])

        #
        WordDictItem_String += "}"

    return WordDictItem_String

def PrintWordDictList(WordDictList, FilterLen = 0, PrintingNum=0, 
    FilterCharType = None, FilterFreq = 0, OneLine=False, 
    PrintIndex=False, BackwardFlag=False, SimpleFormat=False, 
    SortFlag=False, RateFlag=True):
    if(WordDictList == None): return

    # sort by freq
    WordDictList_prt = WordDictList
    if(SortFlag == True):
        WordDictList_Sort = WordDictList.copy();
        WordDictList_Sort.sort(key = lambda wd: (-wd['freq'], wd['word'])) # by freq high, abc
        WordDictList_prt = WordDictList_Sort

    # RateFlag=True ?????? ??????????????? ?????? ????????? ????????? ??????.
    TotalWordFreq = 0
    if(RateFlag == True):
        TotalWordFreq = sum([word_dict['freq'] for word_dict in WordDictList_prt])
        print('TotalWordFreq:', TotalWordFreq)

    #    
    print('??????\t??????\t??????', end='')
    if(RateFlag == True):
        print('\t?????????')
    else:
        print('\n')
    #
    WordDictList_len = len(WordDictList_prt)
    FilterCnt = 0
    for i, WordDictItem in enumerate(WordDictList_prt):
        # filter
        if(FilterLen > 0):
            #=WordLen = WordDictItem['len']
            WordLen = len(WordDictItem['word'])
            if(FilterLen != WordLen):
                continue
        if(FilterCharType != None):
            WordCharType = get_scripts(WordDictItem['word'])
            if(len(FilterCharType) == 1):
                if(FilterCharType != WordCharType):
                    continue
            #else:
            #    if(FilterCharType == 'keyword'):
            #        if(get_keyword_type_num__scripts(WordCharType) >= 1)
            #        continue
        if(FilterFreq > 0): # ?????? ??????
            if(FilterFreq != WordDictItem['freq']):
                continue

        ###            
        FilterCnt += 1
        
        if(OneLine == True):
            pass
        else:
            if(FilterCnt == 1):
                print("[", end='')
            elif(FilterCnt > 1):
                print(", ", end='')

        PrintingIndex = -1
        if(PrintIndex == True):
            PrintingIndex = FilterCnt

        #
        #print(WordDictItem, end='')
        WordDictItem_String = GetWordDictItem_String(WordDictItem, OneLine, 
            PrintingIndex, BackwardFlag, SimpleFormat, TotalWordFreq)
        print(WordDictItem_String, end='')

        if(OneLine == True):
            print("")
        
        if(PrintingNum > 0):
            if(FilterCnt == PrintingNum):
                break

    if(OneLine == False):
        if(WordDictList_len > 0):
            if(FilterCnt > 0):
                print("]", end='')
    print("")

def GetWordDictList_TotalFreq(WordDictList, FilterLen = 0, FilterCharType = None, FilterFreq = 0):
    TotalFreq = 0

    if(WordDictList == None): return TotalFreq
    
    WordDictList_len = len(WordDictList)
    FilterCnt = 0
    for i in range(0, WordDictList_len):
        WordItem = WordDictList[i]
    
        ### filter
        if(FilterLen > 0):
            #WordItemLen = len(WordItem['word'])
            if(FilterLen != WordItem['len']):
                continue
        
        if(FilterCharType != None):
            WordCharType = get_scripts(WordItem['word'])
            if(len(FilterCharType) == 1):
                if(FilterCharType != WordCharType):
                    continue
            #else:
            #    if(FilterCharType == 'keyword'):
            #        if(get_keyword_type_num__scripts(WordCharType) >= 1)
            #        continue

        if(FilterFreq > 0): # ?????? ??????
            if(FilterFreq != WordItem['freq']):
                continue

        ###            
        FilterCnt += 1
        TotalFreq += WordItem['freq']
    
    return TotalFreq

def GetWordDictList_FreqListInfo(WordDictList, FilterLen = 0, FilterCharType = None):
    #
    FreqListInfo = []
    
    TotalFreq = 0

    if(WordDictList == None): 
        return FreqListInfo

    # sort by freq
    WordDictList_Sort = WordDictList.copy();
    WordDictList_Sort.sort(key = lambda wd: (wd['freq'], wd['word'])) # by freq low, abc

    WordDictList_len = len(WordDictList_Sort)
    FilterCnt = 0
    FreqList = []
    FreqListItem = None
    for i in range(0, WordDictList_len):
        WordItem = WordDictList_Sort[i]
        ### filter
        if(FilterLen > 0):
            #WordItemLen = len(WordItem['word'])
            if(FilterLen != WordItem['len']):
                continue
        
        if(FilterCharType != None):
            WordCharType = get_scripts(WordItem['word'])
            if(len(FilterCharType) == 1):
                if(FilterCharType != WordCharType):
                    continue
            #else:
            #    if(FilterCharType == 'keyword'):
            #        if(get_keyword_type_num__scripts(WordCharType) >= 1)
            #        continue

        ###            
        FilterCnt += 1
        TotalFreq += WordItem['freq']

        AddFalg = False
        if(FreqListItem == None):
            AddFalg = True
        else:
            if(FreqListItem['freq'] == WordItem['freq']):
                FreqListItem['count'] += 1
            else:
                AddFalg = True

        if(AddFalg == True):
             FreqListItem = {'freq': WordItem['freq'], 'count': 1}
             FreqList.append(FreqListItem)

    FreqListInfo = {'TotalFreq':TotalFreq, 'ListSum':FilterCnt, 'FilterLen':FilterLen, 'List':FreqList}
    return FreqListInfo

def PrintWordDictListInfo(WordDictListInfo):
    if(WordDictListInfo == None): return
    print ('List Num:', len(WordDictListInfo['List']), 'List Sum:', WordDictListInfo['ListSum'])
    print ('Total Freq:', WordDictListInfo['TotalFreq'])
    if WordDictListInfo.get('FilterLen') != None:
        print ('Len Filter:', WordDictListInfo['FilterLen'])
    if WordDictListInfo.get('FilterFreq') != None:
        print ('Freq Filter:', WordDictListInfo['FilterFreq'])
    print (*WordDictListInfo['List'],sep='\n')

def GetWordDictList_LenListInfo(WordDictList, FilterFreq = 0, FilterCharType = None):
    #
    LenListInfo = []
    
    TotalFreq = 0

    if(WordDictList == None): 
        return LenListInfo

    # sort by freq
    WordDictList_Sort = WordDictList.copy();
    WordDictList_Sort.sort(key = lambda wd: (wd['len'], wd['word'])) # by len low, abc

    WordDictList_len = len(WordDictList_Sort)
    FilterCnt = 0
    LenList = []
    LenListItem = None
    for i in range(0, WordDictList_len):
        WordItem = WordDictList_Sort[i]
        #WordItemLen = len(WordItem['word'])
    
        ### filter
        #if(FilterLen > 0):
        #    if(FilterLen != WordItem['len']):
        #        continue
        
        if(FilterCharType != None):
            WordCharType = get_scripts(WordItem['word'])
            if(len(FilterCharType) == 1):
                if(FilterCharType != WordCharType):
                    continue
            #else:
            #    if(FilterCharType == 'keyword'):
            #        if(get_keyword_type_num__scripts(WordCharType) >= 1)
            #        continue

        if(FilterFreq > 0):
            if(FilterFreq != WordItem['freq']):
                continue

        ###            
        FilterCnt += 1
        TotalFreq += WordItem['freq']

        AddFalg = False
        if(LenListItem == None):
            AddFalg = True
        else:
            if(LenListItem['len'] == WordItem['len']):
                LenListItem['count'] += 1
            else:
                AddFalg = True

        if(AddFalg == True):
             LenListItem = {'len': WordItem['len'], 'count': 1}
             LenList.append(LenListItem)

    LenListInfo = {'TotalFreq':TotalFreq, 'ListSum':FilterCnt, 'FilterFreq':FilterFreq, 'List':LenList}
    return LenListInfo

def GetBackWordDictList__WordDictList(WordDictList, 
    FilterLen = 0, FilterCharType = None, FilterFreq = 0):
    #
    BackWordDictList = []
    #
    if(WordDictList == None): 
        return
    #
    WordDictList_len = len(WordDictList)
    FilterCnt = 0
    for i in range(WordDictList_len):
        WordItem = WordDictList[i]
        # filter
        if(FilterLen > 0):
            #=WordItemLen = WordItem['len']
            WordItemLen = len(WordItem['word'])
            if(FilterLen != WordItemLen):
                continue
        if(FilterCharType != None):
            WordCharType = get_scripts(WordItem['word'])
            if(len(FilterCharType) == 1):
                if(FilterCharType != WordCharType):
                    continue
            #else:
            #    if(FilterCharType == 'keyword'):
            #        if(get_keyword_type_num__scripts(WordCharType) >= 1)
            #        continue
        if(FilterFreq > 0): # ?????? ??????
            if(FilterFreq != WordItem['freq']):
                continue
        ###            
        FilterCnt += 1

        BackWordItem = dict(WordItem)
        BackWordItem['word'] = get_backword_string(WordItem['word']) # ?????? ?????????
        BackWordDictList.append(BackWordItem)
    
    return BackWordDictList
        
def GetBackWordDictList__WordList(WordList, FilterLen = 0, 
    FilterCharType = None, FilterFreq = 0, LowerCasifyFlag=False):
    BackWordDictList = []
    WordDictList = GetWordDictList_WordList \
        (WordList, LowerCasifyFlag=LowerCasifyFlag)
    if(len(WordDictList) > 0):
        BackWordDictList = GetBackWordDictList__WordDictList(WordDictList, 
                            FilterLen, FilterCharType, FilterFreq)
    return BackWordDictList

def BackWordDictList_Suffix(BackWordDictList, Suffix):
    # ?????? ?????? ???????????? ????????? ?????? ?????? ??????
    # BackWordDictList: ????????? ????????? ??????(word) ??????
    # BackWordDictList ????????? ????????? ???????????? ????????? ?????? ??? ????????? ?????? ??????????????? ??????
    BackWordDictList.sort(key = lambda item: (item['word'])) # by abc

    #=suffix_rev = 'elba' <= -able reverse
    suffix_rev = Suffix[::-1] # 'elba' <= -able reverse
    findflag = False
    BackWordDictList_Find = []
    for worddict in BackWordDictList:
        if(worddict['word'].startswith(suffix_rev) == True):
            findflag = True
            worddict_copy = worddict.copy()
            BackWordDictList_Find.append(worddict_copy)
        else:    
            if(findflag == True):
                break # ????????? ???????????? ?????? ????????? ??? ????????? ??????
    #
    return BackWordDictList_Find

def SortWordDictList_CharTypeNum(WordList, EraseNonKeyword=False):
    # rename, not del
    WordDictList_Sort = SortWordDictList_CharTypeNum__List(WordList, EraseNonKeyword=EraseNonKeyword)
    return WordDictList_Sort

def SortWordDictList_CharTypeNum__List(WordList, EraseNonKeyword=False, LowerCasifyFlag=False):
    WordDictList = []
    if(WordList == None): return WordDictList

    WordDictList = GetWordDictList_WordList(WordList, 
        EraseNonKeyword=EraseNonKeyword, LowerCasifyFlag=LowerCasifyFlag)
    #print(WordDictList)
    WordDictList_Sort = WordDictList.copy();
    WordDictList_Sort.sort(key = lambda wd: wd['script_num']) # by char-type-num
    #PrintWordDictList(WordDictList_Sort, OneLine=True, PrintIndex=True, SimpleFormat=True)
    return WordDictList_Sort

def DeleteWordDictList_Filter(WordDictList, FilterFreq=0, FreqType='same', FilterLen=0, FilterNum=0):
    if(WordDictList == None): return
    
    WordDictList_len = len(WordDictList)
    #print('WordDictList Len:', WordDictList_len)

    FilterCnt = 0
    inx = 0
    while(inx < WordDictList_len):
        #print(inx)

        ###
        WordDictItem = WordDictList[inx]
    
        # filter
        delFlag = False
        if(FilterLen > 0):
            #=WordLen = WordDictItem['len']
            WordLen = len(WordDictItem['word'])
            if(FilterLen == WordLen):
                delFlag = True
        if(FilterFreq > 0): # ?????? ??????
            if(FreqType == 'same'):
                if(WordDictItem['freq'] == FilterFreq):
                    delFlag = True
            elif(FreqType == 'more'):
                if(WordDictItem['freq'] > FilterFreq):
                    delFlag = True
            elif(FreqType == 'morethan'):
                if(WordDictItem['freq'] >= FilterFreq):
                    delFlag = True
            elif(FreqType == 'less'):
                if(WordDictItem['freq'] < FilterFreq):
                    delFlag = True
            elif(FreqType == 'lessthan'):
                if(WordDictItem['freq'] <= FilterFreq):
                    delFlag = True
            else:   # ?????? ????????? ????????? ????????? ??????????????? ?????? ?????? ???????????? ??????.
                if(WordDictItem['freq'] == FilterFreq):
                    delFlag = True
            

        if(delFlag == True):
            FilterCnt += 1
            WordDictList.remove(WordDictItem)
            WordDictList_len -= 1

            #print('del num:', FilterCnt)

            #print(WordDictItem)
            #WordDictItem_String = GetWordDictItem_String(WordDictItem, OneLine=True, PrintingIndex=True, BackwardFlag=False, SimpleFormat=True)
            #print(WordDictItem_String)
        else: # ????????? ?????? ????????? ????????? ??????
            inx += 1

        if(FilterNum > 0):
            if(FilterCnt >= FilterNum):
                break
    
    #print('del num:', FilterCnt)

def DeleteWordDictList_ByWordList(WordDictList_Base, WordList_Filter, DelType='match', FilterNum=0):
    if(WordDictList_Base == None): return
    
    WordDictList_len = len(WordDictList_Base)
    #print('WordDictList Len:', WordDictList_len)

    FilterCnt = 0
    inx = 0
    while(inx < WordDictList_len):
        #print(inx)

        ###
        WordDictItem = WordDictList_Base[inx]
        #WordLen = WordDictItem['len']
        #WordLen = len(WordDictItem['word'])
    
        # filter
        delFlag = False
        if(WordDictItem['word'] in WordList_Filter):
            find_topic = True
        else:
            find_topic = False
        if(DelType == 'match'): # ????????? ??????
            if(find_topic != False): 
                delFlag = True
        else: # DelType == 'not' # ????????? ??????
            if(find_topic == False): 
                delFlag = True

        if(delFlag == True):
            FilterCnt += 1
            WordDictList_Base.remove(WordDictItem)
            WordDictList_len -= 1

            #print('del num:', FilterCnt)

            #print(WordDictItem)
            #WordDictItem_String = GetWordDictItem_String(WordDictItem, OneLine=True, PrintingIndex=True, BackwardFlag=False, SimpleFormat=True)
            #print(WordDictItem_String)
        else: # ????????? ?????? ????????? ????????? ??????
            inx += 1

        if(FilterNum > 0):
            if(FilterCnt >= FilterNum):
                break
    
    #print('del num:', FilterCnt)

def DeleteWordDictList_ByWordDictList(WordDictList_Base, WordDictList_Filter, DelType='match', FilterNum=0):
    if(WordDictList_Base == None): return
    
    WordDictList_len = len(WordDictList_Base)
    #print('WordDictList Len:', WordDictList_len)

    FilterCnt = 0
    inx = 0
    while(inx < WordDictList_len):
        #print(inx)

        ###
        WordDictItem = WordDictList_Base[inx]
        #WordLen = WordDictItem['len']
        #WordLen = len(WordDictItem['word'])
    
        # filter
        delFlag = False
        find_topic = next((findItem for findItem in WordDictList_Filter if findItem['word'] == WordDictItem['word']), False)
        if(DelType == 'match'): # ????????? ??????
            if(find_topic != False): 
                delFlag = True
        else: # DelType == 'not' # ????????? ??????
            if(find_topic == False): 
                delFlag = True

        if(delFlag == True):
            FilterCnt += 1
            WordDictList_Base.remove(WordDictItem)
            WordDictList_len -= 1

            #print('del num:', FilterCnt)

            #print(WordDictItem)
            #WordDictItem_String = GetWordDictItem_String(WordDictItem, OneLine=True, PrintingIndex=True, BackwardFlag=False, SimpleFormat=True)
            #print(WordDictItem_String)
        else: # ????????? ?????? ????????? ????????? ??????
            inx += 1

        if(FilterNum > 0):
            if(FilterCnt >= FilterNum):
                break
    
    #print('del num:', FilterCnt)

def MakeWordDictPair(WordDict1, WordDict2, Match=True, SecondFieldUse=False, OnlyCount=False):
    #
    DictPairList = [];

    MatchCnt = 0
    dict_len1 = len(WordDict1)
    for i in range(0, dict_len1):
        hgtopic = WordDict1[i]

        # format: ['word', 'freq']
        DictPairItem = None
        find_topic = next((TopicItem for TopicItem in WordDict2 if TopicItem['word'] == hgtopic['word']), False)
        if(Match == True): # ???????????? ???
            if(find_topic != False):
                ##print(find_topic)
                Freq = hgtopic['freq'] + find_topic['freq']
                DictPairItem = {
                    'word': find_topic['word'],
                    'freq': Freq,
                    '1': hgtopic['freq'],
                    '2': find_topic['freq'],
                }
        else: # ???????????? ?????? ???
            if(find_topic == False):
                if(SecondFieldUse == True): # ??? ?????? ????????? ?????? ??????
                    DictPairItem = {
                        'word': hgtopic['word'],
                        'freq': hgtopic['freq'],
                        '2' : hgtopic['freq'],
                    }
                else: # ??? ?????? ????????? ?????? ??????
                    DictPairItem = {
                        'word': hgtopic['word'],
                        'freq': hgtopic['freq'],
                        '1' : hgtopic['freq'],
                    }
        
        if(DictPairItem != None):
            MatchCnt += 1
            if(OnlyCount == True):
                pass
            else: 
                DictPairList.append(DictPairItem)

    #print('common topic num : ', len(DictPairList))

    #print(DictPairList)
    #PrintDictList_ByLine(DictPairList)

    ####################
    Src1 = ''
    Src2 = ''
    if 'src' in WordDict1: # key??? ?????? ?????? ??????.
        Src1 = WordDict1['src']
    if 'src' in WordDict2: # key??? ?????? ?????? ??????.
        Src2 = WordDict2['src']

    WordDictPair = {
        #----- ??? ?????? ?????? ?????? ??????
        'src1': Src1,
        'num1': len(WordDict1),
        'freq1': GetWordDictList_TotalFreq(WordDict1),
        #----- ??? ?????? ?????? ?????? ??????
        'src2': Src2,
        'num2': len(WordDict2),
        'freq2': GetWordDictList_TotalFreq(WordDict2),
        #----- {???/?????????} ?????? ??????
        #'ListNum': len(DictPairList), # (OnlyCount == True) ??? ?????? ????????? ?????? ???????????? ????????? ?????????.
        'ListNum': MatchCnt,
        'list': DictPairList,
    }
    #print(WordDictPair)

    return WordDictPair

def PrintWordDictPair(WordDictPair):
    print('-----')
    print('src1: ', WordDictPair['src1'])
    print('src1-num: ', WordDictPair['num1'])
    print('src1-freq: ', WordDictPair['freq1'])

    print('-----')
    print('src2: ', WordDictPair['src2'])
    print('src2-num: ', WordDictPair['num2'])
    print('src2-freq: ', WordDictPair['freq2'])

    print('-----')
    print('list num : ', WordDictPair['ListNum'])
    print('list count : ', len(WordDictPair['list']))
    #print(WordDictPair['list'])
    PrintDictList_ByLine(WordDictPair['list'])

    if(len(WordDictPair['list']) > 0):
        WordList_WordDictPair = WordDictPair['list'].copy()
        WordList_WordDictPair.sort(key = lambda wd: (-wd['freq'])) # by freq high
        print('-----')
        print('topic num (sort by freq): ', len(WordList_WordDictPair))
        PrintDictList_ByLine(WordList_WordDictPair)

def UnifyWordDictPair(WordDict1, WordDict2, OnlyCount=False):
    #
    DictPairList_Match = MakeWordDictPair(WordDict1, WordDict2, Match=True, OnlyCount=OnlyCount)
    if(OnlyCount == True): # ????????? ?????? ???????????? ?????? ?????? ????????? ?????? ??????.
        pass
    else:
        DictPairList_First = MakeWordDictPair(WordDict1, WordDict2, Match=False, OnlyCount=OnlyCount)
        DictPairList_Second = MakeWordDictPair(WordDict2, WordDict1, Match=False, SecondFieldUse=True, OnlyCount=OnlyCount)

    #-----
    DictPairList = []
    if(OnlyCount == True): # ????????? ?????? ???????????? ?????? ?????? ????????? ?????? ??????.
        pass
    else:
        DictPairList.extend(DictPairList_Match['list'])
        DictPairList.extend(DictPairList_First['list'])
        DictPairList.extend(DictPairList_Second['list'])

    #-----
    DictPairList.sort(key = lambda wd: (wd['word'])) # by abc

    ####################
    Src1 = ''
    Src2 = ''
    if 'src' in WordDict1: # key??? ?????? ?????? ??????.
        Src1 = WordDict1['src']
    if 'src' in WordDict2: # key??? ?????? ?????? ??????.
        Src2 = WordDict2['src']

    WordNum1 = len(WordDict1)
    WordNum2 = len(WordDict2)
    #=WordNum_Match = DictPairList_Match['list'] # (OnlyCount == True) ??? ?????? ????????? ?????? ???????????? ????????? ?????????.
    WordNum_Match = DictPairList_Match['ListNum']

    WordDictPair = {
        #----- ??? ?????? ?????? ?????? ??????
        'src1': Src1,
        'num1': WordNum1,
        'freq1': GetWordDictList_TotalFreq(WordDict1),
        #----- ??? ?????? ?????? ?????? ??????
        'src2': Src2,
        'num2': WordNum1,
        'freq2': GetWordDictList_TotalFreq(WordDict2),
        #----- {???/?????????} ?????? ??????
        #'ListNum': len(DictPairList), # (OnlyCount == True) ??? ?????? ????????? ?????? ???????????? ????????? ?????????.
        'ListNum': (WordNum1 + WordNum2 - WordNum_Match),
        'list': DictPairList,
    }
    #print(WordDictPair)

    return WordDictPair

def MakeFreqList_WordDictList(WordDict):
    #
    FreqList = [];

    dict_num = len(WordDict)
    for i in range(0, dict_num):
        hgtopic = WordDict[i]

        # format: ['word', 'freq']
        if('freq' not in hgtopic):
            break
        #
        FreqList.append(hgtopic['freq'])
    return FreqList

def GetBasicForm__suiffx_s(realword):
    from hgeng_spell_rule import (
        replace_end__s_dict_4, replace_end__s_dict_5, del_end__s_list_3, 
        del_end__s_list_4, del_end__s_list_5, 
    )
    # ?????? ???????????? ?????????(s ??????, es ??????, 's)
    if(realword.endswith("'s") == True): # ??? ??? {'s} ??????
        basicform = realword[:-2] # ??? ??? {'s} ??????
        return basicform
    #
    basicform = ''
    subword = realword[-5:]
    if(subword in del_end__s_list_5):
        basicform = realword[:-1] # ??? ??? 's' ??????
    else:
        repword = replace_end__s_dict_5.get(subword)
        if(len(realword) >= 5) and (repword is not None):
            # 5?????? ??????: [0] wives -> wife
            headword = realword[:-5]
            basicform = headword + repword # ~wives -> ~wife
        else:                    
            subword = realword[-4:]
            if(subword in del_end__s_list_4):
                basicform = realword[:-1] # ??? ??? 's' ??????
            else:
                repword = replace_end__s_dict_4.get(subword)
                if(len(realword) > 4) and (repword is not None):
                    # 4???????????? ?????? ??????.: [x] lies -> ly
                    headword = realword[:-4]
                    basicform = headword + repword # ~ties -> ~ty
                else:                    
                    subword = realword[-3:]
                    if(subword in del_end__s_list_3):
                        basicform = realword[:-1] # ??? ??? 's' ??????
    #
    return basicform
    
def FilterWordList__WordList6(WordList, ExcFilter=None, 
    CliticsModify=False, ExcChar1=False, ExcNumber=False,
    UnifySpellRule=False):
    '''
    ExcFilter: # ????????? ??????
    CliticsModify: ??????(Clitics) ?????? # {~'s}, {~'t}, {~'d}??? {~}??? ?????????.
    ExcChar1:  # 1???????????? ?????? ?????? ?????????.
    ExcNumber: # ????????? ?????? ?????? ?????????.
    UnifySpellRule: # ?????? ???????????? ?????????(s ??????, es ??????, 's)
    '''
    # old: FilterWordList__WordList5
    if(CliticsModify == True):
        from hgeng_spell_rule import eng_clitics_suffix, eng_clitics_form_dict
    #==print('WordList:', WordList)

    j = 0
    wordnum = len(WordList)
    while(j < wordnum):
        word = WordList[j]
        newword = word

        #
        delFlag = False
        if(ExcFilter != None): # ExcFilter:stopword_list
            if(newword in ExcFilter):
                delFlag = True
        
        # ?????? ????????? ??? ???????????? ?????? ??????
        if(delFlag == False):
            newword = newword.strip('!?,.<>/:;{[]}|~!^&*`()"\'')

        if(delFlag == False) and (CliticsModify == True):
            # {~'m}, {~'s}, {~'t}, {~'d}??? {~}??? ?????????.
            repword = eng_clitics_form_dict.get(newword)
            if(len(newword) > 0) and (repword is not None):
                newword = repword # "wouldn't" -->'would', "wouldn" -->'would',

            #-----
            subword = newword[-3:]
            if(len(newword) > 3) and (subword in eng_clitics_suffix):
                # 3???????????? ?????? ??????.
                newword = newword[:-3] # "'ll", "'re", "'ve", 
            else:
                subword = newword[-2:]
                if(len(newword) > 2) and (subword in eng_clitics_suffix):
                    # 2???????????? ?????? ??????.
                    newword = newword[:-2] # "'m", "'d", "'s", "'t", 

        if(delFlag == False) and (UnifySpellRule == True):
            # ?????? ???????????? ?????????(s ??????, es ??????, 's)
            basicform = GetBasicForm__suiffx_s(newword)
            if(len(basicform) > 0):
                newword = basicform
        
        # ????????? ?????? ????????? ????????? ?????? ??????
        if(ExcFilter != None): # ExcFilter:stopword_list
            if(newword in ExcFilter):
                delFlag = True
        #
        if(delFlag == False) and (ExcChar1 == True):
            if(len(newword) <= 1): # 1???????????? ?????? ?????? ?????????.
                delFlag = True
        if(delFlag == False) and (ExcNumber == True):
            if(newword.isnumeric()): # ????????? ?????? ?????? ?????????.
                delFlag = True
        #
        if(delFlag == True):
            del WordList[j]

            wordnum -= 1
            continue
        #
        WordList[j] = newword
        #
        j += 1
    #=print(WordList)

def GetWordList__Text6(Text, ExcFilter=None, LowerCase=False, 
    CliticsModify=False, ExcChar1=False, ExcNumber=False,
    UnifySpellRule=False):
    '''
    ExcFilter: # ????????? ??????
    LowerCase: # ???????????? ???????????? ??????
    CliticsModify: ??????(Clitics) ?????? # {~'s}, {~'t}, {~'d}??? {~}??? ?????????.
    ExcChar1:  # 1???????????? ?????? ?????? ?????????.
    ExcNumber: # ????????? ?????? ?????? ?????????.
    UnifySpellRule: # ?????? ???????????? ?????????(s ??????, es ??????, 's)
    '''
    # old: GetWordList__Text5
    #==print('Text:', Text)
    word_list = HGTokenize(Text, LowerCase=LowerCase)
    if(LowerCase == True): # ????????????
        #-----
        # HGTokenize() ???????????? ???????????? ???????????? ????????? ???????????? ??? ?????? ???.
        #=word_list = [wd.lower() for wd in word_list]
        #-----
        pass
    FilterWordList__WordList6(word_list, ExcFilter=ExcFilter, 
        CliticsModify=CliticsModify, ExcChar1=ExcChar1, ExcNumber=ExcNumber,
        UnifySpellRule=UnifySpellRule)
    #=print(word_list)
    return word_list

def GetWordLists__TextList(TextList, ExcFilter=None, 
    LowerCase = False, CliticsModify=False, ExcChar1=False, ExcNumber=False,
    UnifySpellRule=False,
    PrintProcState=False):
    '''
    ExcFilter: # ????????? ??????
    LowerCase: # ???????????? ???????????? ??????
    CliticsModify: ??????(Clitics) ?????? # {~'s}, {~'t}, {~'d}??? {~}??? ?????????.
    ExcChar1:  # 1???????????? ?????? ?????? ?????????.
    ExcNumber: # ????????? ?????? ?????? ?????????.
    UnifySpellRule: # ?????? ???????????? ?????????(s ??????, es ??????, 's)
    PrintProcState: ?????? ?????? ??????(????????? ????????? ?????? ?????? ?????? ?????? ??? ?????? ??????)
    '''
    #==print('TextList:', TextList)
    WordLists = []
    for ti, text in enumerate(TextList):
        word_list = GetWordList__Text6(text, ExcFilter=ExcFilter, LowerCase=LowerCase,
            CliticsModify=CliticsModify, ExcChar1=ExcChar1, ExcNumber=ExcNumber,
            UnifySpellRule=UnifySpellRule)
        #        
        WordLists.append(word_list)

        if(PrintProcState == True):
            print(f'[{ti}] make wordlist...')

    #=print(WordLists)
    return WordLists

def FilterWordList__WordList(WordList, WordList_Filter, ExcFlag=True):
    #==print('WordList:', WordList)
    #==print('WordList_Filter:', WordList_Filter)
   
    if(ExcFlag == True):
        WordList_New = [wd for wd in WordList if wd not in WordList_Filter]
    else:
        WordList_New = [wd for wd in WordList if wd in WordList_Filter]

    #=print(WordList_New)
    return WordList_New

def FilterWordLists__WordList(WordLists, WordList_Filter, ExcFlag=True):
    #==print('WordLists:', WordLists)
    #==print('WordList_Filter:', WordList_Filter)

    WordLists_new = []
    for WordList in WordLists:
        if(ExcFlag == True):
            WordList_New = [wd for wd in WordList if wd not in WordList_Filter]
        else:
            WordList_New = [wd for wd in WordList if wd in WordList_Filter]
        WordLists_new.append(WordList_New)

    #=print(WordLists_new)
    return WordLists_new

def GetTextList_Texts__DocInxList(TextList, DocInxList, LineNum=0, NonMargin=False):
    NewTextList = []
    for DocInx in DocInxList:
        if(DocInx < 0): # DocInx : zoro-base
            assert(False)
            NewTextList = None
            break
        else:
            if(LineNum >= 1):
                Texts = TextList[DocInx].splitlines()
                NewTexts = Texts[0:LineNum]
                if(NonMargin == True):
                    NewTexts = []
                    txcnt = 0
                    for ti in Texts:
                        if(txcnt >= LineNum):
                            break
                        if(len(ti) > 0):
                            NewTexts.append(ti.strip(' ') + '\n')
                            txcnt += 1
                Text = ''.join(NewTexts)

            else:
                Text = TextList[DocInx]
            NewTextList.append(Text)
    return NewTextList


#------------------------
#------------------------
#------------------------
from unittest import TestCase, main

class HGTest(TestCase):
    text1 = '?????? ?????? ?????? ?????? ?????? ??????'
    text2 = '?????? ????????? ?????? ????????? ????????????'
    text3 = '?????? ?????? ?????? ?????? ??????'
    text4 = '?????? ????????? ?????? ?????????'
    text5 = '????????? ????????? ????????? ???????????? ?????????'

    TextList = [text1, text2]

    def setUp(self):
        self.a = 'test setup'
        print('setUp(): ok')

    def test_run(self):
        print(self.TextList)

        stoplist = ['??????']
        wordlist = GetWordLists__TextList(self.TextList, ExcFilter=stoplist)
        print(wordlist)

        stoplist = ['??????', '??????']
        wordlist = GetWordLists__TextList(self.TextList, ExcFilter=stoplist)
        print(wordlist)

        print('test_run: ok')

if __name__ == '__main__':
    main()
