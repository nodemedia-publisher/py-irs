from pathlib import Path
filename1 = Path("./../testtext/hgcode/test1.txt");
encoding='euc-kr'
#----------
#----------
import hgsysinc
from hgwordlist import GetKeywordList_File
#---------- keyword sort reverse len
#---------- keyword sort reverse len
KeywordList = GetKeywordList_File(filename1, encoding)
KeywordList.sort(key = lambda wd: -len(wd)) # by len high -> 1
print('KeywordList num:', len(KeywordList))
print(KeywordList)


'''
처리 결과:

===========================================
KeywordList num: 173
['기상전문기자가', '끌어내렸습니다', '18.6도까지', '시작했습니다', '전해드립니다', '움츠러듭니다', '집에가려고요', '9.5도까지', '떨어졌습니다', '이어졌습니다', '오르겠습니다', '우리나라까지', '대륙고기압이', '이어졌습니다', '서해안지역도', '기록했습니다', ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ..., '겨울', '들어', '가장', '낮은', '영하', '영하', '계속', '새해', '점차', '내일', '함께', '함께', '세찬', '전북', '눈이', '왔고', '밖의', '호남', '오늘', '제주', '조금', '곳이', '이후', '맑은', '뉴스', '듯', '올', '뚝', '첫', '찬', '큰', '그', '밤', '더', '큰', '눈']

'''

