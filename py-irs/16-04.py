import hgsysinc
from hgtrie_wordlist import HGTrie, WordList_ag

# 트라이 생성
trietest = HGTrie() 
trietest.MakeTrie__WordList(WordList_ag) 
#=trietest.PrintTrie()

# 접두사 일치 탐색
PrefixList = trietest.GetPrefixList('ag') 
print(f'[ag] PrefixList {len(PrefixList)}:', *PrefixList)
#=print(*PrefixList, sep='\n')

PrefixList = trietest.GetPrefixList('age') 
print(f'[age] PrefixList {len(PrefixList)}:', *PrefixList)


#=# 아래는 임시로 테스트
#=PrefixList = trietest.GetPrefixList('ago') 
#=print(f'[ago] PrefixList {len(PrefixList)}:', *PrefixList)
#=trietest.PrintChild('ago')
#=print()


'''
처리결과:
==========================
[ag] PrefixList 5: age agent ago again agree
[age] PrefixList 2: age agent

'''
