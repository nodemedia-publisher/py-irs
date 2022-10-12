from pathlib import Path
filename1 = Path("./../testtext/hgcode/test1.txt");
encoding='euc-kr'
#----------
#----------
import hgsysinc
from hgwordlist import GetKeywordList_File
#---------- keyword sort
#---------- keyword sort
KeywordList = GetKeywordList_File(filename1, encoding)
KeywordList.sort() # sort by abc -> xyz
print('KeywordList num:', len(KeywordList))
print(KeywordList)


'''
처리 결과:
===========================================
KeywordList num: 173
['10cm의', '15도까지', '18.6도까지', '1월', '1일이라서', '26cm의', '5에서', '9.5도까지', 'KBS', '가장', '강추위', '강추위로', '거리로', '거리의', '것으로', '겨울', '겨울바람이', '계속', '곳이', '그', '기록했습니다', '기분', '기상전문기자가', '기온은', '기온은', '기온을', ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ...'차가운', '찬', '챙겨보지만', '첫', '첫날', '첫날', '첫날부터', '추워서', '추위나', '추위는', '추위에', '출근이', '큰', '큰', '풀린다고', '하지만', '한낮에도', '한파가', '한파와', '함께', '함께', '합니다', '호남', '호남과', '호남지방과', '확장했던']

'''

