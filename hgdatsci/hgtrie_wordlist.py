#--------------------
#--------------------
class HGTrieNode(): 
    def __init__(self):
        self.Child = {}
        self.WordState = False # 현재 노드가 단어임을 알려줌

#--------------------
#--------------------
class HGTrie(): # wordlist 방식으로 구현
    def __init__(self): 
        self.Root = HGTrieNode() 
        self.PrefixResult = [] 

    def InsertWord(self, Word): 
        CurNode = self.Root 
        for Char in Word: 
            if not CurNode.Child.get(Char): # child 노드가 없으면 생성
                CurNode.Child[Char] = HGTrieNode() 
                #=print('New Node:', Word + Char)
            CurNode = CurNode.Child[Char] # child 노드로 이동
        #
        CurNode.WordState = True  # 현재 노드가 단어임을 알려줌
        #=print('Node:', Word)

    def MakeTrie__WordList(self, WordList):
        #=print('WordList:', len(WordList))
        for Word in WordList:
            self.InsertWord(Word)

    def FindNode(self, FindWord):
        CurNode = self.Root 
        for Char in FindWord:
            if not CurNode.Child.get(Char):
                return None
            CurNode = CurNode.Child[Char]
        return CurNode

    def FindAllWord(self, CurNode, PrefixWord): 
        if CurNode.WordState: # 현재 노드가 단어인 경우
            self.PrefixResult.append(PrefixWord)
        # child 노드에서 단어 찾아서 등록
        for Char, Node_s in CurNode.Child.items():
            self.FindAllWord(Node_s, PrefixWord + Char) 

    def GetPrefixList(self, FindWord):
        #
        self.PrefixResult = []
        SearchNode = self.FindNode(FindWord)
        if SearchNode == None: # no word
            return self.PrefixResult
        else:
            self.FindAllWord(SearchNode, FindWord)
            return self.PrefixResult

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
            TraverseNode = self.FindNode(FindWord)
            if TraverseNode == None: # no word
                pass
            else:
                self.PrintNode(TraverseNode, FindWord)

    def PrintChild(self, FindWord=None):
        print(f'{FindWord}')
        if(FindWord == None):
            CurNode = self.Root
        else:
            CurNode = self.FindNode(FindWord)
            if CurNode == None: # no word
                return

        #
        CharNum = 1
        for Char, Node_s in CurNode.Child.items(): 
            print(f'{CharNum}, {Char} ({len(Node_s.Child)})')
            CharNum += 1


#====================================
#====================================
WordList_a = ['abandon','ability','able','ably','abnormal','about','above',
    'abroad','absolute','absolutely','abuse','academy','accept',
    'access','account','achieve','achievement','acknowledge','acknowledgment',
    'acquire','across','act','acting','action','active','actively',
    'activism','activity','actual','actually','add','addition','address',
    'administer','administrate','administration','administrator','admission',
    'admit','adopt','adoption','advance','advanced','adventure','advice',
    'advise','adviser','affect','affection','after','again','against','age',
    'agency','agent','ago','agree','agreement','aim','air','airport','alarm',
    'alert','alien','alive','all','alliance','allocate','allow','almost','alone',
    'along','already','also','always','among','amount','ancient','and','angel',
    'anger','angry','animate','animation','announce','another','answer','ant',
    'anxiety','anxious','anxiously','any','anybody','anymore','anyone','anything',
    'anywhere','apologize','apology','appear','appearance','apply','appoint','approach',
    'approval','approve','area','argue','argument','arm','armed','arms','army','arrange',
    'arrangement','array','arrest','arrive','art','artist','as','ask','asking','asleep',
    'aspect','assemble','assembly','assert','assignment','assist','astronaut','at',
    'atmosphere','atom','attach','attachment','attack','attempt','attend','attendant',
    'attention','attentive','attitude','audience','author','authority','authorize',
    'autonomy','auxiliary','avail','available','avoid','avoidance',
]

WordList_ap = ['apology','appear','appearance',
    'apply','appoint','approach', 'approval','approve',
]

#=WordList_ag = ['again', 'age', 'agent', 'ago', 'agree',]
WordList_ag = ['age', 'agent', 'ago', 'again', 'agree',]

WordList_aX = ['able','about','abroad', #@
    'accept','account','achieve','across','act','action',
    'add','admit','adopt','advice', #@
    'after', #@
    'again','age','ago','agree', 
    'air','airport', #@
    'alarm','alive','all','almost','along','already','also',
    'and','angel','answer','ant','any',
    'apology','appear','apply','appoint','approach','approve',
    'area','argue','arm','army','array','art',
    'at','atom','attach','attachment','attack','attempt','attend','attendant',
    'attention','attentive','attitude',
    'author','authority','authorize','autonomy','auxiliary',
    'avail','available','avoid','avoidance',
]


#=if __name__ == '__main__':
    #=main()



'''
처리결과:
=================


'''
