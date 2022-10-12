#================================
#================================
#================================
class HGTrieNode_naive_l(): 
    def __init__(self):
        self.Child = {}
        self.WordState = False # 현재 노드가 단어임을 알려줌

#--------------------
#--------------------
class HGTrie_naive_l(): # wordlist 방식으로 구현
    def __init__(self): 
        self.Root = HGTrieNode_naive_l() 
        self.PrefixResult = [] 

    def InsertWord(self, Word): 
        CurNode = self.Root 
        for Char in Word: 
            if not CurNode.Child.get(Char):
                CurNode.Child[Char] = HGTrieNode_naive_l() 
                #=print('New Node:', Word + Char)
            CurNode = CurNode.Child[Char] 
        #
        CurNode.WordState = True # 현재 노드가 단어임을 알려줌
        #=print('Node:', Word)

    def MakeTrie__WordList(self, WordList):
        #=print('WordList:', len(WordList))
        for Word in WordList:
            self.InsertWord(Word)

    def TraverseNode(self, FindWord, ExactEnd=True):
        CurNode = self.Root 
        for Char in FindWord:
            if not CurNode.Child.get(Char):
                return None
            CurNode = CurNode.Child[Char]
        if(ExactEnd == True): # 종단 노드 검사
            if(CurNode.WordState == True): # 현재 노드가 단어인 경우
                return CurNode
            else:
                return None
        else: # ExactEnd=False: 검색어를 포함한 것도 찾기
            return CurNode

    def FindAllWord(self, CurNode, FindWord): 
        if CurNode.WordState: # 현재 노드가 단어인 경우
            self.PrefixResult.append(FindWord)
        for Char, Node_s in CurNode.Child.items():
            self.FindAllWord(Node_s, FindWord + Char) 

    def PrintNode(self, CurNode, CurWord):
        if CurNode.WordState: # 현재 노드가 단어인 경우
            self.PrintCnt += 1
            print(f'{self.PrintCnt}, {CurWord}')

        for Char, Node_s in CurNode.Child.items(): 
            self.PrintNode(Node_s, CurWord + Char) 

    def PrintTrie(self, FindWord=None):
        print()
        self.PrintCnt = 0
        if(FindWord == None):
            self.PrintNode(self.Root, '')
        else:
            TraverseNode = self.TraverseNode(FindWord, ExactEnd=False) # ExactEnd=False: 검색어를 포함한 것도 찾기
            if TraverseNode == None: # no word
                pass
            else:
                self.PrintNode(TraverseNode, FindWord)

    def PrintChild(self, FindWord=None):
        print()
        if(FindWord == None):
            CurNode = self.Root
        else:
            CurNode = self.TraverseNode(FindWord, ExactEnd=False) # ExactEnd=False: 검색어를 포함한 것 찾기
            if CurNode == None: # no word
                return
        #
        print(f'{FindWord} ({len(CurNode.Child)})')
        CharNum = 1
        for Char, Node_s in CurNode.Child.items(): 
            print(f'{CharNum}, {Char} ({len(Node_s.Child)})')
            CharNum += 1

    def GetPrefixList(self, FindWord):
        #
        self.PrefixResult = []
        SearchNode = self.TraverseNode(FindWord, ExactEnd=False) # ExactEnd=False: 검색어를 포함한 것 찾기
        if SearchNode == None: # no word
            return self.PrefixResult
        elif not SearchNode.Child: # no child
            return self.PrefixResult
        else:
            self.FindAllWord(SearchNode, FindWord)
            return self.PrefixResult
        

#================================
#================================
#================================
class HGTrieNode_naive_d(): 
    def __init__(self, Weight=0):
        self.Child = {}
        self.WordState = False # 현재 노드가 단어임을 알려줌
        self.Weight = Weight # 가중치 변수 추가

#--------------------
#--------------------
class HGTrie_naive_d(): # dicfreq 방식으로 구현
    def __init__(self): 
        self.Root = HGTrieNode_naive_d() 
        self.PrefixResult = [] 

    def InsertWord(self, Word, Weight=0): 
        CurNode = self.Root 
        for Char in Word: 
            if not CurNode.Child.get(Char):
                CurNode.Child[Char] = HGTrieNode_naive_d() 
                #=print('New Node:', Word + Char)
            CurNode = CurNode.Child[Char] 
        #
        CurNode.WordState = True # 현재 노드가 단어임을 알려줌
        CurNode.Weight = Weight
        #=print('Node:', Word)

    def MakeTrie__WordList(self, WordList):
        #=print('WordList:', len(WordList))
        for Word in WordList:
            self.InsertWord(Word)

    def MakeTrie__DictFreq(self, DictFreq):
        for Word in DictFreq: 
            WordFreq = DictFreq[Word]
            self.InsertWord(Word, Weight=WordFreq)

    def TraverseNode(self, FindWord, ExactEnd=True):
        CurNode = self.Root 
        for Char in FindWord:
            if not CurNode.Child.get(Char):
                return None
            CurNode = CurNode.Child[Char]
        if(ExactEnd == True): # 종단 노드 검사
            if(CurNode.WordState == True): # 현재 노드가 단어인 경우
                return CurNode
            else:
                return None
        else:
            return CurNode

    def FindAllWord(self, CurNode, PrefixWord): 
        if CurNode.WordState: # 현재 노드가 단어인 경우
            self.PrefixResult.append((PrefixWord, CurNode.Weight))#(단어,빈도) 튜플 등록
        # child 노드에서 단어 찾아서 등록
        for Char, Node_s in CurNode.Child.items():
            self.FindAllWord(Node_s, PrefixWord + Char) 

    def GetPrefixList(self, FindWord):
        #
        self.PrefixResult = []
        SearchNode = self.TraverseNode(FindWord, ExactEnd=False) # ExactEnd=False: 검색어를 포함한 것 찾기
        if SearchNode == None: # no word
            return self.PrefixResult
        else:
            self.FindAllWord(SearchNode, FindWord)
            return self.PrefixResult
        
    def PrintNode(self, CurNode, CurWord):
        if CurNode.WordState: # 현재 노드가 단어인 경우
            self.PrintCnt += 1
            print(f'{self.PrintCnt}\t{CurWord} : {CurNode.Weight}')

        for Char, Node_s in CurNode.Child.items(): 
            self.PrintNode(Node_s, CurWord + Char) 

    def PrintTrie(self, FindWord=None):
        print()
        self.PrintCnt = 0
        if(FindWord == None):
            self.PrintNode(self.Root, '')
        else:
            TraverseNode = self.TraverseNode(FindWord, ExactEnd=False) # ExactEnd=False: 검색어를 포함한 것도 찾기
            if TraverseNode == None: # no word
                pass
            else:
                self.PrintNode(TraverseNode, FindWord)

    def PrintChild(self, FindWord=None):
        print()
        if(FindWord == None):
            CurNode = self.Root
        else:
            CurNode = self.TraverseNode(FindWord, ExactEnd=False) # ExactEnd=False: 검색어를 포함한 것 찾기
            if CurNode == None: # no word
                return

        #
        print(f'{FindWord} ({len(CurNode.Child)})')
        CharNum = 1
        for Char, Node_s in CurNode.Child.items(): 
            print(f'{CharNum}, {Char} ({len(Node_s.Child)})')
            CharNum += 1


#================================
#================================
#================================
from unittest import TestCase, main

class HGTest(TestCase):
    #================================
    #================================
    #================================
    def test_trie_1(self): # word-list mode
        WordList_as = ['as','ask','asking','asleep',
            'aspect','assemble','assembly','assert','assignment','assist','astronaut',
        ]

        FindWord = 'ass'
        TrieTest = HGTrie_naive_l() 
        TrieTest.MakeTrie__WordList(WordList_as) 
        SugList = TrieTest.GetPrefixList(FindWord) 
        print()
        print('@@@ WordList Mode @@@')
        print(f'Suggest {len(SugList)}:')
        print(*SugList, sep='\n')

        '''
        @@@ WordList Mode @@@
        Suggest 5:
        assemble
        assembly
        assert
        assignment
        assist        
        '''
    def test_trie_2(self): # dict-freq mode
        DictFreq_as = {'as':1,'ask':2,'asking':3,'asleep':4,
            'aspect':5,'assemble':6,'assembly':7,'assert':8,
            'assignment':9,'assist':10,'astronaut':11,
        }

        FindWord = 'ass'
        TrieTest = HGTrie_naive_d() 
        TrieTest.MakeTrie__DictFreq(DictFreq_as) 
        SugList = TrieTest.GetPrefixList(FindWord) 
        print()
        print('@@@ DictFreq Mode @@@')
        print(f'Suggest {len(SugList)}:')
        #=print(*SugList, sep='\n')
        for ix in SugList:
            print(ix)

        '''
        @@@ DictFreq Mode @@@
        Suggest 5:
        ('assemble', 6)
        ('assembly', 7)
        ('assert', 8)
        ('assignment', 9)
        ('assist', 10)
        '''

if __name__ == '__main__':
    main()



