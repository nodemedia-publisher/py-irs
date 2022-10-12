from pathlib import Path
filename1 = Path("./../testtext/hgcode/test1.txt");
#----------
#----------
import hgsysinc
from hgwordlist import GetKeywordList_File
#----------
#----------
encoding='euc-kr'
KeywordList = GetKeywordList_File(filename1, encoding)
print('KeywordList Num :', len(KeywordList))
print(KeywordList)


#--- imsi
#=from hgchartype import test_script_tok
#=#=test = '5에서 10cm의 적설량을'
#=test = '5에서'
#=test_script_tok(test, debugPrint=True)


'''
처리 결과:
===========================================
KeywordList Num : 173
['새해', '첫날', '강추위', '내일부터', '누그러질', '듯', '새해', '첫날', '강추위로', '시작했습니다', '호남과', '제주', '지방엔', '많은', '눈이', '쌓였는데', '내일부터는', '차가운', '겨울바람이', ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ... ..., '산간지역엔', '눈발이', '조금', '더', '날리는', '곳이', '있겠고', '이후', '당분간은', '큰', '추위나', '눈', '예보없이', '대체로', '맑은', '날씨가', '이어질', '전망입니다', 'KBS', '뉴스']
'''

