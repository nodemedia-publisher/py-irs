#------------------------
#------------------------
import hgsysinc
##import hgbasic
from hgchartype import HGTokenize
from hgwordlist import GetWordDictList_WordList
from hgwordfile import GetWordList_TpxFile

from hgdict import (
    GetDictFreq__WordList, GetDictFreq__WordDictList,
    GetDictFreqs__WordDictLists, 
    DelDictFreqs__WordDict,
    GetDictFreq_Product,
)

#----------
#----------
import importlib
exist_flag = importlib.util.find_spec("hgwordmatrix") is not None
if(exist_flag):
    from hgwordmatrix_low import (
        RunWordDicts_TFIDF, RunDictFreqs_TFIDF, 
        MakeDocWordMatrix__WordDicts, MakeDictFreqs__WordDicts_TFIDF,
        BuildWordDict_TermFreq, BuildWordDict_TFIDF,
    )
    from hgdict import DeleteWordDicts_ByWordDict

#-----
#-----
class HGDistance:
    def __init__(self, WordDicts=None, IDFSmooth=True, Norm='2', DelDocNumRate=0, DelFreq=0):
        self._init_ = True
        self.DictFreqs_ByWordDictLists = None
        self.IDFSmooth = IDFSmooth  # default-state: True
        self.Norm = Norm   # default-state: '2'
        self.DocWordMatrix = None
        self.WordDicts_TFIDF = None
        self.DelDocNumRate = DelDocNumRate # default-state: 0.0
        self.DelFreq = DelFreq # default-state: 0
        self.DictFreqs_TFIDF = None  # {self.WordDicts_TFIDF} 변수를 {DictFreq} 방식으로 변환한 것

        #---        
        if((WordDicts != None) and (len(WordDicts) > 0)):
            self.SetWordDicts(WordDicts=WordDicts, DelDocNumRate=self.DelDocNumRate, DelFreq=self.DelFreq)
            
    def SetWordDicts(self, WordDicts, IDFSmooth=True, Norm='2', DelDocNumRate=0, DelFreq=0):
        #---
        self.IDFSmooth = IDFSmooth  # default-state: True
        self.Norm = Norm   # default-state: '2'
        self.DelDocNumRate = DelDocNumRate # default-state: 0.0
        self.DelFreq = DelFreq # default-state: 0

        self.IDFSmooth = IDFSmooth  # default-state: True
        self.Norm = Norm # default-state: '2'

        #--- 'trans word-dicts to dict-freqs'
        self.DictFreqs_ByWordDictLists = GetDictFreqs__WordDictLists(WordDicts)

        #----- 
        # RunDictFreqs_TFIDF()함수는 내부적으로 RunWordDicts_TFIDF() 호출한다.
        # 그래서 불필요한 변환을 줄이기 위해서 바꾼다.
        #-----
        #=self.DocWordMatrix, self.WordDicts_TFIDF = RunDictFreqs_TFIDF(self.DictFreqs_ByWordDictLists, 
        #=    IDFSmooth=self.IDFSmooth, Norm=self.Norm, DelDocNumRate=self.DelDocNumRate, DelFreq=self.DelFreq)
        #-----
        # RunWordDicts_TFIDF() 함수에서 <WordDicts>에다가 'tfidf'값을 생성해준다.
        import copy
        self.WordDicts_TFIDF = copy.deepcopy(WordDicts)
        self.DocWordMatrix = RunWordDicts_TFIDF(self.WordDicts_TFIDF, IDFSmooth=self.IDFSmooth, 
                            Norm=self.Norm, DelDocNumRate=self.DelDocNumRate, DelFreq=self.DelFreq)
        
        #----- tfidf를 거치면서 필터링된 {~.WordDicts_TFIDF} 맞게 조절(삭제)한다.
        WordMatrix = self.DocWordMatrix['word']
        DelDictFreqs__WordDict(self.DictFreqs_ByWordDictLists, WordMatrix, DelType='not')
        # DelDictFreqs__WordDict() 수행하고 나면, 
        # {self.WordDicts_TFIDF}과 {self.DictFreqs_ByWordDictLists} 항목수가 일치한다.

    def Predict_WordDict_Tfidf(self, WordDict):
        r'''<WordDict>로 <Tfidf>로 변환하여 거리값 계산
        '''
        #
        DocNum = self.DocWordMatrix['DocNum']
        WordMatrix = self.DocWordMatrix['word']

        # WordDict['tf'] 값을 생성
        BuildWordDict_TermFreq(WordDict)

        # WordDict['tfidf'] 값을 생성
        BuildWordDict_TFIDF(WordDict, WordMatrix, DocNum, IDFSmooth=self.IDFSmooth, Norm=self.Norm)
        
        WordDictsCosDistance = GetWordDicts_CosDistance__WordDict(self.WordDicts_TFIDF, WordDict, TFIDFMode=True)
        return WordDictsCosDistance

    def Predict_WordDict_Freq(self, WordDict):
        r'''<Tfidf>값이 아니라 <freq>에 의해서 거리값 계산
        '''
        #=print(WordDict[0])  # value: freq
        #=print(self.DictFreqs_ByWordDictLists[0]) # value: freq
        DictFreqsCosDistance = GetDictFreqs_CosDistance__WordDict(self.DictFreqs_ByWordDictLists, WordDict)
        return DictFreqsCosDistance

    def Predict_WordList_Tfidf(self, WordList):
        r'''<WordList>로 <Tfidf>로 변환하여 거리값 계산
        '''
        #
        WordDict = GetWordDictList_WordList(WordList)
        #=print(WordDict[0])

        WordDictsCosDistance = self.Predict_WordDict_Tfidf(WordDict)
        return WordDictsCosDistance

    def Predict_WordList_Freq(self, WordList):
        r'''<WordList>를 <WordDict>로 변환한 후에 
        <Tfidf>값이 아니라 <freq>에 의해서 거리값 계산
        '''
        #
        WordDict = GetWordDictList_WordList(WordList)

        DictFreqsCosDistance = self.Predict_WordDict_Freq(WordDict)
        return DictFreqsCosDistance

    @classmethod
    def Calc_WordDicts_WordDict_Freq(cls, WordDicts, WordDict_c):
        # <Tfidf>값이 아니라 <freq>에 의해서 거리값 계산
        #=print(WordDict_c[0])  # value: freq
        DictFreqsCosDistance = GetWordDicts_CosDistance__WordDict(WordDicts, WordDict_c)
        return DictFreqsCosDistance

    @classmethod
    def Calc_WordDicts_WordList_Freq(cls, WordDicts, WordList):
        #
        WordDict = GetWordDictList_WordList(WordList)

        DictFreqsCosDistance = HGDistance.Calc_WordDicts_WordDict_Freq(WordDicts, WordDict)
        return DictFreqsCosDistance

    def Predict_DictFreq_Tfidf__(self, DictFreq): 
        r'''#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        #@@@ 이 함수는 다양한 함수 변형을 실험하기 위해 만든 함수이다.
        #@@@ 실제로 호출하면서 외부에서 내부 구조를 알고 
        #@@@ 선행 처리를 해야 하므로 사용하기 어렵다.
        #@@@ 그래서 함수 이름에 언더스코어(__)를 붙여서 실험용 함수로 표시했다.
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        '''

        #-----
        # 이 함수는 {WordDict}를 {DictFreq} 방식으로 변환해서 처리한 것과 같다.
        #-----
        # <DictFreq> 변수에는 ['tfidf'] 값을 가지고 있어야 한다.
        #-----

        #
        if(self.DictFreqs_TFIDF == None): # 사전식 {DictFreq} tfidf 값이 없으면 만든다.
            self.DictFreqs_TFIDF = MakeDictFreqs__WordDicts_TFIDF(self.WordDicts_TFIDF)
        
        #=print(self.DictFreqs_TFIDF[0])  # value: tfidf
        #
        DictFreqsCosDistance = GetDictFreqs_CosDistance(self.DictFreqs_TFIDF, DictFreq)
        return DictFreqsCosDistance

    def Predict_DictFreq_Freq__(self, DictFreq): 
        r'''#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        #@@@ 이 함수는 다양한 함수 변형을 실험하기 위해 만든 함수이다.
        #@@@ 실제로 호출하면서 외부에서 내부 구조를 알고 
        #@@@ 선행 처리를 해야 하므로 사용하기 어렵다.
        #@@@ 그래서 함수 이름에 언더스코어(__)를 붙여서 실험용 함수로 표시했다.
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        '''

        # <Tfidf>값이 아니라 <freq>에 의해서 거리값 계산

        #=print(DictFreq)  # value: freq 
        #=print(self.DictFreqs_ByWordDictLists[0]) # value: freq

        DictFreqsCosDistance = GetDictFreqs_CosDistance(self.DictFreqs_ByWordDictLists, DictFreq)
        return DictFreqsCosDistance

#-----
#-----
def GetEuclidean4(x1, y1, x2, y2):
    import numpy
    distance = numpy.sqrt((x1-x2)**2 + (y1-y2)**2)
    #=import math
    #=distance = math.sqrt((x1-x2)**2 + (y1-y2)**2)
    return distance

def GetEuclidean2(xy1, xy2):
    import numpy
    distance = numpy.sqrt((xy1[0] - xy2[0])**2 + (xy1[1] - xy2[1])**2)
    #=import math
    #=distance = math.sqrt((xy1[0] - xy2[0])**2 + (xy1[1] - xy2[1])**2)
    return distance

#-----
#-----
def GetWordDict_CosDistance(WordDictBase, WordDictComp, TFIDFMode=False):
    #=import math
    #
    CosDistance = 0

    # basic check
    if(TFIDFMode == True):
        if(len(WordDictBase) > 0):
            if('tfidf' not in WordDictBase[0]): # 'tfidf'값이 없으면 종료
                assert False, "'tfidf' not in WordDictBase[0]"
        if(len(WordDictComp) > 0):
            if('tfidf' not in WordDictComp[0]): # 'tfidf'값이 없으면 종료
                assert False, "'tfidf' not in WordDictComp[0]"


    ##----------
    # bunmo-calc
    ##----------
    BaseNum = 0
    basePowSum = 0
    for i, WordDict_i in enumerate(WordDictBase):
        #print(i, ':', WordDict_i['word'])
        if(TFIDFMode == True):
            #=basePow = math.pow(float(WordDict_i['tfidf']), 2)
            basePow = (float(WordDict_i['tfidf'])**2)
        else:
            #=basePow = math.pow(int(WordDict_i['freq']), 2)
            basePow = (int(WordDict_i['freq'])**2)
        #print(basePow)
        basePowSum += basePow
        BaseNum += 1

    CompNum = 0
    compPowSum = 0
    for i, WordDict_c in enumerate(WordDictComp):
        #print(i, ':', WordDict_c['word'])
        if(TFIDFMode == True):
            #=compPow = math.pow(float(WordDict_c['tfidf']), 2)
            compPow = (float(WordDict_c['tfidf'])**2)
        else:
            #=compPow = math.pow(int(WordDict_c['freq']), 2)
            compPow = (int(WordDict_c['freq'])**2)
        #print(compPow)
        compPowSum += compPow
        CompNum += 1
    #-----
    #=print('BaseNum :', BaseNum, '\t', 'CompNum: ', CompNum)
    #print(basePowSum)
    #print(compPowSum)
    #-----
    #=baseRoot = math.sqrt(basePowSum)
    #=compRoot = math.sqrt(compPowSum)
    #-----
    baseRoot = basePowSum**0.5 # square-root
    compRoot = compPowSum**0.5 # square-root
    Bunmo_Total = baseRoot * compRoot
    #=print('Bunmo_Total:', Bunmo_Total)

    ##----------
    # bunja-calc
    ##----------
    BunjaCnt = 0
    Bunja_Total = 0
    baseI = 0
    compI = 0
    while(True):
        WordDict_i = None
        WordDict_c = None
        if(baseI < BaseNum):
            BunjaCnt += 1
            WordDict_i = WordDictBase[baseI]
        if(compI < CompNum):
            WordDict_c = WordDictComp[compI]

        #=print(WordDict_i)
        #=print(WordDict_c)

        #if((WordDict_i != None) and (WordDict_c != None)):
        #    print(baseI, ':', compI, WordDict_i['word'], WordDict_c['word'])
        #else:
        #    if(WordDict_i != None):
        #        print(baseI, ':', compI, WordDict_i['word'], '?')
        #    elif(WordDict_c != None):
        #        print(baseI, ':', compI, '?', WordDict_c['word'])
        #    else:
        #        print(baseI, ':', compI, '?', '?')

        mul_c = 0 # 동시에 주제어가 있지 않으면 '0'
        if((WordDict_i != None) and (WordDict_c != None)):
            if(WordDict_i['word'] == WordDict_c['word']):
                if(TFIDFMode == True):
                    mul_c = float(WordDict_i['tfidf']) * float(WordDict_c['tfidf'])
                else:
                    mul_c = int(WordDict_i['freq']) * int(WordDict_c['freq'])

                #
                baseI += 1
                compI += 1
            elif(WordDict_i['word'] >= WordDict_c['word']):
                compI += 1
            else:
                baseI += 1
        else:
            if(WordDict_i != None):
                baseI += 1
            elif(WordDict_c != None):
                compI += 1
            else:
                break

        #
        #=print('mul_c:', mul_c)
        Bunja_Total += mul_c
    #=print('Bunja_Total:', Bunja_Total)

    #===============
    # sqrt(float) limit 패치
    #===============
    # 제곱근을 구할 때 미세하게 정확도가 떨어진다.
    # 그래서 두 사전이 같으면 값이 같도록 조정한다.
    # DictFreqBase: {'app': 1, 'ban': 1, 'can': 1}
    # DictFreqComp: {'app': 1, 'ban': 1, 'can': 1}
    # (Bunja_Total > Bunmo_Total)
    # (3 > 2.9999999999999996)
    #===============
    if(Bunja_Total > Bunmo_Total):
        if((BunjaCnt == BaseNum) and (BaseNum == CompNum)):
            Bunmo_Total = Bunja_Total # 분모값을 분자값으로 변경하여 아래에서 '1'이 되도록 한다.
    #=print('Bunmo_Total:', Bunmo_Total, 'Bunja_Total:', Bunja_Total)

    ##----------
    # result
    ##----------
    #print(Bunja_Total)
    #print(Bunmo_Total)
    if(Bunja_Total > Bunmo_Total):
        print('WordDictBase:', WordDictBase)
        print('WordDictComp:', WordDictComp)
        #----------
        # 무조건 오류로 처리하지 않고 소수점의 부정확한 계산이면 반올림으로 보정한다.
        #----------
        # 예) (Bunja_Total > Bunmo_Total)=>(208 > 207.99999999999997)
        #----------
        #=import numpy
        #=Bunmo_Total_Round = numpy.round(Bunmo_Total, 7) # {7}자리에서 반올림
        #-----
        Bunmo_Total_Round = round(Bunmo_Total, 7) # {7}자리에서 반올림
        if(Bunja_Total == Bunmo_Total_Round):
            Bunmo_Total = Bunja_Total
        if(Bunja_Total > Bunmo_Total): # 오류 상태
            assert False, f'(Bunja_Total > Bunmo_Total)=>({Bunja_Total} > {Bunmo_Total})' 
        # debug: 
        #=print('소수점의 부정확한 계산이면 반올림으로 보정.')

    if(Bunmo_Total == 0):
        print('WordDictBase:', WordDictBase)
        print('WordDictComp:', WordDictComp)
        assert False, f'(Bunmo_Total == 0)' 
    CosSimilarity = (Bunja_Total / Bunmo_Total)
    if(CosSimilarity > 1):
        assert False, f'(CosSimilarity > 1) ==> {CosSimilarity}' 
    CosDistance = 1 - CosSimilarity

    #
    return CosDistance

def CalcWordDicts_CosDistance(WordDicts, SortDistance=False, TFIDFMode=False):
    ##
    DocDistance = []

    ##
    WordDicts_len = len(WordDicts)
    for i in range(0, WordDicts_len):
        DocDistance_base = []
        for j in range(0, WordDicts_len):
            if(j == i):
                CosDistance = 0 # '1': 거리가 가장 먼 값, 0: 일치할 때, 가장 가까운 값
            #-----------------------------
            # 아래는 계산이 부정확해서 막는다. - 나중에 고치자.(안 고치면 중복 연산 발생)
            #-----------------------------
            elif(j < i): # 앞에서 처리했기 때문에 다시 계산하지 말고 복사해온다.
                CosDistance = GetDocDistance_Distance(DocDistance, j, i) # 'i'와 'j' 값을 바꿔서 전달
            #-----------------------------
            else:            
                CosDistance = GetWordDict_CosDistance(WordDicts[i], WordDicts[j], TFIDFMode=TFIDFMode)

            #print('[', i, ':', j, ']', round(CosDistance, 3))
            DocDistance_comp = {
                'base':i,
                'comp':j,
                'distance':CosDistance,
            }
            DocDistance_base.append(DocDistance_comp)
            #break  # 1개만 처리하고 종료한다.

        DocDistance.append(DocDistance_base)
        #break # 1개만 처리하고 종료한다.

    ## 거리가 가까운 순으로 정렬해준다.
    if(SortDistance == True):    
        DocsNum = len(DocDistance)
        for i in range(0, DocsNum):
            DocDis_i = DocDistance[i]
            DocDis_i.sort(key = lambda item: (item['distance'])) # by low

    ##
    return DocDistance

def GetWordDicts_CosDistance__WordDict(WordDicts, WordDict_Comp, PassInx=None, TFIDFMode=False):
    #=print('WordDicts:', len(WordDicts))
    ##
    DocDistances = {}
    for Inx, WordDict_c in enumerate(WordDicts):
        #=print(f'[{Inx}] WordDict_c:', len(WordDict_c))
        if(PassInx != None): # 비교하지 않고 통과하는 인덱스(목록 안에서 비교할 때는 제외시킬 필요가 있다.)
            if(PassInx == Inx):
                pass
        #
        CosDistance = GetWordDict_CosDistance(WordDict_c, WordDict_Comp, TFIDFMode=TFIDFMode)
        DocDistances[Inx] = CosDistance
    return DocDistances

def GetDocDistance_Distance(DocDistance, LinePos, KanPos):
    CosDistance = 1 # '1': 거리가 가장 먼 값, 0: 일치할 때, 가장 가까운 값

    DocsNum = len(DocDistance)
    if(LinePos < DocsNum):
        DocDis_i = DocDistance[LinePos]
        if(KanPos < len(DocDis_i)):
            DocDis_j = DocDis_i[KanPos]
            CosDistance = DocDis_j['distance']
            if((DocDis_j['base'] != LinePos) or (DocDis_j['comp'] != KanPos)):
                print('logic-error: ', 'base:', LinePos, '\t', 'comp:', KanPos)
                print(DocDis_j)
    return CosDistance

def PrintDocDistance(DocDistance, rankNum=1, Roundval=0, SortDistance=False):
    #=DocsNum = len(DocDistance)

    print()
    for DocDis_i in DocDistance:
        ## 거리가 가까운 순으로 정렬해준다.
        if(SortDistance == True):
            DocDis_sort = DocDis_i.copy()
            DocDis_sort.sort(key = lambda item: (item['distance'])) # by low
            DocDis_i = DocDis_sort

        for j, DocDis_j in enumerate(DocDis_i):
            if(DocDis_j['base'] == DocDis_j['comp']): # 자기 자신과 거리는 '0'이라서 제외
                continue

            prtMsg = '[' + str(j) + '] '
            prtMsg += 'base: ' + str(DocDis_j['base']) + ', '
            prtMsg += 'comp: ' + str(DocDis_j['comp']) + ' '
            prtMsg += 'distance: '
            if(Roundval > 0):
                prtMsg += str(round(DocDis_j['distance'], Roundval))
            else:
                prtMsg += str(DocDis_j['distance'])
            print(prtMsg) # 출력 속도 개선
            if(rankNum > 0):
                if((j + 1) >= rankNum):
                    break
            #break  # (dbg) 1개만 처리하고 종료한다.

        print()
        #break # (dbg) 1개만 처리하고 종료한다.

def TransDocDistance_DistanceMatrix(DocDistance, Roundval=0):
    DocDistanceMatrix = []

    #=DocsNum = len(DocDistance)
    for DocDis_i in DocDistance:
        DocDistanceList = []

        for j, DocDis_j in enumerate(DocDis_i):
            #----- 제외하면 안 된다
            #if(DocDis_j['base'] == DocDis_j['comp']): # 자기 자신과 거리는 '0'이라서 제외
            #    continue

            Distance = DocDis_j['distance']
            if(Roundval > 0):
                Distance = round(Distance, Roundval)

            DocDistanceList.append(Distance)
            #break  # (dbg) 1개만 처리하고 종료한다.
        
        DocDistanceMatrix.append(DocDistanceList)
        #break # (dbg) 1개만 처리하고 종료한다.

    return DocDistanceMatrix

def MakeDocDistancePack__WordDicts(WordDicts, DelDocNumRate=0, DelFreq=0, SortDistance=False, TFIDFMode=False):
    #================================
    ##### filter: low freq, high doc-rate
    #================================
    #
    DocWordMatrix = MakeDocWordMatrix__WordDicts(WordDicts, DelDocNumRate=DelDocNumRate, DelFreq=DelFreq)
    WordMatrix = DocWordMatrix['word']

    temp_print_flag = True
    temp_print_flag = False
    if(temp_print_flag == True):
        ### 임시로 출력해본다
        from hgwordlist import GetWordDictList_TotalFreq
        from hgwordlist import PrintWordDictList

        PrintingNum = 5 # 임시로 각 파일 주제어 사전에서 5개만 출력
        TopicWordDict_len = len(WordDicts)
        #print ('TopicWordDict len :', TopicWordDict_len)
        for i in range(0, TopicWordDict_len):
            TopicWordDict_i = WordDicts[i]
            print('======================================================')
            print('dict ', (i + 1), ' : ', len(TopicWordDict_i), '(단어)', '\t', 'total:', GetWordDictList_TotalFreq(TopicWordDict_i))
            PrintWordDictList(TopicWordDict_i, OneLine=True, PrintIndex=True, PrintingNum=PrintingNum, SimpleFormat=True)

    #================================
    #================================
    ###### 문서 유사도 거리 계산
    DocDistance = CalcWordDicts_CosDistance(WordDicts, SortDistance=SortDistance, TFIDFMode=TFIDFMode)

    #rankNum=1 # 상위 1개만
    #rankNum=3  # 상위 3개만
    #rankNum=0 # 모두 순위 출력
    #PrintDocDistance(DocDistance, rankNum=rankNum, SortDistance=True)

    ###
    DocDistancePack = {
        'DocWordMatrix':DocWordMatrix,
        'DocDistance': DocDistance,
    }
    return DocDistancePack

#---------------------------------
#---------------------------------
#---------------------------------
def GetWordList_CosDistance(WordListBase, WordListComp):
    #
    CosDistance = 0

    frequency_dict1 = GetDictFreq__WordList(WordListBase, FreqRate=False)
    frequency_dict2 = GetDictFreq__WordList(WordListComp, FreqRate=False)
    #=print('frequency_dict1:', frequency_dict1)
    #=print('frequency_dict2:', frequency_dict2)

    #
    CosDistance = GetDictFreq_CosDistance(frequency_dict1, frequency_dict2)
    return CosDistance

def GetWordLists_CosDistance(WordLists, WordListComp):
    CosDistances = []
    for WordList in WordLists:
        CosDistance = GetWordList_CosDistance(WordList, WordListComp)
        CosDistances.append(CosDistance)
    return CosDistances

#---------------------------------
#---------------------------------
def GetDictFreq_CosDistance(DictFreqBase, DictFreqComp):
    #-----
    #=print('DictFreqBase:', DictFreqBase)
    #=print('DictFreqComp:', DictFreqComp)
    ##----------
    # bunmo-calc
    ##----------
    #=basePowSum = sum([(value**2) for key, value in DictFreqBase.items()])
    basePowSum = 0
    for BaseNum, WordDict_i in enumerate(DictFreqBase):
        #=print(WordDict_i)
        basePowSum += (DictFreqBase[WordDict_i]**2)

    #=compPowSum = sum([(value**2) for key, value in DictFreqComp.items()])
    compPowSum = 0
    for CompNum, WordDict_c in enumerate(DictFreqComp):
        #=print(WordDict_c)
        compPowSum += (DictFreqComp[WordDict_c]**2)
    #-----
    #=print('BaseNum :', BaseNum, '\t', 'CompNum: ', CompNum)
    #=print(basePowSum)
    #=print(compPowSum)
    #-----
    baseRoot = basePowSum**0.5 # square-root
    compRoot = compPowSum**0.5 # square-root
    Bunmo_Total = baseRoot * compRoot

    ##----------
    # bunja-calc
    ##----------
    Bunja_Total, BunjaCnt = GetDictFreq_Product(DictFreqBase, DictFreqComp)
    if(Bunja_Total == 0): # 공통단어가 하나도 없는 경우
        #=print('@@@@@ (Bunja_Total == 0)', '\t', 'Bunmo_Total:', Bunmo_Total)
        pass
    if(Bunmo_Total == 0): # 로직 오류(함수 입력이 잘못된 경우)
        print('BaseNum :', BaseNum, '\t', 'CompNum: ', CompNum)
        assert False, '(Bunmo_Total == 0)' 
        CosDistance = 1 # 가장 멀리 있는 상태
        return CosDistance
    
    #===============
    # sqrt(float) limit 패치
    #===============
    # 제곱근을 구할 때 미세하게 정확도가 떨어진다. 그래서 두 사전이 같으면 값이 같게 조정함.
    # DictFreqBase: {'app': 1, 'ban': 1, 'can': 1}
    # DictFreqComp: {'app': 1, 'ban': 1, 'can': 1}
    # (Bunja_Total > Bunmo_Total)
    # (3 > 2.9999999999999996)
    #===============
    #----------
    # result
    #----------
    #=print(Bunja_Total)
    #=print(Bunmo_Total)
    if(Bunja_Total > Bunmo_Total): # 오류 상태
        #----------
        # 무조건 오류로 처리하지 않고 소수점의 부정확한 계산이면 반올림으로 보정한다.
        #----------
        # 예) (Bunja_Total > Bunmo_Total)=>(208 > 207.99999999999997)
        #----------
        #=import numpy
        #=Bunmo_Total_Round = numpy.round(Bunmo_Total, 7) # {7}자리에서 반올림
        #-----
        Bunmo_Total_Round = round(Bunmo_Total, 7) # {7}자리에서 반올림
        if(Bunja_Total == Bunmo_Total_Round):
            Bunmo_Total = Bunja_Total #분모값을 분자값으로 변경,아래에서 '1'이 되도록 함.
        if(Bunja_Total > Bunmo_Total): # 오류 상태
            print('DictFreqBase:', DictFreqBase)
            print('DictFreqComp:', DictFreqComp)
            assert False, f'(Bunja_Total > Bunmo_Total)=>({Bunja_Total} > {Bunmo_Total})' 
        # debug: 
        #=print('소수점의 부정확한 계산이면 반올림으로 보정.')
    #
    CosSimilarity = (Bunja_Total / Bunmo_Total)
    if(CosSimilarity > 1):
        assert False, f'(CosSimilarity > 1) ==> {CosSimilarity}' 
    CosDistance = 1 - CosSimilarity
    #
    return CosDistance

def GetDictFreqs_CosDistance(DictFreqs, DictFreqComp):
    ##
    CosDistances = {}
    for inx, DictFreq_c in enumerate(DictFreqs):
        if(len(DictFreq_c) <= 0):
            assert False, '(len(DictFreq_c) <= 0)'
        CosDistance = GetDictFreq_CosDistance(DictFreq_c, DictFreqComp)
        CosDistances[inx] = CosDistance
        #break # 임시로 1개만 처리하고 종료한다.
    ##
    return CosDistances

def GetDictFreqs_CosDistanceMatrix(DictFreqs):
    ##
    CosDistanceMatix = []
    for li, DictFreq_l in enumerate(DictFreqs):
        CosDistances = GetDictFreqs_CosDistance(DictFreqs, DictFreq_l)
        CosDistanceMatix.append(CosDistances)
        #break # 임시로 1개만 처리하고 종료한다.
    ##
    return CosDistanceMatix

def GetDictFreq_CosDistance__Text(DictFreqBase, TextComp, LowerCase=False):
    #=print('DictFreqBase:', DictFreqBase)
    #=print('TextComp:', TextComp)
    WordListComp = HGTokenize(TextComp, LowerCase=LowerCase)

    #
    CosDistance = GetDictFreq_CosDistance__WordList(DictFreqBase, WordListComp)
    return CosDistance

def GetDictFreq_CosDistance__WordList(DictFreqBase, WordListComp):
    #=print('DictFreqBase:', DictFreqBase)
    #=print('WordListComp:', WordListComp)
    DictFreqComp = GetDictFreq__WordList(WordListComp, FreqRate=False)
    #=print('DictFreqComp:', DictFreqComp)

    #
    CosDistance = GetDictFreq_CosDistance(DictFreqBase, DictFreqComp)
    return CosDistance

def GetDictFreqs_CosDistance__Text(DictFreqs, TextComp, LowerCase=False):
    #=print('DictFreqBase:', DictFreqBase)
    #=print('TextComp:', TextComp)
    WordListComp = HGTokenize(TextComp, LowerCase=LowerCase)

    #=print('WordListComp:', WordListComp)
    DictFreqComp = GetDictFreq__WordList(WordListComp, FreqRate=False)
    #=print('DictFreqComp:', DictFreqComp)

    CosDistances = GetDictFreqs_CosDistance(DictFreqs, DictFreqComp)
    return CosDistances

def GetDictFreqs_CosDistance__WordList(DictFreqs, WordListComp):
    #=print('WordListComp:', WordListComp)
    DictFreqComp = GetDictFreq__WordList(WordListComp, FreqRate=False)
    #=print('DictFreqComp:', DictFreqComp)

    CosDistances = GetDictFreqs_CosDistance(DictFreqs, DictFreqComp)
    return CosDistances

def GetDictFreqs_CosDistance__WordDict(DictFreqs, WordDictComp):
    #=print('WordDictComp:', WordDictComp)
    DictFreqComp = GetDictFreq__WordDictList(WordDictComp, FreqRate=False)
    #=print('DictFreqComp:', DictFreqComp)

    CosDistances = GetDictFreqs_CosDistance(DictFreqs, DictFreqComp)
    return CosDistances

#================================
#================================
#================================
def GetDictFreq_Tanimoto_Distance(DictFreqBase, DictFreqComp, DebugPrint=False):
    #=print('DictFreqBase:', DictFreqBase)
    #=print('DictFreqComp:', DictFreqComp)
    #--------------------------------------------
    # Tanimoto coefficient
    # https://en.wikipedia.org/wiki/Jaccard_index
    # @@@ Tanimoto 거리는 지문 유사도 검사에 효과적이다.
    # Tanimoto 거리는 Jacard 거리에 빈도 가중치를 부여한 것이다.
    # Why is Tanimoto index an appropriate choice for fingerprint-based similarity calculations
    # https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4456712/pdf/13321_2015_Article_69.pdf
    #--------------------------------------------
    ProductBC, ProductCnt = GetDictFreq_Product(DictFreqBase, DictFreqComp)
    if(DebugPrint == True):
        print('Product:', ProductBC)
    #
    SquareSumBase = sum([(DictFreqBase[d] * DictFreqBase[d]) for d in DictFreqBase])
    SquareSumComp = sum([(DictFreqComp[d] * DictFreqComp[d]) for d in DictFreqComp])
    if(DebugPrint == True):
        print('SquareSumBase:', SquareSumBase)
        print('SquareSumComp:', SquareSumComp)

    Bunmo = (SquareSumBase + SquareSumComp - ProductBC)
    Similarity = ProductBC / Bunmo
    #    
    Distance = 1 - Similarity
    return Distance

def GetWordList_Tanimoto_Distance(WordListBase, WordListComp):
    #
    CosDistance = 0

    DictFreqBase = GetDictFreq__WordList(WordListBase, FreqRate=False)
    DictFreqComp = GetDictFreq__WordList(WordListComp, FreqRate=False)
    #=print('DictFreqBase:', DictFreqBase)
    #=print('DictFreqComp:', DictFreqComp)

    #
    Distance = GetDictFreq_Tanimoto_Distance(DictFreqBase, DictFreqComp)
    return Distance

def GetDictFreq_Jacard_Distance(DictFreqBase, DictFreqComp):
    #=print('DictFreqBase:', DictFreqBase)
    #=print('DictFreqComp:', DictFreqComp)
    #--------------------------------------------
    # https://en.wikipedia.org/wiki/Jaccard_index
    #--------------------------------------------
    BaseSet = set([d for d in DictFreqBase])
    CompSet = set([d for d in DictFreqComp])
    
    InterSec = BaseSet.intersection(CompSet)
    UnionSec = BaseSet.union(CompSet)
    
    #
    Similarity = len(InterSec) / len(UnionSec)
    Distance = 1 - Similarity
    return Distance

def GetWordList_Jacard_Distance(WordListBase, WordListComp):
    #
    CosDistance = 0

    DictFreqBase = GetDictFreq__WordList(WordListBase, FreqRate=False)
    DictFreqComp = GetDictFreq__WordList(WordListComp, FreqRate=False)
    #=print('DictFreqBase:', DictFreqBase)
    #=print('DictFreqComp:', DictFreqComp)

    #
    Distance = GetDictFreq_Jacard_Distance(DictFreqBase, DictFreqComp)
    return Distance

def GetEditDistance(BaseStr, CompStr, Norm=False, DebugPrint=False): # Levenshtein Distance
    #--------------------------------------------
    # https://en.wikipedia.org/wiki/Levenshtein_distance
    #--------------------------------------------
    # {BaseStr, CompStr} 변수는 1글자로된 단순 문자열이 아닐 수도 있다.
    # GetEditDistance_NGram() 함수에서도 호출하는데 이 때에는 항목이 2글자 이상이다. 
    # 아래 코드에서 인덱스 방식으로 처리하므로 개별 항목에 대한 
    # 길이와 관계없이 처리하므로 길이에 영향을 받지 않는다.
    #--------------------------------------------
    BaseLen = len(BaseStr)
    CompLen = len(CompStr)
    #
    #=#-----------
    #=#--- type 1: {type 2}와 같으며, 2차원 배열 로직 때문에 {BaseLen, CompLen} 변수 위치가 다르다.
    #=#-----------
    #=DisTable = []
    #=for _ in range(BaseLen + 1):
    #=    base_line = []
    #=    for _ in range(CompLen + 1):
    #=        base_line.append(0)
    #=    DisTable.append(base_line)
    #=#-----------
    #=#--- type 2:
    #=#-----------
    DisTable = [[0 for _ in range(CompLen + 1)] for _ in range(BaseLen + 1)] 
    #
    for i in range(1, BaseLen + 1):
        DisTable[i][0] = i
    for j in range(1, CompLen + 1):
        DisTable[0][j] = j
    #=print(*DisTable, sep='\n'), print()
    #
    for j in range(1, CompLen + 1):
        for i in range(1, BaseLen + 1):
            SubstitutionCost = 1
            if((i <= BaseLen) and (j <= CompLen)):
                if BaseStr[i-1] == CompStr[j-1]:
                    SubstitutionCost = 0
                #=print(f'[{i}:{j}] [{BaseStr[i-1]}:{CompStr[j-1]}]')
            DelVal = DisTable[i-1][j] + 1   # deletion 
            InsVal = DisTable[i][j-1] + 1   # insertion
            SubVal = DisTable[i-1][j-1] + SubstitutionCost # substitution
            DisTable[i][j] = min([DelVal, InsVal, SubVal])
            if(DebugPrint == True):
                BaseChar = BaseStr[i-1] # 인덱스는 '+1'된 상태이므로 원래 문자열의 글자는 '-1' 해야 한다.
                CompChar = CompStr[j-1] # 인덱스는 '+1'된 상태이므로 원래 문자열의 글자는 '-1' 해야 한다.
                print(f'[{i}:{j}] ({BaseChar},{CompChar})<{DisTable[i][j]}> ', end='')
                print(f'D:{DelVal}, I:{InsVal}, S:{SubVal}')
    #
    if(DebugPrint == True):
        print(), 
        #=print(*DisTable, sep='\n') # 이렇게 출력하면 가로,세로가 바뀐 상태로 보임
        for j in range(CompLen + 1):
            for i in range(BaseLen + 1):
                print(DisTable[i][j], end='\t')
            print()
        print()
    #
    Distance = DisTable[BaseLen][CompLen]
    #
    if(Norm == True):
        NormLen = max([BaseLen, CompLen])
        if(NormLen > 0):
            NormSimilarity = (NormLen - Distance) / NormLen
            if(NormSimilarity > 1):
                assert False
            Distance = 1 - NormSimilarity # NormSimilarity는 유사도를 의미하므로 거리 개념으로 바꿈
    #
    return Distance

#---------------------------------
#---------------------------------
def RunHgdistance_WordDict(WordDicts_Base,  WordDict_Comp, 
    run_type = 1,
    comp_textfile=None, # {run_type = 5,6,8}에서만 사용, 나머지는 사용하지 않음
    encoding='utf-8', # {run_type = 5,6,8}에서만 사용, 나머지는 사용하지 않음
    DelDocNumRate=0, # 지우지 않는다.
    DelFreq=0, # 지우지 않는다.
    ):
    r'''#------------------------------------------------------
    #------------------------------------------------------
    #----- 여러 가지 유형(함수)을 이용해서 유사도를 계산해본다.
    #------------------------------------------------------
    #------------------------------------------------------
    #run_type = 1   # <=== [tfidf]값 적용, 이 방식이 가장 단순하다.
    #--run_type = 2  # <=== [tfidf]값 적용, 
    #--run_type = 3  # <=== [tfidf]값이 아니라 [freq]방식으로 처리
    #run_type = 4  # <=== [tfidf]값이 아니라 [freq]방식으로 처리
    #run_type = 5   # <=== [tfidf]값 적용, 
    #run_type = 6   # <=== [tfidf]값이 아니라 [freq]방식으로 처리
    #run_type = 7  # <=== [tfidf]값이 아니라 [freq]방식으로 처리하
    #run_type = 8  # <=== [tfidf]값이 아니라 [freq]방식으로 처리하기 때문에 어색하다.
    #------------------------------------------------------
    #------------------------------------------------------
    '''

    print('#================================')
    print('trans word-dicts to dict-freqs, trans dict-freqs to word-matrix, dict-freqs-tfidf')
    HGDistance_Gate = HGDistance(WordDicts=WordDicts_Base, DelDocNumRate=DelDocNumRate, DelFreq=DelFreq)
    #=print(WordDicts_Base[0][:10])

    ResultCosDistances = None

    #
    TFIDFMode = None

    if(run_type == 1): # [freq] word-dict format version
        TFIDFMode = True

        #=WordDict_Find = HGDistance_Gate.WordDicts_TFIDF[0] # test 첫 번째 문서로 유사도 행렬 구하기
        WordDict_Find = WordDict_Comp
        ResultCosDistances = HGDistance_Gate.Predict_WordDict_Tfidf(WordDict_Find)
        #-----------------------
        #@@@ 은 (run_type == 1)과 결과가 같다.
        #    이 구간에 넘어오기 전에 이미 {tfidf}값으로 바뀌어 있는 상태이다.
        #-----------------------

    elif(run_type == 2): # [tfidf] dict-freq format version
        # (run_type == 2)는 (run_type == 1)을 변형해서 만든 것이다.

        #
        TFIDFMode = True

        #===== make-tfidf
        WordMatrix = HGDistance_Gate.DocWordMatrix['word']
        
        BuildWordDict_TermFreq(WordDict_Comp)
        BuildWordDict_TFIDF(WordDict_Comp, WordMatrix, HGDistance_Gate.DocWordMatrix['DocNum'], 
            IDFSmooth=HGDistance_Gate.IDFSmooth, Norm=HGDistance_Gate.Norm)

        #------------
        # Predict_DictFreq_Tfidf__() 함수에서 tfidf 값으로 계산하려면 
        # test 용 데이터도 반드시 값으로 변환해줘야 한다.
        #------------
        #=print(WordDict_Comp[0])  # value: freq
        DictFreq_Find = {dic_i['word']:dic_i['tfidf'] for dic_i in WordDict_Comp} # value: tfidf
        #=print(DictFreq_Find)  # value: tfidf

        ResultCosDistances = HGDistance_Gate.Predict_DictFreq_Tfidf__(DictFreq_Find)

        #-----------------------
        #@@@ (run_type == 2)은 (run_type == 1)과 결과가 같다.
        #    word-dict 형식을 dict-freq 형식으로 변환한 것이다.
        #    변환하기 전에 이 구간에 넘어오기 전에 
        #    이미 {tfidf}값으로 바뀌어 있는 상태라서 (run_type == 1)과 결과가 같다.
        #
        #    이 코드는 내부 처리 과정을 분해한 후에 
        #    테스트를 위한 것으로 사용법이 복잡해서 사용하지 않도록 유도한다.
        #    ==> 이 방식은 사용하지 않는다.
        #-----------------------

    elif(run_type == 3): # [freq] dict-freq format version
        #------------
        from hgdict import GetDictFreq__WordDictList

        #------------
        #=print(WordDict_Comp[0])  # value: freq
        DictFreq_Find = GetDictFreq__WordDictList(WordDict_Comp) # value: freq
        #=print(DictFreq_Find)  # value: freq 

        ResultCosDistances = HGDistance_Gate.Predict_DictFreq_Freq__(DictFreq_Find)

        #-----------------------
        #@@@ 빈도값으로 코사인 유사도를 계산하니까 수치가 달라질 뿐 
        #    전체적인 결과는 비슷하다.
        #-----------------------
    elif(run_type == 4): # [freq] dict-freq & word-dict format version
        #------------
        #=print(WordDict_Comp[0])  # value: freq
        ResultCosDistances = HGDistance_Gate.Predict_WordDict_Freq(WordDict_Comp)

        #-----------------------
        #@@@ 빈도값으로 코사인 유사도를 계산하니까 수치가 달라질 뿐 
        #    전체적인 결과는 비슷하다.
        #-----------------------
    elif(run_type == 5): # [tfidf] word-list format version
        #
        TFIDFMode = True

        # (run_type == 5)는 (run_type == 1)을 변형해서 만든 것이다.
        # Predict_WordList_Tfidf()함수에서 <WordList>를 <WordDict>로 변환한다.
        #------------
        WordList_Test = GetWordList_TpxFile(comp_textfile, encoding=encoding)
        #=print(WordList_Test[0])  # value: string
        ResultCosDistances = HGDistance_Gate.Predict_WordList_Tfidf(WordList_Test)
    elif(run_type == 6): # [freq] word-list format version
        # (run_type == 6)는 (run_type == 4)을 변형해서 만든 것이다.
        # Predict_WordList_Freq()함수에서 <WordList>를 <WordDict>로 변환한다.
        #------------
        WordList_Test = GetWordList_TpxFile(comp_textfile, encoding=encoding)
        #=print(WordList_Test[0])  # value: string
        ResultCosDistances = HGDistance_Gate.Predict_WordList_Freq(WordList_Test)

        #-----------------------
        #@@@ 빈도값으로 코사인 유사도를 계산하니까 수치가 달라질 뿐 
        #    전체적인 결과는 비슷하다.
        #-----------------------
    elif(run_type == 7): # [freq] word-dict format version
        #=print(WordDict_Comp[0])  # value: freq
        #=print(WordDicts_Base[0][:10])

        #-----
        # 필터 처리로 학습용 목록에서 단어를 제외시킨다.
        #-----
        import copy
        WordDicts_New = copy.deepcopy(WordDicts_Base)
        WordMatrix = HGDistance_Gate.DocWordMatrix['word']

        DeleteWordDicts_ByWordDict(WordDicts_New, WordMatrix, DelType='not')
        #=print(WordDicts_New[0][:10])

        #-----
        #-----
        ResultCosDistances = HGDistance_Gate.Calc_WordDicts_WordDict_Freq(WordDicts_New, WordDict_Comp)

        #-----------------------
        #@@@ 빈도값으로 코사인 유사도를 계산하니까 수치가 달라질 뿐 
        #    전체적인 결과는 비슷하다.
        #-----------------------
    elif(run_type == 8): # [freq] word-list format version
        # (run_type == 8)는 (run_type == 7)을 변형해서 만든 것이다.
        # Calc_WordDicts_WordList_Freq()함수에서 <WordList>를 <WordDict>로 변환한다.
        #------------
        WordList_Test = GetWordList_TpxFile(comp_textfile, encoding=encoding)
        #=print(WordList_Test[0])  # value: string
        #=print(WordDicts_Base[0][:10])

        #-----
        # 필터 처리로 학습용 목록에서 단어를 제외시킨다.
        #-----
        import copy
        WordDicts_New = copy.deepcopy(WordDicts_Base)
        WordMatrix = HGDistance_Gate.DocWordMatrix['word']

        DeleteWordDicts_ByWordDict(WordDicts_New, WordMatrix, DelType='not')
        #=print(WordDicts_New[0][:10])

        #-----
        #-----
        ResultCosDistances = HGDistance_Gate.Calc_WordDicts_WordList_Freq(WordDicts_New, WordList_Test)

        #-----------------------
        #@@@ 빈도값으로 코사인 유사도를 계산하니까 수치가 달라질 뿐 
        #    전체적인 결과는 비슷하다.
        #-----------------------

    #    
    return HGDistance_Gate, ResultCosDistances, TFIDFMode

