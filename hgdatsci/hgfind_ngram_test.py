#---
#---
from hgworddistance import PrintNGramVocabulary_WordList
from hgworddistance import MakeStringNGram
from hgkbd import HGTransString2KBDJamo
from hgdistance import GetEditDistance
#-----------------------
#-----------------------
def TestNGramDict_KBDJamo(NGramVocabulary, FindWord, NGram=1, 
    SpellCheckMode=False,
    EditDistanceLimit=False, # 편집을 위해서 필요하다.
    debugPrint=False,
    ):
    #=print('NGram:', NGram)
    #=FindWord = '란국경ㅈ' # '한국경ㅈ'의 철자 오류 입력
    #=FindWord = '란국' # '한국'의 철자 오류 입력
    FindWord_KBDjamo = HGTransString2KBDJamo(FindWord)
    FindWord_KBDjamo_Len = len(FindWord_KBDjamo)

    #---------
    NGramList = MakeStringNGram(FindWord_KBDjamo, NGram=NGram, MoreThan=True)

    if(debugPrint == True):
        #---------
        # 편집 코드
        #---------
        # 기본 목록 출력
        print(), print(f'@@@ [코드] 순서 : 문자열 : 문자열 길이 : 포함된 어휘수 @@@')
        #=NGramListLen = len(NGramList)
        PrintNGramVocabulary_WordList(NGramVocabulary, NGramList, PrintNum=0, LeadingString='')

        # 길이순 정렬(길이가 긴 것을 가중치 높게 주기 위해서 앞에서 먼저 검사하도록 함)
        NGramList = sorted(NGramList, key=lambda item: -len(item)) # by high

        # 기본 목록 출력
        print(), print(f'@@@ [길이] 순서 : 문자열 : 문자열 길이 : 포함된 어휘수 @@@')
        #=NGramListLen = len(NGramList)
        PrintNGramVocabulary_WordList(NGramVocabulary, NGramList, PrintNum=0, LeadingString='')
            
        # 구체적인 N그램에 포함된 어휘 목록 출력
        #=NGramListLen = len(NGramList)
        for inx, dic_f in enumerate(NGramList):
            NGramDicVocabulary = NGramVocabulary.get(dic_f)
            if(NGramDicVocabulary == None): # n-gram에 속하는 단어가 없는 경우
                #=print('NGramList[', dic_f, '] - (NGramDicVocabulary == None)', )
                continue
            #=print(f'NGramList({dic_f}): {len(NGramDicVocabulary)} {NGramDicVocabulary}')
            #=NGramDicVocabulary_format: [{'key': 'roqkfwpgksrndur', 'word': '개발제한구역', 'weight': 7}, ...]
            NGramDicVocabularyNum = len(NGramDicVocabulary)

            print(), print()
            print(), print(f'@@@  {inx+1} : {dic_f} : {len(dic_f)} : {NGramDicVocabularyNum}  @@@')
            
            for sub_j, NGDic_I in enumerate(NGramDicVocabulary):
                print(f"{sub_j+1} :", NGDic_I)
                #=format: {'key': 'roqkfwpgksrndur', 'word': '개발제한구역', 'weight': 7}
                #=print(f"{sub_j+1} : {NGDic_I['word']} : {NGDic_I['weight']}")

            print_msg_string = ''
            for sub_j, NGDic_I in enumerate(NGramDicVocabulary):
                print_msg_string += f"{NGDic_I['word']}({NGDic_I['weight']}), "
                #=format: {'key': 'roqkfwpgksrndur', 'word': '개발제한구역', 'weight': 7}
                #=print(f"{sub_j+1} : {NGDic_I['word']} : {NGDic_I['weight']}")
            print(print_msg_string)

        print(), print(), print()

    
    #===================
    #===================
    #===================
    # '편집 거리 계산'
    if(SpellCheckMode == True): # 철자 교정 상태
        print(), print ('편집 거리 계산: 검색어랑 편집 거리가 가까운 단어만 선택')
        MinDistance = (-1) # '0': 똑같은 단어는 '0'이라서 이보다 작은 초깃값
    else:
        print(), print ('편집 거리 계산')
    #---
    NGDic_Distance = {}

    EditDistanceCount = 0 # 편집용 코드
    MinDistance_NGramWord = '' # 편집용 코드
    for inx, dic_f in enumerate(NGramList):
        NGramDicVocabulary = NGramVocabulary.get(dic_f)
        if(NGramDicVocabulary == None): # n-gram에 속하는 단어가 없는 경우
            #=print('NGramList[', dic_f, '] - (NGramDicVocabulary == None)', )
            continue
        #=print(f'NGramList({dic_f}): {len(NGramDicVocabulary)} {NGramDicVocabulary}')
        #=NGramDicVocabulary_format: [{'key': 'roqkfwpgksrndur', 'word': '개발제한구역', 'weight': 7}, ...]
        #=NGramDicVocabularyNum = len(NGramDicVocabulary)

        for sub_j, NGDic_I in enumerate(NGramDicVocabulary):
            #=print(f"{sub_j+1} :", NGDic_I)
            #=format: {'key': 'roqkfwpgksrndur', 'word': '개발제한구역', 'weight': 7}
            #=print(f"{sub_j+1} : {NGDic_I['word']} : {NGDic_I['weight']}")

            NGDic_Jamo = NGDic_I['key']
            #=NGDic_Word = NGDic_I['word']
            #=NGDic_weight = NGDic_I['weight']

            EditDistance = GetEditDistance(FindWord_KBDjamo, NGDic_Jamo)
            #=print('EditDistance:', EditDistance)
            EditDistanceCount += 1 # 편집용 코드

            if(EditDistanceLimit == True):
                # 편집 거리가 검색어 길이와 같으면 완전히 다른 관련 없는 단어다.
                if(EditDistance >= FindWord_KBDjamo_Len): # 편집 거리가 검색어 길이와 같으면 완전히 다른 관련 없는 단어다.
                    continue # 완전히 다른 단어이면 모으지 않고 통과한다.

            #============================
            #============================
            if(SpellCheckMode == True): # 철자 교정 상태
                # 가장 가까운 편집 거리 찾기
                if(MinDistance < 0): # 처음 비교하는 경우
                    MinDistance = EditDistance
                    MinDistance_NGramWord = dic_f # 편집용 코드
                else:
                    if(MinDistance < EditDistance): # 최소 편집 거리보다 크면 제외
                        continue
                    elif(MinDistance == EditDistance): # 최소 편집 거리와 같은 경우:등록
                        pass
                    else: # 최소 편집 거리보다 작은 경우: 새로 등록하기 위해 초기화
                        MinDistance = EditDistance
                        NGDic_Distance.clear()
                        MinDistance_NGramWord = dic_f # 편집용 코드
            else: # 전체 목록을 찾아서 출력할 때(편집용)
                pass # 가장 가까운 편집 거리를 찾지 말고 모두 선택(전체 목록을 찾을 때)
            #
            #=NGDic_Item = [NGDic_Word, EditDistance, NGDic_weight]
            #=NGDic_Distance[NGDic_Jamo] = NGDic_Item
            NGDic_Distance[NGDic_Jamo] = \
                [NGDic_I['word'], EditDistance, NGDic_I['weight']]
    #
    if(SpellCheckMode == True): # 철자 교정 상태
        print(), print(NGDic_Distance)
        print(), 

    if(debugPrint == True):
        print('# 편집용 코드')
        print('EditDistanceCount:', EditDistanceCount)
        print('MinDistance_NGramWord:', MinDistance_NGramWord) # 어는 N그램에서 찾았는지 확인
        print(), 

    #============================
    #============================
    #============================
    if(SpellCheckMode == True): # 철자 교정 상태
        if(debugPrint == True):
            print ('#--------------------')
            print ('#--------------------')
            print ('#--------------------')
            print ('# 아래 블록은 편집용 코드 - 빈도 정렬하기 전 상태(코드 순서)로 출력이 필요')
            print ('#--------------------')
            print ('편집 거리 정렬') # (sort by low)
            dict_by_keys = sorted(NGDic_Distance.items(), key=lambda item: item[1][1]) # by low
            IncludeDic_High = {dic[0]:dic[1] for dic in dict_by_keys} 
            #=print(), print(IncludeDic_High)
            #=print(), print(*IncludeDic_High.items(), sep='\n')

            print('#--------------------')
            print('# 편집용 코드 - 탭 출력')
            print('#--------------------')
            if(FindWord_KBDjamo != FindWord): # 두벌식 자모 
                print ('순서\t두벌식 자모\t음절(원래 단어)\t편집 거리\t빈도')
            else: # 바뀐 것이 없는 상태
                print ('순서\tKey\tWord\t편집 거리\t빈도')
            for i, Dict in enumerate(IncludeDic_High):
                print(f'{i+1}\t{Dict}\t', end='')
                print(*IncludeDic_High[Dict], sep='\t')
            print ('#--------------------')
            print ('#--------------------')
            print ('#--------------------')

        #============================
        #============================
        #============================
        # 철자 교정 상태(SpellCheckMode == True)일 경우에는 최소 편집 거리 항목만 모았기 때문에 
        # 가중치(빈도) 정렬을 하면 교정 후보가 된다.
        #============================
        #============================
        #============================
        print(), print ('가중치(빈도) 정렬') # (sort by high)
        dict_by_keys = sorted(NGDic_Distance.items(), key=lambda item: -item[1][2]) # by high
        #=IncludeDic_High = dict(dict_by_keys)
        IncludeDic_High = {dic[0]:dic[1] for dic in dict_by_keys} 
        #=print(), print(IncludeDic_High)
        #=print(), print(*IncludeDic_High.items(), sep='\n')

        #= from hgbasic import PrintDict_KeyValue_ByLine
        #= PrintDict_KeyValue_ByLine(IncludeDic_High) # 편집용 코드
        #= PrintDict_KeyValue_ByLine(IncludeDic_High, SepChar='\t') # 편집용 코드 - 탭 출력
        
        print ('순서: key([word, distance, freq)]')
        for i, Dict in enumerate(IncludeDic_High):#format:{key: [word, distance, freq)], ...}
            print(f'{i+1}: ', f'{Dict}({IncludeDic_High[Dict]})')
        
        if(debugPrint == True):
            print('#--------------------')
            print('# 편집용 코드 - 탭 출력')
            print('#--------------------')
            if(FindWord_KBDjamo != FindWord): # 두벌식 자모 
                print ('순서\t두벌식 자모\t음절(원래 단어)\t편집 거리\t빈도')
            else: # 바뀐 것이 없는 상태
                print ('순서\tKey\tWord\t편집 거리\t빈도')
            for i, Dict in enumerate(IncludeDic_High):
                print(f'{i+1}\t{Dict}\t', end='')
                print(*IncludeDic_High[Dict], sep='\t')
            print()

        #============================
        #============================
        #============================
        for Dict in IncludeDic_High: # format: {key: [word, distance, freq)], ...}
            OriginWord = IncludeDic_High[Dict][0]
            print(f"<{FindWord}> 이 단어가 맞나요? ===>", OriginWord)
            break # 첫 번째 위치한 교정 단어를 찾으면 루프 탈출
    else:
        # '편집 거리 정렬'
        print(), print ('편집 거리 정렬') # (sort by low)
        dict_by_keys = sorted(NGDic_Distance.items(), key=lambda item: item[1][1]) # by low
        #=IncludeDic_High = dict(dict_by_keys)
        IncludeDic_High = {dic[0]:dic[1] for dic in dict_by_keys} 
        #=print(), print(IncludeDic_High)
        #=print(), print(*IncludeDic_High.items(), sep='\n')

        print ('순서: key([word, distance, freq)]')
        for i, Dict in enumerate(IncludeDic_High):#format:{key: [word, distance, freq)], ...}
            print(f'{i+1}: ', f'{Dict}({IncludeDic_High[Dict]})')
        
        if(debugPrint == True):
            print('#--------------------')
            print('# 편집용 코드 - 탭 출력')
            print('#--------------------')
            if(FindWord_KBDjamo != FindWord): # 두벌식 자모 
                print ('순서\t두벌식 자모\t음절(원래 단어)\t편집 거리\t빈도')
            else: # 바뀐 것이 없는 상태
                print ('순서\tKey\tWord\t편집 거리\t빈도')
            for i, Dict in enumerate(IncludeDic_High):
                print(f'{i+1}\t{Dict}\t', end='')
                print(*IncludeDic_High[Dict], sep='\t')













