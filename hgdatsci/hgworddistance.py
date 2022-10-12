#=from hgalign import HGAlign, RunSeqAlign
#---------------------------------
#---------------------------------
import hgsysinc
from hgdistance import GetDictFreq_Tanimoto_Distance, GetEditDistance
from hgkbd import (
    HGTransString2EngString, HGTransString2KBDJamo,
    HGGetSyllable_JaumMoumString,
    HGTransChoJungJongJamo2KBDJamo,
)
from hgunicode import hgGetChoJungJongString

#-----
#-----
import inspect
 
def _lline_(): # 다른 라이브러리와 함수 이름이 겹치지 않도록 'l'자를 추가
   return inspect.currentframe().f_back.f_lineno

#
class HGEditDistance:
    def __init__(self):
        self._init_ = True
            
    def _test(self):
        return True

#---------------------------------
#---------------------------------
__match_score__ = 2
__no_match_score__ = (-1)
__gab_char__ = '-'

#================================
#================================
#================================
def TestEditDistance(base_v, comp_v, DebugPrint=False):
    import importlib
    exist_flag = importlib.util.find_spec("hgalign") is not None
    if(exist_flag):
        import hgalign
        EditSimilaritys = hgalign.RunSeqAlign(base_v, comp_v, DebugPrint=DebugPrint)
        print('\n EidtSimilarity:')
        # format: [[total_score, BaseStr, CompStr],...]
        for i, Similarity in enumerate(EditSimilaritys):
            print(f'[{i}] ({Similarity[0]}) <{Similarity[1]} :: {Similarity[2]}>')
        print()

    Distance = GetWordDistance_Leven(base_v, comp_v, DebugPrint=DebugPrint)
    print('EditDistance[L]:', Distance, f'({base_v},{comp_v})')

    Distance = GetWordDistance_Jacard(base_v, comp_v, DebugPrint=DebugPrint)
    print('EditDistance[J]:', Distance, f'({base_v},{comp_v})')

    Distance = GetWordDistance_Tanimoto(base_v, comp_v)
    print('EditDistance[T]:', Distance, f'({base_v},{comp_v})')

    Distance = GetWordDistance_Cosine(base_v, comp_v, DebugPrint=DebugPrint)
    print('EditDistance[C]:', round(Distance, 3), f'({base_v},{comp_v})')
    
    print()

def TestEditDistance_Jamo3(base_v, comp_v, DebugPrint=False, ShowJamo=False, SeqAlign=False):
    base_j = hgGetChoJungJongString(base_v)
    comp_j = hgGetChoJungJongString(comp_v)

    if(SeqAlign==True):
        import importlib
        exist_flag = importlib.util.find_spec("hgalign") is not None
        if(exist_flag):
            from hgunicode import hgSyllableStr__Jamo3Str
            from 자모 import 자모_음절변환
            import hgalign
            
            EditSimilaritys = hgalign.RunSeqAlign(base_j, comp_j, DebugPrint=DebugPrint)
            # format: [[total_score, BaseStr, CompStr],...]
            print()
            print(f'EidtSimilarity: {base_v} ^^^ {comp_v}')
            for i, Similarity in enumerate(EditSimilaritys):
                #=hgstring_1 = 자모_음절변환(Similarity[1]) # 자모_음절변환() 옛한글까지 처리하므로 무겁다.
                #=hgstring_2 = 자모_음절변환(Similarity[2]) # 자모_음절변환() 옛한글까지 처리하므로 무겁다.
                hgstring_1 = hgSyllableStr__Jamo3Str(Similarity[1])
                hgstring_2 = hgSyllableStr__Jamo3Str(Similarity[2])
                #-----------
                # 아래는 사용하지 않는다.
                # 부분적으로 유사한 것을 뽑지 않는데 부분 유사어를 뽑지 않는 것이 반드시 좋은 것은 아니다.
                #-----------
                #=__gab_char__ = '-'
                #=AlignWord = hgstring_1.replace(__gab_char__,'')
                #=if(base_v == AlignWord): 
                #=    # 기준 단어가 변형된 것은 안 된다.(자모에서는 기준 단어가 변경되기도 한다.)
                #=    print(f'[{i}] ({Similarity[0]}) <{hgstring_1} :: {Similarity[2]} ({hgstring_2})>')
                #=else:
                #=    print(f'<No Match Base>[{i}] ({Similarity[0]}) <{hgstring_1} :: {Similarity[2]} ({hgstring_2})>')
                #-----------
                print(f'[{i}] ({Similarity[0]}) <{hgstring_1} :: {Similarity[2]} ({hgstring_2})>')
    if(ShowJamo == True):
        # 초,중,종 자모 글자는 글자가 밀려서 보이는 경우가 있으므로 밀리지 않도록 채움문자로 보충해서 출력한다.
        from 자모 import 자모열_채움문자보충_음절변환
        base_fill = 자모열_채움문자보충_음절변환(base_j)
        comp_fill = 자모열_채움문자보충_음절변환(comp_j)
        print(f"음절\t초중종 자모\t초중종 자모 길이\t초중종 자모 채움문자")
        print(f"{base_v}\t{base_j}\t{len(base_j)}\t{base_fill}")
        print(f"{comp_v}\t{comp_j}\t{len(comp_j)}\t{comp_fill}")
    print('EditDistance:', GetEditDistance(base_j, comp_j, DebugPrint=DebugPrint))

def TestEditDistance_Jamo2(base_v, comp_v, DebugPrint=False, ShowJamo=False, SeqAlign=False):
    base_j = HGTransString2KBDJamo(base_v)
    comp_j = HGTransString2KBDJamo(comp_v)

    if(SeqAlign==True):
        import importlib
        exist_flag = importlib.util.find_spec("hgalign") is not None
        if(exist_flag):
            import hgalign
            
            EditSimilaritys = hgalign.RunSeqAlign(base_j, comp_j, DebugPrint=DebugPrint)
            # format: [[total_score, BaseStr, CompStr],...]
            print()
            print(f'EidtSimilarity: {base_v} ^^^ {comp_v}')
            for i, Similarity in enumerate(EditSimilaritys):
                hgstring_1 = HGGetSyllable_JaumMoumString(Similarity[1])
                hgstring_2 = HGGetSyllable_JaumMoumString(Similarity[2])
                #-----------
                # 아래는 사용하지 않는다.
                # 부분적으로 유사한 것을 뽑지 않는데 부분 유사어를 뽑지 않는 것이 반드시 좋은 것은 아니다.
                #-----------
                #=__gab_char__ = '-'
                #=AlignWord = hgstring_1.replace(__gab_char__,'')
                #=if(base_v == AlignWord): 
                #=    # 기준 단어가 변형된 것은 안 된다.(자모에서는 기준 단어가 변경되기도 한다.)
                #=    print(f'[{i}] ({Similarity[0]}) <{hgstring_1} :: {Similarity[2]} ({hgstring_2})>')
                #=else:
                #=    print(f'<No Match Base>[{i}] ({Similarity[0]}) <{hgstring_1} :: {Similarity[2]} ({hgstring_2})>')
                #-----------
                print(f'[{i}] ({Similarity[0]}) <{hgstring_1} :: {Similarity[2]} ({hgstring_2})>')
    if(ShowJamo == True):
        base_jamo = HGGetSyllable_JaumMoumString(base_j)
        comp_jamo = HGGetSyllable_JaumMoumString(comp_j)
        print(f"{base_v}\t{base_j}\t{len(base_j)}")
        print(f"{comp_v}\t{comp_j}\t{len(comp_j)}")
    #
    print('EditDistance:', GetEditDistance(base_j, comp_j, DebugPrint=DebugPrint))

def PrintVocabulary(Vocabulary, PrintNum=0, LeadingString='', PrintGuide=False):
    from hgdict import PrintDictFreq
    PrintDictFreq(Vocabulary, PrintNum=PrintNum, 
        LeadingString=LeadingString, PrintGuide=PrintGuide)

def FindDisWord_Vocabulary(UserWord, 
    DictFreqList, # 검색어 사전(format1:{word:freq}, format2:{word:{doc-id:freq}}
    DisNum=10, # 찾을 개수
    DisMax=3,  # 편집 거리 한계값(이 값보다 크면 사용하지 않는다.)
    LowerCasifyFlag=False, # 대문자롤 소문자로 변환
    FullwidthAsciiTrans=False, # 전각 영문자를 아스키 영문자로 변환
    HalfJamoTrans=False, # HalfJamoTrans: 반각 자모를 두벌식 자모로 변환
    ChoJungJongJamoTrans=False, # ChoJungJongJamoTrans: 초중종 자모를 두벌식 자모로 변환
    DebugPrint=False,
    ):
    """
    DictFreqList: 검색어 사전(format1:{word:freq}, format2:{word:{doc-id:freq}}
    DisNum=10: 찾을 개수
    DisMax=3: 편집 거리 한계값(이 값보다 크면 사용하지 않는다.)
    LowerCasifyFlag: 대문자롤 소문자로 변환
    FullwidthAsciiTrans: 전각 영문자를 아스키 영문자로 변환
    HalfJamoTrans:반각 자모를 두벌식 자모로 변환
    ChoJungJongJamoTrans: 초중종 자모를 두벌식 자모로 변환
    
    검색어 사전(DictFreqList)이 두벌식 자모가 아니면 
    {HalfJamoTrans, ChoJungJongJamoTrans} 변수를 적용할 경우에 소용이 없다.
    """
    #========================
    # 영문자 확장 처리
    #========================
    if(FullwidthAsciiTrans == True): # 전각 영문자를 (반각) 영문자(아스키)로 변환
        from hgunicode import HGGetAsciiString__FullwidthAsciiString
        AsciiString = HGGetAsciiString__FullwidthAsciiString(UserWord)
        #----- 변환 결과를 확인할 필요 없음. 바뀐 것이 없으면 원래 것을 반환하기 때문.
        #=if(UserWord != AsciiString):
        #=    UserWord = AsciiString
        #-----
        UserWord = AsciiString
    #
    if(LowerCasifyFlag == True): # 대문자롤 소문자로 통합하기 위해서 소문자 변환
        UserWord = UserWord.lower() # 대문자롤 소문자로 통합하기 위해서 소문자 변환
    #========================
    # 한글 확장 처리
    #========================
    if(HalfJamoTrans == True): # HalfJamoTrans: 반각 자모를 두벌식 자모로 변환
        from hgunicode import HGGetCompatibleJamoString__HalfJamoString
        KBDJamoString = HGGetCompatibleJamoString__HalfJamoString(UserWord)
        #----- 변환 결과를 확인할 필요 없음. 바뀐 것이 없으면 원래 것을 반환하기 때문.
        #=if(UserWord != KBDJamoString):
        #=    UserWord = KBDJamoString
        #-----
        UserWord = KBDJamoString
    if(ChoJungJongJamoTrans == True): # ChoJungJongJamoTrans: 초중종 자모를 두벌식 자모로 변환
        KBDJamoString = HGTransChoJungJongJamo2KBDJamo(UserWord)
        #----- 변환 결과를 확인할 필요 없음. 바뀐 것이 없으면 원래 것을 반환하기 때문.
        #=if(UserWord != KBDJamoString):
        #=    UserWord = KBDJamoString
        #-----
        UserWord = KBDJamoString
    #========================
    #========================
    #========================
    #
    UserWordLen = len(UserWord)
    DisWord = {}
    for inx, DictWord in enumerate(DictFreqList):
        #
        if(DebugPrint == True):
            if(inx > 0):
                modval = (inx % 500)
                if(modval == 0):
                        print(inx,'...')
        #=if(inx > 1500): 
        #=    break

        #=print(inx, ':', DictWord)

        #=# temp
        #=if(len(DictWord) <= len(UserWord)): # 임시로 검색어보다 큰 것만 허용
        #=    continue

        #--------------------------
        EditDistance = GetEditDistance(UserWord, DictWord)
        #=print('EditDistance:', EditDistance)

        # 편집 거리가 검색어 길이와 같으면 완전히 다른 관련 없는 단어다.
        if(EditDistance >= UserWordLen): # 편집 거리가 검색어 길이와 같으면 완전히 다른 관련 없는 단어다.
            continue
        # 편집 거리 최대 한계 검사 -  편집 거리 최대 한계(3)를 벗어나면 어색하다.
        if((DisMax > 0) and (EditDistance > DisMax)): # 편집 거리 최대 한계(3)를 벗어나면 어색하다.
            continue # 이 함수 밖에서 (DisMax=0)으로 바꿔서 전부 출력하는 경우 있음
        #
        if(type(DictFreqList[DictWord]) == int): # format1: {word:freq}
            DictWord_DocNum = DictFreqList[DictWord]
        else: # farmat2: {word:{doc-id:freq}}
            DictWord_DocNum = len(DictFreqList[DictWord])
        DisWord[DictWord] = (EditDistance, DictWord_DocNum) # (편집거리, 단어-문서수)
        if(DebugPrint == True):
            print(DictWord, ':', DictWord_DocNum)

        if(DisNum > 0): # 편집거리 단어가 많으면 (DisNum * 5) 크면 중간 삭제한다.
            if(len(DisWord) > (DisNum * 5)): # 단어 등록 제한 검사
                DelDictDistance(DisWord, ByOrderHigh=False, DictNum=DisNum)
    #
    if(DisNum > 0):
        if(len(DisWord) > DisNum): # 단어 등록 제한 검사
            DelDictDistance(DisWord, ByOrderHigh=False, DictNum=DisNum)
    #
    return DisWord

def DelDictDistance(DictDistance, ByOrderHigh=True, DictNum=0):
    # filtering
    if(len(DictDistance) <= 0):
        return
    if(DictNum > 0): # 단어 개수 제한
        if(len(DictDistance) <= DictNum):
            return

    # format: ('amendment', (11, 8))  ('word', (거리값, 단어-문서수))
    if(ByOrderHigh == True): # [맨 뒤] 가장 작은 값 지우기
        DictDistance_Sort = sorted(DictDistance.items(), key=lambda kv: -kv[1][0]) # by high value(Distance)
    else: # [맨 뒤] 가장 큰 값 지우기
        DictDistance_Sort = sorted(DictDistance.items(), key=lambda kv: kv[1][0]) # by low value(Distance)

    if(DictNum > 0): # 단어 개수 제한
        DictNum_word = None
        if(len(DictDistance_Sort) > DictNum):
            DictNum_word = DictDistance_Sort[DictNum - 1] # 지정한 위치 단어

        while(True):
            if(len(DictDistance_Sort) <= DictNum):
                break

            LastDistanceWord = DictDistance_Sort[len(DictDistance_Sort) - 1]
            #=print(LastDistanceWord)

            if(DictNum_word != None):
                # 단어 개수 제한 위치의 단어가 마지막 단어의 거리가 같으면 지우지 않고 끝낸다.
                #=print(DictNum_word)
                #=print(LastDistanceWord)
                if(DictNum_word[1][0] == LastDistanceWord[1][0]): # format: ('imprudent', (1, 1))
                    break

            #
            del DictDistance[LastDistanceWord[0]] # format: ('imprudent', (1, 1))
            del DictDistance_Sort[len(DictDistance_Sort) - 1]

    else: # 단어 개수 제한이 없으면 1개만 지운다.
        LastDistanceWord = DictDistance_Sort[len(DictDistance_Sort) - 1]
        #=print(LastDistanceWord)
        del DictDistance[LastDistanceWord[0]] # format: ('imprudent', (1, 1))

#================================
#================================
#================================
def GetWordDistance_Jacard(BaseSeq, CompSeq, DebugPrint=False): # Jacard Similarity
    #--------------------------------------------
    # https://en.wikipedia.org/wiki/Jaccard_index
    #--------------------------------------------
    BaseSet = set(BaseSeq)
    CompSet = set(CompSeq)
    
    InterSec = BaseSet.intersection(CompSet)
    UnionSec = BaseSet.union(CompSet)
    if(DebugPrint == True):
        print(f'InterSec ({len(InterSec)}):', InterSec)
        print(f'UnionSec ({len(UnionSec)}):', UnionSec)
    #
    Similarity = len(InterSec) / len(UnionSec)
    Distance = 1 - Similarity

    # test
    __strict_checking__ = False
    #=__strict_checking__ = True
    if(__strict_checking__ == True):
        from hgdict import GetDictFreq__WordList
        from hgdistance import GetDictFreq_Jacard_Distance
        BaseCharList = [c for c in BaseSeq]
        CompCharList = [c for c in CompSeq]
        DictFreqBase = GetDictFreq__WordList(BaseCharList)
        DictFreqComp = GetDictFreq__WordList(CompCharList)
        if(GetDictFreq_Jacard_Distance(DictFreqBase, DictFreqComp) != Distance):
            assert False

    return Distance

def GetWordDistance_Tanimoto(BaseSeq, CompSeq, DebugPrint=False): # Tanimoto coefficient
    #--------------------------------------------
    # https://en.wikipedia.org/wiki/Jaccard_index
    #
    # @@@ Tanimoto 거리는 지문 유사도 검사에 효과적이다.
    # Tanimoto 거리는 Jacard 거리에 빈도 가중치를 부여한 것이다.
    # Why is Tanimoto index an appropriate choice for fingerprint-based similarity calculations
    # https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4456712/pdf/13321_2015_Article_69.pdf
    #--------------------------------------------
    from hgdict import GetDictFreq_Char__String
    DictFreqBase = GetDictFreq_Char__String(BaseSeq)
    DictFreqComp = GetDictFreq_Char__String(CompSeq)
    if(DebugPrint == True):
        print(DictFreqComp)
        print(f"{BaseSeq}:{DictFreqBase}")
        print(f"{CompSeq}:{DictFreqComp}")
    #
    Distance = GetDictFreq_Tanimoto_Distance(DictFreqBase, DictFreqComp, DebugPrint=DebugPrint)
    return Distance

def GetWordDistance_Cosine(BaseSeq, CompSeq, DebugPrint=False):
    from hgdict import GetDictFreq_Char__String
    from hgdistance import GetDictFreq_CosDistance
    #---
    DictFreqBase = GetDictFreq_Char__String(BaseSeq)
    DictFreqComp = GetDictFreq_Char__String(CompSeq)
    if(DebugPrint == True):
        print(DictFreqBase)
        print(DictFreqComp)
    Distance = GetDictFreq_CosDistance(DictFreqBase, DictFreqComp)
    return Distance

def GetWordDistance_Leven(BaseSeq, CompSeq, DebugPrint=False): # Jacard Similarity
    Distance = GetEditDistance(BaseSeq, CompSeq, DebugPrint=DebugPrint)
    return Distance

#================================
#================================
#================================
# 한글 처리 옵션
__Hng_AsItIs__ = 1 # 한글: 변형없이 그대로 처리(음절)
__Hng_2_Jamo__ = 2 # 한글: 키보드(두벌식) 자모로 처리
__Hng_2_Eng__ = 3 # 한글: 영문자로 처리
__Hng_2_Jamo3__ = 4 # 한글: 초중종 자모로 처리(사전식) # 초성,중성,종성 방식으로 사전식으로 처리
#============================

def MakeStringNGram(BaseSeq, NGram=1, MoreThan=False, EditDistanceMode=False):
    NGramList = []
    BaseLen = len(BaseSeq)
    for i in range(BaseLen + 1 - NGram):
        NGramWord = BaseSeq[i:(i + NGram)] # [NGram]길이만큼만 분리
        NGramList.append(NGramWord)
        if(MoreThan == True): # [NGram]길이부터 모두 분리
            # MoreThan ex: : N(3) abcde = abc, _abcd_, _abcde_, bcd, _bcde_, cde
            j = 1
            while((i + NGram + j) <= BaseLen):
                EndPos = (i + NGram + j)
                NGramWord = BaseSeq[i:EndPos]
                NGramList.append(NGramWord)
                j += 1
    if(EditDistanceMode == True): 
        # 편집거리에서는 맨 앞에 길이가 충족되지 않은 짧은 조각도 추가한다.
        if((NGram >= 2) and (BaseLen >= NGram)):
            i = 1
            while(i < NGram):
                NGramWord = BaseSeq[0:NGram - i]
                NGramList.insert(0, NGramWord)
                i += 1
    #
    return NGramList

def GetEditDistance_NGram(BaseStr, CompStr, NGram=1, DebugPrint=False):
    BaseNgram = MakeStringNGram(BaseStr, NGram=NGram)
    CompNgram = MakeStringNGram(CompStr, NGram=NGram)
    EditDistance_Ngram = GetEditDistance(BaseNgram, CompNgram, DebugPrint=DebugPrint)
    return EditDistance_Ngram

def MakeNGramVocabulary__DictFreq(DictFreq, NGram=1, EngLow=True, 
    HngFmt=__Hng_AsItIs__):
    NGramVocabulary = {}
    AddNGramVocabulary__DictFreq(NGramVocabulary, 
        DictFreq, NGram=NGram, EngLow=EngLow, HngFmt=HngFmt)
    return NGramVocabulary

def AddNGramVocabulary__DictFreq(NGramVocabulary, DictFreq, 
    NGram=1, EngLow=True, 
    HngFmt=__Hng_AsItIs__):
    for i, CurWord in enumerate(DictFreq):
        WordFreq = DictFreq[CurWord]
        AddNGramVocabulary__WordWeight(NGramVocabulary, CurWord, 
            Weight=WordFreq, NGram=NGram, EngLow=EngLow, HngFmt=HngFmt)
        #=if(i >= 100):
        #=    break

def AddNGramVocabulary_Simple(NGramVocabulary, Word, RealWord=None, Weight=0, NGram=1):
    # N그램 처리용 단어(Word)와 출력을 위한 진짜 단어(RealWord)가 다른 경우에 {진짜 단어(RealWord)}값이 있다.
    if(RealWord == None): # 진짜 단어(RealWord)가 없으면 Word --> RealWord
        RealWord=Word
    #
    dic_ngram = MakeStringNGram(Word, NGram=NGram, MoreThan=True)
    for ngram_word in dic_ngram:
        if(NGramVocabulary.get(ngram_word) is None):
            NGramVocabulary[ngram_word] = []
        NGramItem = {'key':Word, 'word':RealWord, 'weight':Weight}
        NGramVocabulary[ngram_word].append(NGramItem)

def AddNGramVocabulary__WordWeight(NGramVocabulary, Word, 
    RealWord=None, Weight=0, NGram=1, EngLow=True, 
    HngFmt=__Hng_AsItIs__):
    # N그램 처리용 단어(Word)와 출력을 위한 진짜 단어(RealWord)가 다른 경우에 {진짜 단어(RealWord)}값이 있다.
    if(RealWord == None): # 진짜 단어(RealWord)가 없으면 Word --> RealWord
        RealWord=Word
    if(EngLow == True):
        Word = Word.lower() # 소문자 변환
    #
    AddNGramVocabulary_Simple(NGramVocabulary, Word, 
        RealWord=RealWord, Weight=Weight, NGram=NGram)

    #---------
    # 한글 변환
    #---------
    if(HngFmt == __Hng_AsItIs__): # 한글: 변형없이 그대로 처리
        pass #. 변형없이 그대로 사용
    elif(HngFmt == __Hng_2_Jamo__): # 한글: 두벌식(키보드) 자모로 처리
        #. [한글] ---> [두벌식(키보드) 자모]
        KBDJamoString = HGTransString2KBDJamo(Word)
        if(KBDJamoString != Word): # [한글]이 [두벌식(키보드) 자모]로 바뀔 때 달라진다.
            AddNGramVocabulary_Simple(NGramVocabulary, KBDJamoString, 
                RealWord=RealWord, Weight=Weight, NGram=NGram)
    elif(HngFmt == __Hng_2_Eng__): # 한글: 영문자로 처리
        #. [한글] ---> [영문자] (한국 ---> gksrnr) 입력 오류 해결
        dic_eng = HGTransString2EngString(Word)
        if(dic_eng != Word): # [한글]이 영문으로 바뀔 때 달라진다.
            AddNGramVocabulary_Simple(NGramVocabulary, dic_eng, 
                RealWord=RealWord, Weight=Weight, NGram=NGram)
    elif(HngFmt == __Hng_2_Jamo3__): # 한글: 초중종 자모로 처리(사전식)
        # 알고리즘 차원에서 추가한 것임, 초성,중성,종성(사전식) 알고리즘을 설명할 때만 사용
        #. [한글] ---> [초중종 자모]
        KBDJamo3String = hgGetChoJungJongString(Word)
        if(KBDJamo3String != Word): # [한글]이 [초중종 자모]로 바뀔 때 달라진다.
            AddNGramVocabulary_Simple(NGramVocabulary, KBDJamo3String, 
                RealWord=RealWord, Weight=Weight, NGram=NGram)
    else:
        assert False

def WeightNGramVocabulary(NGramVocabulary):
    for i, ngram_keyword in enumerate(NGramVocabulary):
        ngram_word_dict = NGramVocabulary[ngram_keyword]
        #=print(f'{ngram_keyword}:{ngram_word_dict}')
        # ngram_word_dict__format: [{'key': '(1997.7.23)', 'word': '(1997.7.23)', 'weight': 1},...]
        ngram_word_dict_sort = sorted(ngram_word_dict, key = lambda item: -item['weight']) # by high
        NGramVocabulary[ngram_keyword] = ngram_word_dict_sort
        #=print(f'{ngram_keyword}:{ngram_word_dict}')
        #=if(i >= 100):
        #=    break

def PrintNGramVocabulary_Save__20201001(NGramVocabulary, PrintNum=0, PrintVocabularyList=False):
    for i, ngkey in enumerate(NGramVocabulary):
        #=print(ngkey)
        print(f'{i+1}, {ngkey} ({len(NGramVocabulary[ngkey])}) :', end='')
        if(PrintVocabularyList == True):
            print(f'{NGramVocabulary[ngkey]}', end='')
        print()

        if(PrintNum > 0):
            if((i+1) >= PrintNum):
                break

def PrintNGramVocabulary_New(NGramVocabulary, PrintNum=0, LeadingString=''):
    for i, ngkey in enumerate(NGramVocabulary):
        #=print(ngkey) # format: {'key': 'giver', 'word': 'giver', 'weight': 1},
        print(LeadingString, end='')
        print(f"{i+1}, {ngkey['key']}: {ngkey['weight']}")
        if(PrintNum > 0):
            if((i+1) >= PrintNum):
                break

def PrintNGramVocabulary_WordList(NGramVocabulary, WordList, PrintNum=0, LeadingString=''):
    for inx, dic_f in enumerate(WordList):
        NGramDicVocabulary = NGramVocabulary.get(dic_f)
        if(NGramDicVocabulary == None): # n-gram에 속하는 단어가 없는 경우
            #=print('NGramList[', dic_f, '] - (NGramDicVocabulary == None)', )
            NGramDicVocabularyNum = 0
        else: 
            #=print(f'NGramList({dic_f}): {len(NGramDicVocabulary)} {NGramDicVocabulary}')
            #=NGramDicVocabulary_format: [{'key': 'roqkfwpgksrndur', 'word': '개발제한구역', 'weight': 7}, ...]
            NGramDicVocabularyNum = len(NGramDicVocabulary)
        print(LeadingString, end='')
        print(f'{inx+1} : {dic_f} : {len(dic_f)} : {NGramDicVocabularyNum}')
        if(PrintNum > 0):
            if((inx+1) >= PrintNum):
                break

def PrintNGramSuggest(NGramResult, PrintNum=0, LeadingString=''):
    for i, ngwork in enumerate(NGramResult):
        #=print(ngwork) # format: {'word': 'vernm', 'realword': 'government', 'weight': 620},
        print(LeadingString, end='')
        print(f"{i+1}, {ngwork['realword']}: {ngwork['weight']}")
        if(PrintNum > 0):
            if((i+1) >= PrintNum):
                break


#================================
#================================
#================================
from unittest import TestCase, main

class HGTest(TestCase):
    def _test_lv(self):
        print('----------------------------------')
        print('GetEditDistance')
        print('----------------------------------')
        
        base_v = 'sitting'
        comp_v = 'kitten'
        Distance = GetEditDistance(base_v, comp_v, DebugPrint=True)
        print ('EditDistance[L]:', Distance, f'({base_v},{comp_v})') # EditDistance: 3

        base_v = 'kitten'
        comp_v = 'sitting'
        Distance = GetEditDistance(base_v, comp_v, DebugPrint=True)
        print ('EditDistance[L]:', Distance, f'({base_v},{comp_v})') # EditDistance: 3

        base_v = 'Sunday'
        comp_v = 'Saturday'
        Distance = GetEditDistance(base_v, comp_v, DebugPrint=True)
        print ('EditDistance[L]:', Distance, f'({base_v},{comp_v})') # EditDistance: 3

        base_v = 'govenment'
        comp_v = 'government'
        Distance = GetEditDistance(base_v, comp_v)
        print ('EditDistance[L]:', Distance, f'({base_v},{comp_v})') # EditDistance: 1

        base_v = 'govenment'
        comp_v = 'representatives'
        Distance = GetEditDistance(base_v, comp_v)
        print ('EditDistance[L]:', Distance, f'({base_v},{comp_v})') # EditDistance: 12

        base_v = 'money'
        comp_v = 'monkey'
        Distance = GetEditDistance(base_v, comp_v)
        print ('EditDistance[L]:', Distance, f'({base_v},{comp_v})') # EditDistance: 1

        base_v = 'taming text'
        comp_v = 'tamming test'
        Distance = GetEditDistance(base_v, comp_v)
        print ('EditDistance[L]:', Distance, f'({base_v},{comp_v})') # EditDistance: 2

        base_v = 'arrow'
        comp_v = 'arro'
        Distance = GetEditDistance(base_v, comp_v)
        print ('EditDistance[L]:', Distance, f'({base_v},{comp_v})') # EditDistance: 2
        Distance = GetEditDistance(base_v, comp_v, Norm=True)
        print ('EditDistance[LNorm]:', Distance, f'({base_v},{comp_v})') # EditDistance: 0.83(<-2)


        base_v = 'mae'
        comp_v = 'make'
        Distance = GetEditDistance(base_v, comp_v)
        print ('EditDistance[L]:', Distance, f'({base_v},{comp_v})') # EditDistance: 1

        
        base_v = '동해물 백두산이'
        comp_v = '동해물과 백두산이'
        Distance = GetEditDistance(base_v, comp_v)
        print ('EditDistance[L]:', Distance, f'({base_v},{comp_v})') # EditDistance: 1

    def _test_lv_norm(self):
        print('----------------------------------')
        print('GetEditDistance Norm')
        print('----------------------------------')
        
        base_v = 'sitting'
        comp_v = 'kitten'
        Distance = GetEditDistance(base_v, comp_v, Norm=True)
        print ('EditDistance[LN]:', Distance, f'({base_v},{comp_v})') # EditDistance: 0.57(<-3)

        base_v = 'kitten'
        comp_v = 'sitting'
        Distance = GetEditDistance(base_v, comp_v, Norm=True)
        print ('EditDistance[LN]:', Distance, f'({base_v},{comp_v})') # EditDistance: 0.57(<-3)

        base_v = 'Sunday'
        comp_v = 'Saturday'
        Distance = GetEditDistance(base_v, comp_v, Norm=True)
        print ('EditDistance[LN]:', Distance, f'({base_v},{comp_v})') # EditDistance: 0.625(<-3)

        base_v = 'govenment'
        comp_v = 'government'
        Distance = GetEditDistance(base_v, comp_v, Norm=True)
        print ('EditDistance[LN]:', Distance, f'({base_v},{comp_v})') # EditDistance: 0.9(<-1)

        base_v = 'govenment'
        comp_v = 'representatives'
        Distance = GetEditDistance(base_v, comp_v, Norm=True)
        print ('EditDistance[LN]:', Distance, f'({base_v},{comp_v})') # EditDistance: 0.2(<-12)

        base_v = 'money'
        comp_v = 'monkey'
        Distance = GetEditDistance(base_v, comp_v, Norm=True)
        print ('EditDistance[LN]:', Distance, f'({base_v},{comp_v})') # EditDistance: 0.83(<-1)

        base_v = 'taming text'
        comp_v = 'tamming test'
        Distance = GetEditDistance(base_v, comp_v, Norm=True)
        print ('EditDistance[LN]:', Distance, f'({base_v},{comp_v})') # EditDistance: 0.83(<-2)

    def _test_jc(self):
        print('----------------------------------')
        print('Distance_Jacard')
        print('----------------------------------')

        base_v = 'sitting'
        comp_v = 'kitten'
        Distance = GetWordDistance_Jacard(base_v, comp_v, DebugPrint=True)
        print ('EditDistance[J]:', round(Distance, 3), f'({base_v},{comp_v})') # EditDistance[J]: 0.571

        base_v = 'kitten'
        comp_v = 'sitting'
        Distance = GetWordDistance_Jacard(base_v, comp_v, DebugPrint=True)
        print ('EditDistance[J]:', round(Distance, 3), f'({base_v},{comp_v})') # EditDistance[J]: 0.571

        base_v = 'Sunday'
        comp_v = 'Saturday'
        Distance = GetWordDistance_Jacard(base_v, comp_v, DebugPrint=True)
        print ('EditDistance[J]:', round(Distance, 3), f'({base_v},{comp_v})') # EditDistance[J]: 0.375

        base_v = 'govenment'
        comp_v = 'government'
        Distance = GetWordDistance_Jacard(base_v, comp_v)
        print ('EditDistance[J]:', round(Distance, 3), f'({base_v},{comp_v})') # EditDistance[J]: 0.125

        base_v = 'govenment'
        comp_v = 'representatives'
        Distance = GetWordDistance_Jacard(base_v, comp_v)
        print ('EditDistance[J]:', round(Distance, 3), f'({base_v},{comp_v})') # EditDistance[J]: 0.667

        base_v = 'mapping'
        comp_v = 'mappings'
        Distance = GetWordDistance_Jacard(base_v, comp_v)
        print ('EditDistance[J]:', round(Distance, 3), f'({base_v},{comp_v})') # EditDistance[J]: 0.143

        base_v = 'money'
        comp_v = 'monkey'
        Distance = GetWordDistance_Jacard(base_v, comp_v)
        print ('EditDistance[J]:', round(Distance, 3), f'({base_v},{comp_v})') # EditDistance[J]: 0.167

    def _test_tm(self):
        print('----------------------------------')
        print('Distance_Tanimoto')
        print('----------------------------------')

        base_v = 'sitting'
        comp_v = 'kitten'
        Distance = GetWordDistance_Tanimoto(base_v, comp_v)
        print ('EditDistance[T]:', round(Distance, 3), f'({base_v},{comp_v})') # EditDistance[T]: 0.417

        base_v = 'kitten'
        comp_v = 'sitting'
        Distance = GetWordDistance_Tanimoto(base_v, comp_v)
        print ('EditDistance[T]:', round(Distance, 3), f'({base_v},{comp_v})') # EditDistance[T]: 0.417

        base_v = 'Sunday'
        comp_v = 'Saturday'
        Distance = GetWordDistance_Tanimoto(base_v, comp_v)
        print ('EditDistance[T]:', round(Distance, 3), f'({base_v},{comp_v})') # EditDistance[T]: 0.4

        base_v = 'govenment'
        comp_v = 'government'
        Distance = GetWordDistance_Tanimoto(base_v, comp_v)
        print ('EditDistance[T]:', round(Distance, 3), f'({base_v},{comp_v})') # EditDistance[T]: 0.071

        base_v = 'govenment'
        comp_v = 'representatives'
        Distance = GetWordDistance_Tanimoto(base_v, comp_v)
        print ('EditDistance[T]:', round(Distance, 3), f'({base_v},{comp_v})') # EditDistance[T]: 0.606

        base_v = 'mapping'
        comp_v = 'mappings'
        Distance = GetWordDistance_Tanimoto(base_v, comp_v)
        print ('EditDistance[T]:', round(Distance, 3), f'({base_v},{comp_v})') # EditDistance[T]: 0.1

        base_v = 'money'
        comp_v = 'monkey'
        Distance = GetWordDistance_Tanimoto(base_v, comp_v)
        print ('EditDistance[T]:', round(Distance, 3), f'({base_v},{comp_v})') # EditDistance[T]: 0.167

    def _test_ngram(self):
        BaseSeq = 'government'
        print()
        print(MakeStringNGram(BaseSeq, NGram=1))
        print(MakeStringNGram(BaseSeq, NGram=1, EditDistanceMode=True))
        print(MakeStringNGram(BaseSeq, NGram=2))
        print(MakeStringNGram(BaseSeq, NGram=2, EditDistanceMode=True))
        print(MakeStringNGram(BaseSeq, NGram=3))
        print(MakeStringNGram(BaseSeq, NGram=3, EditDistanceMode=True))

    def _test_ngram_morethan(self):
        BaseSeq = 'government'
        print()
        print(MakeStringNGram(BaseSeq, NGram=1))
        print(MakeStringNGram(BaseSeq, NGram=1, MoreThan=True))
        #print(MakeStringNGram(BaseSeq, NGram=2))
        #print(MakeStringNGram(BaseSeq, NGram=2, MoreThan=True))
        #print(MakeStringNGram(BaseSeq, NGram=3))
        #print(MakeStringNGram(BaseSeq, NGram=3, MoreThan=True))

        print(MakeStringNGram(BaseSeq, NGram=5))
        print(MakeStringNGram(BaseSeq, NGram=5, MoreThan=True))

        #=print(MakeStringNGram('gksrnrwbd', NGram=5, MoreThan=True))

    def _test_lv_gram(self):
        print('----------------------------------')
        print('GetEditDistance - NGram')
        print('----------------------------------')
        
        #-----------------
        base_v = 'sitting'
        comp_v = 'kitten'

        NGram = 1
        baseGram = MakeStringNGram(base_v, NGram=NGram)
        compGram = MakeStringNGram(comp_v, NGram=NGram)
        Distance = GetEditDistance(baseGram, compGram, DebugPrint=True)
        print (f'EditDistance[L-NGram({NGram})]:', Distance, f'({base_v},{comp_v})')
        # ==> EditDistance[L-NGram(1)]: 3 (sitting,kitten)

        #=#
        #=import ngram
        #=print('ngram:', ngram.NGram.compare(base_v, comp_v, N=NGram)) 
        #=결과가 GetEditDistance()함수와 다르네.

        NGram = 2
        baseGram = MakeStringNGram(base_v, NGram=NGram)
        compGram = MakeStringNGram(comp_v, NGram=NGram)
        Distance = GetEditDistance(baseGram, compGram, DebugPrint=True)
        print (f'EditDistance[L-NGram({NGram})]:', Distance, f'({base_v},{comp_v})')
        # ==> EditDistance[L-NGram(1)]: 3 (sitting,kitten)

        #-----------------
        base_v = 'taming text'
        comp_v = 'tamming test'

        NGram = 1
        baseGram = MakeStringNGram(base_v, NGram=NGram)
        compGram = MakeStringNGram(comp_v, NGram=NGram)
        Distance = GetEditDistance(baseGram, compGram, DebugPrint=True)
        print (f'EditDistance[L-NGram({NGram})]:', Distance, f'({base_v},{comp_v})')
        # ==> EditDistance[L-NGram(1)]: 2 (taming text,tamming test)

        NGram = 2
        baseGram = MakeStringNGram(base_v, NGram=NGram)
        compGram = MakeStringNGram(comp_v, NGram=NGram)
        Distance = GetEditDistance(baseGram, compGram, DebugPrint=True)
        print (f'EditDistance[L-NGram({NGram})]:', Distance, f'({base_v},{comp_v})')
        # ==> EditDistance[L-NGram(2)]: 3 (taming text,tamming test)

        NGram = 3
        baseGram = MakeStringNGram(base_v, NGram=NGram)
        compGram = MakeStringNGram(comp_v, NGram=NGram)
        Distance = GetEditDistance(baseGram, compGram, DebugPrint=True)
        print (f'EditDistance[L-NGram({NGram})]:', Distance, f'({base_v},{comp_v})')
        # ==> EditDistance[L-NGram(3)]: 4 (taming text,tamming test)

    def _test_lv_jamo_1(self):
        tmp_jamo_list1 = [
            'ㄹㅏㄴㄱㅜ',
            'ㄹㅏㄴㄱㅜㄱ',
            'ㅏㄴㄱㅜㄱ',
            'ㅏㄴㄱㅜㄱㄱ',
            'ㅏㄴㄱㅜㄱㄱㅕ',
            'ㅏㄴㄱㅜㄱㄱㅕㅇ',
            'ㅏㄴㄱㅜㄱㄱㅕㅇㅈ',
            'ㅏㄴㄱㅜㄱㄱㅕㅇㅈㅔ',
            'ㄴㄱㅜㄱㄱ',
            'ㄴㄱㅜㄱㄱㅕ',
            'ㄴㄱㅜㄱㄱㅕㅇ',
            'ㄴㄱㅜㄱㄱㅕㅇㅈ',
            'ㄴㄱㅜㄱㄱㅕㅇㅈㅔ',
            'ㄱㅜㄱㄱㅕ',
            'ㄱㅜㄱㄱㅕㅇ',
            'ㄱㅜㄱㄱㅕㅇㅈ',
            'ㄱㅜㄱㄱㅕㅇㅈㅔ',
            'ㅜㄱㄱㅕㅇ',
            'ㅜㄱㄱㅕㅇㅈ',
            'ㅜㄱㄱㅕㅇㅈㅔ',
            'ㄱㄱㅕㅇㅈ',
            'ㄱㄱㅕㅇㅈㅔ',
            'ㄱㅕㅇㅈㅔ'
            ]

        tmp_jamo_list2 = [
            'ㄹㅏㄴㄱㅜ',
            'ㄹㅏㄴㄱㅜㄱ',
            'ㅏㄴㄱㅜㄱ',
            'ㅏㄴㄱㅜㄱㄱ',
            'ㅏㄴㄱㅜㄱㄱㅕ',
            'ㅏㄴㄱㅜㄱㄱㅕㅇ',
            'ㅏㄴㄱㅜㄱㄱㅕㅇㅈ',
            'ㄴㄱㅜㄱㄱ',
            'ㄴㄱㅜㄱㄱㅕ',
            'ㄴㄱㅜㄱㄱㅕㅇ',
            'ㄴㄱㅜㄱㄱㅕㅇㅈ',
            'ㄱㅜㄱㄱㅕ',
            'ㄱㅜㄱㄱㅕㅇ',
            'ㄱㅜㄱㄱㅕㅇㅈ',
            'ㅜㄱㄱㅕㅇ',
            'ㅜㄱㄱㅕㅇㅈ',
            'ㄱㄱㅕㅇㅈ',
            ]

        #       
        #=base_v = 'ㄹㅏㄴㄱㅜㄱㄱㅕㅇㅈㅔ'
        base_v = 'ㄹㅏㄴㄱㅜㄱㄱㅕㅇㅈ'
        print ('EditDistance[L]:', base_v)

        #=tmp_jamo = tmp_jamo_list1
        tmp_jamo = tmp_jamo_list2

        sort_res = {}
        for jamo_t in tmp_jamo:
            Distance = GetEditDistance(base_v, jamo_t, DebugPrint=False)
            print (Distance, f'({jamo_t})')
            sort_res[jamo_t] = Distance
        
        dis_sort = sorted(sort_res.items(), key = lambda item: item[1]) # by low
        print(*dis_sort, sep='\n')
        for key, value in dis_sort:
            print (f'{key} : {value}')

    def test_lv_jamo_2(self):
        tmp_jamo_list1 = [
            '한국방송광고진흥공사',
            '한국방송카메라기자협회',
            '한국방송통신대학교',
            ]

        #       
        base_v = '란국방송'
        base_eng = HGTransString2EngString(base_v) # 한글->영문자
        print ('EditDistance[L]:', f'{base_v}[{base_eng}]')

        tmp_jamo = tmp_jamo_list1

        sort_res = {}
        for jamo_t in tmp_jamo:
            jamo_eng = HGTransString2EngString(jamo_t) # 한글->영문자

            Distance = GetEditDistance(base_eng, jamo_eng, DebugPrint=False)
            print (Distance, f'({jamo_eng}[{jamo_t}])')
            sort_res[jamo_t] = Distance
        
        dis_sort = sorted(sort_res.items(), key = lambda item: item[1]) # by low
        print(), print(*dis_sort, sep='\n')
        for key, value in dis_sort:
            print (f'{key} : {value}')

    def _test_lv_jamo_3(self):
        tmp_jamo_list1 = [
            'ㅎㅏㄴㄱㅜㄱㄱㅕㅇㅈㅔ', # '한국경제',
            'ㅁㅣㄱㅜㄱㄱㅕㅇㅈㅔ', # '미국경제',
            'ㅈㅜㅇㄱㅜㄱㄱㅕㅇㅈㅔ', # '중국경제',
            ]

        #       
        base_v = 'ㅁㅏㄱㅜㄱㄱㅕㅇㅈㅔ'   #'마국경제'
        print ('EditDistance[L]:', f'{base_v}')

        tmp_jamo = tmp_jamo_list1

        sort_res = {}
        for jamo_t in tmp_jamo:
            Distance = GetEditDistance(base_v, jamo_t, DebugPrint=False)
            print (Distance, f'({jamo_t})')
            sort_res[jamo_t] = Distance
        
        dis_sort = sorted(sort_res.items(), key = lambda item: item[1]) # by low
        print(*dis_sort, sep='\n')
        for key, value in dis_sort:
            print (f'{key} : {value}')

    def _test_lv_gram_2(self):
        print('----------------------------------')
        print('GetEditDistance - NGram')
        print('----------------------------------')
        
        #-----------------
        base_v = 'ㄷㅐㅎㅓㄴㅁㅣㄴㄱㅜㄱ'
        comp_v = 'ㄷㅐㅎㅏㄴㅁㅣㄴㄱㅜㄱ'

        NGram = 1
        baseGram = MakeStringNGram(base_v, NGram=NGram)
        compGram = MakeStringNGram(comp_v, NGram=NGram)
        Distance = GetEditDistance(baseGram, compGram, DebugPrint=False)
        print (f'EditDistance[L-NGram({NGram})]:', Distance, f'({base_v},{comp_v})')

        #=#
        #=import ngram
        #=print('ngram:', ngram.NGram.compare(base_v, comp_v, N=NGram)) 
        #=결과가 GetEditDistance()함수와 다르네.

        NGram = 2
        baseGram = MakeStringNGram(base_v, NGram=NGram)
        compGram = MakeStringNGram(comp_v, NGram=NGram)
        Distance = GetEditDistance(baseGram, compGram, DebugPrint=False)
        print (f'EditDistance[L-NGram({NGram})]:', Distance, f'({base_v},{comp_v})')


        NGram = 3
        baseGram = MakeStringNGram(base_v, NGram=NGram)
        compGram = MakeStringNGram(comp_v, NGram=NGram)
        Distance = GetEditDistance(baseGram, compGram, DebugPrint=False)
        print (f'EditDistance[L-NGram({NGram})]:', Distance, f'({base_v},{comp_v})')

        NGram = 4
        baseGram = MakeStringNGram(base_v, NGram=NGram)
        compGram = MakeStringNGram(comp_v, NGram=NGram)
        Distance = GetEditDistance(baseGram, compGram, DebugPrint=False)
        print (f'EditDistance[L-NGram({NGram})]:', Distance, f'({base_v},{comp_v})')


        comp_list = ['ㄷㅐㅎㅏㄴㅁㅣㄴㄱㅜㄱ',
            'ㅎㅏㄴㅁㅣㄴㄱㅜㄱ',
            'ㄷㅐㅎㅏㄴㅁㅣㄴㄱㅜㄱㅊㅔㅇㅠㄱㅅㅏㅇ',
            'ㄷㅐㅎㅏㄴㅁㅣㄴㄱㅜㄱㅊㅔㅇㅠㄱㅅㅏㅇ',
            'ㄷㅐㅎㅏㄴㅁㅣㄴㄱㅜㄱㅇㅕㄱㅅㅏㅂㅏㄱㅁㅜㄹㄱㅗㅏㄴ',
            'ㄷㅐㅎㅏㄴㅁㅣㄴㄱㅜㄱㅎㅗ',
            'ㄷㅐㅎㅏㄴㅁㅣㄴㄱㅜㄱㅇㅖㅅㅜㄹㅇㅜㅓㄴ',
            'ㄷㅐㅎㅏㄴㅁㅣㄴㄱㅜㄱㅅㅓㄴㅅㅜㄷㅏㄴㅈㅏㅇ',
            'ㅂㅐㅎㅓㄴㅁㅣㄴ',
            'ㄴㅏㅁㅣㄴㄱㅜㅅ',
            ]
        for NGram in range(1,5):
            for comp_v in comp_list:
                baseGram = MakeStringNGram(base_v, NGram=NGram)
                compGram = MakeStringNGram(comp_v, NGram=NGram)
                Distance = GetEditDistance(baseGram, compGram, DebugPrint=False)
                print (f'EditDistance[L-NGram({NGram})]:', Distance, f'({base_v},{comp_v})')
            print(), print()



if __name__ == '__main__':
    main()



