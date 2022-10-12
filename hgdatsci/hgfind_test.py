import hgsysinc

def Find_1_Subword(InputWord, Vocabulary, debugPrint=False):
    # 첫 번째 글자를 제외하고 두 번째 글자부터 부분 단어 만들기
    #-----
    #=InputWord = 'fovern'
    #=InputWord = 'fovernment'
    SubWord = InputWord[1:] # 두 번째 글자부터 단어 만듦
    #
    print('input:', InputWord)
    print('sub input:', SubWord)
    print('순서: 단어(빈도)')
    
    # 사전에서 부분 문자열 일치 탐색
    FindNum = 0
    for Dict in Vocabulary: 
        if(Dict.find(SubWord) >= 0):
            FindNum += 1
            print(f'{FindNum}: {Dict}({Vocabulary[Dict]})')
            #=print(f'{FindNum}: {Dict}')
    #----------------
    #----------------
    if(debugPrint != True):
        return
    print()
    print('#-------------------------')
    print('# 빈도순 정렬')
    print('#-------------------------')
    IncludeDic = {}
    for Dict in Vocabulary: 
        if(Dict.find(SubWord) >= 0):
            IncludeDic[Dict] = Vocabulary[Dict]
    print (IncludeDic)

    # sort by high 
    dict_by_keys = sorted(IncludeDic.items(), key=lambda item: -item[1]) # by high
    IncludeDic_High = {dic[0]:dic[1] for dic in dict_by_keys} 
    print('# 빈도순 정렬:', IncludeDic_High)

    #=print(), print(*IncludeDic_High.items(), sep='\n')

    print()
    print('순서: 단어\(빈도)')
    for i, Dict in enumerate(IncludeDic_High):
        print(f'{i+1}: {Dict}({Vocabulary[Dict]})')
    print(),print(),

    print('#-------------------------')
    print('# 편집 거리 계산')
    print('#-------------------------')
    from hgdistance import GetEditDistance
    
    IncludeDic_Distance = {}
    for DictWord in Vocabulary: 
        if(DictWord.find(SubWord) >= 0):
            EditDistance = GetEditDistance(InputWord, DictWord)
            #=print('EditDistance:', EditDistance)
            WordFreq = Vocabulary[DictWord]
            IncludeDic_Distance[DictWord] = [EditDistance, WordFreq]
    print('# 편집 거리 계산:', IncludeDic_Distance)

    # sort by low 
    dict_by_keys = sorted(IncludeDic_Distance.items(), key=lambda item: item[1][0]) # by low

    print('순서: 단어\t[편집거리, 빈도]')
    for i, Dict_i in enumerate(dict_by_keys):
        print(f'{i+1}: {Dict_i[0]}\t{Dict_i[1]}')
    print(),print(),

    print('#-------------------------')
    print('# 다시 사전형(dict)으로 변환')
    print('#-------------------------')
    IncludeDic_High = {dic[0]:dic[1] for dic in dict_by_keys} 
    print(IncludeDic_High)

    #=print(), print(*IncludeDic_High.items(), sep='\n')

    print()
    for i, Dict in enumerate(IncludeDic_High):
        print(f'{i+1}: {Dict}({IncludeDic_High[Dict][0]}, {IncludeDic_High[Dict][1]})')
    print()

    for i, Dict in enumerate(IncludeDic_High):
        print(f'{i+1}\t{Dict}\t{IncludeDic_High[Dict][0]}\t{IncludeDic_High[Dict][1]}')
    print()

def Check_1_Subword(InputWord, Vocabulary, debugPrint=False):
    # 첫 번째 글자를 제외하고 두 번째 글자부터 부분 단어 만들기
    #-----
    from hgdistance import GetEditDistance
    #-----
    SubWord = InputWord[1:] # 두 번째 글자부터 단어 만듦
    #
    print('input:', InputWord)
    print('sub input:', SubWord)

    # 부분 문자열을 포함한 단어를 찾아서 편집 거리 계산
    IncludeDic_Distance = {}
    for DictWord in Vocabulary: 
        if(DictWord.find(SubWord) >= 0):
            EditDistance = GetEditDistance(InputWord, DictWord)
            #=print('EditDistance:', EditDistance)
            WordFreq = Vocabulary[DictWord]
            IncludeDic_Distance[DictWord] = [EditDistance, WordFreq]
    if(debugPrint == True):
        print (IncludeDic_Distance)
        print()

    # 편집 거리 오름차순 정렬: format : {'word':[distance, freq], ...}
    dict_by_keys = sorted(IncludeDic_Distance.items(), key=lambda item: item[1][0]) # by low

    print('순서: 단어\t[편집거리, 빈도]')
    for i, Dict_i in enumerate(dict_by_keys):
        print(f'{i+1}: {Dict_i[0]}\t{Dict_i[1]}')
    print(),print(),print(),

def Check_3_Subword(InputWord, Vocabulary, debugPrint=False):
    #-----
    from hgdistance import GetEditDistance
    #-----
    # 세 번째 글자까지 제외하고 네 번째 글자부터 부분 단어 만들기
    #=InputWord = 'gobernment'
    SubWord = InputWord[3:] # 네 번째 글자부터 단어 만듦
    #
    print('input:', InputWord)
    print('sub input:', SubWord)

    # 편집 거리 계산
    IncludeDic_Distance = {}
    for DictWord in Vocabulary: 
        if(DictWord.find(SubWord) >= 0):
            EditDistance = GetEditDistance(InputWord, DictWord)
            #=print('EditDistance:', EditDistance)
            WordFreq = Vocabulary[DictWord]
            IncludeDic_Distance[DictWord] = [EditDistance, WordFreq]
    if(debugPrint == True):
        print (IncludeDic_Distance)
        print()

    # sort by low 
    dict_by_keys = sorted(IncludeDic_Distance.items(), key=lambda item: item[1][0]) # by low

    print('순서: 단어\t[편집거리, 빈도]')
    for i, Dict_i in enumerate(dict_by_keys):
        print(f'{i+1}: {Dict_i[0]}\t{Dict_i[1]}')
    print(),print(),print(),

    if(debugPrint == True):
        print('#-------------------------')
        print('# 다시 사전형(dict)으로 변환')
        print('#-------------------------')
        IncludeDic_High = {dic[0]:dic[1] for dic in dict_by_keys} 
        print(), print(IncludeDic_High)

        #=print(), print(*IncludeDic_High.items(), sep='\n')

        print()
        for i, Dict in enumerate(IncludeDic_High):
            print(f'{i+1}: {Dict}({IncludeDic_High[Dict][0]}, {IncludeDic_High[Dict][1]})')
        print()

        for i, Dict in enumerate(IncludeDic_High):
            print(f'{i+1}\t{Dict}\t{IncludeDic_High[Dict][0]}\t{IncludeDic_High[Dict][1]}')
        print()
