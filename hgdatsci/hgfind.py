#------------------------
#------------------------
import re
from unittest import TestCase, main

from hgworddistance import (
    AddNGramVocabulary__DictFreq, 
    MakeStringNGram, WeightNGramVocabulary,
)

from hgkbd import (
    HGTransString2EngString, HGTransString2KBDJamo,
    HGTransHalfJamo2KBDJamo, HGTransChoJungJongJamo2KBDJamo,
)

import hgsysinc
from hgunicode import hgGetChoJungJongString

#-----
#-----
# '\n' 문자는 줄바뀜을 막기 위해 출력 가능한 문자로 바꾼다.
__replace_lf__display_char0__ = ' ' # space
__replace_lf__display_char1__ = '¶' # 00B6
__replace_lf__display_char2__ = '⌫' #232B  ERASE TO THE LEFT
__replace_lf__display_char3__ = '⎆' # 2386  ENTER SYMBOL
#=__replace_lf__display_char__ = __replace_lf__display_char2__ # 유니코드를 쓰면 도스창에서 리다이렉션 에러 발생
__replace_lf__display_char__ = __replace_lf__display_char0__ # 도스창에서 리다이렉션 에러 방지

class HGFind():
    def __init__(self):
        self.__init__ = True

def FileScanLine(find, filename, encoding = 'cp949'):
    from pathlib import Path
    real_filename = Path(filename)
    file = open(real_filename, 'r', encoding=encoding)
    lines = file.readlines()
    file.close()

    find_pos = 0
    for txt in lines:
        find_inx = txt.find(find) 
        if(find_inx >= 0): # 처음으로 발견, 위치를 출력하고 종료
            find_pos += find_inx
            #=findlen = len(find)
            #=print('find:', find_pos, txt[find_inx: find_inx + findlen])
            #=print('===>', filename)
            return find_pos
        find_pos += len(txt)
    #
    return (-1)

def FileScan(find, filename, encoding = 'cp949'):
    from pathlib import Path
    real_filename = Path(filename)
    file = open(real_filename, 'r', encoding=encoding)
    try:
        texts = file.read()
    except UnicodeDecodeError:
    # UnicodeDecodeError:  # 'cp949' codec can't decode byte 0x80 in position 2: illegal multibyte sequence
    # UnicodeDecodeError:  # 'utf-8' codec can't decode byte 0xb0 in position 0: invalid start byte
        file.close()
        if(encoding == 'cp949'):
            file = open(real_filename, 'r', encoding='utf8')
        else: 
            file = open(real_filename, 'r', encoding='cp949')
        texts = file.read()
    file.close()

    find_pos = texts.find(find) 
    #=if(find_pos >= 0): # 처음으로 발견, 위치를 출력하고 종료
    #=    print('find:', find_pos)
    #=    print('===>', filename)
    return find_pos

def FilesScan(find, pathname, encoding = 'cp949'):
    import glob
    filenum = 0
    for filename in glob.glob(pathname):
        filenum += 1
        #=print(f'{filenum}:', filename)
        find_inx = FileScan(find, filename, encoding = encoding)
        if(find_inx >= 0): # 처음으로 발견, 위치를 출력하고 종료
            return filename, find_inx
    #
    return (-1)

def HGFileScanPos(Find, filename, encoding = 'cp949', LowerCasifyFlag=False):
    from pathlib import Path
    from hgwordfile import ReadTxtFile

    filetext = ReadTxtFile(filename, encoding=encoding)
    if(LowerCasifyFlag == True):
        filetext = filetext.lower() # 대문자롤 소문자로 통합하기 위해서 소문자 변환

    resultFind = HGTextScanPos(Find, filetext)
    return resultFind

def HGTextScanPos(Find, Text):
    """텍스트에 검색어 위치 반환: format: [find_pos, ...]"""
    #-----
    FindNum = 0
    findlen = len(Find)

    begin_pos = 0
    resultDoc = []
    while(True):
        find_pos = Text.find(Find, begin_pos) 
        if(find_pos >= 0):
            #=print(Text[find_pos: find_pos + findlen], ':', find_pos)
            # format: [find_pos, ...]
            resultDoc.append(find_pos)
            FindNum += 1
            begin_pos = (find_pos + findlen)
        else:
            break
    return resultDoc

def HGTextScanPos_Wordlist(Wordlist, Text, debugPrint=False):
    """텍스트에 검색어들의 위치 반환: format: [find_pos, ...]"""
    #-----
    ScanPos_Wordlist = list()
    for Word in Wordlist:
        ScanPos = HGTextScanPos(Word, Text)
        if(debugPrint == True):
            print(f'[{Word}] ScanPos {len(ScanPos)}:')
            #=print(*ScanPos, sep = '\n')
            print(ScanPos)
            print()
        #
        ScanPos_Wordlist.append({'word':Word, 'pos_list':ScanPos})
    #
    if(debugPrint == True):
        print(f'ScanPos_Wordlist {len(ScanPos_Wordlist)}:')
        print(ScanPos_Wordlist)
        print()
    #    
    return ScanPos_Wordlist

def HGTextScan(Find, Text): 
    """
    텍스트에 검색어가 몇 회 등장하는가
    """
    findlen = len(Find)
    FindNum = 0
    begin_pos = 0
    while(True):
        find_pos = Text.find(Find, begin_pos) 
        if(find_pos >= 0):
            #=print(Text[find_pos: find_pos + findlen], ':', find_pos)
            FindNum += 1
            begin_pos = (find_pos + findlen)
        else:
            break
    return FindNum

def HGScanPos(Find, TextList):
    results = []
    for doc_i, text in enumerate(TextList):
        resultDoc = HGTextScanPos(Find, text)
        if(len(resultDoc) > 0):
            results.append({'doc':doc_i, 'pos':resultDoc})
    return results

def HGScan(Find, TextList):
    results = []
    for doc_i, text in enumerate(TextList):
        FindNum = HGTextScan(Find, text)
        if(FindNum > 0):
            results.append({doc_i:FindNum}) # format: {docid:freq}
    return results

def HGDictFinder(Find, BaseDictFreq):
    if(Find in BaseDictFreq):
        # foramt: {'word': {13: 1, 27: 1, 30: 1, 47: 1}}
        DocList = BaseDictFreq[Find]
        #-----
        #=print(DocList)
        #-----
        #=TotalFreq = sum([DocList[doc_f] for doc_f in DocList])
        #=print(f'{Find} : {len(DocList)} 문서, {TotalFreq}회')
        #=for i, docid in enumerate(DocList):
        #=    print(f'{i+1}: ({docid}, {DocList[docid]})  (문서번호, 빈도)')
        #-----
        # foramt: {13: 1, 27: 1, 30: 1, 47: 1}
        return DocList
    else:
        return None

def PrintVocabulary(Vocabulary, PrintNum=0, LeadingString='', PrintGuide=False):
    if(PrintGuide == True):
        print('\n---By abc Order ---')

    #-----    
    # Vocabulary 항목이 list 일 때
    #-----    
    dict_by_keys = sorted(Vocabulary.items(), key=lambda item: item[0]) # by key: a->z
    for i, dic in enumerate(dict_by_keys):
        print(LeadingString, end='')
        print(f'{i}, {dic[0]}: {dic[1]}') # format: [('that', 13),...]
        if(PrintNum > 0):
            if(i >= PrintNum):
                break
    if(PrintNum > 0): 
        # 맨 끝에서 일부 출력
        print('...')
        print('...')

        for i, dic in enumerate(dict_by_keys):
            if(i > len(dict_by_keys) - PrintNum):
                print(f'{i}, {dic[0]}: {dic[1]}') # format: [('that', 13),...]

def PrintDictFind(Find, BaseDictFreq):
    results = HGDictFinder(Find, BaseDictFreq)
    if(results != None):
        # foramt: {13: 1, 27: 1, 30: 1, 47: 1}
        #=print(results)
        DocNum = len(results)
        TotalFreq = sum([results[doc_f] for doc_f in results])
        print(f'{Find} : {DocNum} 문서, {TotalFreq}회')
        print('순서: (문서번호, 빈도)')
        for i, docid in enumerate(results):
            print(f'{i+1}: ({docid}, {results[docid]})')
    else:
        print('Not Found:', Find)
    print()

def CatchPreText(Text, KwdPos, PreTextLen = 5, 
    WordBreak=False,  # {WordBreak:True} 공백문자 단위로 처리, 아니면 글자 단위 처리
):
    TextLen = len(Text)
    Cnt = 0
    AlignPos = KwdPos
    AlignPos -= 1
    while(AlignPos >= 0):
        #print('[', Cnt, ']', AlignPos) # debug
        WorkPos = AlignPos
        WorkLen = 1
        # print(Text[AlignPos: AlignPos+10]) # debug

        Cnt += 1
        AlignPos = WorkPos
        if(Cnt >= PreTextLen):
            break
        if(WorkLen == 1):
            if(Text[WorkPos] == '\n'): # 줄바꿈이면 그만한다
                break
        # count
        AlignPos -= 1

    #print('AlignPos:', AlignPos) # debug
    if(AlignPos < 0):
        AlignPos = 0

    #-----------
    #-----------
    if(WordBreak == True): # (WordBreak == True) 공백문자 단위로 처리
        WorkPos = AlignPos
        while(WorkPos < KwdPos):
            #print('[', Cnt, ']', WorkPos) # debug
            # print(Text[WorkPos: WorkPos+10]) # debug
            CurChar = Text[WorkPos]
            if(CurChar == '\n'): # 줄바꿈이면 그만한다
                break
            elif(CurChar == ' '): # 공백문자이면 그만한다
                break
            elif(CurChar == '\t'): # 탭문자이면 그만한다
                break

            # count
            WorkPos += 1 # 계산 주의
            Cnt -= 1
        #
        if(AlignPos != WorkPos): # 선행 위치가 달라졌으면 바꾼다.
            AlignPos = WorkPos # 바로 위에서 검사하지 않고 곧 바로 바꿔도 되지만 디버깅을 위해서

    #-----------
    # 맨 앞에서 선행길이가 모자라면 채운다.
    FillChar = ' '
    AlignPreWord = ''
    while(Cnt < PreTextLen): 
        AlignPreWord += FillChar
        Cnt += 1

    #print('[AlignPos : KwdPos]', AlignPos, ':',  KwdPos) # debug
    PreWord = Text[AlignPos: KwdPos]
    AlignPreWord += PreWord

    #-----------
    # '\n' 문자는 줄바뀜을 막기 위해 출력 가능한 문자로 바꾼다.
    AlignPreWord = AlignPreWord.replace('\n', __replace_lf__display_char__)

    #-----------
    #print(len(PreWord), ':', PreWord) # debug
    #print(len(AlignPreWord), ':', AlignPreWord) # debug

    #print(PreWord)
    #print(AlignPreWord)

    return AlignPreWord

def CatchPostText(Text, KwdPos, PostTextLen = 5, 
    WordBreak=False, # {WordBreak:True} 공백문자 단위로 처리, 아니면 글자 단위 처리
):
    TextLen = len(Text)
    Cnt = 0
    AlignPos = KwdPos

    #-------------------------
    # 지정 위치 다음 음절로 이동
    #-------------------------
    #print('[', Cnt, ']', AlignPos) # debug
    WorkPos = AlignPos
    WorkLen = 1
    Post_AlignPos_Start = (WorkPos + WorkLen)
    AlignPos = Post_AlignPos_Start

    #------------------
    # 후행음절 찾기 시작
    #------------------
    while(AlignPos < TextLen):
        #print('[', Cnt, ']', AlignPos) # debug
        WorkPos = AlignPos
        WorkLen = 1
        AlignPos = (WorkPos + WorkLen)
        Cnt += 1
        if(Cnt >= PostTextLen):
            break
        if(WorkLen == 1):
            if(Text[WorkPos] == '\n'): # 줄바꿈이면 그만한다
                break

    #print('Cnt :', Cnt)
    #print('AlignPos:', AlignPos) # debug
    if(AlignPos > TextLen):
        AlignPos = TextLen

    #-----------
    #-----------
    if(WordBreak == True): # (WordBreak == True) 공백문자 단위로 처리
        WorkPos = AlignPos
        while(WorkPos > KwdPos):
            #print('[', Cnt, ']', WorkPos) # debug
            # print(Text[WorkPos: WorkPos+10]) # debug
            CurChar = Text[WorkPos]
            if(CurChar == '\n'): # 줄바꿈이면 그만한다
                break
            elif(CurChar == ' '): # 공백문자이면 그만한다
                break
            elif(CurChar == '\t'): # 탭문자이면 그만한다
                break

            # count
            WorkPos -= 1 # 계산 주의
            Cnt -= 1
        #
        if(AlignPos != WorkPos): # 선행 위치가 달라졌으면 바꾼다.
            AlignPos = WorkPos # 바로 위에서 검사하지 않고 곧 바로 바꿔도 되지만 디버깅을 위해서

    #-----------
    # 맨 끝에서 후행길이가 모자라면 채운다.
    FillChar = ' '
    Align_PostWord = ''
    while(Cnt < PostTextLen): 
        Align_PostWord += FillChar
        Cnt += 1

    #print('[Post_AlignPos_Start:AlignPos]', Post_AlignPos_Start, ':', AlignPos) # debug
    PostWord = Text[Post_AlignPos_Start: AlignPos]
    Align_PostWord = PostWord + Align_PostWord

    #-----------
    # '\n' 문자는 줄바뀜을 막기 위해 출력 가능한 문자로 바꾼다.
    Align_PostWord = Align_PostWord.replace('\n', __replace_lf__display_char__)

    #-----------
    #print(len(PostWord), ':', PostWord) # debug
    #print(len(Align_PostWord), ':', Align_PostWord) # debug

    #print(PostWord) # debug
    #print(Align_PostWord) # debug

    return Align_PostWord

def CatchCenterText__Pos(Text, KwdPos, 
    KeyLen=1,
    PreTextLen=15, PostTextLen=15, 
    SepChar='', 
    WordBreak=False, # {WordBreak:True} 공백문자 단위로 처리, 아니면 글자 단위 처리
    HtmlMode=False, # 결과를 웹페이지(html) 방식으로 처리
):
    # 초기화
    PreWord = '';    FindWord = '';    PostWord = ''
    
    #----- PreWord
    PreWord = CatchPreText(Text, KwdPos, PreTextLen = PreTextLen, WordBreak=WordBreak)
    #print(PreWord)
    
    #----- PostWord
    PostWord = CatchPostText(Text, KwdPos, PostTextLen = PostTextLen, WordBreak=WordBreak)
    #print(PostWord)

    #----- 찾는 음절
    #print('[', 찾은회수, ']', KwdPos) # debug
    WorkPos = KwdPos
    #=WorkLen = 1
    WorkLen = KeyLen
    FindWord = Text[WorkPos: (WorkPos + WorkLen)]
    PostWord_Modify = PostWord[(KeyLen - 1):]
    
    #----- KWIC(Key Word In Context) 생성
    AlignString = ''
    if(HtmlMode == True): # 결과를 웹페이지(html) 방식으로 처리    
        #=AlignString += "<table>"
        #=AlignString += "<tr"
        AlignString += "<td align=right>"

        AlignString += PreWord

        AlignString += "</td>"
        AlignString += "<td align=left>"
    else:
        AlignString += PreWord

    if(len(SepChar) > 0):
        AlignString += SepChar

    #
    if(HtmlMode == True): # 결과를 웹페이지(html) 방식으로 처리    
        AlignString += "<font color=blue>"
        AlignString += "<b>"

        AlignString += FindWord

        AlignString += "</b>"
        AlignString += "</font>"

        AlignString += "</td>"
        AlignString += "<td align=left>"
    else:
        AlignString += FindWord

    #
    if(len(SepChar) > 0):
        AlignString += SepChar

    #
    if(HtmlMode == True): # 결과를 웹페이지(html) 방식으로 처리    
        AlignString += PostWord_Modify

        AlignString += "</td>"
        #=AlignString += "</tr"
        #=AlignString += "</table>"
    else:
        AlignString += PostWord_Modify

    #=print(AlignString)
    #
    return AlignString

def CatchCenterText__String(Find, String, 
    LowerCasifyFlag=False, # 대문자롤 소문자로 통합할 것인가
    PreTextLen=15, PostTextLen=15, 
    SepChar='', 
    WordBreak=False, # {WordBreak:True} 공백문자 단위로 처리, 아니면 글자 단위 처리
    CaptionAdd=False, # 헤더 추가
    IndexAdd=False, # 인덱스 추가
    PrintMode=False, # 직접 출력(반환값 없음)
    HtmlMode=False, # 결과를 웹페이지(html) 방식으로 처리
): 
    #---------
    # {WordBreak=False} # 글자 단위로 처리
    # {WordBreak=True} # 공백문자 단위로 처리
    #---------
    #===================
    #===================
    if(LowerCasifyFlag == True):
        String = String.lower() # 대문자롤 소문자로 통합하기 위해서 소문자 변환

    #===================
    #===================
    #=Find = 'goodness'

    #=ResultPosList = HGFileScanPos(Find, filename, encoding=encoding, LowerCasifyFlag=LowerCasifyFlag) 
    ResultPosList = HGTextScanPos(Find, String)
    FindNum = len(ResultPosList)

    #=if(PrintMode == True):
    #=    print('Find Num:', FindNum)
    #=    #=print(*ResultPosList, sep = '\n')

    #===================
    #===================
    #=PreTextLen = 40  # 앞쪽 여백
    #=PostTextLen = 40 # 뒤쪽 여백
    FindLen = len(Find)
    PostTextLen_Work = (PostTextLen + FindLen) # 뒤쪽 여백 조절

    #
    CenterText_Result = ''
    if(HtmlMode == True) : # 결과를 웹페이지(html) 방식으로 처리    
        table_line = "<table>"
        if(PrintMode == True):
            print(table_line)
        else:
            CenterText_Result += table_line
    else:
        if(CaptionAdd == True):
            CenterFind = Find.center((PreTextLen + PostTextLen) + FindLen, '*') 
            if(PrintMode == True):
                print(CenterFind)
            else:
                CenterText_Result += CenterFind
                CenterText_Result += '\n'
    #
    for i, KwdPos in enumerate(ResultPosList):
        CenterText = CatchCenterText__Pos(String, KwdPos=KwdPos, KeyLen=FindLen, 
            PreTextLen=PreTextLen, PostTextLen=PostTextLen_Work, 
            SepChar=SepChar, WordBreak=WordBreak, HtmlMode=HtmlMode)

        IndexString = ''    
        if(IndexAdd == True):
            IndexString = str(i+1)
            IndexString += '\t'

        if(HtmlMode == True) : # 결과를 웹페이지(html) 방식으로 처리    
            #
            tr_line = "<tr>"

            #
            tr_line += "<td>"
            tr_line += IndexString
            if(len(IndexString) > 0): # 인덱스를 포함한 경우
                tr_line += "</td>"
                #
                tr_line += "<td>"
            #
            tr_line += CenterText
            tr_line += "</td>"
            
            #
            tr_line += "</tr>"
            tr_line += "\n"  # 텍스트로 볼 때 문단 구분을 위해서 추가

            #
            if(PrintMode == True):
                print(tr_line)
            else:
                CenterText_Result += tr_line
        else:
            if(PrintMode == True):
                print(f'{IndexString}', end='')
                print(CenterText)
            else:
                CenterText_Result += IndexString
                CenterText_Result += CenterText
                CenterText_Result += '\n'

    #
    if(HtmlMode == True) : # 결과를 웹페이지(html) 방식으로 처리    
        if(PrintMode == True):
            print("</table>")
        else:
            CenterText_Result += "</table>"
    else:
        if(PrintMode == True):
            print(),print(),print(),
    #
    return CenterText_Result, FindNum

def CatchCenterText__String_Wordlist(Wordlist, String, 
    LowerCasifyFlag=False, # 대문자롤 소문자로 통합할 것인가
    PreTextLen=15, PostTextLen=15, 
    SepChar='', 
    WordBreak=False, # {WordBreak:True} 공백문자 단위로 처리, 아니면 글자 단위 처리
    CaptionAdd=False, # 헤더 추가
    IndexAdd=False, # 인덱스 추가
    PrintMode=False, # 직접 출력(반환값 없음)
    HtmlMode=False, # 결과를 웹페이지(html) 방식으로 처리
): 
    #---------
    # {WordBreak=False} # 글자 단위로 처리
    # {WordBreak=True} # 공백문자 단위로 처리
    #---------
    #===================
    #===================
    if(LowerCasifyFlag == True):
        String = String.lower() # 대문자롤 소문자로 통합하기 위해서 소문자 변환

    #-----
    # caption
    #-----
    CenterText_Result = ''
    if(HtmlMode == True) : # 결과를 웹페이지(html) 방식으로 처리    
        table_line = "<table>"
        if(PrintMode == True):
            print(table_line)
        else:
            CenterText_Result += table_line
    else:
        if(CaptionAdd == True):
            #-----
            # 여러 단어(Wordlist)로 처리할 때는 텍스트 방식의 캡쳐 처리가 어려워서 막는다.
            #-----
            #=CenterFind = Find.center((PreTextLen + PostTextLen) + FindLen, '*') 
            #=if(PrintMode == True):
            #=    print(CenterFind)
            #=else:
            #=    CenterText_Result += CenterFind
            #=    CenterText_Result += '\n'
            #-----
            pass

    #-----
    #-----
    FindNum_Total = 0
    TotalInx = 0
    for word_inx, Find in enumerate(Wordlist):
        #===================
        #===================
        #=Find = 'goodness'

        #=ResultPosList = HGFileScanPos(Find, filename, encoding=encoding, LowerCasifyFlag=LowerCasifyFlag) 
        ResultPosList = HGTextScanPos(Find, String)
        FindNum = len(ResultPosList)
        FindNum_Total += FindNum

        #=if(PrintMode == True):
        #=    print('Find Num:', FindNum)
        #=    #=print(*ResultPosList, sep = '\n')

        #===================
        #===================
        #=PreTextLen = 40  # 앞쪽 여백
        #=PostTextLen = 40 # 뒤쪽 여백
        FindLen = len(Find)
        PostTextLen_Work = (PostTextLen + FindLen) # 뒤쪽 여백 조절

        #
        for pos_inx, KwdPos in enumerate(ResultPosList):
            CenterText = CatchCenterText__Pos(String, KwdPos=KwdPos, KeyLen=FindLen, 
                PreTextLen=PreTextLen, PostTextLen=PostTextLen_Work, 
                SepChar=SepChar, WordBreak=WordBreak, HtmlMode=HtmlMode)

            IndexString = ''    
            if(IndexAdd == True):
                IndexString = str(TotalInx+1)
                IndexString += '\t'

            if(HtmlMode == True) : # 결과를 웹페이지(html) 방식으로 처리    
                #
                tr_line = "<tr>"

                #
                tr_line += "<td>"
                tr_line += IndexString
                if(len(IndexString) > 0): # 인덱스를 포함한 경우
                    tr_line += "</td>"
                    #
                    tr_line += "<td>"
                #
                tr_line += CenterText
                tr_line += "</td>"
                
                #
                tr_line += "</tr>"
                tr_line += "\n"  # 텍스트로 볼 때 문단 구분을 위해서 추가

                #
                if(PrintMode == True):
                    print(tr_line)
                else:
                    CenterText_Result += tr_line
            else:
                if(PrintMode == True):
                    print(f'{IndexString}', end='')
                    print(CenterText)
                else:
                    CenterText_Result += IndexString
                    CenterText_Result += CenterText
                    CenterText_Result += '\n'
            # next
            TotalInx += 1

    #
    if(HtmlMode == True) : # 결과를 웹페이지(html) 방식으로 처리    
        if(PrintMode == True):
            print("</table>")
        else:
            CenterText_Result += "</table>"
    else:
        if(PrintMode == True):
            print(),print(),print(),
    #
    return CenterText_Result, FindNum_Total

def CatchCenterText__File(Find, filename, encoding='cp949', 
    LowerCasifyFlag=False, # 대문자롤 소문자로 통합할 것인가
    PreTextLen=15, PostTextLen=15, 
    SepChar='', 
    WordBreak=False, # {WordBreak:True} 공백문자 단위로 처리, 아니면 글자 단위 처리
    CaptionAdd=False, # 헤더 추가
    IndexAdd=False, # 인덱스 추가
    PrintMode=False, # 직접 출력(반환값 없음)
    HtmlMode=False, # 결과를 웹페이지(html) 방식으로 처리
): 
    #
    from hgwordfile import ReadTxtFile
    filetext = ReadTxtFile(filename, encoding=encoding)

    #    
    CenterText_Result, FindNum = CatchCenterText__String(Find, filetext, 
        LowerCasifyFlag=LowerCasifyFlag, # 대문자롤 소문자로 통합할 것인가
        PreTextLen=PreTextLen, PostTextLen=PostTextLen, 
        SepChar=SepChar, 
        WordBreak=WordBreak, # {WordBreak:True} 공백문자 단위로 처리, 아니면 글자 단위 처리
        CaptionAdd=CaptionAdd, # 헤더 추가
        IndexAdd=IndexAdd, # 인덱스 추가
        PrintMode=PrintMode, # 직접 출력(반환값 없음)
        HtmlMode=HtmlMode, # 결과를 웹페이지(html) 방식으로 처리
    )
    return CenterText_Result, FindNum

def CatchCenterText__File_Wordlist(Wordlist, filename, encoding='cp949', 
    LowerCasifyFlag=False, # 대문자롤 소문자로 통합할 것인가
    PreTextLen=15, PostTextLen=15, 
    SepChar='', 
    WordBreak=False, # {WordBreak:True} 공백문자 단위로 처리, 아니면 글자 단위 처리
    CaptionAdd=False, # 헤더 추가
    IndexAdd=False, # 인덱스 추가
    PrintMode=False, # 직접 출력(반환값 없음)
    HtmlMode=False, # 결과를 웹페이지(html) 방식으로 처리
): 
    #
    from hgwordfile import ReadTxtFile
    filetext = ReadTxtFile(filename, encoding=encoding)

    #    
    CenterText_Result, FindNum = CatchCenterText__String_Wordlist(Wordlist, filetext, 
        LowerCasifyFlag=LowerCasifyFlag, # 대문자롤 소문자로 통합할 것인가
        PreTextLen=PreTextLen, PostTextLen=PostTextLen, 
        SepChar=SepChar, 
        WordBreak=WordBreak, # {WordBreak:True} 공백문자 단위로 처리, 아니면 글자 단위 처리
        CaptionAdd=CaptionAdd, # 헤더 추가
        IndexAdd=IndexAdd, # 인덱스 추가
        PrintMode=PrintMode, # 직접 출력(반환값 없음)
        HtmlMode=HtmlMode, # 결과를 웹페이지(html) 방식으로 처리
    )
    return CenterText_Result, FindNum

#================================
#================================
#================================
def MatchPrefix_WordList_naive(PrefixStr, WordList):
    MatchList = []
    for Word in WordList:
        if Word.startswith(PrefixStr):
            MatchList.append(Word)
    return MatchList

def MatchPrefix_Dict_naive(PrefixStr, Dict):
    MatchDict = {}
    for key in Dict:
        if key.startswith(PrefixStr):
            MatchDict[key] = Dict[key]
    return MatchDict

def MatchPrefix_SortDict_naive(PrefixStr, Dict, CheckElapse=False):
    if(CheckElapse == True):
        # 경과 시간 측정을 위해서 추가
        from datetime import datetime
        time_beg = datetime.now()
    #
    findFlag = False
    MatchDict = {} # format: {word: freq}
    for key in Dict:
        if key.startswith(PrefixStr):
            MatchDict[key] = Dict[key] # format: {word: freq}
            findFlag = True
        else:
            if findFlag == True: # 정렬 상태이므로 더 이상 일치하는 것이 없는 경우
                break
    if(CheckElapse == True):
        # 경과 시간 측정을 위해서 추가
        time_end = datetime.now()
        elapsed = time_end - time_beg
        print(f'{PrefixStr}  Elapsed:', elapsed)
    #
    return MatchDict

#================================
#================================
#================================
class HGTrieNode():
    # WordList & DictFreq 둘다 지원
    def __init__(self, KeyChar='', Weight=0, ParentNode=None):
        self.Child = {}
        self.IsWord = False # .IsWord(True) 종단 노드, 단어를 형성
        #
        self.Weight = Weight
        #
        self.KeyChar = KeyChar
        # real-word (not key-char-word)
        self.RealWord = '' # {self.IsWord}값이 'True'일 때는 값을 보유한다.
        # twin-proc
        self.RealWord_Multi = '' # {self.RealWord}값이 '1'개가 아니라 '2'개일 때 사용
        self.Weight_Multi = 0
        #
        self.ParentNode = ParentNode

    def GetFullKeyName(self, OnlyParent=False):
        FullKeyName = ''
        if(OnlyParent == False): # 현재 자신의 이름을 포함
            FullKeyName = self.KeyChar
        
        CurNode = self.ParentNode
        while(CurNode):
            FullKeyName = CurNode.KeyChar + FullKeyName
            CurNode = CurNode.ParentNode
        return FullKeyName
    
    def GetChildNum(self):
        return len(self.Child)
    
    def PrintInfo(self):
        FullKeyName = self.GetFullKeyName()
        print('FullKeyName:', FullKeyName)
        print('Child:', len(self.Child))
        print('IsWord:', self.IsWord)
        print('Weight:', self.Weight)
        print('KeyChar:', self.KeyChar)
        print('RealWord:', self.RealWord)
        # twin-proc
        print('RealWord_Multi:', self.RealWord_Multi) # {self.RealWord}값이 '1'개가 아니라 '2'개일 때 사용
        print('Weight_Multi :', self.Weight_Multi )

#============================
#============================
# 한글 처리 옵션
__Hng_AsItIs__ = 1 # 한글: 변형없이 그대로 처리(음절)
__Hng_2_Jamo__ = 2 # 한글: 키보드 자모로 처리
__Hng_2_Eng__ = 3 # 한글: 영문자로 처리
__Hng_2_Jamo3__ = 4 # 한글: 초중종 자모로 처리(사전식)
#============================
#============================

class HGTrie():
    #====================================
    #=FindWord(FindWord): 단어(FindWord)와 일치하는 단어 목록 반환
    #=IsVocabulary(FindWord): 단어(FindWord)가 있는지 확인
    #=SearchWord(FindWord): 단어(FindWord)를 탐색하여 해당 노드 반환
    #====================================
    
    # 한글 변환(음절 그대로,  두벌식(키보드) 자모, 영문자, 초중종 자모)
    Opt_Hng_Fmt = __Hng_2_Jamo__ # 한글: 두벌식(키보드) 자모로 처리(default)

    #=Opt_Hng_Fmt = __Hng_AsItIs__ # 한글: 변형없이 그대로 (음절 단위) 처리
    #=Opt_Hng_Fmt = __Hng_2_Jamo__ # 한글:  두벌식(키보드) 자모로 처리(default)
    #=Opt_Hng_Fmt = __Hng_2_Eng__ # 한글: 영문자로 처리
    #=Opt_Hng_Fmt = __Hng_2_Jamo3__ = 4 # 한글: 초중종 자모로 처리(사전식)

    Opt_Hng_HalfwidthTrans = True # (default:True) 반각 자모를 (전각) 두벌식(키보드) 자모 변환: 'ﾾￂﾤﾡￓﾡ'->'ㅎㅏㄴㄱㅜㄱ'
    Opt_ChoJungJongJamoTrans = True # (default:True) 초중종 자모를 (전각) 두벌식(키보드) 자모 변환: '대한민국'(초중종 자모)->'ㄷㅐㅎㅏㄴㅁㅣㄴㄱㅜㄱ'

    # 영어 처리    
    #=Opt_LowerEngWord = False
    Opt_LowerEngWord = True # (default:True)
    Opt_FullwidthTrans = True # (default:True) # 전각 아스키 알파벳을 (기본 라틴) 아스키 알파벳으로 변환: 'ｋｏｒｅａ' -> 'korea', 'ｇｋｓｒｎｒ' -> 'gksrnr'{한국}

    #
    Opt_SuggestNum = 10 # 추천 단어수
    _SuggestNum_Max_ = 100 # 추천 단어 최댓값

    #
    #=Opt_NGramUse = False
    Opt_NGramUse = True 
    #=Opt_NGramMake = False
    Opt_NGramMake = True
    Opt_NGramValue = 5
    

    #
    def __init__(self, SuggestNum=None):
        self.Root = HGTrieNode() 
        self.SuggestResult = [] 
        self.PrintCnt = 0
        
        if(SuggestNum != None):
            self.SetSuggestNum(SuggestNum)
        #
        self.NGramVocabulary = {}
        # stopword
        self.stoplist = None

    def SetSuggestNum(self, SuggestNum):
        SuggestNum = int(SuggestNum)
        if(SuggestNum <= 0):
            assert False
        self.Opt_SuggestNum = SuggestNum
        if(self.Opt_SuggestNum > self._SuggestNum_Max_):
            self.Opt_SuggestNum = self._SuggestNum_Max_

    def SetNGramValue(self, NGramValue):
        NGramValue = int(NGramValue)
        if(NGramValue <= 0):
            assert False
        self.Opt_NGramValue = NGramValue

    def PrintOpt(self):
        print('HGTrie.CountTrie:', self.CountTrie())
        print('HGTrie.Opt_LowerEngWord:', self.Opt_LowerEngWord) # 영문자 소문자 변환
        print('HGTrie.Opt_FullwidthTrans:', self.Opt_FullwidthTrans) # 전각 아스키를 (기본 라틴) 아스키 변환
        print('HGTrie.Opt_Hng_HalfwidthTrans:', self.Opt_Hng_HalfwidthTrans) # 반각 자모를 (전각) 두벌식 자모 변환
        print('HGTrie.Opt_ChoJungJongJamoTrans:', self.Opt_ChoJungJongJamoTrans) # 초중종 자모를 (전각) 두벌식(키보드) 자모 변환
        print('HGTrie.Opt_NGramUse:', self.Opt_NGramUse) # make n-gram suggest
        print('HGTrie.Opt_Hng_Fmt:', self.Opt_Hng_Fmt)
        print('HGTrie.NGramVocabulary:', len(self.NGramVocabulary))
        print() # 함수 이후에 출력과 간격을 위해 한 줄 건너뛰도록

    def InsertNode(self, Word, RealWord='', Weight=0):
        #
        CurNode = self.Root 
        for Char in Word: 
            if not CurNode.Child.get(Char):
                CurNode.Child[Char] = HGTrieNode(KeyChar=Char, ParentNode=CurNode) 
            CurNode = CurNode.Child[Char] 
        #
        if(CurNode.RealWord != ''): # 이미 노드가 있는 경우
            # 대소문자를 무시하여 비교
            if(CurNode.RealWord.lower() == RealWord.lower()): # 소문자 형태가 같은 경우
                # 새로 등록되는 것과 이미 등록된 것이 같은 경우 - 소문자형을 등록해준다.
                if(RealWord.islower()): # 새로운 단어로 변경
                    CurNode.RealWord = RealWord
                    CurNode.Weight = Weight
                elif(CurNode.RealWord.islower()): # 원래 등록된 것을 그대로 사용
                    pass
                else: # 소문자 형태가 없는 경우 - 소문자 형태로 변환한다.
                    CurNode.RealWord = CurNode.RealWord.lower()
                    if(CurNode.Weight < Weight): # 가중치 비교하여 새것을 할당
                        CurNode.Weight = Weight
                return
            
            # 소문자 형태로 일치하지 않는 경우 - [영문자]단어가 있는 상태에서 [한글->영문자] 변환 단어가 겹치는 경우
            if(CurNode.RealWord_Multi != ''): # 두 번째 {RealWord}까지 있는 경우 - '2'개 이상은 등록하지 않는다.
                print(f'[Exist] {Word} : {CurNode.RealWord} / {CurNode.RealWord_Multi}  <===>  {RealWord}')
            else: # 두 번째 {RealWord}가 없으면 생성
                CurNode.RealWord_Multi = RealWord # {CurNode.RealWord}값이 '1'개가 아니라 '2'개일 때 사용
                CurNode.Weight_Multi = Weight
                #=print(f'[Multi] {Word} : {CurNode.RealWord} / {CurNode.RealWord_Multi}  <===>  {RealWord}')

                #--- tmp test
                #=if((CurNode.RealWord == 'db') or (Word == 'db')):
                #=    print(f'[check] {Word} : {CurNode.RealWord} <===>  {RealWord}')
                #=    print(vars(CurNode))
            return
        
        #
        #=if(RealWord == ''): 
        #=    RealWord = Word # {RealWord} 내용이 없으면 {Word}로 채워준다.
        CurNode.IsWord = True
        CurNode.Weight = Weight
        CurNode.RealWord = RealWord
        #=print('Node:', Word)

        #
        return CurNode

    def InsertWord(self, Word, RealWord='', Weight=0):
        return_node = self.InsertWord_StepByStep(Word, RealWord, Weight)
        return return_node

    def InsertWord_StepByStep(self, Word, RealWord='', Weight=0):
        #---------
        # 영문자 변환: 전각 알파벳 변환, 소문자 변환
        #---------
        EngWord = self.GetEngKeyword(Word)

        #---------
        # 한글 변환
        #---------
        HngTrieKey = self.GetHngTrieKeyword(EngWord)
        if(HngTrieKey != EngWord): # 한글 변형이 있는 경우(한글->자모/영문자)
            if(RealWord == ''): 
                # 외부에서 진짜 단어(RealWord)를 지정하지 않아도 
                # 여기서 바뀌면 진짜 단어(RealWord)를 (바뀌기 전의) 'word'를 전달
                RealWord = Word
            return_node = self.InsertNode(HngTrieKey, RealWord, Weight)
            return return_node # 한글 변형으로 등록되면 종료한다.

        #-----------
        # 영문자 처리
        #-----------
        return_node = self.InsertNode(EngWord, RealWord=RealWord, Weight=Weight)
        return return_node

    def GetEngKeyword(self, Word):
        # 전각 아스키 알파벳을 (기본 라틴) 아스키 알파벳으로 변환: 'ｋｏｒｅａ' -> 'korea', 'ｇｋｓｒｎｒ' -> 'gksrnr'{한국}
        if(self.Opt_FullwidthTrans == True ):
            from hgunicode import HGGetAsciiString__FullwidthAsciiString
            EngWord = HGGetAsciiString__FullwidthAsciiString(Word)
        else: # 전각 알파벳 변환이 아닌 경우에는 그대로 전달
            EngWord = Word

        #. 소문자 변환: 'gkSWhr' <--- '한족' 한영변환 오류 입력 해결
        if(self.Opt_LowerEngWord == True):
            EngKeyword = EngWord.lower()
        else: # 소문자 변환이 아닌 경우에는 그대로 전달
            EngKeyword = EngWord # original - 영문자 변형 없이 그대로 등록한다.
        #
        return EngKeyword

    def GetHngTrieKeyword(self, Word):
        """한글에 대하여 [트라이-키]를 적용하기 위해서 변환한다."""
        #---
        NewWord = Word
        #---
        # 반각 자모를 (전각) 두벌식(키보드) 자모 변환: 'ﾾￂﾤﾡￓﾡ'->'ㅎㅏㄴㄱㅜㄱ'
        #---
        if(self.Opt_Hng_HalfwidthTrans == True): # (default:True) # 반각 자모를 (전각) 두벌식(키보드) 자모 변환: 'ﾾￂﾤﾡￓﾡ'->'ㅎㅏㄴㄱㅜㄱ'
            NewWord = HGTransHalfJamo2KBDJamo(Word) # 반각 자모 -> (전각) 두벌식 자모
        #---
        # 초중종 자모를 (전각) 두벌식(키보드) 자모 변환: '대한민국'(초중종 자모)->'ㄷㅐㅎㅏㄴㅁㅣㄴㄱㅜㄱ'
        #---
        if(self.Opt_ChoJungJongJamoTrans == True): # (default:True) 초중종 자모를 (전각) 두벌식(키보드) 자모 변환: '대한민국'(초중종 자모)->'ㄷㅐㅎㅏㄴㅁㅣㄴㄱㅜㄱ'
            NewWord_from_ChoJungJong = HGTransChoJungJongJamo2KBDJamo(NewWord) # 초중종 자모 -> (전각) 두벌식 자모
            NewWord = NewWord_from_ChoJungJong
        #---
        if(self.Opt_Hng_Fmt == __Hng_AsItIs__): # 한글: 변형없이 그대로 처리
            #. 변형없이 그대로 사용
            return NewWord
        elif(self.Opt_Hng_Fmt == __Hng_2_Jamo__): # 한글: 키보드 자모로 처리
            #. [한글] ---> [키브도 자모]
            # HGTransString2KBDJamo() 함수는 디폴트(HalfJamoTrans=True)로 반각 자모를 두벌식 자모로 
            # 변환하므로 여기에 맞게 반드시 옵션을 전달해야 한다.
            KBDJamoString = HGTransString2KBDJamo(NewWord, 
                                HalfJamoTrans=self.Opt_Hng_HalfwidthTrans,
                                ChoJungJongJamoTrans=self.Opt_ChoJungJongJamoTrans)
            #=if(KBDJamoString == NewWord): # [한글]이 없어서 바뀐 것이 없는 경우
            #=    return
            return KBDJamoString
        elif(self.Opt_Hng_Fmt == __Hng_2_Eng__): # 한글: 영문자로 처리
            #. [한글] ---> [영문자] (한국 ---> gksrnr) 입력 오류 해결
            ExtEngWord = HGTransString2EngString(NewWord)
            #=if(ExtEngWord == NewWord): # [한글]이 없어서 바뀐 것이 없는 경우
            #=    return
            return ExtEngWord
        elif(self.Opt_Hng_Fmt == __Hng_2_Jamo3__): # 한글: 초중종 자모로 처리(사전식)
            # 알고리즘 차원에서 추가한 것으로 초성,중성,종성(사전식) 알고리즘을 설명할 때만 사용
            #. [한글] ---> [초중종 자모]
            KBDJamo3String = hgGetChoJungJongString(NewWord, jamo=True, CompatibleJamo2ChoJungJong=True)
            #=if(KBDJamo3String == NewWord): # [한글]이 없어서 바뀐 것이 없는 경우
            #=    return
            return KBDJamo3String
        else:
            assert False
            return None

    def GetUniqueEng(self, Word):
        # 어휘에 대하여 하나의 [트라이-키]를 적용하기 위해서 [전각/소문자] [영어]로 변환
        #---------
        # 영문자 변환: 전각 알파벳 변환, 소문자 변환
        #---------
        EngWord = self.GetEngKeyword(self, Word)
        #=if(EngWord == Word): # 바뀐 것이 없는 경우(다음으로 이동)
        #=    return
        
        #. [한글] ---> [영문자] 확장 (한국 ---> gksrnr) 입력 오류 해결
        ExtEngWord = HGTransString2EngString(EngWord)
        #=if(ExtEngWord == Word): # [한글]이 없어서 바뀐 것이 없는 경우
        #=    return

        return ExtEngWord

    def MakeTrie__WordList(self, WordList):
        #=print('WordList:', len(WordList))
        self.AddTrie__WordList(WordList)

    def AddTrie__WordList(self, WordList):
        #=print('WordList:', len(WordList))
        for Word in WordList: 
            self.InsertWord(Word, RealWord=Word)

    def MakeTrie__DictFreq(self, DictFreq):
        self.__init__()
        self.AddTrie__DictFreq(DictFreq)

    def AddTrie__DictFreq(self, DictFreq):
        for Dict in DictFreq: 
            self.InsertWord(Dict, RealWord=Dict, Weight=DictFreq[Dict])
        #
        self.AddNGram__DictFreq(DictFreq)

    def MakeNGram__DictFreq(self, DictFreq, NGram=5):
        self.NGramVocabulary = {}
        self.Opt_NGramValue = NGram
        self.AddNGram__DictFreq(DictFreq)

    def AddNGram__DictFreq(self, DictFreq):
        if(self.Opt_NGramMake != True):
            return
        AddNGramVocabulary__DictFreq(self.NGramVocabulary, 
            DictFreq, NGram=self.Opt_NGramValue, HngFmt=self.Opt_Hng_Fmt)
        #
        WeightNGramVocabulary(self.NGramVocabulary) # 가중치(빈도) 순으로 정렬(탐색시간 단축 위해)

    def FindNode(self, FindWord):
        SearchNode = self.TraverseNode(FindWord, ExactEnd=True) # ExactEnd=True: 종단에 있는 검색어만 찾기
        return SearchNode

    def TraverseNode(self, FindWord, ExactEnd=True):
        #
        CurNode = self.Root 
        for Char in FindWord:
            if not CurNode.Child.get(Char):
                return None
            CurNode = CurNode.Child[Char]
        if(ExactEnd == True): # 종단 노드일 때만 반환(종단 키 노드 검사)
            if(CurNode.IsWord == True): # 종단 키 노드
                return CurNode
            else:
                return None
        else: # 종단 키 노드가 아니어도 반환
            return CurNode

    def FindWordNode(self, CurNode, FindWord):
        if CurNode.IsWord: 
            # stopword
            if(self.stoplist is not None):
                if CurNode.RealWord in self.stoplist:
                    return # 불용어라서 등록하지 않고 종료
                if CurNode.RealWord_Multi in self.stoplist:
                    return # 불용어라서 등록하지 않고 종료
            # 
            self.SuggestResult.append({'word':FindWord, 
                'realword':CurNode.RealWord, 'weight':CurNode.Weight})
            if(CurNode.RealWord_Multi): # 두 번째 {RealWord}값이 있으면 추가
                self.SuggestResult.append({'word':FindWord, 
                    'realword':CurNode.RealWord_Multi, 'weight':CurNode.Weight_Multi})
        #
        for Char, Node_s in CurNode.Child.items(): 
            self.FindWordNode(Node_s, (FindWord + Char))

    def FindWord(self, FindWord):
        """
        접두사 일치 단어 탐색:
        FindWord로 시작하는 단어 목록 반환
        """
        #. init
        self.SuggestResult = [] 
        #. 접두사 노드 탐색
        SearchNode = self.TraverseNode(FindWord, ExactEnd=False) # ExactEnd=False: 종단이 아니어도 검색어를 포함한 것 찾기
        if SearchNode: 
            self.FindWordNode(SearchNode, FindWord) # 접두사로 시작하는 단어 노드 탐색
        #
        return self.SuggestResult

    def IsVocabulary(self, FindWord):
        SearchNode = self.TraverseNode(FindWord, ExactEnd=True) # ExactEnd=True: 종단에 있는 검색어만 찾기
        if(SearchNode == None):
            return False
        else:
            return True

    def SearchWord(self, FindWord, 
        LowerCasifyFlag=False, # 대문자롤 소문자로 변환
        FullwidthAsciiTrans=False, # 전각 영문자를 아스키 영문자로 변환
        HalfJamoTrans=False, # HalfJamoTrans: 반각 자모를 두벌식 자모로 변환
        ChoJungJongJamoTrans=False, # ChoJungJongJamoTrans: 초중종 자모를 두벌식 자모로 변환
        ):
        """
        FindWord를 검색하여 해당 노드 반환
        -------
        LowerCasifyFlag: 대문자롤 소문자로 변환
        FullwidthAsciiTrans: 전각 영문자를 아스키 영문자로 변환
        HalfJamoTrans: 반각 자모를 두벌식 자모로 변환
        ChoJungJongJamoTrans: 초중종 자모를 두벌식 자모로 변환
        
        트라이의 {HGTrie.Opt_Hng_Fmt} 두벌식 자모(__Hng_2_Jamo__:2)가 아니면 
        {HalfJamoTrans, ChoJungJongJamoTrans} 변수를 적용할 경우에 소용이 없다.
        """
        #-----
        # 단어 검색이므로 추쳔 결과(SuggestResult)는 사용하지 않는다.
        #-----
        #=#. init
        #=self.SuggestResult = [] 
        #-----
        #. 접두사 노드 탐색
        SearchNode = self.TraverseNode(FindWord, ExactEnd=True) # ExactEnd=True: 종단에 있는 검색어만 찾기
        if SearchNode is not None: # 해당 노드가 있는 경우
            return SearchNode
        #
        if(FullwidthAsciiTrans == True): # 전각 영문자를 아스키 영문자로 변환
            from hgunicode import HGGetAsciiString__FullwidthAsciiString
            AsciiString = HGGetAsciiString__FullwidthAsciiString(FindWord)
            if(AsciiString != FindWord): # 전각 아스키 -> 아스키 변환
                SearchNode = self.TraverseNode(AsciiString, ExactEnd=True) # ExactEnd=True: 종단에 있는 검색어만 찾기
                if SearchNode is not None: # 해당 노드가 있는 경우
                    return SearchNode 
        
        if(LowerCasifyFlag == True): # 대문자롤 소문자로 변환
            FindWord_lower = FindWord.lower() # 대문자롤 소문자로 통합하기 위해서 소문자 변환
            if(FindWord_lower != FindWord): # 소문자 변환
                SearchNode = self.TraverseNode(FindWord_lower, ExactEnd=True) # ExactEnd=True: 종단에 있는 검색어만 찾기
                if SearchNode is not None: # 해당 노드가 있는 경우
                    return SearchNode 

            if(FullwidthAsciiTrans == True): # 전각 영문자를 아스키 영문자로 변환
                FindWord_lower = AsciiString.lower() # 대문자롤 소문자로 통합하기 위해서 소문자 변환
                if(FindWord_lower != AsciiString): # 전각 아스키 -> 아스키 변환 -> 소문자 변환
                    SearchNode = self.TraverseNode(FindWord_lower, ExactEnd=True) # ExactEnd=True: 종단에 있는 검색어만 찾기
                    if SearchNode is not None: # 해당 노드가 있는 경우
                        return SearchNode 
            
        if(HalfJamoTrans == True): # 반각 자모를 두벌식 자모로 변환
            from hgunicode import HGGetCompatibleJamoString__HalfJamoString
            KBDJamoString = HGGetCompatibleJamoString__HalfJamoString(FindWord)
            if(KBDJamoString != FindWord): # 반각 자모 -> 두벌식 자모
                SearchNode = self.TraverseNode(KBDJamoString, ExactEnd=True) # ExactEnd=True: 종단에 있는 검색어만 찾기
                if SearchNode is not None: # 해당 노드가 있는 경우
                    return SearchNode
            
        if(ChoJungJongJamoTrans == True): # 초중종 자모를 두벌식 자모로 변환
            KBDJamoString = HGTransChoJungJongJamo2KBDJamo(FindWord)
            if(KBDJamoString != FindWord): # 초중종 자모 -> 두벌식 자모
                SearchNode = self.TraverseNode(KBDJamoString, ExactEnd=True) # ExactEnd=True: 종단에 있는 검색어만 찾기
                if SearchNode is not None: # 해당 노드가 있는 경우
                    return SearchNode 
        #---------------
        #. 한글 변환 옵션 확인
        #---------------
        HngTrieKey = self.GetHngTrieKeyword(FindWord)
        if(HngTrieKey != FindWord): # 한글 변형이 있는 경우(한글->두벌식 자모/초중종 자모/영문자)
            SearchNode = self.TraverseNode(HngTrieKey, ExactEnd=True) # ExactEnd=True: 종단에 있는 검색어만 찾기
            if SearchNode is not None: # 해당 노드가 있는 경우
                return SearchNode 
        
        #
        return SearchNode

    @classmethod
    def ImportSuggestion(cls, FindWord, 
        SuggestionList, SuggestionNew, SuggestNum=None,
        HngFmt=__Hng_AsItIs__):
        if(SuggestNum != None): # 추천 개수 제한 있는 경우
            #=print(SuggestNum, ':', len(SuggestionList))
            if(len(SuggestionList) >= SuggestNum): # 버퍼를 다 채웠기 때문에 그냥 종료
                return False # 오류가 아니라 추가로 받아들이지 않았다는 뜻
        #
        SuggestionNewNum = len(SuggestionNew)
        for new_i, SuggestionItem in enumerate(SuggestionNew):
            #
            if(SuggestNum != None): # 추천 개수 제한 있는 경우
                if(len(SuggestionList) >= SuggestNum): # 버퍼를 다 채운 경우
                    if(cls.Opt_Hng_Fmt == __Hng_2_Jamo3__): 
                        # 한글: 초중종 자모로 처리(사전식)
                        break # 초중종 자모로 처리(사전식)는 가중치를 사용하지 않는다.
                    else:
                        # [SuggestNum]-번째 추천 단어 이후의 가중치(빈도)가 같은지 검사
                        LastSuggestion = SuggestionList[-1] # 마지막 등록한 추천 단어
                        #=print('LastSuggestion:', LastSuggestion)
                        if(LastSuggestion['weight'] == SuggestionItem['weight']): 
                            # 가중치(빈도)가 같은 경우: 지정한 개수를 초과해서 등록
                            pass # 다음으로 이동하여 등록
                        else: # 맨 마지막으로 등록한 것과 가중치(빈도)가 다른 경우 - 종료
                            break

            # 중복 검사
            isAlready = False
            if(len(SuggestionItem['realword']) > 0):#성능테스트 때 realword값 없을 때 있음
                isAlready = next((si for si in SuggestionList 
                                if si['realword'] == SuggestionItem['realword']), None)
            if(not isAlready): # 중복 확인
                SuggestionList.append(SuggestionItem)
        #-------------------------
        # 지정한 추천 개수 초과 검사
        #-------------------------
        if(SuggestNum != None): # 추천 개수 제한 있는 경우
            if(len(SuggestionList) > SuggestNum): # 추천 단어 초과
                if(cls.Opt_Hng_Fmt == __Hng_2_Jamo3__):#한글:초중종 자모 처리(사전식)
                    pass # 초중종 자모로 처리(사전식)에서는 가중치를 사용하지 않는다.
                else:
                    # 맨 끝쪽에 가중치(빈도) 같은 단어가 여럿 있는 경우
                    # --> (편집 거리로) 2차 가중치 처리
                    #=print('len(SuggestionList):', len(SuggestionList))
                    WeightSuggestList_SameWeight(FindWord, 
                        SuggestionList, SuggestNum, HngFmt=HngFmt)
                #---------
                # {SuggestNum}를 초과한 것은 삭제
                #---------
                # 외부에서 온 변수라서 직접 전달하면 로컬 변수로 변해서 함수 밖에서 사라진다.
                #= SuggestionList = SuggestionList[:SuggestNum]
                #---------
                while(True):
                    if(len(SuggestionList) > SuggestNum):
                        #=print('SuggestionList[-1]:', SuggestionList[-1])
                        del SuggestionList[-1]
                    else:
                        break
                #=print('len(SuggestionList):', len(SuggestionList))
        #
        return True

    def ExtendSuggestion_ByEng(self, FindWord, SuggestList):
        # 검색어 공백 제거
        FindWord = FindWord.strip()
        if(len(FindWord) <= 0):
            return

        #---------
        # 영문자 변환: 전각 알파벳 변환, 소문자 변환
        # 소문자 변환: 'gkSWhr', 'gKsWhr', 'GKSWHR' <--- '한족' 한영변환 오류 입력 해결
        #---------
        EngWord = self.GetEngKeyword(FindWord)
        if(EngWord != FindWord):
            New_Suggest = self.FindWord(EngWord)
            if(self.Opt_Hng_Fmt == __Hng_2_Jamo3__): # 한글: 초중종 자모로 처리(사전식)
                # 초중종 자모로 처리(사전식)에서는 빈도순 정렬을 하지 않는다.
                SugList_Sort = New_Suggest.copy()
            else:
                SugList_Sort = sorted(New_Suggest, key=lambda item: -item['weight']) # by high
            #-----
            # ImportSuggestion() 안에서 비교 대상이 같아야 한다.
            # {FindWord} -> {EngWord}
            #-----
            #=self.ImportSuggestion(FindWord, SuggestList, 
            #=    SugList_Sort, self.Opt_SuggestNum, HngFmt=self.Opt_Hng_Fmt)
            #-----
            self.ImportSuggestion(EngWord, SuggestList, 
                SugList_Sort, self.Opt_SuggestNum, HngFmt=self.Opt_Hng_Fmt)
            #=print(len(SuggestList), ':', SuggestList)

    def ExtendSuggestion_ByHng2Eng(self, FindWord, SuggestList):
        # 검색어 공백 제거
        FindWord = FindWord.strip()
        if(len(FindWord) <= 0):
            return 

        #------------------
        #. 한글 -> 영문 변환: 'ㅏㅠㄴ'(kbs), '듄'(ebs), 'ㅏㅐㄱㄷㅁ(korea)' <--- '한족' 한영변환 오류 입력 해결
        #------------------
        HngTrieKey = self.GetHngTrieKeyword(FindWord)
        if(HngTrieKey != FindWord): # 한글 변형이 있는 경우(한글->자모/영문자)
            #=print(HngTrieKey)
            New_Suggest = self.FindWord(HngTrieKey)
            if(self.Opt_Hng_Fmt == __Hng_2_Jamo3__): # 한글: 초중종 자모로 처리(사전식)
                # 초중종 자모로 처리(사전식)에서는 빈도순 정렬을 하지 않는다.
                SugList_Sort = New_Suggest.copy()
            else:
                SugList_Sort = sorted(New_Suggest, key=lambda item: -item['weight']) # by high
            #-----
            # ImportSuggestion() 안에서 비교 대상이 같아야 한다.
            # {FindWord} -> {HngTrieKey}
            #-----
            #=self.ImportSuggestion(FindWord, SuggestList, SugList_Sort, self.Opt_SuggestNum)
            #-----
            self.ImportSuggestion(HngTrieKey, SuggestList, 
                SugList_Sort, self.Opt_SuggestNum, HngFmt=self.Opt_Hng_Fmt)
            
            #=print(len(SuggestList), ':', SuggestList)
            if(len(SuggestList) >= self.Opt_SuggestNum):
                return 

            #---------
            # 영문자 변환: 전각 알파벳 변환, 소문자 변환
            #---------
            self.ExtendSuggestion_ByEng(HngTrieKey, SuggestList)
            #=if(len(SuggestList) >= self.Opt_SuggestNum):
            #=    return SuggestList

    def GetSuggestion_Default(self, FindWord, SuggestList):
        # 검색어 공백 제거(==> 트라이 생성에도 반영되어 있어야 한다.)
        FindWord = FindWord.strip()
        if(len(FindWord) <= 0):
            return 

        #------------------
        # 1. original-word
        #------------------
        New_Suggest = self.FindWord(FindWord)
        #=print('self.FindWord(),', len(New_Suggest), ':', '\n', New_Suggest)
        if(self.Opt_Hng_Fmt == __Hng_2_Jamo3__): # 한글: 초중종 자모로 처리(사전식)
            # 초중종 자모로 처리(사전식)에서는 빈도순 정렬을 하지 않는다.
            SugList_Sort = New_Suggest.copy()
        else:
            SugList_Sort = sorted(New_Suggest, key=lambda item: -item['weight']) # by high
        #-----
        # ImportSuggestion() 안에서 비교 대상이 같아야 한다.
        #-----
        #=self.ImportSuggestion(FindWord, SuggestList, SugList_Sort, self.Opt_SuggestNum)
        #-----
        self.ImportSuggestion(FindWord, SuggestList, 
            SugList_Sort, self.Opt_SuggestNum, HngFmt=self.Opt_Hng_Fmt)
        
        #=print('self.ImportSuggestion(), ', len(SuggestList), ':', '\n', SuggestList)
        #=if(len(SuggestList) >= self.Opt_SuggestNum):
        #=    return 

    def ExtendSuggestion_NGram(self, FindWord, SuggestList):
        # 검색어 공백 제거(==> 트라이 생성에도 반영되어 있어야 한다.)
        FindWord = FindWord.strip()
        if(len(FindWord) <= 0):
            return 

        #---------
        #. n-gram:
        #---------
        if(self.Opt_NGramUse != True): #  n-gram suggest
            return

        #------------------
        #. n-gram: 'givernm' <--- [governm] <=== [government], {gi^vernm^} <=== 5-gram(^vernm^)
        #------------------
        if(self.Opt_Hng_Fmt == __Hng_2_Jamo3__): # 한글: 초중종 자모로 처리(사전식)
            # 초중종 자모로 처리(사전식)에서는 빈도순 정렬을 하지 않는다.
            #==================
            assert False, \
            """
            # (철자 오류를 교정하는) {Opt_NGramUse}옵션이 켜 있을 때는                 
            # 이 방식을 지원하지 않습니다.
            # GetSuggestion_NGram() 함수는 가중치(빈도) 정렬에 최적화된 상태라서 
            # 고치려면 복잡해서 지금은 처리하지 않는다.
            # 특히 초중종 자모로 처리(사전식)하는 방식은 특별한 경우가 아니면 
            # 사용하기 어렵기 때문에 이 블록은 처리하지 않고 넘어갑니다.
            # 나중에 검토할 계획입니다.
            #-----------------------------------
            # GetSuggestion_NGram() 함수를 따라가면서 
            # self.Opt_Hng_Fmt == __Hng_2_Jamo3__ 조건을 확인하여 이 상태이면 
            # 빈도순으로 정렬하지 않고 코드 순서로 정렬해주면 되는데 
            # 생각보다 확인해야 하는 부분이 많아서 나중에 업그레이드를 검토한다.
            """
            pass 
        else:
            SuggestionNGram = GetSuggestion_NGram(FindWord, self.NGramVocabulary, 
                NGram=self.Opt_NGramValue, LowerEng=self.Opt_LowerEngWord, 
                HngFmt=self.Opt_Hng_Fmt, FullwidthTrans=self.Opt_FullwidthTrans, 
                HalfJamoTrans = self.Opt_Hng_HalfwidthTrans, 
                ChoJungJongJamoTrans = self.Opt_ChoJungJongJamoTrans, 
                SuggestNum=self.Opt_SuggestNum, 
                PrintDebug=False)
            #=print('~~~\n', *SuggestionNGram, sep='\n')
            self.ImportSuggestion(FindWord, SuggestList, SuggestionNGram, 
                    SuggestNum=self.Opt_SuggestNum, HngFmt=self.Opt_Hng_Fmt)
            
            #=print('self.ImportSuggestion(), ', len(SuggestList), ':', '\n', SuggestList)
            #=if(len(SuggestList) >= self.Opt_SuggestNum):
            #=    return 

    def GetSuggestion(self, FindWord):
        #=print('Opt_SuggestNum:', self.Opt_SuggestNum)
        #
        Return_Suggest = []

        # 검색어 공백 제거(==> 트라이 생성에도 반영되어 있어야 한다.)
        FindWord = FindWord.strip()
        if(len(FindWord) <= 0):
            return Return_Suggest

        #------------------
        # 1. original-word
        #------------------
        self.GetSuggestion_Default(FindWord, Return_Suggest)
        if(len(Return_Suggest) >= self.Opt_SuggestNum):
            return Return_Suggest
        
        #---------
        # 영문자 변환: 전각 알파벳 변환, 소문자 변환
        #---------
        self.ExtendSuggestion_ByEng(FindWord, Return_Suggest)
        if(len(Return_Suggest) >= self.Opt_SuggestNum):
            return Return_Suggest

        #------------------
        #. 한글 변환 -> 영문/자모: 'ㅏㅠㄴ'(kbs), '듄'(ebs), 'ㅏㅐㄱㄷㅁ(korea)' <--- '한족' 한영변환 오류 입력 해결
        #------------------
        self.ExtendSuggestion_ByHng2Eng(FindWord, Return_Suggest)
        if(len(Return_Suggest) >= self.Opt_SuggestNum):
            return Return_Suggest
                

        #------------------
        #. n-gram: 'givernm' <--- [governm] <=== [government], {gi^vernm^} <=== 5-gram(^vernm^)
        #------------------
        self.ExtendSuggestion_NGram(FindWord, Return_Suggest)
        if(len(Return_Suggest) >= self.Opt_SuggestNum):
            return Return_Suggest
        #
        return Return_Suggest

    def PrintNode(self, CurNode, CurWord):
        if CurNode.IsWord:
            self.PrintCnt += 1
            print(f'{self.PrintCnt}, {CurWord} : {CurNode.Weight}')

        for Char, Node_s in CurNode.Child.items(): 
            self.PrintNode(Node_s, CurWord + Char) 

    def PrintChildNode(self, FindWord=None):
        if(FindWord == None):
            CurNode = self.Root
        else:
            CurNode = self.TraverseNode(FindWord, ExactEnd=False) # ExactEnd=False: 검색어를 포함한 것 찾기
            if CurNode == None: # no word
                return

        print(), print('Print Child Node:', len(CurNode.Child))
        for i, node_char in enumerate(CurNode.Child):
            #=print(f'{i+1} : {node_char}')
            ChildNode = CurNode.Child[node_char]
            print(f'{i+1} : {ChildNode.GetFullKeyName()}')

    def PrintTrie(self, FindWord=None):
        self.PrintCnt = 0
        if(FindWord == None):
            self.PrintNode(self.Root, '')
        else:
            TraverseNode = self.TraverseNode(FindWord, ExactEnd=False) # ExactEnd=False: 검색어를 포함한 것 찾기
            if TraverseNode == None: # no word
                pass
            else:
                self.PrintNode(TraverseNode, FindWord)

    def CountNode(self, CurNode, CurWord):
        """CurNode에 속한 {단어}인 자식 노드 개수"""
        CountNum = 0
        if CurNode.IsWord: 
            CountNum += 1

        for Char, Node_s in CurNode.Child.items(): 
            SubCountNum = self.CountNode(Node_s, CurWord + Char)
            CountNum += SubCountNum
        return CountNum

    def CountTrie(self, FindWord=None): 
        """검색어에 따린 자식을 순환적으로 전부 계산"""
        CountNum = 0
        if(FindWord == None):
            CountNum = self.CountNode(self.Root, '')
        else:
            TraverseNode = self.TraverseNode(FindWord, ExactEnd=False) # ExactEnd=False: 검색어를 포함한 것 찾기
            if TraverseNode == None: # no word
                pass
            else:
                CountNum = self.CountNode(TraverseNode, FindWord)
        return CountNum

    def GetChildNum(self, FindWord=None):
        ChildNum = 0
        if(FindWord == None):
            ChildNum = len(self.Root.Child)
        else:
            TraverseNode = self.TraverseNode(FindWord, ExactEnd=False) # ExactEnd=False: 검색어를 포함한 것 찾기
            if TraverseNode == None: # no word
                pass
            else:
                ChildNum = len(TraverseNode.Child)
        return ChildNum


#================================
#================================
#================================
def PrintSuggestionList(SugList):
    # format: [{'word': 'authorize', 'realword': '', 'weight': 9}, ...]
    # format: [{'word':'gksrnr','realword':'한국','weight':10}, ...]
    for si, SugItem in enumerate(SugList):
        if(len(SugItem['realword']) > 0): # 'realword'에 값이 있는 경우
            SuggestWord = SugItem['realword']
        else:
            SuggestWord = SugItem['word']
        print(f"{si+1} : {SuggestWord} ({SugItem['weight']})")

def GetSuggestion_NGram(FindWord, NGramVocabulary, 
    NGram=2, SuggestNum=10, 
    HngFmt=__Hng_AsItIs__, 
    LowerEng=False, 
    FullwidthTrans = False, # 전각 알파벳을 (기본 라틴) 알파벳으로 변환
    HalfJamoTrans=False,  # 전각 자모를 (전각) 두벌식 자모로 변환
    ChoJungJongJamoTrans=False, # 초중종 자모를 (전각) 두벌식 자모로 변환
    PrintDebug=False):
    #
    NGramSuggestionList = []

    #------------------
    # original
    #------------------
    NGramSuggestionList_Org = GetSuggestion_NGramWord(FindWord, 
        NGramVocabulary, NGram=NGram, SuggestNum=SuggestNum, HngFmt=HngFmt, 
        PrintDebug=PrintDebug)
    HGTrie.ImportSuggestion(FindWord, NGramSuggestionList, 
                    NGramSuggestionList_Org, HngFmt=HngFmt)
    #---------
    # 영문자 변환: 전각 알파벳 변환, 소문자 변환
    #---------
    #------------------
    # 전각 아스키 알파벳을 (기본 라틴) 아스키 알파벳으로 변환: 'ｋｏｒｅａ' -> 'korea', 'ｇｋｓｒｎｒ' -> 'gksrnr'{한국}
    #------------------
    if(FullwidthTrans == True ):
        from hgunicode import HGGetAsciiString__FullwidthAsciiString
        EngWord = HGGetAsciiString__FullwidthAsciiString(FindWord)
        if(EngWord != FindWord): 
            # 'ｚｈｆｌｄｋ'  # ('zhfldk') '코리아' 한영변환 오류 입력 해결
            NGramSuggestionList_Eng = GetSuggestion_NGramWord(EngWord, 
                NGramVocabulary, NGram=NGram, SuggestNum=SuggestNum, HngFmt=HngFmt, 
                PrintDebug=PrintDebug)
            #-----
            # ImportSuggestion() 안에서 비교 대상이 같아야 한다.
            # {FindWord} -> {EngWord}
            #-----
            #=HGTrie.ImportSuggestion(FindWord, NGramSuggestionList, NGramSuggestionList_Eng)
            #-----
            HGTrie.ImportSuggestion(EngWord, NGramSuggestionList, 
                                NGramSuggestionList_Eng, HngFmt=HngFmt)

    #. 소문자 변환: 'GIVERNM' <--- 'givernm'  <--- 'governm' 한영변환 오류 입력 해결
    #. 소문자 변환: 'gkSWhr' <--- '한족' 한영변환 오류 입력 해결
    if(LowerEng == True):
        LowerEngWord = ""
        # 
        if(FullwidthTrans == True ): # 전각 아스키 알파벳을 (기본 라틴) 아스키 알파벳으로 변환
            from hgunicode import HGGetAsciiString__FullwidthAsciiString
            EngWord = HGGetAsciiString__FullwidthAsciiString(FindWord)
            if(EngWord != FindWord): 
                LowerEngWord = EngWord.lower() # {기본 라틴} 알파벳을 소문자로 변경
        #
        if(LowerEngWord == ""): # 위에서 바뀐게 없다면 여기서 소문자로 변경
            LowerEngWord = FindWord.lower()
        if(LowerEngWord != FindWord): 
            # 'gkSWhr', 'gKsWhr', 'GKSWHR' # '한족' 한영변환 오류 입력 해결
            NGramSuggestionList_Eng = GetSuggestion_NGramWord(LowerEngWord, 
                NGramVocabulary, NGram=NGram, SuggestNum=SuggestNum, HngFmt=HngFmt, 
                PrintDebug=PrintDebug)
            #-----
            # ImportSuggestion() 안에서 비교 대상이 같아야 한다.
            # {FindWord} -> {LowerEngWord}
            #-----
            #=HGTrie.ImportSuggestion(FindWord, NGramSuggestionList, NGramSuggestionList_Eng)
            #-----
            HGTrie.ImportSuggestion(LowerEngWord, NGramSuggestionList, 
                                NGramSuggestionList_Eng, HngFmt=HngFmt)

    #---------
    # 한글 변환: 반각 자모({전각}두벌식 자모) 변환, 한영 변환
    #---------
    #---
    # 반각 자모를 (전각) 두벌식(키보드) 자모 변환: 'ﾾￂﾤﾡￓﾡ'->'ㅎㅏㄴㄱㅜㄱ'
    #---
    HngWord = FindWord
    if(HalfJamoTrans == True): # 반각 자모를 (전각) 두벌식(키보드)자모 변환: 'ﾾￂﾤﾡￓﾡ'->'ㅎㅏㄴㄱㅜㄱ'
        HngWord = HGTransHalfJamo2KBDJamo(FindWord) # 반각 자모 -> (전각) 두벌식 자모
    #---
    # 초중종 자모를 (전각) 두벌식(키보드) 자모 변환: '대한민국'(초중종 자모)->'ㄷㅐㅎㅏㄴㅁㅣㄴㄱㅜㄱ'
    #---
    if(ChoJungJongJamoTrans == True): # 초중종 자모를 (전각) 두벌식(키보드) 자모 변환: '대한민국'(초중종 자모)->'ㄷㅐㅎㅏㄴㅁㅣㄴㄱㅜㄱ'
        HngWord_from_ChoJungJong = HGTransChoJungJongJamo2KBDJamo(HngWord) # 초중종 자모 -> (전각) 두벌식 자모
        HngWord = HngWord_from_ChoJungJong # 2-step for debugging

    #------------------
    #. 한글 -> 영문 변환 + ngram: 'givernㅡ' <--- 'governm' 한영변환 오류 입력 해결
    #. __Hng_2_Jamo__: {한글: 키보드 자모로 처리} 방식에는 {한글}+{영문} 혼용
    #------------------
    if(HngFmt == __Hng_AsItIs__): # 한글: 변형없이 그대로 처리
        pass #. 변형없이 그대로 사용
    elif(HngFmt == __Hng_2_Jamo__): # 한글: 키보드 자모로 처리
        #. [한글] ---> [키보드자모]
        # HGTransString2KBDJamo() 함수는 디폴트(HalfJamoTrans=True)로 반각 자모를 두벌식 자모로 
        # 변환하므로 여기에 맞게 반드시 옵션을 전달해야 한다.
        KBDJamoString = HGTransString2KBDJamo(HngWord, 
                            HalfJamoTrans=HalfJamoTrans, ChoJungJongJamoTrans=ChoJungJongJamoTrans)
        if((KBDJamoString != HngWord) or # [한글]이 [두벌식(키보드)자모]로 바뀔 때 달라진다.
           (KBDJamoString != FindWord)): # [반각 자모]가 (전각) [두벌식(키보드)자모]로 바뀔 때 달라진다.
            NGramSuggestionList_Jamo = GetSuggestion_NGramWord(KBDJamoString, 
                NGramVocabulary, NGram=NGram, SuggestNum=SuggestNum, HngFmt=HngFmt, 
                PrintDebug=PrintDebug)
            #-----
            # ImportSuggestion() 안에서 비교 대상이 같아야 한다.
            # {HngWord} -> {KBDJamoString}
            #-----
            #=HGTrie.ImportSuggestion(HngWord, NGramSuggestionList, NGramSuggestionList_Jamo)
            #-----
            HGTrie.ImportSuggestion(KBDJamoString, NGramSuggestionList, 
                                NGramSuggestionList_Jamo, HngFmt=HngFmt)            
            
            #------------------
            #. 소문자 변환: 'GIVERNㅡ' <--- 'GIVERNM' <--- 'givernm' <--- 'governm' 한영변환 오류 입력 해결
            #------------------
            if(LowerEng == True):
                LowerEngWord = KBDJamoString.lower()
                if(LowerEngWord != HngWord): # 'gkSWhr', 'gKsWhr', 'GKSWHR' # '한족' 한영변환 오류 입력 해결
                    NGramSuggestionList_Eng = GetSuggestion_NGramWord(LowerEngWord, 
                        NGramVocabulary, NGram=NGram, SuggestNum=SuggestNum, HngFmt=HngFmt, 
                        PrintDebug=PrintDebug)
                    #-----
                    # ImportSuggestion() 안에서 비교 대상이 같아야 한다.
                    # {HngWord} -> {LowerEngWord}
                    #-----
                    #=HGTrie.ImportSuggestion(HngWord, NGramSuggestionList, NGramSuggestionList_Eng)
                    #-----
                    HGTrie.ImportSuggestion(LowerEngWord, NGramSuggestionList, 
                                        NGramSuggestionList_Eng, HngFmt=HngFmt)
    elif(HngFmt == __Hng_2_Eng__): # 한글: 영문자로 처리
        #. [한글] ---> [영문자] (한국 ---> gksrnr) 입력 오류 해결
        ExtEngWord = HGTransString2EngString(HngWord)
        if(ExtEngWord != HngWord): # [한글]이 영문으로 바뀔 때 달라진다.
            NGramSuggestionList_Eng = GetSuggestion_NGramWord(ExtEngWord, 
                NGramVocabulary, NGram=NGram, SuggestNum=SuggestNum, HngFmt=HngFmt, 
                PrintDebug=PrintDebug)
            #-----
            # ImportSuggestion() 안에서 비교 대상이 같아야 한다.
            # {HngWord} -> {ExtEngWord}
            #-----
            #=HGTrie.ImportSuggestion(HngWord, NGramSuggestionList, NGramSuggestionList_Eng)
            #-----
            HGTrie.ImportSuggestion(ExtEngWord, NGramSuggestionList, 
                                NGramSuggestionList_Eng, HngFmt=HngFmt)
            
            #------------------
            #. 소문자 변환: 'GIVERNㅡ' <--- 'GIVERNM' <--- 'givernm' <--- 'governm' 한영변환 오류 입력 해결
            #------------------
            if(LowerEng == True):
                LowerEngWord = ExtEngWord.lower()
                if(LowerEngWord != HngWord): # 'gkSWhr', 'gKsWhr', 'GKSWHR' # '한족' 한영변환 오류 입력 해결
                    NGramSuggestionList_Eng = GetSuggestion_NGramWord(LowerEngWord, 
                        NGramVocabulary, NGram=NGram, SuggestNum=SuggestNum, HngFmt=HngFmt, 
                        PrintDebug=PrintDebug)
                    #-----
                    # ImportSuggestion() 안에서 비교 대상이 같아야 한다.
                    # {HngWord} -> {LowerEngWord}
                    #-----
                    #=HGTrie.ImportSuggestion(HngWord, NGramSuggestionList, NGramSuggestionList_Eng)
                    #-----
                    HGTrie.ImportSuggestion(LowerEngWord, NGramSuggestionList, 
                                        NGramSuggestionList_Eng, HngFmt=HngFmt)

    elif(HngFmt == __Hng_2_Jamo3__): # 한글: 초중종 자모로 처리(사전식)
        # 알고리즘 차원에서 추가한 것으로 초성,중성,종성(사전식) 알고리즘을 설명할 때만 사용
        #. [한글] ---> [초중종 자모]
        KBDJamo3String = hgGetChoJungJongString(HngWord, jamo=True, CompatibleJamo2ChoJungJong=True)
        if(KBDJamo3String != HngWord): # [한글]이 [초중종 자모]로 바뀔 때 달라진다.
            NGramSuggestionList_Jamo3 = GetSuggestion_NGramWord(KBDJamo3String, 
                NGramVocabulary, NGram=NGram, SuggestNum=SuggestNum, HngFmt=HngFmt, 
                PrintDebug=PrintDebug)
            #-----
            # ImportSuggestion() 안에서 비교 대상이 같아야 한다.
            # {HngWord} -> {KBDJamo3String}
            #-----
            #=HGTrie.ImportSuggestion(HngWord, NGramSuggestionList, NGramSuggestionList_Jamo3)
            #-----
            HGTrie.ImportSuggestion(KBDJamo3String, NGramSuggestionList, 
                                NGramSuggestionList_Jamo3, HngFmt=HngFmt)
            
            #------------------
            #. 소문자 변환: 'GIVERNㅡ' <--- 'GIVERNM' <--- 'givernm' <--- 'governm' 한영변환 오류 입력 해결
            #------------------
            if(LowerEng == True):
                LowerEngWord = KBDJamo3String.lower()
                if(LowerEngWord != HngWord): # 'gkSWhr', 'gKsWhr', 'GKSWHR' # '한족' 한영변환 오류 입력 해결
                    NGramSuggestionList_Eng = GetSuggestion_NGramWord(LowerEngWord, 
                        NGramVocabulary, NGram=NGram, SuggestNum=SuggestNum, HngFmt=HngFmt, 
                        PrintDebug=PrintDebug)
                    #-----
                    # ImportSuggestion() 안에서 비교 대상이 같아야 한다.
                    # {HngWord} -> {LowerEngWord}
                    #-----
                    #=HGTrie.ImportSuggestion(HngWord, NGramSuggestionList, NGramSuggestionList_Eng)
                    #-----
                    HGTrie.ImportSuggestion(LowerEngWord, NGramSuggestionList, 
                                        NGramSuggestionList_Eng, HngFmt=HngFmt)
    else:
        assert False

    #--------------------
    # [n-gram suggest] sort by high
    #--------------------
    SugList_Sort = sorted(NGramSuggestionList, key=lambda item: -item['weight']) # by high
    #=print(), print(*SugList_Sort, sep='\n')
    return SugList_Sort

def GetSuggestion_NGramWord(FindWord, NGramVocabulary, NGram=2, SuggestNum=10, 
    HngFmt=__Hng_AsItIs__,
    PrintDebug=False):
    # 검색어 NGram 변환
    NGramList = MakeStringNGram(FindWord, NGram=NGram, MoreThan=True)
    if(PrintDebug == True):
        print(), print(f'[{FindWord}] {NGram}-Gram: {NGramList}')
        NGramDicVocSum = 0
        for NGramDicNum, NGramListWord in enumerate(NGramList):
            NGramDicVocabulary = NGramVocabulary.get(NGramListWord)
            if(NGramDicVocabulary):
                NGramDicVocSum += len(NGramDicVocabulary)
                print(f'{NGramDicNum+1}, {NGramListWord} ({len(NGramDicVocabulary)}) :')
                #=PrintVocabulary(NGramDicVocabulary, LeadingString='\t')
        print('NGramDicVocSum:', NGramDicVocSum)
        print()

    # 길이순 정렬(길이가 긴 것을 가중치 높게 주기 위해서 앞에서 먼저 검사하도록 함)
    NGramList = sorted(NGramList, key=lambda item: -len(item)) # by high
    if(PrintDebug == True):
        from hgdistance import GetEditDistance
        #=print(NGramList) # 디버그용
        #=print(*NGramList, sep='\n') # 디버그용
        print(), print(f'[{FindWord}] {NGram}-Gram <길이 순서로 출력>')
        print(f'순서\tN그램 단어\tN그램 단어 길이\t편집 거리\t연관 검색어 수')
        for nix, NGramListWord in enumerate(NGramList):
            EditDistance = GetEditDistance(FindWord, NGramListWord)
            print(f'{nix+1}\t{NGramListWord}\t{len(NGramListWord)}\t{EditDistance}\t', end='')
            #
            NGramDicVocabulary = NGramVocabulary.get(NGramListWord)
            if(NGramDicVocabulary):
                print(f'{len(NGramDicVocabulary)}', end='')
            print()
        print()
        
        print('# 하나 더 출력한다. 이번에는 값이 없는 것은 제외')
        print(), print(f'[{FindWord}] {NGram}-Gram <길이 순서로 출력>')
        print(f'순서\tN그램 단어\tN그램 단어 길이\t편집 거리\t연관 검색어 수')
        NGramCnt = 0
        for nix, NGramListWord in enumerate(NGramList):
            NGramDicVocabulary = NGramVocabulary.get(NGramListWord)
            if(NGramDicVocabulary):
                NGramCnt += 1
                EditDistance = GetEditDistance(FindWord, NGramListWord)
                print(f'{NGramCnt}\t{NGramListWord}\t{len(NGramListWord)}\t{EditDistance}\t', end='')
                print(f'{len(NGramDicVocabulary)}', end='')
                print()
        print()


    #-----
    # 바로 위에서 정렬한 것을 가지고 여기서 편집 거리 제한을 걸지 않는 것이 좋다.
    # N그램 검색어(FindWord)와 N그램 목록의 항목이랑 편집 거리 제한을 둘 경우에는 
    # 추천이 안 될 수도 있으므로 편집 거리 제한은 두지 않는 것이 바람직하다.
    #
    # 검색어에 대한 N그램 어휘 목록을 길이 순서로 정렬한 뒤에 
    # 두벌식 자모로 변환한 (철자 오류 상태의) 검색어와의 편집 거리가 
    # '3'을 초과하지 않는 것까지 처리할 경우, 
    # 원래 단어 길이가 긴 경우에는 되레 일치하는 부분 문자열을 찾지 못하는 
    # 경우가 발생할 수 있다.
    # a) '헌극경ㅈ', 'ㅏㄴ극경ㅈ'  ===> '한국경제'를 가장 먼저 추천한다.
    # b) '란국경ㅈ'   ===> '한국경제'를 가장 먼저 추천한다.
    # a)의 경우에 '한국경제'를 찾으려면 'ㄱㄱㅕㅇㅈ'(편집거리:5)로 찾기 때문에 
    # 편집 거리 제한(3)을 두면 'ㄱㄱㅕㅇㅈ' 어휘는 편집거리가 제한 범위보다 커져서 
    # 포함될 수 없다. 그러면 못 찾게 되므로 아래 생각처럼 편집 거리 제한을 두면 안 된다.
    # ===> @@@  15 : ㄱㄱㅕㅇㅈ : 5 : 73  @@@
    # 1 : {'key': 'ㅎㅏㄴㄱㅜㄱㄱㅕㅇㅈㅔ', 'word': '한국경제', 'weight': 614}
    # 
    # 다만 b)도 '한국경제'를 가장 먼저 추천하지만 a)와 b)의 전체 추천 목록은 다르다.
    #-----

    #--------------------
    # find n-gram suggest
    #--------------------
    NGramSuggestionList = []
    FindSuggestion_NGramList(NGramList, FindWord, NGramVocabulary, 
        NGramSuggestionList, SuggestNum=SuggestNum, HngFmt=HngFmt)

    #--------------------
    # [n-gram suggest] sort by high
    #--------------------
    SugList_Sort=sorted(NGramSuggestionList,key=lambda item:-item['weight'])# by high
    #=print(), print(*SugList_Sort, sep='\n')
    return SugList_Sort

def FindSuggestion_NGramList(NGramList, FindWord, 
    NGramVocabulary, NGramSuggestionList, SuggestNum=10, HngFmt=__Hng_AsItIs__):
    # find n-gram suggest
    NGramListLen = len(NGramList)
    for inx, NGramWord in enumerate(NGramList):
        NGramDicVocabulary = NGramVocabulary.get(NGramWord)
        if(NGramDicVocabulary == None): # n-gram에 속하는 단어가 없는 경우
            #=print('NGramList[', NGramWord, '] - (NGramDicVocabulary == None)', )
            #-----
            # 다음 {NGramWord}으로 가기 전에 추천 개수를 채웠으면 중단해야 한다.
            #-----
            if(SuggestNum > 0):
                if(len(NGramSuggestionList) >= SuggestNum): # 버퍼 꽉 채움 - 중단
                    break
            #
            continue
        #=print(f'NGramList({NGramWord}): {len(NGramDicVocabulary)} {NGramDicVocabulary}')
        #=NGramDicVocabulary_format:[{'key':'roqkfwpgks','word':'개발제한','weight':7},...]
        
        for NGramDic_Value in NGramDicVocabulary:
            #=print(NGramDic_Value)
            #=format: {'key': 'roqkfwpgks','word':'개발제한구역','weight':7}
            # 중복 검사
            isAlready = next((si for si in NGramSuggestionList 
                            if si['realword'] == NGramDic_Value['word']), None)
            if(not isAlready): # 중복 확인
                #=format: HGTrie.SuggestResult.append(
                #{'word':FindWord,'realword':CurNode.RealWord,'weight':CurNode.Weight}
                #)
                NGramSuggestion_Item = {'word':NGramWord, 
                    'realword':NGramDic_Value['word'], 'weight':NGramDic_Value['weight']}
                NGramSuggestionList.append(NGramSuggestion_Item)
                if(SuggestNum > 0): # 추천목록 개수 제한이 있으면 정렬해준다.
                    SugList_Sort = sorted(NGramSuggestionList, 
                                    key=lambda item: -item['weight']) # by high
                    #-----
                    # 외부에서 넘어온 것이라서 직접 전달하면 함수 밖에서 사라진다.
                    # NGramSuggestionList = SugList_Sort 
                    #-----
                    NGramSuggestionList.clear() # 외부에서 넘어온 것은 clear() 한 후 확장
                    NGramSuggestionList.extend(SugList_Sort)
            #
            if(SuggestNum > 0):
                if(len(NGramSuggestionList) >= SuggestNum): # 버퍼 꽉 채움 - 중단
                    # 방금 추가한 것의 가중치가 [목록 맨 마지막 항목]의 가중치보다 크면 
                    # 중단하지 않고 다음 항목을 계속 추가해야 한다.
                    # 여러 N그램 단어를 순차적으로 처리하기 때문에 
                    # 길이가 긴 것부터 목록이 채워진다.
                    # 현재 이후의 N그램 단어의 길이가 현재와 같으면 계속 찾아야 한다.
                    # 나중의 N그램 단어에 속한 것들의 가중치가 높은 경우도 있으므로 
                    # 무조건 추천개수(SuggestNum)를 채웠다고 종료하면 안 된다.
                    NGramSuggestionList_Tail = NGramSuggestionList[-1]
                    Tail_weight = int(NGramSuggestionList_Tail['weight'])
                    #=print(len(NGramSuggestionList), ':', SuggestNum, '^', NGramSuggestionList_Tail)
                    if(int(NGramDic_Value['weight']) < Tail_weight):
                        break
                    else: 
                        if(len(NGramSuggestionList) > SuggestNum): 
                            #-----
                            # 버퍼를 초과함 - 맨 마지막 것을 지운다.
                            #-----
                            # 초과된 맨 마지막 것을 무조건 지우면 안 된다.
                            # 맨 마지막 직전 것과 가중치(빈도)가 같으면 남겨주고 
                            # 이 함수 끝날 때 따로 조절해야 한다.
                            if(SuggestNum >= 2):
                                NGramSuggestionList_Tail2 = NGramSuggestionList[-2]
                                Tail_weight2 = int(NGramSuggestionList_Tail2['weight'])
                                if(Tail_weight == Tail_weight2):
                                    # 맨 마지막의 직전 것과 가중치가 같으면 지우지 않는다.
                                    pass 
                                else:
                                    del NGramSuggestionList[-1]
        #
        if(SuggestNum > 0):
            if(len(NGramSuggestionList) >= SuggestNum): # 버퍼 꽉 채움
                # 곧 바로 끝내지 말고, 유사도(편집길이)가 같은 다음 단어까지 확인해야 한다.
                if((inx + 1) < NGramListLen):
                    FindWord_Next = NGramList[inx + 1]
                    if(len(FindWord_Next) == len(NGramWord)): 
                        # 현재 {FindWord}와 다음 {FindWord} 길이가 같은 경우
                        pass # 다음 검사로 넘어가도록 한다.
                    else: 
                        # 현재 {FindWord}와 다음 {FindWord} 길이가 다르면 
                        # 더 이상 찾을 필요가 없다.
                        break
                else: # 맨 끝 단어인 경우
                    break # 루프가 끝나기 때문에 {pass}를 해도 되지만 확실하게 break함.

    # 가중치 추가 조절 - 가중치가 같은 것은 편집거리로 가까운 것에 우선 순위를 둔다.
    WeightSuggestList_SameWeight(FindWord, 
        NGramSuggestionList, SuggestNum, HngFmt=HngFmt)

    #
    if(SuggestNum > 0): 
        if(len(NGramSuggestionList) > SuggestNum): 
            # SuggestNum보다 조금 더 만들 때가 있다.
            #-----
            # 외부에서 넘어온 것이라서 직접 전달하면 함수 밖에서 사라진다.
            #= NGramSuggestionList = NGramSuggestionList[:SuggestNum] 
            #-----
            while(True):
                if(len(NGramSuggestionList) > SuggestNum):
                    del NGramSuggestionList[-1]
                else:
                    break

def WeightSuggestList_SameWeight(FindWord, SuggestionList, SuggestNum, 
    HngFmt=__Hng_AsItIs__, 
    DebugPrint=False):
    # 가중치로 정렬하고, 가중치가 같은 것은 편집거리로 가까운 것에 2차로 우선 순위를 둔다.
    #---
    import copy
    from hgdistance import GetEditDistance

    #-----
    if(DebugPrint == True): # before
        print(), print('[before] WeightSuggestList_SameWeight() :', *SuggestionList, sep='\n')

    #---
    #=print('[prev] same', *SuggestionList, sep='\n'), print()

    # 가중치로 1차 정렬
    SugList_Sort = sorted(SuggestionList, key=lambda item: -item['weight']) # by high
    if(SuggestNum >= 2):
        # 가중치가 같은 것을 찾아서 편집거리로 2차 정렬        
        SugList_Sort_Len = len(SugList_Sort)
        nix_t = 0
        while(nix_t < SugList_Sort_Len):
            Sug_Cur = SugList_Sort[nix_t]
            if((nix_t + 1) < SugList_Sort_Len): # 맨 끝은 안 된다.
                # 똑같은 가중치를 가진 단어 찾기
                SameNum = 1
                Sug_Next = SugList_Sort[nix_t + SameNum]
                while(True):
                    if(Sug_Next['weight'] == Sug_Cur['weight']): # 가중치가 똑 같은 경우
                        SameNum += 1
                        Sug_Cur = Sug_Next
                    else:
                        break
                    if((nix_t + SameNum) >= SugList_Sort_Len): # 맨 끝은 안 된다.
                        break
                    Sug_Next = SugList_Sort[nix_t + SameNum]
                
                # 똑같은 가중치를 가진 단어 확인
                if(SameNum >= 2):
                    SugList_Sort_Same = SugList_Sort[nix_t:(nix_t+SameNum)]
                    #=print('SugList_Sort_Same:', *SugList_Sort_Same, sep='\n')

                    # 편집 거리 계산 후 정렬
                    sort_res = {}
                    for same_item in SugList_Sort_Same:
                        # format: same_item={'word':'gksrnr','realword':'한국','weight':10}
                        KeyWord = same_item['word']
                        SameRealWord = same_item['realword']
        
                        #------------------
                        #------------------
                        # [Word]는 [키]이므로 반드시 [RealWord]를 전달해야 함.
                        # 트라이에서 넘어온 추천 목록은 상관이 없지만 
                        # NGram에서 넘어온 경우에는 [Word]는 부분 문자열이고 
                        # [RealWord]가 검색어 사전 어휘이므로 검색어랑 비교해야 한다.
                        #------------------
                        if(HngFmt == __Hng_AsItIs__): # 한글: 변형없이 그대로 처리
                            #. [RealWord]는 [Word]와 문자 상태가 같은 경우: 
                            KBDCharString = SameRealWord # 
                        elif(HngFmt == __Hng_2_Jamo__): # 한글: 키보드 자모로 처리
                            KBDCharString = HGTransString2KBDJamo(SameRealWord) # 한글 음절->두벌식 자모 변환
                        elif(HngFmt == __Hng_2_Eng__): # 한글: 영문자로 처리
                            KBDCharString = HGTransString2EngString(SameRealWord) # 한영변환
                        elif(HngFmt == __Hng_2_Jamo3__): # 한글: 초중종 자모로 처리(사전식)
                            # 알고리즘 차원에서 추가한 것으로 초성,중성,종성(사전식) 알고리즘을 설명할 때만 사용
                            KBDCharString = hgGetChoJungJongString(SameRealWord) # [초중종 자모]로 변환
                        else:
                            assert False                            
                        #
                        Distance = GetEditDistance(FindWord, KBDCharString)
                        #=print (Distance, f'({jamo_eng}[{same_t}])')
                        sort_res[SameRealWord] = Distance
                    #
                    dis_sort = sorted(sort_res.items(), key=lambda item:item[1]) # by low
                    #=print(*dis_sort, sep='\n')
                    #
                    for sort_i, sort_item in enumerate(dis_sort): # format: dis_sort <- tuple
                        #=print (f'{sort_item[0]}')
                        RealWord = sort_item[0] # [0]:'realword'  [1]:weight
                        isAlready = next((si for si in 
                            SugList_Sort_Same if si['realword'] == RealWord), None)
                        if(isAlready == None):
                            assert False
                        SugList_Sort[nix_t + sort_i] = copy.deepcopy(isAlready)

                    # next
                    nix_t += SameNum
                    continue
            # next
            nix_t += 1
    #    
    #=print('SugList_Sort:', *SugList_Sort, sep='\n')

    #-----
    # 정렬 결과를 돌려준다.
    #-----
    #= SuggestionList = SugList_Sort # 외부에서 넘어온 것이라 직접 전달하면 함수 밖에서 사라짐
    #-----
    SuggestionList.clear() # 외부에서 넘어온 것이라서 clear() 한 후에 넘겨줘야 한다.
    SuggestionList.extend(SugList_Sort)

    #-----
    if(DebugPrint == True): # after
        print(), print('[after] WeightSuggestList_SameWeight() :', *SuggestionList, sep='\n')
        print()

def GetSpellCheck_NGram(FindWord, NGramVocabulary, NGram=2, 
    LowerEng=True, # 영문 대문자를 소문자로 변환
    Hng2Jamo=False, # 한글을 두벌식 자모로 변환
    Hng2Eng=False, # 한글을 영문자로 변환
    Eng2Jamo=False, # 영문자로 두벌식 자모로 변환
    EditDistanceLimit = 3, # 편집 거리 제한
    FullwidthAsciiTrans=False, # 전각 영문자를 아스키 영문자로 변환
    HalfJamoTrans=False, # 반각 자모를 두벌식 자모로 변환
    ChoJungJongJamoTrans=False, # 초중종 자모를 두벌식 자모로 변환
    PrintDebug=False):
    """
    LowerEng: 영문 대문자를 소문자로 변환
    Hng2Jamo: 한글을 두벌식 자모로 변환
    Hng2Eng: # 한글을 영문자로 변환
    Eng2Jamo: # 영문자로 두벌식 자모로 변환
    EditDistanceLimit: # 편집 거리 제한
    FullwidthAsciiTrans: 전각 영문자를 아스키 영문자로 변환
    HalfJamoTrans: 반각 자모를 두벌식 자모로 변환
    ChoJungJongJamoTrans: 초중종 자모를 두벌식 자모로 변환

    검색어 사전(DictFreqList)이 두벌식 자모가 아니면 {HalfJamoTrans, ChoJungJongJamoTrans} 변수를 적용할 경우에 소용이 없다.
    """    
    #=====
    from hgdistance import GetEditDistance

    #=====
    #=====
    #=print('NGram:', NGram)

    #
    if(FullwidthAsciiTrans == True): # 전각 영문자를 아스키 영문자로 변환
        from hgunicode import HGGetAsciiString__FullwidthAsciiString
        AsciiString = HGGetAsciiString__FullwidthAsciiString(FindWord)
        #----- 변환 결과를 확인할 필요 없음. 바뀐 것이 없으면 원래 것을 반환하기 때문.
        #=if(FindWord != AsciiString): # 전각 아스키 -> 아스키 변환
        #=    FindWord = AsciiString
        #-----
        FindWord = AsciiString
    #
    if(HalfJamoTrans == True): # 반각 자모를 두벌식 자모로 변환
        #-----
        # 논리적으로는 Hng2Jamo(True:한글을 두벌식 자모로 변환)에서 처리하는 게 맞지만
        # 이럴 경우에는 {Hng2Jamo=True}와 {HalfJamoTrans=True}를 동시에 지정해야 하므로 
        # API 호출 상 직관적이지 않다. 직관적으로는 {HalfJamoTrans=True}만 지정해도 
        # 처리될 것으로 기대하므로 여기서 따로 처리한다.
        #-----
        from hgunicode import HGGetCompatibleJamoString__HalfJamoString
        KBDJamoString = HGGetCompatibleJamoString__HalfJamoString(FindWord)
        #----- 변환 결과를 확인할 필요 없음. 바뀐 것이 없으면 원래 것을 반환하기 때문.
        #=if(KBDJamoString != FindWord): # 반각 자모 -> 두벌식 자모
        #-    FindWord = KBDJamoString
        #-----
        FindWord = KBDJamoString
    #            
    if(ChoJungJongJamoTrans == True): # 초중종 자모를 두벌식 자모로 변환
        #-----
        # 논리적으로는 Hng2Jamo(True:한글을 두벌식 자모로 변환)에서 처리하는 게 맞지만
        # 이럴 경우에는 {Hng2Jamo=True}와 {HalfJamoTrans=True}를 동시에 지정해야 하므로 
        # API 호출 상 직관적이지 않다. 직관적으로는 {ChoJungJongJamoTrans=True}만 지정해도 
        # 처리될 것으로 기대하므로 여기서 따로 처리한다.
        #-----
        KBDJamoString = HGTransChoJungJongJamo2KBDJamo(FindWord)
        #----- 변환 결과를 확인할 필요 없음. 바뀐 것이 없으면 원래 것을 반환하기 때문.
        #=if(KBDJamoString != FindWord): # 초중종 자모 -> 두벌식 자모
        #-    FindWord = KBDJamoString
        #-----
        FindWord = KBDJamoString

    #------------------
    #------------------
    if(LowerEng == True):
        #.소문자 변환:'GIVERNMENT'<-'givernment'<-'government' 한영변환 오류 해결
        FindWord = FindWord.lower()
    if(Hng2Jamo == True): # 한글을 두벌식 자모로 변환
        #-----
        # HGTransString2KBDJamo() 함수는 기본값을 {반각 자모->두벌식 자모}, 
        # {초종중 자모 -> 두벌식 자모}로 변환하는데 이 함수의 매개변수와 연동하지 않고 
        # 변환하도록 냅둔다.
        # 직관적으로 Hng2Jamo(True:한글을 두벌식 자모로 변환)하는 것은 
        # {HalfJamoTrans=True}와 {ChoJungJongJamoTrans=True}도 포함하기 때문이다.
        #-----
        #=FindWord = HGTransString2KBDJamo(FindWord, HalfJamoTrans=HalfJamoTrans, 
        #=                ChoJungJongJamoTrans=ChoJungJongJamoTrans) # 한글->키보드 자모
        #-----
        FindWord = HGTransString2KBDJamo(FindWord)        
    if(Hng2Eng == True): # 한글을 영문자로 변환
        #. 한글 -> 영문 변환 + ngram: 'givernㅡ' <- 'governm' 한영변환 오류 해결
        #-----
        # HGTransString2EngString() 함수는 기본값을 {반각 자모->두벌식 자모}, 
        # {초종중 자모 -> 두벌식 자모}로 변환하는데 이 함수의 매개변수와 연동하지 않고 
        # 변환하도록 냅둔다.
        # 직관적으로 Hng2Jamo(True:한글을 두벌식 자모로 변환)하는 것은 
        # {HalfJamoTrans=True}와 {ChoJungJongJamoTrans=True}도 포함하기 때문이다.
        #-----
        #=FindWord = HGTransString2EngString(FindWord, HalfJamoTrans=HalfJamoTrans, 
        #=                ChoJungJongJamoTrans=ChoJungJongJamoTrans)
        #-----
        FindWord = HGTransString2EngString(FindWord)
    if(Eng2Jamo == True): # 영문자로 두벌식 자모로 변환
        from hgkbd import HGGetJaumMoum__EngString
        #-----
        # HGGetJaumMoum__EngString() 함수는 기본값을 {전각 아스키->아스키}로 변환하는데 
        # 이 함수의 매개변수와 연동하지 않고 변환하도록 냅둔다.
        # 직관적으로 Eng2Jamo(True:영문자로 두벌식 자모로 변환)하는 것은 
        # {FullwidthAsciiTrans=True}도 포함하기 때문이다.
        #-----
        #=FindWord = HGGetJaumMoum__EngString(FindWord, FullwidthAsciiTrans=FullwidthAsciiTrans) # 영문자 -> 두벌식 자모 변환
        #-----
        FindWord = HGGetJaumMoum__EngString(FindWord) # 영문자 -> 두벌식 자모 변환

    #------------------
    #------------------
    #=print('FindWord:', FindWord)
    NGramList = MakeStringNGram(FindWord, NGram=NGram, MoreThan=True)
    #=== spell-check 일 때는 길이순 정렬이 효과없다.
    #=# 길이순 정렬(길이가 긴 것을 가중치 높게 주기 위해서 앞에서 먼저 검사하도록 함) <= 여기서 필요 없음
    #=NGramList = sorted(NGramList, key=lambda item: -len(item)) # by high

    #===================
    #===================
    # '편집 거리 계산' # 검색어랑 편집 거리가 가까운 단어만 선택
    NGDic_Distance = {}
    MinDistance = (-1) # '0': 똑같은 단어는 '0'이라서 이보다 작은 초기값

    for inx, NGramWord in enumerate(NGramList):
        NGramDicVocabulary = NGramVocabulary.get(NGramWord)
        if(NGramDicVocabulary == None): # n-gram에 속하는 단어가 없는 경우
            #=print('NGramList[', NGramWord, '] - (NGramDicVocabulary == None)', )
            continue
        #=print(f'NGramList({NGramWord}): {len(NGramDicVocabulary)} {NGramDicVocabulary}')
        #=NGramDicVocabulary_format: [{'key': 'roqkfwpgksrndur', 'word': '개발제한구역', 'weight': 7}, ...]
        #=NGramDicVocabularyNum = len(NGramDicVocabulary)

        for sub_j, NGDic_I in enumerate(NGramDicVocabulary):
            #=print(f"{sub_j+1} :", NGDic_I)
            #=format: {'key': 'roqkfwpgksrndur', 'word': '개발제한구역', 'weight': 7}
            #=print(f"{sub_j+1} : {NGDic_I['word']} : {NGDic_I['weight']}")

            NGDic_Jamo = NGDic_I['key']
            #=NGDic_Word = NGDic_I['word']
            #=NGDic_weight = NGDic_I['weight']

            EditDistance = GetEditDistance(FindWord, NGDic_Jamo)
            #=print('EditDistance:', EditDistance)

            #============================
            # 연관 단어 편집 거리 제한:
            # 검색어(FindWord)와 편집 거리가 제한값(기본값:3)을 초과하면 어색한 경우가 
            # 많아서 그 이상의 단어는 등록하지 않도록 막는다
            #============================
            if(EditDistanceLimit > 0): # 값이 있을 때 검사
                if(EditDistance > EditDistanceLimit): # {EditDistanceLimit = 3}
                    continue

            #============================
            #============================
            # 가장 가까운 편집 거리 찾기
            if(MinDistance < 0): # 처음 비교하는 경우
                MinDistance = EditDistance
            else:
                if(MinDistance < EditDistance): # 최소 편집 거리보다 크면 제외
                    continue
                elif(MinDistance == EditDistance): # 최소 편집 거리와 같은 경우:등록
                    pass
                else: # 최소 편집 거리보다 작은 경우: 새로 등록하기 위해서 초기화
                    MinDistance = EditDistance
                    NGDic_Distance.clear()

            #============================
            #============================
            # 교정 후보 단어 등록
            #============================
            # format: [origin-word, EditDistance, weight(freq)]
            #============================
            # 등록 방법1
            #=NGDic_Item = [NGDic_Word, EditDistance, NGDic_weight]
            #=NGDic_Distance[NGDic_Jamo] = NGDic_Item

            # 등록 방법2
            #=NGDic_Distance[NGDic_Jamo] = [NGDic_I['word'], EditDistance, NGDic_I['weight']]

            # 등록 방법3
            NGDic_Item = [NGDic_I['word'], EditDistance, NGDic_I['weight']]
            NGDic_Distance[NGDic_Jamo] = NGDic_Item
    #
    #=print(), print(NGDic_Distance)

    # 위에서 편집 거리 제한(EditDistanceLimit)을 둘 경우에는 값이 없을 수도 있다.
    if(len(NGDic_Distance) <= 0):
        # 철자 오류 교정 후보 반환
        SpellCheckWord = ''
        return SpellCheckWord

    #------------------------------
    # 아래 블록은 철자 교정(SpellCheck)와 관련이 없어서 막는다.
    #------------------------------
    #=#============================
    #=#============================
    #=# '편집 거리 정렬' # (sort by low)
    #=dict_by_keys = sorted(NGDic_Distance.items(), key=lambda item: item[1][1]) # by low
    #=IncludeDic_High = {dic[0]:dic[1] for dic in dict_by_keys} 
    #=#=print(), print ('편집 거리 정렬') # (sort by low)
    #=#=print(), print(IncludeDic_High)
    #=
    #=#=from hgbasic import PrintDict_KeyValue_ByLine
    #=#=PrintDict_KeyValue_ByLine(IncludeDic_High)
    #=#=PrintDict_KeyValue_ByLine(IncludeDic_High, SepChar='\t') # 편집용 탭 출력
    #------------------------------


    #============================
    #============================
    #============================
    # '가중치(빈도) 정렬' # (sort by high)
    #=print(), print ('가중치(빈도) 정렬') # (sort by high)
    dict_by_keys = sorted(NGDic_Distance.items(), key=lambda item: -item[1][2]) # by high
    #=IncludeDic_High = dict(dict_by_keys)
    IncludeDic_High = {dic[0]:dic[1] for dic in dict_by_keys} 
    #=print(), print(IncludeDic_High)

    #=print(), print(*IncludeDic_High.items(), sep='\n')
    #=PrintDict_KeyValue_ByLine(IncludeDic_High)
    #=PrintDict_KeyValue_ByLine(IncludeDic_High, SepChar='\t') # 편집용 탭 출력

    #============================
    #============================
    #============================
    # 철자 오류 교정 후보 반환
    SpellCheckWord = ''
    if(len(IncludeDic_High) > 0):
        for Dict in IncludeDic_High: # format: {key: [word, distance, weight], ...}
            SpellCheckWord = IncludeDic_High[Dict][0] # 'word'
            break # 첫 번째 위치한 교정 단어를 찾으면 루프 탈출
    return SpellCheckWord

def get_ngram_word__MaxWordNum(NGramVocabulary):
    #-----
    # get max link-word in ngram-dict
    #-----
    max_num = 0
    max_nword = None
    for nword in NGramVocabulary:
        cur_num = len(NGramVocabulary[nword])
        if(cur_num > max_num):
            max_num = cur_num
            max_nword = nword
    #
    max_nword_list = NGramVocabulary[max_nword]
    #=print(f'<NGram Dict Max> {max_nword} ({len(max_nword_list)}):', max_nword_list)
    print(f'NGram Dict Max: {max_nword} ({len(max_nword_list)}):')
    print("순서: 두벌식 자모 문자열(빈도) [검색어 사전 단어]")
    for li, item in enumerate(max_nword_list):
        # format: {'key':dic_eng, 'word':RealWord, 'weight':Weight}
        print(f"{li+1}: {item['key']} ({item['weight']}) [{item['word']}]")

    # 편집 코드
    print("순서\t두벌식 자모 문자열\t빈도\t검색어 사전 단어")
    for li, item in enumerate(max_nword_list):
        # format: {'key':dic_eng, 'word':RealWord, 'weight':Weight}
        print(f"{li+1}\t{item['key']}\t{item['weight']}\t{item['word']}")
    print(),print(),print(),print(),print(),

def GetSpellCheck_Find(FindWord, DictFreqList,
    LowerCasifyFlag=False, FullwidthAsciiTrans=False, 
    HalfJamoTrans=False, ChoJungJongJamoTrans=False,
    ):
    """
    DictFreqList: 검색어 사전(format1:{word:freq}, format2:{word:{doc-id:freq}}
    LowerCasifyFlag: 대문자롤 소문자로 변환
    FullwidthAsciiTrans: 전각 영문자를 아스키 영문자로 변환
    HalfJamoTrans: 반각 자모를 두벌식 자모로 변환
    ChoJungJongJamoTrans: 초중종 자모를 두벌식 자모로 변환

    검색어 사전(DictFreqList)이 두벌식 자모가 아니면 {HalfJamoTrans, ChoJungJongJamoTrans} 변수를 적용할 경우에 소용이 없다.
    """
    #-----
    from hgworddistance import FindDisWord_Vocabulary
    #-----
    #
    SpellCheckWord = ''
    # 검색어 사전 탐색
    if(FindWord in DictFreqList): # 사전에 있는 경우
        SpellCheckWord = FindWord
        return SpellCheckWord
        
    # [편집 거리]로 검색어 사전 탐색에서 철자 교정
    DisWord = FindDisWord_Vocabulary(FindWord, DictFreqList,
                LowerCasifyFlag=LowerCasifyFlag, FullwidthAsciiTrans=FullwidthAsciiTrans, 
                HalfJamoTrans=HalfJamoTrans, ChoJungJongJamoTrans=ChoJungJongJamoTrans)
    #=print('DisWord Num:', len(DisWord)) # format: { 'word':(distance, freq), ...}
    if(len(DisWord) > 0):
        # 편집 거리 순서 정렬 # by low value(distance)
        DisWord_Sort = sorted(DisWord.items(), key=lambda kv: (kv[1][0], -kv[1][1])) # by low value(distance)
        SpellCheckWord = DisWord_Sort[0][0]
    #
    return SpellCheckWord

def Han2EngChecker(FindWord, DictFreqList, SpellWordMode = False, 
    HalfJamoTrans=False, 
    ChoJungJongJamoTrans=False,
    printCodeOrder=False):
    """
    DictFreqList: 검색어 사전(format1:{word:freq}, format2:{word:{doc-id:freq}}
    SpellWordMode: 철자 교정 모드
    HalfJamoTrans: 반각 자모를 두벌식 자모로 변환
    ChoJungJongJamoTrans: 초중종 자모를 두벌식 자모로 변환
    """
    #-----
    from hgworddistance import FindDisWord_Vocabulary
    #-----
    # 한영 변환
    EngWord = HGTransString2EngString(FindWord, 
                HalfJamoTrans=HalfJamoTrans, ChoJungJongJamoTrans=ChoJungJongJamoTrans)
    print(f'[한영변환] {FindWord} ===> {EngWord}')

    # [편집 거리]로 검색어 사전 탐색에서 철자 교정
    #=print('EditDistance:')
    DisWord = FindDisWord_Vocabulary(EngWord, DictFreqList, DisNum=10)
    if(printCodeOrder == True):
        print()
        print('# 코드 순서 출력')
        DisWord_Sort = sorted(DisWord.items(), key=lambda kv: kv[0]) # by a->z
        for i, x in enumerate(DisWord_Sort):
            print((i+1), ':', x[0] , x[1])
        print()
    if(len(DisWord) > 0):
        # 편집 거리 순서로 정렬 (by low value(distance))
        DisWord_Sort = sorted(DisWord.items(), key=lambda kv: (kv[1][0], -kv[1][1])) # by low value(distance)
        #
        if(SpellWordMode == True):
            SpellCheckWord = DisWord_Sort[0][0] # format:(('word', (distance, freq)), ...)
            print(f"<{FindWord}> 이 단어가 맞나요? ===>", SpellCheckWord)
            return
        #
        print()
        print('DisWord Num:', len(DisWord)) # format: { 'word':(distance, freq), ...}
        print('# 편집 거리 순서 출력') # by low value(distance)
        for i, x in enumerate(DisWord_Sort): # format: (('word', (distance, freq)), ...)
            print((i+1), ':', x[0] , x[1])
    else:
        print(f'[{EngWord}({FindWord})] 교정한 검색어가 없습니다.')
    print()

def Eng2HngChecker(FindWord, DictFreqList, SpellWordMode = False, 
    FullwidthAsciiTrans= False, 
    printCodeOrder=False):
    """
    DictFreqList: 검색어 사전(format1:{word:freq}, format2:{word:{doc-id:freq}}
    SpellWordMode: 철자 교정 모드
    FullwidthAsciiTrans: 전각 영문자를 아스키 영문자로 변환
    """
    #-----    
    from hgkbd import HGGetJaumMoum__EngString, HGGetSyllable_JaumMoumString
    from hgworddistance import FindDisWord_Vocabulary
    # 영한 변환
    JaumMoumWord = HGGetJaumMoum__EngString(FindWord, FullwidthAsciiTrans=FullwidthAsciiTrans)
    print(f'[영한변환] {FindWord}  ===>  {JaumMoumWord}')

    # [편집 거리]로 검색어 사전 탐색에서 철자 교정
    #=print('EditDistance:') # 두벌식 자모 문자열로 편집 거리 비교
    DisWord = FindDisWord_Vocabulary(JaumMoumWord, DictFreqList, DisNum=10,
        FullwidthAsciiTrans=FullwidthAsciiTrans)
    if(printCodeOrder == True):
        print()
        print('# 코드 순서 출력')
        DisWord_Sort = sorted(DisWord.items(), key=lambda kv: kv[0]) # by a->z
        for i, x in enumerate(DisWord_Sort):
            SyllableWord = HGGetSyllable_JaumMoumString(x[0])
            print(f"{(i+1)}: {x[0]}({SyllableWord}) {x[1]}")
        print()
    if(len(DisWord) > 0):
        # 편집 거리 순서로 정렬 (by low value(distance))
        DisWord_Sort = sorted(DisWord.items(), key=lambda kv: (kv[1][0], -kv[1][1])) # by low value(distance), high-freq
        #
        if(SpellWordMode == True):
            SpellCheckWord = DisWord_Sort[0][0] # format:(('word', (distance, freq)), ...)
            print(f"<{FindWord}> 이 단어가 맞나요? ===>", SpellCheckWord)
            return
        #
        print()
        print('DisWord Num:', len(DisWord)) # format: { 'word':(distance, freq), ...}
        print('# 편집 거리 순서 출력') # by low value(distance)
        for i, x in enumerate(DisWord_Sort): # format: (('word', (distance, freq)), ...)
            SyllableWord = HGGetSyllable_JaumMoumString(x[0]) # 'word'
            print(f"{(i+1)}: {x[0]}({SyllableWord}) {x[1]}") 
    else:
        print(f'[{JaumMoumWord}({FindWord})] 교정한 검색어가 없습니다.')
    print()

def PrintMatchDictFreq(Prefix, DictFreq, Title=None):
    print()
    if(Title!=None):
        print('#-----------------------------')
        print('@@@ ', Title, '@@@')
        print('#-----------------------------')
    print(f'prefix [{Prefix}]: {len(DictFreq)}')
    #=print(*DictFreq, sep='\n')
    for i, dic in enumerate(DictFreq):
        print(f'{i+1}, {dic} : {DictFreq[dic]}') # format: {'that': 13, ...}


#================================
#================================
#================================
class HGTest(TestCase):
    #================================
    #================================
    #================================
    def test_trie_1(self): # word-list mode
        WordList_as = ['as','ask','asking','asleep',
            'aspect','assemble','assembly','assert','assignment','assist','astronaut',
        ]

        FindWord = 'ass'
        TrieTest = HGTrie() 
        TrieTest.MakeTrie__WordList(WordList_as) 
        SugList = TrieTest.GetSuggestion(FindWord) 
        print()
        print('@@@ WordList Mode @@@')
        print(f'Suggest {len(SugList)}:')
        print(*SugList, sep='\n')

        '''
        @@@ WordList Mode @@@
        Suggest 5:
        {'assemble': 0}
        {'assembly': 0}
        {'assert': 0}
        {'assignment': 0}
        {'assist': 0}
        '''
    def test_trie_2(self): # dict-freq mode
        DictFreq_as = {'as':1,'ask':2,'asking':3,'asleep':4,
            'aspect':5,'assemble':6,'assembly':7,'assert':8,
            'assignment':9,'assist':10,'astronaut':11,
        }

        FindWord = 'ass'
        TrieTest = HGTrie() 
        TrieTest.MakeTrie__DictFreq(DictFreq_as) 
        SugList = TrieTest.GetSuggestion(FindWord) 
        print()
        print('@@@ DictFreq Mode @@@')
        print(f'Suggest {len(SugList)}:')
        print(*SugList, sep='\n')

        '''
        @@@ DictFreq Mode @@@
        Suggest 5:
        {'assemble': 6}
        {'assembly': 7}
        {'assert': 8}
        {'assignment': 9}
        {'assist': 10}
        '''

if __name__ == '__main__':
    main()



