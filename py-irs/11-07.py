from pathlib import Path
filename1 = Path("./../testtext/hgcode/test1.txt");
encoding='euc-kr'
#----------
#----------
import hgsysinc
from hgwordlist import GetKeywordList_File
#---------- keyword sort len
#---------- keyword sort len
KeywordList = GetKeywordList_File(filename1, encoding)
KeywordList.sort(key = lambda wd: len(wd)) # by len 1-> high
print('KeywordList num:', len(KeywordList))
print(KeywordList)


'''
처리 결과:

===========================================
KeywordList num: 173
['듯', '올', '뚝', '첫', '찬', '큰', '그', '밤', '더', '큰', '눈', '새해', '첫날', '새해', '첫날', '제주', '많은', '눈이', '조금', '새해', '영하', '나온', '장갑', '몸이', '절로', '1월', '기분', '좋게', '너무', '안에', '손도', '빨리', '오늘', '아침', '겨울', '들어', '가장', '낮은', '영하', ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ..., '전해드립니다', '움츠러듭니다', '집에가려고요', '9.5도까지', '떨어졌습니다', '이어졌습니다', '오르겠습니다', '우리나라까지', '대륙고기압이', '이어졌습니다', '서해안지역도', '기록했습니다', '기상전문기자가', '끌어내렸습니다', '18.6도까지']

'''

