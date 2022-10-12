from pathlib import Path
filename1 = Path("./../testtext/hgcode/test1.txt");
encoding='euc-kr'
#----------
#----------
import hgsysinc
from hgwordlist import GetKeywordList_File
#---------- keyword sort reverse
#---------- keyword sort reverse
KeywordList = GetKeywordList_File(filename1, encoding)
KeywordList.sort(reverse=True) # by xyz -> abc
print('KeywordList num:', len(KeywordList))
print(KeywordList)

'''
처리 결과:
===========================================
KeywordList num: 173
['확장했던', '호남지방과', '호남과', '호남', '합니다', '함께', '함께', '한파와', '한파가', '한낮에도', '하지만', '풀린다고', '큰', '큰', '출근이', '추위에', '추위는', '추위나', '추워서', '첫날부터', '첫날', '첫날', '첫', '챙겨보지만', '찬', '차가운',  ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ..., '기온을', '기온은', '기온은', '기상전문기자가', '기분', '기록했습니다', '그', '곳이', '계속', '겨울바람이', '겨울', '것으로', '거리의', '거리로', '강추위로', '강추위', '가장', 'KBS', '9.5도까지', '5에서', '26cm의', '1일이라서', '1월', '18.6도까지', '15도까지', '10cm의']

'''

