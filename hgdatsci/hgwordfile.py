#------------------------
#------------------------
from unittest import TestCase, main
from typing import List

import hgsysinc
##import hgbasic

from hgwordlist import GetWordDictList_WordList
#-----
from typing import NamedTuple
class HGBookSelf(NamedTuple): # v3.6
    doc: str
    text: str
    state: bool

#-----
#-----
def ReadCsvFile(filename, encoding='utf-8', DeleteComment=False, seperator='\t'):
    #---
    from pathlib import Path
    
    #---
    cvs_list = []
    
    #=print(filename)
    lines = ReadTxtFile(filename, encoding, DeleteComment, ReturnList=True)
    #-----
    #-----
    #=print(lines)
    
    for li, cur_line in enumerate(lines):
        #
        cur_line = cur_line.strip()
        if(len(cur_line) <= 0):
            continue
        #
        if(DeleteComment == True): # '//' (코멘트)로 시작하는 문단 지우기
            tmp_lt = cur_line[:2]
            if(tmp_lt == "//"):
                continue # pass
        #
        if(len(seperator) >= 1):
            token_list = cur_line.split(seperator)
        else:
            token_list = cur_line[:]
        #
        cvs_list.append(token_list)
    #
    return cvs_list

def ReadTxtFile(filename, encoding='utf-8', DeleteComment=False, ReturnList=False):
    from pathlib import Path
    #
    lines = []
    
    #print(filename)
    real_filename = Path(filename)
    if real_filename.is_file():
        if real_filename.exists():
            pass
        else: 
            if(ReturnList == True): # 문단 목록으로 반환
                return lines
            else:            
                return ""
    else:
        print("file not found: %s" %filename)
        if(ReturnList == True): # 문단 목록으로 반환
            return lines
        else:            
            return ""
    #    
    file = open(real_filename, 'r', encoding=encoding)
    try:
        lines = file.readlines()
    except UnicodeDecodeError: 
        # 'cp949' codec can't decode byte 0xeb in position 1:
        # 'euc_kr' codec can't decode byte 0x8b in position 1443: illegal multibyte sequence
        # 'utf-8' codec can't decode byte 0xb0 in position 0: invalid start byte
        file.close()
    #
    if(file.closed == True):
        file = open(real_filename, 'r', encoding='utf8') # 'utf8'로 다시 읽어본다.
        try:
            lines = file.readlines()
        except UnicodeDecodeError: #'cp949' codec can't decode byte 0xeb in position 1:
            file.close()
    #
    if(file.closed == True):
        file = open(real_filename, 'r', encoding='cp949') # 'cp949'로 다시 읽어본다.
        try:
            lines = file.readlines()
        except UnicodeDecodeError: #'cp949' codec can't decode byte 0xeb in position 1:
            file.close()
            # 세 가지 인코딩으로 읽지 못하면 그냥 종료한다.
            if(ReturnList == True): # 문단 목록으로 반환
                return lines
            else:            
                return ""
    #-----
    #-----
    #print(lines)
    if(DeleteComment == True): # '//' (코멘트)로 시작하는 문단 지우기
        newlines = []
        for li, lt in enumerate(lines):
            tmp_lt = lt[:]
            tmp_lt.strip()
            tmp_lt = tmp_lt[:2]
            if(tmp_lt == "//"):
                pass
            else:
                newlines.append(lt)
        lines = newlines
    #
    if(ReturnList == True): # 문단 목록으로 반환
        return lines
    # 텍스트로 반환
    textall = ''.join(lines)
    return textall

def GetFilelist__Filepath(pathname, ReadNum=-1, PrintFilename=False):
    from pathlib import Path
    if(PrintFilename == True):
        print('pathname:', pathname)
    
    #
    Filelist = []

    #
    import glob
    ReadCnt = 0
    for filename in glob.glob(pathname):
        if(PrintFilename == True): print(f'[FILE {ReadCnt}] ', filename)

        filename_sys = Path(filename) # {Path()}함수는 {string}이 아니라 시스템 파일 이름으로 반환
        if filename_sys.is_file(): # 파일인가
            ReadCnt += 1
            Filelist.append(filename) # {Filelist} 변수는 string 목록으로 반환해야 한다.
            if(ReadNum > 0):
                if(ReadCnt >= ReadNum):
                    break
    #print ('len :', len(Filelist))
    return Filelist

def MakeWordList__TpxWordMan(HGTpxWordMan, ListType='word', ReadNum=-1):
    HGTopicList_result = []

    if(HGTpxWordMan == None): 
        return HGTopicList_result
    
    #HGTopicHeader = HGTpxWordMan['header']
    HGTopicList = HGTpxWordMan['list']
    ReadCnt = 0
    RealReadCnt = 0
    for wi, hgtopic in enumerate(HGTopicList):
        #=hgtopic_len = len(hgtopic)
        #-------
        # format: ['주제어', '빈도', '문단ID', '문장ID']
        #-------
        if(ListType=='word'):
            HGTopicList_result.append(hgtopic[0])
            RealReadCnt += 1

        ###            
        ReadCnt += 1
        if(ReadNum > 0): # 읽을 개수 검사
            if(ReadCnt >= ReadNum):
                break;
    #
    #=print('RealReadCnt:', RealReadCnt)
    #
    return HGTopicList_result

def MakeWordDict__TpxWordMan(HGTpxWordMan, ReadNum=-1):
    TopicWordList = MakeWordList__TpxWordMan(HGTpxWordMan, ListType='word', ReadNum=ReadNum)
    TopicWordDict = GetWordDictList_WordList(TopicWordList)
    return TopicWordDict

def HGTpxWordMan_GetFile(filename, encoding='utf-8', ReadNum=-1, PrintTextFlag = False):
    HGTpxWordMan = GetHGTpxWordMan_TpxFile(filename, encoding, ReadNum, PrintTextFlag)
    return HGTpxWordMan

def GetHGTpxWordMan_TpxFile(filename, encoding='utf-8', ReadNum=-1, PrintTextFlag = False):
    from pathlib import Path

    HGTopicList = []
    TopicHeader = None

    #
    if(type(filename) == str):
        filename = Path(filename)
    if filename.is_file():
        if filename.exists():pass
        else: return HGTopicList
    else:
        print("file not found: %s" %filename)
        return HGTopicList

    file = open(filename, 'r', encoding=encoding)

    ReadCnt = 0
    RealReadCnt = 0
    while True:
        try:
            line = file.readline()
            if not line: 
                break
            if(PrintTextFlag == True): 
                print(line)

            line = line.strip() # 양끝 공백문자 지움
            if(len(line) > 0):
                #-if(line != None): HGTopicList.append(line)
                word_tok = line.split('\t')
                if(word_tok != None): 
                    # format: ['주제어', '빈도', '문단ID', '문장ID']
                    if(ReadCnt == 0): # 맨 처음 읽음
                        TopicHeader = word_tok
                    else:
                        HGTopicList.append(word_tok)
                    #
                    RealReadCnt += 1
        except UnicodeDecodeError as UDError:
            print('[',filename,']', '\n', (ReadCnt + 1), 'line ', UDError)
            pass

        ###            
        ReadCnt += 1
        if(ReadNum > 0): # 읽을 개수 검사
            if(ReadCnt >= ReadNum):
                break
    ###        
    file.close()
    ###
    #=print('RealReadCnt:', RealReadCnt, f'({filename})')
    ###
    HGTpxWordMan = {
        'header': TopicHeader,
        'list': HGTopicList,
    }
    return HGTpxWordMan

def GetHGTpxText_TpxFile(filename, encoding='utf-8', IgnoreError=False, ReadNum=-1, PrintTextFlag = False):
    from pathlib import Path
    #-------------------
    # 결과를 텍스트로 반환
    #-------------------
    HGTopicText = ""

    if(type(filename) == str):
        filename = Path(filename)
    if filename.is_file():
        if filename.exists():pass
        else: return HGTopicText
    else:
        print("file not found: %s" %filename)
        return HGTopicText

    errors = None
    if(IgnoreError == True):
        errors = 'ignore'
    file = open(filename, 'r', encoding=encoding, errors=errors)

    TopicHeader = None
    ReadCnt = 0;
    RealReadCnt = 0
    while True:
        try:
            line = file.readline()
            if not line: 
                break
            if(PrintTextFlag == True): 
                print(line)

            line = line.strip() # 양끝 공백문자 지움
            if(len(line) > 0):
                #-if(line != None): HGTopicList.append(line)
                word_tok = line.split('\t')
                if(word_tok != None): 
                    # format: ['주제어', '빈도', '문단ID', '문장ID']
                    if(ReadCnt == 0): # 맨 처음 읽음
                        TopicHeader = word_tok
                    else:
                        HGTopicText += word_tok[0] # '주제어'
                        HGTopicText += '\t'
                    #
                    RealReadCnt += 1
            else: # 내용은 없고 줄바꿈만 있는 경우
                if(len(HGTopicText) > 0): # 앞에 실제 텍스트(주제어)가 하나라도 있을 때만 줄바꿈을 넣어준다.
                    HGTopicText += '\n' #
        except UnicodeDecodeError as UDError:
            print('[',filename,']', '\n', (ReadCnt + 1), 'line ', UDError)
            pass
        ###            
        ReadCnt += 1
        if(ReadNum > 0): # 읽을 개수 검사
            if(ReadCnt >= ReadNum):
                break
    ###        
    file.close()
    ###
    #=print('RealReadCnt:', RealReadCnt, f'({filename})')
    ###
    return HGTopicText

def GetWordList_TpxFile(filename, encoding='utf-8', IgnoreError=False, ReadNum=-1, PrintTextFlag = False):
    from pathlib import Path

    real_filename = Path(filename)
    HGTopicText = GetHGTpxText_TpxFile(real_filename, encoding=encoding, 
                    IgnoreError=IgnoreError, ReadNum=ReadNum, PrintTextFlag=PrintTextFlag)
    #print(HGTopicText)

    HGTopicText.rstrip() # 문서 끝쪽에 있는 공백문자 지운다.
    #print(HGTopicText)

    HGTopicText = HGTopicText.split()
    #print(HGTopicText)

    return HGTopicText

def MakeWordDicts_TpxWordFilePath(FilePath, encoding='utf-8', ReadNum=-1, PrintFilename=False):
    import glob
    from pathlib import Path

    TopicWordDicts = []

    for filename in glob.glob(FilePath):
        #print(filename)
    
        filename = Path(filename)
        if(PrintFilename == True):
            print('[FILE] ', filename)

        TopicWordDict = MakeWordDict__TpxWordFile(filename, encoding=encoding, ReadNum=ReadNum)
        if(len(TopicWordDict) <= 0):
            print("word dict : 0")
        TopicWordDicts.append(TopicWordDict)

    #print ('len :', len(TopicWordDicts))
    return TopicWordDicts

def MakeWordDict__TpxWordFile(filename, encoding='utf-8', ReadNum=-1, PrintTextFlag = False):
    TopicWordDict = {}

    HGTpxWordMan = GetHGTpxWordMan_TpxFile(filename, encoding=encoding, ReadNum=ReadNum, PrintTextFlag=PrintTextFlag)
    if(len(HGTpxWordMan) <= 0):
        return TopicWordDict

    TopicWordDict = MakeWordDict__TpxWordMan(HGTpxWordMan)
    return TopicWordDict

def MakeWordDicts_TpxWordFileList(FileList, encoding='utf-8', ReadNum=-1, PrintFilename=False):
    '''
    return format:
    [
    [{'word': '2도', 'freq': 1, 'len': 2, 'script_num': 2}, ...]
    [{'word': '1', 'freq': 1, 'len': 1, 'script_num': 1}, ...]
    ...
    ]
    '''
    from pathlib import Path

    TopicWordDicts = []

    FileList_len = len(FileList)
    #print('len :', FileList_len)
    
    for i in range(0, FileList_len):
        filename_i = FileList[i]
        filename_i = filename_i.strip() # 양끝 공백문자 지움
        if(len(filename_i) <= 0):
            continue

        filename_i = Path(filename_i)
        if(PrintFilename == True):
            print('[FILE] ', filename_i)

        TopicWordDict = MakeWordDict__TpxWordFile(filename_i, encoding=encoding, ReadNum=ReadNum)
        if(len(TopicWordDict) <= 0):
            print("word dict : 0")
        TopicWordDicts.append(TopicWordDict)

    #print ('len :', len(TopicWordDicts))
    return TopicWordDicts

def MakeWordDicts_TpxPath(pathname, encoding='utf-8', ReadNum=-1, PrintFilename=False):
    if(PrintFilename == True):
        print('pathname:', pathname)
    
    #
    TopicWordDicts = []

    #
    import glob
    for filename in glob.glob(pathname):
        if(PrintFilename == True):
            print('[FILE] ', filename)

        TopicWordDict = MakeWordDict__TpxWordFile(filename, encoding=encoding, ReadNum=ReadNum)
        if(len(TopicWordDict) <= 0):
            print(f'{filename} :', " word dict : 0")
        TopicWordDicts.append(TopicWordDict)

    #print ('len :', len(TopicWordDicts))
    return TopicWordDicts

#-----
#-----
def GetDictFreq_WordFreqText(filename, encoding='utf-8', IgnoreError=False, ReadNum=-1, PrintTextFlag = False):
    from pathlib import Path
    #
    DictFreq = {}
    if(type(filename) == str):
        filename = Path(filename)
    if filename.is_file():
        if filename.exists():pass
        else: return DictFreq
    else:
        print("file not found: %s" %filename)
        return DictFreq

    errors = None
    if(IgnoreError == True):
        errors = 'ignore'
    file = open(filename, 'r', encoding=encoding, errors=errors)

    ReadCnt = 0;
    while True:
        try:
            line = file.readline()
            if not line: 
                break
            if(PrintTextFlag == True): 
                print(line)

            line = line.strip() # 양끝 공백문자 지움
            if(len(line) > 0):
                #-if(line != None): HGTopicList.append(line)
                word_tok = line.split('\t')
                if(word_tok != None): 
                    if(len(word_tok) == 3): # format: ['순서', '주제어', '빈도']
                        TopicWord = word_tok[1]
                        Freq = word_tok[2]
                    elif(len(word_tok) == 2): # format: ['주제어', '빈도']
                        TopicWord = word_tok[0]
                        Freq = word_tok[1]
                    else: # 형식이 맞지 않는 경우
                        break
                    DictFreq[TopicWord] = int(Freq)
            else: # 내용은 없고 줄바꿈만 있는 경우
                pass
        except UnicodeDecodeError as UDError:
            print('[',filename,']', '\n', (ReadCnt + 1), 'line ', UDError)
            pass
        ###            
        ReadCnt += 1
        if(ReadNum > 0): # 읽을 개수 검사
            if(ReadCnt >= ReadNum):
                break
    ###        
    file.close()
    ###
    return DictFreq

def GetDictFreq_WordFreqFile2(filename, encoding='utf-8'):
    '''# format: ['주제어', '빈도'] 처리용'''
    # format: ['주제어', '빈도'] 처리 전용으로 상대적으로 짧은 길이로 만든 함수.
    from pathlib import Path
    #
    DictFreq = {}
    if(type(filename) == str):
        filename = Path(filename)
    if filename.is_file():
        if filename.exists():
            pass
        else: 
            return DictFreq
    else:
        print("file not found: %s" %filename)
        return DictFreq
    #
    file = open(filename, 'r', encoding=encoding)
    #
    ReadCnt = 0;
    while True:
        try:
            line = file.readline()
            if not line: 
                break
            #
            line = line.strip() # 양끝 공백문자 지움
            if(len(line) <= 0): # 내용은 없고 줄바꿈만 있는 경우
                continue
            #
            word_tok = line.split('\t')
            if(word_tok is not None): 
                if(len(word_tok) == 2): # format: ['주제어', '빈도']
                    TopicWord = word_tok[0]
                    Freq = word_tok[1]
                else: # 형식이 맞지 않는 경우
                    break
                DictFreq[TopicWord] = int(Freq)
        except UnicodeDecodeError as UDError:
            print('[',filename,']', '\n', (ReadCnt + 1), 'line ', UDError)
            pass
        ###
        ReadCnt += 1
    ###        
    file.close()
    ###
    return DictFreq

#-----
#-----
def MakeDictFreq__TpxWordFile(filename, encoding='utf-8', ReadNum=-1, PrintTextFlag = False):
    #---
    from hgdict import GetDictFreq__WordList
    #---
    DictFreq = {}
    #---
    HGTpxWordMan = GetHGTpxWordMan_TpxFile(filename, encoding=encoding, ReadNum=ReadNum, PrintTextFlag=PrintTextFlag)
    if(len(HGTpxWordMan) <= 0):
        return DictFreq
    #---
    TopicWordList = MakeWordList__TpxWordMan(HGTpxWordMan, ListType='word', ReadNum=ReadNum)
    DictFreq = GetDictFreq__WordList(TopicWordList)
    #
    return DictFreq

def MakeDictFreqs_TpxWordFileList(FileList, encoding='utf-8', ReadNum=-1, PrintFilename=False):
    from pathlib import Path
    #=print(f'FileList Num :', len(FileList))

    DictFreqs = []
    for fi, filename_i in enumerate(FileList):
        filename_i = filename_i.strip() # 양끝 공백문자 지움
        if(len(filename_i) <= 0):
            continue
        #
        filename_i = Path(filename_i)
        if(PrintFilename == True):
            print('[FILE] ', filename_i)
        #
        DictFreq = MakeDictFreq__TpxWordFile(filename_i, encoding=encoding, ReadNum=ReadNum)
        #=if(len(DictFreq) <= 0):
        #=    print("word dict : 0")
        DictFreqs.append(DictFreq)

    #print ('len :', len(DictFreqs))
    return DictFreqs

#-----
#-----
def ReadBookSelf__TpxPath(pathname, is_state = False, encoding='utf-8'):
    import glob
    from pathlib import Path
    
    data: List[HGBookSelf] = []
    for filename in glob.glob(pathname):
        #print(filename)
    
        real_filename = Path(filename)
        HGTopicText = GetHGTpxText_TpxFile(real_filename, encoding=encoding)
        #print(HGTopicText)

        HGTopicText.rstrip() # 문서 끝쪽에 있는 공백문자 지운다.
        #print(HGTopicText)

        if(len(HGTopicText) > 0):
            data.append(HGBookSelf(filename, HGTopicText, is_state))
    
    return data
    
def ReadBookSelf__TpxFile(filename, is_state = False, encoding='utf-8'):
    from pathlib import Path

    return_data: List[HGBookSelf] = []
    #print(filename)

    real_filename = Path(filename)
    HGTopicText = GetHGTpxText_TpxFile(real_filename, encoding=encoding)
    #print(HGTopicText)

    HGTopicText.rstrip() # 문서 끝쪽에 있는 공백문자 지운다.
    #print(HGTopicText)

    if(len(HGTopicText) > 0):
        return_data.append(HGBookSelf(filename, HGTopicText, is_state))

    return return_data

def ReadBookSelf__TpxFileList(FileList, is_state = False, encoding='utf-8'):
    from pathlib import Path
    #print('FileList Num :', len(FileList))
   
    data: List[HGBookSelf] = []
    for fi, filename in enumerate(FileList):
        #=print(f'[{fi}] filename:', filename)
        real_filename = Path(filename)
        HGTopicText = GetHGTpxText_TpxFile(real_filename, encoding=encoding)
        #print(HGTopicText)

        HGTopicText.rstrip() # 문서 끝쪽에 있는 공백문자 지운다.
        #print(HGTopicText)

        if(len(HGTopicText) > 0):
            data.append(HGBookSelf(filename, HGTopicText, is_state))
    #    
    return data
    
def ReadBookSelf__TxtPath(pathname, is_state = False, encoding='utf-8'):
    import glob
    from pathlib import Path
    
    return_data: List[HGBookSelf] = []
    for filename in glob.glob(pathname):
        #print(filename)
    
        real_filename = Path(filename)
        file = open(real_filename, 'r', encoding=encoding)
        try:
            lines = file.readlines()
        except UnicodeDecodeError: #'cp949' codec can't decode byte 0xeb in position 1:
            file.close()
            file = open(real_filename, 'r', encoding='utf8') # 'utf8'로 다시 읽어본다.
            lines = file.readlines()
        file.close()

        #print(lines)
        textall = ''.join(lines)

        if(len(lines) > 0):
            return_data.append(HGBookSelf(filename, textall, is_state))
    
    return return_data
    
def ReadBookSelf__TxtFile(filename, is_state = False, encoding='utf-8'):
    from pathlib import Path
    
    return_data: List[HGBookSelf] = []
    #print(filename)

    real_filename = Path(filename)
    file = open(real_filename, 'r', encoding=encoding)
    lines = file.readlines()
    #print(lines)
    textall = ''.join(lines)

    if(len(lines) > 0):
        return_data.append(HGBookSelf(filename, textall, is_state))

    return return_data

def PrintBookSelf_DocList(BookSelf, Tilte=None):
    print()
    if(Tilte != None):
        print(f'{Tilte}:', end='');
    print(len(BookSelf))
    for bi, bd in enumerate(BookSelf):
        print(f'{bi}: {bd.doc}')
    print(), print(), print()

def PrintBookSelf_Text__DocInxList(BookSelf, DocInxList, Tilte=None, HeadLineNum=None):
    print()
    if(Tilte != None):
        print(f'{Tilte}:', end='');
    print(len(DocInxList))

    textlist = [book.text for book in BookSelf]
    for di in DocInxList:
        print()
        print('\n++++=++++=++++=++++=++++=++++=++++=++++=++++=++++=\n')
        print (F'{(di+1)} :')
        if((HeadLineNum != None) and (HeadLineNum > 0)):
            curtext_lines = textlist[di].splitlines()
            curtext_lines = [li.strip() for li in curtext_lines]
            curtext_lines = [li for li in curtext_lines if len(li) > 0]
            curtext_lines = curtext_lines[:HeadLineNum]
            print('\n'.join(curtext_lines))  
        else:
            print (textlist[di])
        print()

def GetBookSelf_TextList__DocInxList(BookSelf, DocInxList, LineNum=0, NonMargin=False):
    TextList = []
    for DocInx in DocInxList:
        if(DocInx < 0): # DocInx : zoro-base
            assert(False)
            TextList = None
            break
        else:
            if(LineNum >= 1):
                Texts = BookSelf[DocInx].text.splitlines()
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
                Text = BookSelf[DocInx].text
            TextList.append(Text)
    return TextList

def load_textlist__txtpath(pathname, encoding='utf-8', DebugPrint=False):
    #=encoding='utf-8' 
    #=encoding='euc-kr' # 표준완성형이라서 범위를 벗어난 통합완성형 코드가 있으면 오류 발생하여 읽지 못한다.
    #=encoding='cp949'
    txt_list = ReadBookSelf__TxtPath(pathname, is_state = False, encoding=encoding)
    if(DebugPrint == True):
        print('files:', len(txt_list), pathname)
    #
    textlist = [book.text for book in txt_list]
    return textlist

class HGTest(TestCase):

    def setUp(self):
        self.a = 'test setup'

    def test_run(self):
        print('test: ok')

if __name__ == '__main__':
    main()



