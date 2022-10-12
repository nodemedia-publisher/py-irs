#------------------------
#------------------------
import hgsysinc
from hgwordfile import (
    ReadTxtFile,
    ReadBookSelf__TxtPath, ReadBookSelf__TpxPath, 
    PrintBookSelf_DocList, GetDictFreq_WordFreqText,
    load_textlist__txtpath,
)

#---
#---
def time_laps_example(): # 경과 시간 측정용 예제 코드 - 지우지 않고 참고용 보관
    from datetime import datetime
    time_beg = datetime.now()

    # for - range(시작값=0, 끝값, 증분값=1)
    곱하기 = 1
    for i in range(1, 1001):
        곱하기 *= i
    print(len(str(곱하기)), '자리')
    #-print(곱하기)

    time_end = datetime.now()
    elapsed = time_end - time_beg
    print('Elapsed:', elapsed)

#---
#---
def load_textlist_kbs_type2_89(TextSelect_Simple = True):
    #encoding='utf-8' 
    #encoding='euc-kr'#표준완성형 범위를 벗어난 통합완성형 코드는 오류 때문에 못 읽는다
    encoding='cp949'

    #=TextSelect_Simple = True # 공백문자 토큰 사용
    #=TextSelect_Simple = False # 미리 해석된 주제어 토큰 사용
    #--- 
    if(TextSelect_Simple == True):
        TokenTitle = '{공백문자}' 

        pathname_1 = './../testtext/hgdatsci/_-wet_txt_89/*.txt'
        wet_txt_list1 = ReadBookSelf__TxtPath(pathname_1, is_state=True, encoding=encoding)

        pathname_2 = './../testtext/hgdatsci/_-spo_txt_104/*.txt'
        wet_txt_list2= ReadBookSelf__TxtPath(pathname_2, is_state=False, encoding=encoding)
    else:
        TokenTitle = '{주제어}' 

        pathname_1 = './../testtext/hgdatsci/_-wet_89/*.txt.tpx-wordlist.txt'
        wet_txt_list1 = ReadBookSelf__TpxPath(pathname_1, is_state=True, encoding=encoding)

        pathname_2 = './../testtext/hgdatsci/_-spo_104/*.txt.tpx-wordlist.txt'
        wet_txt_list2= ReadBookSelf__TpxPath(pathname_2, is_state=False, encoding=encoding)

    wet_txt_list = wet_txt_list1.copy()
    wet_txt_list.extend(wet_txt_list2)
    #=PrintBookSelf_DocList(wet_txt_list)

    #
    print('@@@ [날씨]와 [스포츠]로 분류 테스트', len(wet_txt_list), 'files(',
            len(wet_txt_list1), '+', len(wet_txt_list2),') @@@')
    print('@@@ @@@ [토큰처리] - ', TokenTitle)
    print('files 1:', len(wet_txt_list1), pathname_1)
    print('files 2:', len(wet_txt_list2), pathname_2)
    print('files:', len(wet_txt_list))

    return wet_txt_list, TokenTitle, wet_txt_list1, wet_txt_list2

def load_textlist_kbs_type2_10(TextSelect_Simple = True):
    #encoding='utf-8' 
    #encoding='euc-kr' # 표준완성형이라서 범위를 벗어난 통합완성형 코드가 있으면 오류 발생하여 읽지 못한다.
    encoding='cp949'

    #=TextSelect_Simple = True # 공백문자 토큰 사용
    #=TextSelect_Simple = False # 미리 해석된 주제어 토큰 사용
    #--- 
    if(TextSelect_Simple == True):
        TokenTitle = '{공백문자}' 

        pathname_1 = './../testtext/hgdatsci/_-wet_txt_10/*.txt'
        wet_txt_list1 = ReadBookSelf__TxtPath(pathname_1, is_state=True, encoding=encoding)

        pathname_2 = './../testtext/hgdatsci/_-spo_txt_10/*.txt'
        wet_txt_list2= ReadBookSelf__TxtPath(pathname_2, is_state=False, encoding=encoding)
    else:
        TokenTitle = '{주제어}' 

        #pathname_1 = './../testtext/hgdatsci/_-wet_10/*.txt.tpx-wordlist.txt'
        #wet_txt_list1 = ReadBookSelf__TpxPath(pathname_1, is_state=True, encoding=encoding)
        #
        #pathname_2 = './../testtext/hgdatsci/_-spo_10/*.txt.tpx-wordlist.txt'
        #wet_txt_list2= ReadBookSelf__TpxPath(pathname_2, is_state=False, encoding=encoding)
        assert False, '아직 준비가 되어 있지 않습니다.'

    wet_txt_list = wet_txt_list1.copy()
    wet_txt_list.extend(wet_txt_list2)
    #=PrintBookSelf_DocList(wet_txt_list)

    #
    print('@@@ [날씨]와 [스포츠]로 분류 테스트', len(wet_txt_list), 'files(',
            len(wet_txt_list1), '+', len(wet_txt_list2),') [kmeans] @@@')
    print('@@@ @@@ [토큰처리] - ', TokenTitle)
    print('files 1:', len(wet_txt_list1), pathname_1)
    print('files 2:', len(wet_txt_list2), pathname_2)
    print('files:', len(wet_txt_list))

    return wet_txt_list, TokenTitle, wet_txt_list1, wet_txt_list2

def load_textlist_kbs_stop(TextSelect_Simple = True):
    #---stopword

    #=TextSelect_Simple = True # 공백문자 토큰 사용
    #=TextSelect_Simple = False # 미리 해석된 주제어 토큰 사용
    #--- 
    if(TextSelect_Simple == True):
        stop_file_kbs = './../testtext/hgdatsci/_kbs_stop_word.txt/'
        stop_file_wet = './../testtext/hgdatsci/_wet_stop_word.txt/'
        stop_file_spo = './../testtext/hgdatsci/_spo_stop_word.txt/'
    else:
        stop_file_kbs = './../testtext/hgdatsci/_kbs_stop_morp.txt/'
        stop_file_wet = './../testtext/hgdatsci/_wet_stop_morp.txt/'
        stop_file_spo = './../testtext/hgdatsci/_spo_stop_morp.txt/'

    stop_kbs = ReadTxtFile(stop_file_kbs, DeleteComment=True)
    stop_wet = ReadTxtFile(stop_file_wet, DeleteComment=True)
    stop_spo = ReadTxtFile(stop_file_spo, DeleteComment=True)
    stoplist = stop_wet + stop_spo + stop_kbs
    stoplist = set(stoplist.split())
    
    #=print('stoplist:', stoplist)

    return stoplist

def load_textlist_kbs_type1(filenum=10, PrintFlag=False, Category='wet', TextSelect_Simple = True):
    #encoding='utf-8' 
    #encoding='euc-kr' # 표준완성형이라서 범위를 벗어난 통합완성형 코드가 있으면 오류 발생하여 읽지 못한다.
    encoding='cp949'

    #
    if(type(filenum) == str):
        filenum = int(filenum)

    #
    pathname = None
    
    #=TextSelect_Simple = True # 공백문자 토큰 사용
    #=TextSelect_Simple = False # 미리 해석된 주제어 토큰 사용
    #--- 
    if(Category == 'wet'):  # '{날씨}
        if(TextSelect_Simple == True):
            pathname_10 = './../testtext/hgdatsci/_-wet_txt_10/*.txt'
            pathname_20 = './../testtext/hgdatsci/_-wet_txt_20/*.txt'
            pathname_89 = './../testtext/hgdatsci/_-wet_txt_89/*.txt'
        else:
            pathname_10 = './../testtext/hgdatsci/_-wet_10/*.txt.tpx-wordlist.txt'
            pathname_20 = './../testtext/hgdatsci/_-wet_20/*.txt.tpx-wordlist.txt'
            pathname_89 = './../testtext/hgdatsci/_-wet_89/*.txt.tpx-wordlist.txt'
    else: # 'spo' = {스포츠}
        if(TextSelect_Simple == True):
            pathname_10 = './../testtext/hgdatsci/_-spo_txt_10/*.txt'
            pathname_20 = './../testtext/hgdatsci/_-spo_txt_20/*.txt'
            pathname_89 = './../testtext/hgdatsci/_-spo_txt_104/*.txt'
        else:
            pathname_10 = './../testtext/hgdatsci/_-spo_10/*.txt.tpx-wordlist.txt'
            pathname_20 = './../testtext/hgdatsci/_-spo_20/*.txt.tpx-wordlist.txt'
            pathname_89 = './../testtext/hgdatsci/_-spo_104/*.txt.tpx-wordlist.txt'

    if(filenum == 10):
        pathname = pathname_10
    elif(filenum == 20):
        pathname = pathname_20
    elif((filenum == 89) or (filenum == 104)):
        pathname = pathname_89
    else:
        return None

    if(TextSelect_Simple == True):
        txt_list = ReadBookSelf__TxtPath(pathname, encoding=encoding)
    else:
        txt_list = ReadBookSelf__TpxPath(pathname, encoding=encoding)
    #=print('files:', len(txt_list))

    #
    if(PrintFlag == True):
        print('@@@ ', end='')
        if(Category == 'wet'):  # '{날씨}
            print('[날씨] ', end='')
        else:
            print('[스포츠] ', end='')
        print(len(txt_list), 'files(',len(txt_list),') @@@')
        print('files:', len(txt_list), pathname)

    #
    return txt_list

def load_textlist_president(TextSelect_Simple = True, PrintFlag=False, WordDictType=False):
    #encoding='utf-8' 
    #encoding='euc-kr' # 표준완성형이라서 범위를 벗어난 통합완성형 코드가 있으면 오류 발생하여 읽지 못한다.
    encoding='cp949'

    #=TextSelect_Simple = True # 공백문자 토큰 사용
    #=TextSelect_Simple = False # 미리 해석된 주제어 토큰 사용
    #--- 
    if(TextSelect_Simple == True):
        pathname_pr = './../testtext/hgdatsci/_presi_txt/*.txt'
        pathname = pathname_pr
        txt_list = ReadBookSelf__TxtPath(pathname, encoding=encoding)
    else:
        pathname_pr = './../testtext/hgdatsci/_presi/*.txt.tpx-wordlist.txt'
        pathname = pathname_pr
        txt_list = ReadBookSelf__TpxPath(pathname, encoding=encoding)

    if(PrintFlag == True):
        print('@@@ 대한민국 대통령 취임사 19개 파일 @@@')
        print('files:', len(txt_list), pathname)

    #
    if(WordDictType == True):
        from hgwordlist import GetWordDictList_String

        WordDictLists = []
        for book in txt_list:
            WordDictList = GetWordDictList_String(book.text)
            WordDictLists.append(WordDictList)
        return WordDictLists
    else:
        textlist = [book.text for book in txt_list]
        return textlist

def load_textlist_kbs_type5(TextSelect_Simple = True):
    #encoding='utf-8' 
    #encoding='euc-kr' # 표준완성형이라서 범위를 벗어난 통합완성형 코드가 있으면 오류 발생하여 읽지 못한다.
    encoding='cp949'

    #=TextSelect_Simple = True # 공백문자 토큰 사용
    #=TextSelect_Simple = False # 미리 해석된 주제어 토큰 사용
    #--- 
    if(TextSelect_Simple == True):
        TokenTitle = '{공백문자}' 

        pathname_1 = './../testtext/hgdatsci/_-spo_cate_5_txt/base/*.txt'
        pathname_2 = './../testtext/hgdatsci/_-spo_cate_5_txt/basket/*.txt'
        pathname_3 = './../testtext/hgdatsci/_-spo_cate_5_txt/foot/*.txt'
        pathname_4 = './../testtext/hgdatsci/_-spo_cate_5_txt/skate/*.txt'
        pathname_5 = './../testtext/hgdatsci/_-spo_cate_5_txt/volley/*.txt'

        wet_txt_list1 = ReadBookSelf__TxtPath(pathname_1, is_state=False, encoding=encoding)
        wet_txt_list2= ReadBookSelf__TxtPath(pathname_2, is_state=False, encoding=encoding)
        wet_txt_list3= ReadBookSelf__TxtPath(pathname_3, is_state=False, encoding=encoding)
        wet_txt_list4= ReadBookSelf__TxtPath(pathname_4, is_state=False, encoding=encoding)
        wet_txt_list5= ReadBookSelf__TxtPath(pathname_5, is_state=False, encoding=encoding)
    else:
        TokenTitle = '{주제어}' 

        pathname_1 = './../testtext/hgdatsci/_-spo_cate_5/base/*.txt.tpx-wordlist.txt'
        pathname_2 = './../testtext/hgdatsci/_-spo_cate_5/basket/*.txt.tpx-wordlist.txt'
        pathname_3 = './../testtext/hgdatsci/_-spo_cate_5/foot/*.txt.tpx-wordlist.txt'
        pathname_4 = './../testtext/hgdatsci/_-spo_cate_5/skate/*.txt.tpx-wordlist.txt'
        pathname_5 = './../testtext/hgdatsci/_-spo_cate_5/volley/*.txt.tpx-wordlist.txt'

        wet_txt_list1 = ReadBookSelf__TpxPath(pathname_1, is_state=False, encoding=encoding)
        wet_txt_list2= ReadBookSelf__TpxPath(pathname_2, is_state=False, encoding=encoding)
        wet_txt_list3= ReadBookSelf__TpxPath(pathname_3, is_state=False, encoding=encoding)
        wet_txt_list4= ReadBookSelf__TpxPath(pathname_4, is_state=False, encoding=encoding)
        wet_txt_list5= ReadBookSelf__TpxPath(pathname_5, is_state=False, encoding=encoding)

    wet_txt_list = wet_txt_list1.copy()
    wet_txt_list.extend(wet_txt_list2)
    wet_txt_list.extend(wet_txt_list3)
    wet_txt_list.extend(wet_txt_list4)
    wet_txt_list.extend(wet_txt_list5)
    #=PrintBookSelf_DocList(wet_txt_list)

    #
    print('@@@ [스포츠]로 분류 테스트', len(wet_txt_list), 'files(',
            len(wet_txt_list1), '+', len(wet_txt_list2), '+', 
            len(wet_txt_list3), '+', len(wet_txt_list4), '+', 
            len(wet_txt_list5), 
            ') @@@')
    print('@@@ @@@ [토큰처리] - ', TokenTitle)
    print('files 1:', len(wet_txt_list1), pathname_1)
    print('files 2:', len(wet_txt_list2), pathname_2)
    print('files 3:', len(wet_txt_list3), pathname_3)
    print('files 4:', len(wet_txt_list4), pathname_4)
    print('files 5:', len(wet_txt_list5), pathname_5)
    print('files:', len(wet_txt_list))

    return wet_txt_list, TokenTitle, wet_txt_list1, wet_txt_list2, wet_txt_list3, wet_txt_list4, wet_txt_list5

def load_textlist_reuters_type5():
    from _reuters_func import LoadReuterNewsText

    # topic-select
    TopicSet1 = ('alum', 'copper', 'gold', 'iron-steel', 'silver')
    TopicSet2 = ('alum', 'copper', 'gold', 'gas', 'lead', 'rubber', 'silver', 'zinc')
    TopicSet3 = ('alum', 'copper', 'gold', 'nat-gas', 'lead', 'rubber', 'silver', 'zinc')
    TopicSet11 = ('coffee','cocoa', 'cotton', 'orange', 'sugar')
    TopicSet12 = ('rice', 'corn', 'soybean', 'wheat')

    # news folder
    #reuter_folder = None
    reuter_folder = 'C:/Users/ia/Desktop/pyexam/ext-src/reuters21578/'
    TopicSet = TopicSet1 # 금속 원자재
    DocLists, TopicLists = LoadReuterNewsText(reuter_folder, PrintFilename=True, TopicSet=TopicSet)

    # 주제별로 검사용 파일 묶음으로 변환(성능 평가에서 필요)
    txt_list1 = []
    txt_list2 = []
    txt_list3 = []
    txt_list4 = []
    txt_list5 = []
    for toc_i, topic in enumerate(TopicSet):
        print(toc_i, ':', topic)
        for DocID in DocLists:
            if(topic == TopicLists[DocID]):
                if(toc_i == 0):
                    txt_list1.append(DocLists[DocID])
                elif(toc_i == 1):
                    txt_list2.append(DocLists[DocID])
                elif(toc_i == 2):
                    txt_list3.append(DocLists[DocID])
                elif(toc_i == 3):
                    txt_list4.append(DocLists[DocID])
                elif(toc_i == 4):
                    txt_list5.append(DocLists[DocID])
    #=print('textlen:', len(txt_list1), len(txt_list2), len(txt_list3), len(txt_list4), len(txt_list5))

    #=textlist = [DocLists[DocID] for DocID in DocLists] # DocLists format : dict
    textlist = []
    textlist.extend(txt_list1)
    textlist.extend(txt_list2)
    textlist.extend(txt_list3)
    textlist.extend(txt_list4)
    textlist.extend(txt_list5)
    #=print(len(textlist))

    #
    print('@@@ [Reuter 뉴스] 테스트', len(textlist), 'files(',
            len(txt_list1), '+', len(txt_list2), '+', 
            len(txt_list3), '+', len(txt_list4), '+', 
            len(txt_list5), 
            ') @@@')
    print('files 1:', len(txt_list1))
    print('files 2:', len(txt_list2))
    print('files 3:', len(txt_list3))
    print('files 4:', len(txt_list4))
    print('files 5:', len(txt_list5))
    print('files:', len(textlist), reuter_folder)

    return textlist, TopicSet, txt_list1, txt_list2, txt_list3, txt_list4, txt_list5

def load_train_test_kbs_type2(filenum=10, PrintFlag=False, TextSelect_Simple = True, SplitRate=0.9):
    from hgbasic import SplitListRate

    #-----
    bookself_kbs_wet = load_textlist_kbs_type1(filenum=filenum, 
            PrintFlag=PrintFlag, Category='wet', TextSelect_Simple = TextSelect_Simple)
    bookself_kbs_spo = load_textlist_kbs_type1(filenum=filenum, 
            PrintFlag=PrintFlag, Category='spo', TextSelect_Simple = TextSelect_Simple)
    if(PrintFlag == True):
        print()
        print(f'bookself_kbs_wet [{len(bookself_kbs_wet)}]:')
        print(f'bookself_kbs_spo [{len(bookself_kbs_spo)}]:')

    txtlist_wet = [book.text for book in bookself_kbs_wet]
    txtlist_spo = [book.text for book in bookself_kbs_spo]
    #=print()
    #=print(f'txtlist_wet [{len(txtlist_wet)}]:')
    #=print(f'txtlist_spo [{len(txtlist_spo)}]:')

    #-----
    train_wet, test_wet = SplitListRate(txtlist_wet, rate=SplitRate)
    train_spo, test_spo = SplitListRate(txtlist_spo, rate=SplitRate)
    #=print()
    #=print(f'train_wet [{len(train_wet)}], ', f'test_wet [{len(test_wet)}]')
    #=print(f'train_spo [{len(train_spo)}], ', f'test_spo [{len(test_spo)}]')

    #-----
    train_doclist_wet = [book.doc for book in bookself_kbs_wet][:len(train_wet)]
    train_doclist_spo = [book.doc for book in bookself_kbs_spo][:len(train_spo)]
    test_doclist_wet = [book.doc for book in bookself_kbs_wet][len(train_wet):]
    test_doclist_spo = [book.doc for book in bookself_kbs_spo][len(train_spo):]
    #=print()
    #=print(f'train_doclist_wet [{len(train_doclist_wet)}]:')
    #print(f'train_doclist_spo [{len(train_doclist_spo)}]:')
    #=print()
    #print(f'test_doclist_wet [{len(test_doclist_wet)}]:')
    #print(f'test_doclist_spo [{len(test_doclist_spo)}]:')

    train_doclist = train_doclist_wet + train_doclist_spo
    test_doclist = test_doclist_wet + test_doclist_spo

    if(PrintFlag == True):
        print()
        print('train doclist:')
        for i, doc_i in enumerate(train_doclist):
            print(f'{i} : {doc_i}')
        print()
        print('test doclist:')
        for i, doc_i in enumerate(test_doclist):
            print(f'{i} : {doc_i}')


    #-----
    trains_txt = train_wet + train_spo
    tests_txt = test_wet + test_spo
    #=print()
    #=print(f'trains_txt [{len(trains_txt)}]:')
    #=print(f'tests_txt [{len(tests_txt)}]:')

    #-----
    train_label = ['w' for i in train_wet] + ['s' for i in train_spo]
    test_label = ['w' for i in test_wet] + ['s' for i in test_spo]
    if(PrintFlag == True):
        print()
        print(f'train_label [{len(train_label)}]:', train_label)
        print(f'test_label [{len(test_label)}]:', test_label)

    #-----
    return trains_txt, tests_txt, train_label, test_label, train_doclist, test_doclist

def load_train_test_kbs_type5(PrintFlag=False, TextSelect_Simple = True, SplitRate=0.9):
    from hgbasic import SplitListRate

    #---
    TextSelect_Simple = False
    kbs_txt_list, TokenTitle, kbs_txt_list1, kbs_txt_list2, \
        kbs_txt_list3, kbs_txt_list4, kbs_txt_list5 = \
        load_textlist_kbs_type5(TextSelect_Simple = TextSelect_Simple)
    if(PrintFlag == True):
        print()
        print(f'bookself_kbs [{len(kbs_txt_list)}]:')

    txtlist_1 = [book.text for book in kbs_txt_list1]
    txtlist_2 = [book.text for book in kbs_txt_list2]
    txtlist_3 = [book.text for book in kbs_txt_list3]
    txtlist_4 = [book.text for book in kbs_txt_list4]
    txtlist_5 = [book.text for book in kbs_txt_list5]
    #=print()
    #=print(f'txtlist_1 [{len(txtlist_1)}]:')
    #=print(f'txtlist_2 [{len(txtlist_2)}]:')
    #=print(f'txtlist_3 [{len(txtlist_3)}]:')
    #=print(f'txtlist_4 [{len(txtlist_4)}]:')
    #=print(f'txtlist_5 [{len(txtlist_5)}]:')

    #-----
    train_1, test_1 = SplitListRate(txtlist_1, rate=SplitRate)
    train_2, test_2 = SplitListRate(txtlist_2, rate=SplitRate)
    train_3, test_3 = SplitListRate(txtlist_3, rate=SplitRate)
    train_4, test_4 = SplitListRate(txtlist_4, rate=SplitRate)
    train_5, test_5 = SplitListRate(txtlist_5, rate=SplitRate)
    #=print()
    print(f'train_1 [{len(train_1)}], ', f'test_1 [{len(test_1)}]')
    print(f'train_2 [{len(train_2)}], ', f'test_2 [{len(test_2)}]')
    print(f'train_3 [{len(train_3)}], ', f'test_3 [{len(test_3)}]')
    print(f'train_4 [{len(train_4)}], ', f'test_4 [{len(test_4)}]')
    print(f'train_5 [{len(train_5)}], ', f'test_5 [{len(test_5)}]')

    #-----
    train_doclist_1 = [book.doc for book in kbs_txt_list1][:len(train_1)]
    train_doclist_2 = [book.doc for book in kbs_txt_list2][:len(train_2)]
    train_doclist_3 = [book.doc for book in kbs_txt_list3][:len(train_3)]
    train_doclist_4 = [book.doc for book in kbs_txt_list4][:len(train_4)]
    train_doclist_5 = [book.doc for book in kbs_txt_list5][:len(train_5)]

    test_doclist_1 = [book.doc for book in kbs_txt_list1][len(train_1):]
    test_doclist_2 = [book.doc for book in kbs_txt_list2][len(train_2):]
    test_doclist_3 = [book.doc for book in kbs_txt_list3][len(train_3):]
    test_doclist_4 = [book.doc for book in kbs_txt_list4][len(train_4):]
    test_doclist_5 = [book.doc for book in kbs_txt_list5][len(train_5):]

    #=print()
    #=print(f'train_doclist_1 [{len(train_doclist_1)}]:')
    #=print(f'train_doclist_2 [{len(train_doclist_2)}]:')
    #=print(f'train_doclist_3 [{len(train_doclist_3)}]:')
    #=print(f'train_doclist_4 [{len(train_doclist_4)}]:')
    #print(f'train_doclist_5 [{len(train_doclist_5)}]:')

    train_doclist = train_doclist_1 + train_doclist_2 + train_doclist_3 + train_doclist_4 + train_doclist_5
    test_doclist = test_doclist_1 + test_doclist_2 + test_doclist_3 + test_doclist_4 + test_doclist_5

    if(PrintFlag == True):
        print()
        print('train doclist:', len(train_doclist))
        for i, doc_i in enumerate(train_doclist):
            print(f'{i} : {doc_i}')
        print()
        print('test doclist:', len(test_doclist))
        for i, doc_i in enumerate(test_doclist):
            print(f'{i} : {doc_i}')


    #-----
    trains_txt = train_1 + train_2 + train_3 + train_4 + train_5
    tests_txt = test_1 + test_2 + test_3 + test_4 + test_5
    #=print()
    #=print(f'trains_txt [{len(trains_txt)}]:')
    #print(f'tests_txt [{len(tests_txt)}]:')

    #-----
    #=train_label = ['1' for i in train_1] + ['2' for i in train_2] + ['3' for i in train_3] + ['4' for i in train_4] + ['5' for i in train_5]
    train_label = ['1' for i in train_1]
    train_label += ['2' for i in train_2]
    train_label += ['3' for i in train_3]
    train_label += ['4' for i in train_4]
    train_label += ['5' for i in train_5]
    test_label = ['1' for i in test_1]
    test_label += ['2' for i in test_2]
    test_label += ['3' for i in test_3]
    test_label += ['4' for i in test_4]
    test_label += ['5' for i in test_5]
    if(PrintFlag == True):
        print()
        print(f'train_label [{len(train_label)}]:', train_label)
        print(f'test_label [{len(test_label)}]:', test_label)

    #-----
    return trains_txt, tests_txt, train_label, test_label, train_doclist, test_doclist

def load_train_test_reuters_type5(PrintFlag=False, SplitRate=0.9):
    from hgbasic import SplitListRate

    #---
    TextSelect_Simple = False
    reut_txt_list, TopicSet, txtlist_1, txtlist_2, \
        txtlist_3, txtlist_4, txtlist_5 = \
        load_textlist_reuters_type5()
    if(PrintFlag == True):
        print()
        print(f'bookself_reuter [{len(reut_txt_list)}]:')

    #=print()
    #=print(f'txtlist_1 [{len(txtlist_1)}]:')
    #=print(f'txtlist_2 [{len(txtlist_2)}]:')
    #=print(f'txtlist_3 [{len(txtlist_3)}]:')
    #=print(f'txtlist_4 [{len(txtlist_4)}]:')
    #=print(f'txtlist_5 [{len(txtlist_5)}]:')

    #-----
    train_1, test_1 = SplitListRate(txtlist_1, rate=SplitRate)
    train_2, test_2 = SplitListRate(txtlist_2, rate=SplitRate)
    train_3, test_3 = SplitListRate(txtlist_3, rate=SplitRate)
    train_4, test_4 = SplitListRate(txtlist_4, rate=SplitRate)
    train_5, test_5 = SplitListRate(txtlist_5, rate=SplitRate)
    print()
    print(f'train_1 [{len(train_1)}], ', f'test_1 [{len(test_1)}]')
    print(f'train_2 [{len(train_2)}], ', f'test_2 [{len(test_2)}]')
    print(f'train_3 [{len(train_3)}], ', f'test_3 [{len(test_3)}]')
    print(f'train_4 [{len(train_4)}], ', f'test_4 [{len(test_4)}]')
    print(f'train_5 [{len(train_5)}], ', f'test_5 [{len(test_5)}]')

    #-----
    train_doclist_1 = [i for i in range(len(train_1))]
    train_doclist_2 = [(i+len(train_doclist_1)) for i in range(len(train_2))]
    train_doclist_3 = [(i+len(train_doclist_2)) for i in range(len(train_3))]
    train_doclist_4 = [(i+len(train_doclist_3)) for i in range(len(train_4))]
    train_doclist_5 = [(i+len(train_doclist_4)) for i in range(len(train_5))]

    test_doclist_1 = [i for i in range(len(test_1))]
    test_doclist_2 = [(i+len(test_doclist_1)) for i in range(len(test_2))]
    test_doclist_3 = [(i+len(test_doclist_2)) for i in range(len(test_3))]
    test_doclist_4 = [(i+len(test_doclist_3)) for i in range(len(test_4))]
    test_doclist_5 = [(i+len(test_doclist_4)) for i in range(len(test_5))]

    #=print()
    #=print(f'train_doclist_1 [{len(train_doclist_1)}]:')
    #=print(f'train_doclist_2 [{len(train_doclist_2)}]:')
    #=print(f'train_doclist_3 [{len(train_doclist_3)}]:')
    #=print(f'train_doclist_4 [{len(train_doclist_4)}]:')
    #=print(f'train_doclist_5 [{len(train_doclist_5)}]:')

    train_doclist = train_doclist_1 + train_doclist_2 + train_doclist_3 + train_doclist_4 + train_doclist_5
    test_doclist = test_doclist_1 + test_doclist_2 + test_doclist_3 + test_doclist_4 + test_doclist_5

    if(PrintFlag == True):
        print()
        print('train doclist:', len(train_doclist))
        for i, doc_i in enumerate(train_doclist):
            print(f'{i} : {doc_i}')
        print()
        print('test doclist:', len(test_doclist))
        for i, doc_i in enumerate(test_doclist):
            print(f'{i} : {doc_i}')


    #-----
    trains_txt = train_1 + train_2 + train_3 + train_4 + train_5
    tests_txt = test_1 + test_2 + test_3 + test_4 + test_5
    #=print()
    #=print(f'trains_txt [{len(trains_txt)}]:')
    #=print(f'tests_txt [{len(tests_txt)}]:')

    #-----
    # 숫자로 [레이블]표시
    train_label = ['0' for i in train_1]
    train_label += ['1' for i in train_2]
    train_label += ['2' for i in train_3]
    train_label += ['3' for i in train_4]
    train_label += ['4' for i in train_5]
    
    test_label = ['0' for i in test_1]
    test_label += ['1' for i in test_2]
    test_label += ['2' for i in test_3]
    test_label += ['3' for i in test_4]
    test_label += ['4' for i in test_5]
    #==# 문자열로 [레이블]표시
    #==train_label = [TopicSet[0] for i in train_1]
    #==train_label += [TopicSet[1] for i in train_2]
    #==train_label += [TopicSet[2] for i in train_3]
    #==train_label += [TopicSet[3] for i in train_4]
    #==train_label += [TopicSet[4] for i in train_5]
    #==
    #==test_label = [TopicSet[0] for i in test_1]
    #==test_label += [TopicSet[1] for i in test_2]
    #==test_label += [TopicSet[2] for i in test_3]
    #==test_label += [TopicSet[3] for i in test_4]
    #==test_label += [TopicSet[4] for i in test_5]

    if(PrintFlag == True):
        print()
        print(f'train_label [{len(train_label)}]:', train_label)
        print(f'test_label [{len(test_label)}]:', test_label)

    #-----
    return trains_txt, tests_txt, train_label, test_label, train_doclist, test_doclist

def load_textlist_us_president(PrintFlag=False, WordDictType=False):
    #-----
    # 미국 대통령 취임 연설
    # https://en.wikisource.org/wiki/Category:U.S._Presidential_Inaugural_Addresses
    # 59개 파일
    #-----
    from hgcrawl import get_inauguration_text_folder

    #encoding='utf-8' 
    #encoding='euc-kr' # 표준완성형이라서 범위를 벗어난 통합완성형 코드가 있으면 오류 발생하여 읽지 못한다.
    encoding='cp949'

    #---
    #=textfoler = './../ext-src/data/inauguration/text'
    textfoler = get_inauguration_text_folder()
    #---
    pathname_pr = textfoler + '/*.txt'
    pathname = pathname_pr
    txt_list = ReadBookSelf__TxtPath(pathname, encoding=encoding)

    if(PrintFlag == True):
        print('@@@ 미국 대통령 취임사 파일 @@@')
        print('files:', len(txt_list), pathname)

    #
    if(WordDictType == True):
        from hgwordlist import GetWordDictList_String

        WordDictLists = []
        for book in txt_list:
            WordDictList = GetWordDictList_String(book.text)
            WordDictLists.append(WordDictList)
        return WordDictLists
    else:
        textlist = [book.text for book in txt_list]
        return textlist

def load_dictfreq_kbs_2009(SortFlag=True): # [KBS 9시 뉴스: 2009년]
    from pathlib import Path
    #
    filename = Path('./../testtext/hgdatsci/_kbs_2009_/2009.가나순_WordList.txt')
    DictFreq = load_dictfreq_kbs_wordlist(filename, SortFlag)
    return DictFreq

def load_dictfreq_kbs_wordlist(filename, SortFlag=True):
    #encoding='utf-8' 
    #encoding='euc-kr'#표준완성형 범위를 벗어난 통합완성형 코드는 오류 때문에 못 읽는다
    encoding='cp949'
    #
    #=from pathlib import Path
    #=filename = Path('./../testtext/hgdatsci/_kbs_01_16/2009.tgx_WordList.txt')
    DictFreq = GetDictFreq_WordFreqText(filename, encoding=encoding)

    #
    TokenTitle = '{주제어}' 
    print('@@@ [KBS 9시 뉴스] @@@')
    print('@@@ @@@ [토큰처리] - ', TokenTitle)
    print('file:', filename)

    if SortFlag == True: # sort by a->z
        dict_by_keys = sorted(DictFreq.items(), key=lambda item: item[0]) #by key:a->z
        #=DictFreq_AZ = {dic[0]:dic[1] for dic in dict_by_keys} 
        DictFreq_AZ = dict(dict_by_keys)
        #print(*DictFreq_AZ, sep='\n')
        return DictFreq_AZ
    else:
        return DictFreq

def load_dictfreq_kbs_01_16(SortFlag=True): # [KBS 9시 뉴스: 16년치(2001~2016)]
    from pathlib import Path

    #encoding='utf-8' 
    #encoding='euc-kr' # 표준완성형이라서 범위를 벗어난 통합완성형 코드가 있으면 오류 발생하여 읽지 못한다.
    encoding='cp949'

    #
    FileList = [
        Path('./../testtext/hgdatsci/_kbs_01_16/2001.tgx_WordList_norm.txt'),
        Path('./../testtext/hgdatsci/_kbs_01_16/2002.tgx_WordList_norm.txt'),
        Path('./../testtext/hgdatsci/_kbs_01_16/2003.tgx_WordList_norm.txt'),
        Path('./../testtext/hgdatsci/_kbs_01_16/2004.tgx_WordList_norm.txt'),
        Path('./../testtext/hgdatsci/_kbs_01_16/2005.tgx_WordList_norm.txt'),
        Path('./../testtext/hgdatsci/_kbs_01_16/2006.tgx_WordList_norm.txt'),
        Path('./../testtext/hgdatsci/_kbs_01_16/2007.tgx_WordList_norm.txt'),
        Path('./../testtext/hgdatsci/_kbs_01_16/2008.tgx_WordList_norm.txt'),
        Path('./../testtext/hgdatsci/_kbs_01_16/2009.tgx_WordList_norm.txt'),
        Path('./../testtext/hgdatsci/_kbs_01_16/2010.tgx_WordList_norm.txt'),
        Path('./../testtext/hgdatsci/_kbs_01_16/2011.tgx_WordList_norm.txt'),
        Path('./../testtext/hgdatsci/_kbs_01_16/2012.tgx_WordList_norm.txt'),
        Path('./../testtext/hgdatsci/_kbs_01_16/2013.tgx_WordList_norm.txt'),
        Path('./../testtext/hgdatsci/_kbs_01_16/2014.tgx_WordList_norm.txt'),
        Path('./../testtext/hgdatsci/_kbs_01_16/2015.tgx_WordList_norm.txt'),
        Path('./../testtext/hgdatsci/_kbs_01_16/2016.tgx_WordList_norm.txt'),
    ]
    DictFreq = {}
    for filename in FileList:
        #=filename = Path('./../testtext/hgdatsci/_kbs_01_16/2009.tgx_WordList.txt')
        DictFreq_year = load_dictfreq_kbs_wordlist(filename, SortFlag)
        for dic in DictFreq_year:
            if(dic in DictFreq):
                DictFreq[dic] += DictFreq_year[dic]
            else:
                DictFreq[dic] = DictFreq_year[dic]

    #
    TokenTitle = '{주제어}' 
    print('@@@ [KBS 9시 뉴스] @@@')
    print('@@@ @@@ [토큰처리] - ', TokenTitle)
    print('files:', *FileList, sep='\n')

    if SortFlag == True: # sort by a->z
        dict_by_keys = sorted(DictFreq.items(), key=lambda item: item[0]) # by key: a->z
        #=DictFreq_AZ = {dic[0]:dic[1] for dic in dict_by_keys}
        DictFreq_AZ = dict(dict_by_keys)
        #print(*DictFreq_AZ, sep='\n')
        return DictFreq_AZ
    else:
        return DictFreq

def load_dictfreq_us_president(SortFlag=True):
    from hgdict import MakeDictFreq__EngTextList
    #
    us_president = load_textlist_us_president()
    Vocabulary = MakeDictFreq__EngTextList(us_president)

    if SortFlag == True: # sort by a->z
        dict_by_keys=sorted(Vocabulary.items(),key=lambda item:item[0]) # by key:a->z
        #=Vocabulary_AZ = {dic[0]:dic[1] for dic in dict_by_keys} 
        Vocabulary_AZ = dict(dict_by_keys)
        #print(*Vocabulary_AZ, sep='\n')
        return Vocabulary_AZ
    else:
        return Vocabulary

def load_Alice_Adventures():
    #-----
    # 이상한 나라의 앨리스
    #-----
    from hgcrawl import get_filename__Alice_Adventures
    filename1 = get_filename__Alice_Adventures() # {이상한 나라의 앨리스}의 파일 경로
    
    #-----
    # 해당 파일이 있는지 검사하여 없으면 다운로드한다.
    #-----
    from pathlib import Path
    file_check = Path(filename1)
    if ((file_check.is_file() == True) and (file_check.exists() == True)):
            pass
    else:
        from hgcrawl import download_gutenberg_Anne_of_Green_Gables
        download_gutenberg_Anne_of_Green_Gables()

    #-----
    #-----
    from hgwordfile import ReadTxtFile
    ReadTxt = ReadTxtFile(filename1, encoding='utf-8', DeleteComment=False)
    return ReadTxt

def load_Anne_of_Green_Gables():
    #-----
    # 빨강 머리 앤
    #-----
    from hgcrawl import get_filename__Anne_of_Green_Gables
    filename1 = get_filename__Anne_of_Green_Gables() # {빨강 머리 앤}의 파일 경로
    
    #-----
    # 해당 파일이 있는지 검사하여 없으면 다운로드한다.
    #-----
    from pathlib import Path
    file_check = Path(filename1)
    if ((file_check.is_file() == True) and (file_check.exists() == True)):
            pass
    else:
        from hgcrawl import download_gutenberg_Anne_of_Green_Gables
        download_gutenberg_Anne_of_Green_Gables()

    #-----
    #-----
    from hgwordfile import ReadTxtFile
    ReadTxt = ReadTxtFile(filename1, encoding='utf-8', DeleteComment=False)
    return ReadTxt

def load_dictfreq_Anne_of_Green_Gables(SortFlag=True):
    # 빨강 머리 앤
    from hgcrawl import get_filename__Anne_of_Green_Gables
    filename1 = get_filename__Anne_of_Green_Gables() # {빨강 머리 앤}의 파일 경로
    
    # 해당 파일이 있는지 검사하여 없으면 다운로드한다.
    from pathlib import Path
    file_check = Path(filename1)
    if ((file_check.is_file() == True) and (file_check.exists() == True)):
            pass
    else:
        from hgcrawl import download_gutenberg_Anne_of_Green_Gables
        download_gutenberg_Anne_of_Green_Gables()

    #    
    from hgdict import load_dictfreq_eng_textfile
    encoding = 'utf-8' 
    DictFreq = load_dictfreq_eng_textfile(filename1, encoding, SortFlag, toLower=True)
    return DictFreq

def load_dictfreq_Alice_Adventures(SortFlag=True):
    # 이상한 나라의 앨리스
    from hgcrawl import get_filename__Alice_Adventures
    filename1 = get_filename__Alice_Adventures() # 이상한 나라의 앨리스

    # 해당 파일이 있는지 검사하여 없으면 다운로드한다.
    from pathlib import Path
    file_check = Path(filename1)
    if ((file_check.is_file() == True) and (file_check.exists() == True)):
            pass
    else:
        from hgcrawl import download_gutenberg_Alice_Adventures
        download_gutenberg_Alice_Adventures()

    #    
    from hgdict import load_dictfreq_eng_textfile
    encoding = 'utf-8' 
    DictFreq = load_dictfreq_eng_textfile(filename1, encoding, SortFlag, toLower=True)
    return DictFreq

def load_textlist_kbs_each_2001_2016(DebugPrint=False): # [KBS 9시 뉴스: 15년치(2001~2015)]
    # 개별 뉴스 파일을 읽은다. 1일 평균 35개 * 365일 * 15년
    # [2016] 개별 뉴스는 'utf-8' 인코딩이라서 제외하고 [2015]년까지만 읽는다.
    from pathlib import Path

    #encoding='utf-8' 
    #encoding='euc-kr' # 표준완성형이라서 범위를 벗어난 통합완성형 코드가 있으면 오류 발생하여 읽지 못한다.
    encoding='cp949'

    #
    PathList = [ # 2001년 ~ 2016년
        './../../../../../hgproj80/textdata/kbs9news/worker/-txt_each_all/2001/*.txt',
        './../../../../../hgproj80/textdata/kbs9news/worker/-txt_each_all/2002/*.txt',
        './../../../../../hgproj80/textdata/kbs9news/worker/-txt_each_all/2003/*.txt',
        './../../../../../hgproj80/textdata/kbs9news/worker/-txt_each_all/2004/*.txt',
        './../../../../../hgproj80/textdata/kbs9news/worker/-txt_each_all/2005/*.txt',
        './../../../../../hgproj80/textdata/kbs9news/worker/-txt_each_all/2006/*.txt',
        './../../../../../hgproj80/textdata/kbs9news/worker/-txt_each_all/2007/*.txt',
        './../../../../../hgproj80/textdata/kbs9news/worker/-txt_each_all/2008/*.txt',
        './../../../../../hgproj80/textdata/kbs9news/worker/-txt_each_all/2009/*.txt',
        './../../../../../hgproj80/textdata/kbs9news/worker/-txt_each_all/2010/*.txt',
        './../../../../../hgproj80/textdata/kbs9news/worker/-txt_each_all/2011/*.txt',
        './../../../../../hgproj80/textdata/kbs9news/worker/-txt_each_all/2012/*.txt',
        './../../../../../hgproj80/textdata/kbs9news/worker/-txt_each_all/2013/*.txt',
        './../../../../../hgproj80/textdata/kbs9news/worker/-txt_each_all/2014/*.txt',
        './../../../../../hgproj80/textdata/kbs9news/worker/-txt_each_all/2015/*.txt',
        './../../../../../hgproj80/textdata/kbs9news/worker/-txt_each_all/2016_utf8_txt/201601/*.txt',
        './../../../../../hgproj80/textdata/kbs9news/worker/-txt_each_all/2016_utf8_txt/201602/*.txt',
        './../../../../../hgproj80/textdata/kbs9news/worker/-txt_each_all/2016_utf8_txt/201603/*.txt',
        './../../../../../hgproj80/textdata/kbs9news/worker/-txt_each_all/2016_utf8_txt/201604/*.txt',
        './../../../../../hgproj80/textdata/kbs9news/worker/-txt_each_all/2016_utf8_txt/201605/*.txt',
        './../../../../../hgproj80/textdata/kbs9news/worker/-txt_each_all/2016_utf8_txt/201606/*.txt',
        './../../../../../hgproj80/textdata/kbs9news/worker/-txt_each_all/2016_utf8_txt/201607/*.txt',
        './../../../../../hgproj80/textdata/kbs9news/worker/-txt_each_all/2016_utf8_txt/201608/*.txt',
        './../../../../../hgproj80/textdata/kbs9news/worker/-txt_each_all/2016_utf8_txt/201609/*.txt',
        './../../../../../hgproj80/textdata/kbs9news/worker/-txt_each_all/2016_utf8_txt/201610/*.txt',
        './../../../../../hgproj80/textdata/kbs9news/worker/-txt_each_all/2016_utf8_txt/201611/*.txt',
        './../../../../../hgproj80/textdata/kbs9news/worker/-txt_each_all/2016_utf8_txt/201612/*.txt',
    ]
    #    
    textlist_kbs_each = []
    for inx, pathname in enumerate(PathList):
        #=pathname = './../../../../../hgproj80/textdata/kbs9news/worker/-txt_each_all/2001/*.txt'
        textlist = load_textlist__txtpath(pathname, encoding)
        textlist_kbs_each.extend(textlist)
        if(DebugPrint == True):
            print(f'@@@ [{inx+1}]textlist_kbs_each {len(textlist_kbs_each)} :', pathname)
    return textlist_kbs_each

def load_textlist_gutenberg(pathname = None):
    #-----------
    # gutenberg porject: ??개 파일
    # https://www.gutenberg.org/
    #-----------
    encoding='utf-8' 
    #encoding='euc-kr'#표준완성형 범위를 벗어난 통합완성형 코드는 오류 때문에 못 읽는다
    #=encoding='cp949'
    if(pathname is not None):
        pathname_r = pathname
        if((pathname.endswith('\\') == False) and (pathname.endswith('/') == False)):
            pathname_r += "/" # 맨 끝에 폴더 구분 문자 추가
    else: 
        pathname_r = './../ext-src/data/gutenberg/text/'
    pathname_r += '*.txt'
    bookself_gutenberg = ReadBookSelf__TxtPath(pathname_r, is_state=True, encoding=encoding)

    textlist = [book.text for book in bookself_gutenberg]
    #
    #=print('@@@ [gutenberg] 텍스트', len(textlist), 'files(',
    #=        len(textlist),') @@@')
    #=print('files:', len(textlist))

    return textlist

def load_dictfreq_gutenberg(SortFlag=True, pathname = None, 
    Stoplist=None,
    Vocabulary=None,
    LowerCase=True,  # 대문자는 소문자로 변환
    CliticsModify=True, # {~'s}, {~'t}, {~'d}는 {~}로 바꾼다.
    ExcChar1=True,  # 1글자보다 작은 것은 지운다.
    ExcNumber=True, # 숫자만 있는 것은 지운다.
    UnifySpellRule=False,
    PrintProcState=False, 
    ):
    '''
    Stoplist:  목록에 있는 단어 제외(stopword)
    Vocabulary: 어휘집(Vocabulary:단어 목록)에 있는 단어만 처리
    CliticsModify: 접어(Clitics) 분리 # {~'s}, {~'t}, {~'d}는 {~}로 바꾼다.
    ExcChar1:   1글자 단어는 제외(영어는 이래되 되지만 한글을 이렇게 하면 안 된다.)
    ExcNumber:  숫자는 제외
    UnifySpellRule: # 철자 규칙으로 단일화(s 제거, es 변형, 's)
    PrintProcState: 진행 상태 출력(텍스트 목록이 많을 경우 오래 걸릴 때 출력 필요)
    '''
    #=from hgdict import MakeDictFreq__EngTextList
    from hgdict import GetDictFreq__TextList
    #
    textlist = load_textlist_gutenberg(pathname)

    #=DictFreq = MakeDictFreq__EngTextList(textlist)
    DictFreq = GetDictFreq__TextList(textlist, 
        ExcFilter=Stoplist, # 불용어 처리
        Vocabulary=Vocabulary, # 어휘집(Vocabulary:단어 목록)에 있는 단어만 처리
        LowerCase=LowerCase,  # 대문자는 소문자로 변환
        CliticsModify=CliticsModify, # {~'s}, {~'t}, {~'d}는 {~}로 바꾼다.
        ExcChar1=ExcChar1,  # 1글자보다 작은 것은 지운다.
        ExcNumber=ExcNumber, # 숫자만 있는 것은 지운다.
        UnifySpellRule=UnifySpellRule, # 철자 규칙으로 단일화(s 제거, es 변형, 's)
        PrintProcState=PrintProcState, # 진행 상태 출력(텍스트 목록이 많을 경우 오래 걸릴 때 출력 필요)
    )
    #
    if SortFlag == True: # sort by a->z
        dict_by_keys=sorted(DictFreq.items(),key=lambda item:item[0]) # by key:a->z
        #=DictFreq_AZ = {dic[0]:dic[1] for dic in dict_by_keys} 
        DictFreq_AZ = dict(dict_by_keys)
        #print(*DictFreq_AZ, sep='\n')
        return DictFreq_AZ
    else:
        return DictFreq

def load_dictfreq_gutenberg_wordlist(Stopword=True):
    from hgwordfile import GetDictFreq_WordFreqFile2
    #-----------------------
    # gutenberg porject
    guten_pathname = './../ext-src/data/gutenberg/'
    fileame = 'gutenberg' + '_wordfreq' + '.tpx'
    read_file = guten_pathname + fileame

    print('dictionary reading:', read_file)
    DictFreq = GetDictFreq_WordFreqFile2(read_file, encoding='utf-8')
    #=print(f'DictFreq [{len(DictFreq)}]:')
    print()

    #-----------
    # 불용어 처리
    #-----------
    if(Stopword == True):
        from hgdict_low import TransDictfreq__Stoplist
        # 불용어 파일 읽기
        fileame = 'gutenberg_wordfreq_quatation' + '.txt'
        stop_file = guten_pathname + fileame
        stopword_txt = ReadTxtFile(stop_file)
        stoplist_gutenberg = stopword_txt.split()

        # 불용어 제거
        #=print('DictFreq:', len(DictFreq))
        DelNum = TransDictfreq__Stoplist(DictFreq, stoplist_gutenberg)
        #=print('DictFreq_New:', len(DictFreq))
        #=print('stop num:', DelNum)
    #        
    return DictFreq

#=if __name__ == '__main__':
#=    main()
