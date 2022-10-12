# 키워드의 길이와 사전 순서에 따른 복합 정렬
from pathlib import Path
filename1 = Path("./../testtext/hgcode/test1.txt");
encoding='euc-kr'
#----------
#----------
import hgsysinc
from hgwordlist import GetKeywordList_File
#---------- keyword sort code & len
#---------- keyword sort code & len
# ver 1
KeywordList = GetKeywordList_File(filename1, encoding)
KeywordList.sort(key = lambda wd: (len(wd), wd)) # by [len 1-> high] and [abc->xyz]
print('KeywordList num:', len(KeywordList))
print(KeywordList)

'''
처리 결과:

===========================================
['그', '눈', '더', '듯', '뚝', '밤', '올', '찬', '첫', '큰', '큰', '1월', '가장', '겨울', '계속', '곳이', '기분', '나온', '낮은', '내일', '너무', '눈이', '눈이', '뉴스', '들어', '많은', '맑은', '몸이', '밖의', '빨리', '새해', '새해', '새해', '새해', '세찬', '손도', '아침', '안에', '영하', ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ..., '9.5도까지', '기록했습니다', '대륙고기압이', '떨어졌습니다', '서해안지역도', '시작했습니다', '오르겠습니다', '우리나라까지', '움츠러듭니다', '이어졌습니다', '이어졌습니다', '전해드립니다', '집에가려고요', '18.6도까지', '기상전문기자가', '끌어내렸습니다']

'''

