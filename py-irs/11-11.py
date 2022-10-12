from pathlib import Path
filename1 = Path("./../testtext/hgcode/test1.txt");
encoding='euc-kr'
#----------
#----------
import hgsysinc
from hgwordlist import GetKeywordList_File
from hgwordlist import GetWordDictList_WordList
#---------- KeywordList -> word dict
#---------- KeywordList -> word dict
KeywordList = GetKeywordList_File(filename1, encoding=encoding)
WordDictList = GetWordDictList_WordList(KeywordList)
print('word num:', len(KeywordList))
print('word dict num:', len(WordDictList))
print(*WordDictList, sep='\n')


'''
처리 결과:
===========================================
word num: 173
word dict num: 153
{'word': '10cm의', 'freq': 1, 'len': 5, 'script_num': 3}
{'word': '15도까지', 'freq': 1, 'len': 5, 'script_num': 2}
{'word': '18.6도까지', 'freq': 1, 'len': 7, 'script_num': 4}
{'word': '1월', 'freq': 1, 'len': 2, 'script_num': 2}
{'word': '1일이라서', 'freq': 1, 'len': 5, 'script_num': 2}
{'word': '26cm의', 'freq': 1, 'len': 5, 'script_num': 3}
{'word': '5에서', 'freq': 1, 'len': 3, 'script_num': 2} 
{'word': '9.5도까지', 'freq': 1, 'len': 6, 'script_num': 4}
{'word': 'KBS', 'freq': 1, 'len': 3, 'script_num': 1}
{'word': '가장', 'freq': 1, 'len': 2, 'script_num': 1}
{'word': '강추위', 'freq': 1, 'len': 3, 'script_num': 1}
{'word': '강추위로', 'freq': 1, 'len': 4, 'script_num': 1}
{'word': '거리로', 'freq': 1, 'len': 3, 'script_num': 1}
{'word': '거리의', 'freq': 1, 'len': 3, 'script_num': 1}
{'word': '것으로', 'freq': 1, 'len': 3, 'script_num': 1}
{'word': '겨울', 'freq': 1, 'len': 2, 'script_num': 1}
{'word': '겨울바람이', 'freq': 1, 'len': 5, 'script_num': 1}
{'word': '계속', 'freq': 1, 'len': 2, 'script_num': 1}
{'word': '곳이', 'freq': 1, 'len': 2, 'script_num': 1}
{'word': '그', 'freq': 1, 'len': 1, 'script_num': 1}
{'word': '기록했습니다', 'freq': 1, 'len': 6, 'script_num': 1}
{'word': '기분', 'freq': 1, 'len': 2, 'script_num': 1}
{'word': '기상전문기자가', 'freq': 1, 'len': 7, 'script_num': 1}
{'word': '기온은', 'freq': 2, 'len': 3, 'script_num': 1}
{'word': '기온을', 'freq': 1, 'len': 3, 'script_num': 1}
...
{'word': '끌어내렸습니다', 'freq': 1, 'len': 7, 'script_num': 1}
{'word': '나온', 'freq': 1, 'len': 2, 'script_num': 1}
{'word': '나왔는데', 'freq': 1, 'len': 4, 'script_num': 1}
{'word': '날리는', 'freq': 1, 'len': 3, 'script_num': 1}
{'word': '날씨가', 'freq': 2, 'len': 3, 'script_num': 1}
{'word': '낮기온이', 'freq': 1, 'len': 4, 'script_num': 1}
{'word': '낮부터', 'freq': 1, 'len': 3, 'script_num': 1}
{'word': '낮은', 'freq': 1, 'len': 2, 'script_num': 1}
{'word': '내려갔고', 'freq': 1, 'len': 4, 'script_num': 1}
{'word': '내일', 'freq': 1, 'len': 2, 'script_num': 1}
{'word': '내일부터', 'freq': 1, 'len': 4, 'script_num': 1}
{'word': '내일부터는', 'freq': 2, 'len': 5, 'script_num': 1}
{'word': '너무', 'freq': 1, 'len': 2, 'script_num': 1}
{'word': '누그러질', 'freq': 2, 'len': 4, 'script_num': 1}
{'word': '눈', 'freq': 1, 'len': 1, 'script_num': 1}
{'word': '눈구름의', 'freq': 1, 'len': 4, 'script_num': 1}
{'word': '눈발이', 'freq': 2, 'len': 3, 'script_num': 1}
{'word': '눈이', 'freq': 2, 'len': 2, 'script_num': 1}
{'word': '뉴스', 'freq': 1, 'len': 2, 'script_num': 1}
{'word': '단단히', 'freq': 1, 'len': 3, 'script_num': 1}
{'word': '당분간은', 'freq': 1, 'len': 4, 'script_num': 1}
{'word': '대관령의', 'freq': 1, 'len': 4, 'script_num': 1}
{'word': '대륙고기압이', 'freq': 1, 'len': 6, 'script_num': 1}
{'word': '대설특보와', 'freq': 1, 'len': 5, 'script_num': 1}
{'word': '대전시', 'freq': 1, 'len': 3, 'script_num': 1}
{'word': '대체로', 'freq': 1, 'len': 3, 'script_num': 1}
{'word': '더', 'freq': 1, 'len': 1, 'script_num': 1}
{'word': '들어', 'freq': 1, 'len': 2, 'script_num': 1}
{'word': '들어가고', 'freq': 1, 'len': 4, 'script_num': 1}
{'word': '듯', 'freq': 1, 'len': 1, 'script_num': 1}
{'word': '떨어졌습니다', 'freq': 1, 'len': 6, 'script_num': 1}
{'word': '뚝', 'freq': 1, 'len': 1, 'script_num': 1}
{'word': '만들어진', 'freq': 1, 'len': 4, 'script_num': 1}
{'word': '많은', 'freq': 1, 'len': 2, 'script_num': 1}
{'word': '맑은', 'freq': 1, 'len': 2, 'script_num': 1}
{'word': '매서운', 'freq': 2, 'len': 3, 'script_num': 1}
{'word': '머물러', 'freq': 1, 'len': 3, 'script_num': 1}
{'word': '모자까지', 'freq': 1, 'len': 4, 'script_num': 1}
{'word': '모처럼', 'freq': 1, 'len': 3, 'script_num': 1}
{'word': '목도리와', 'freq': 1, 'len': 4, 'script_num': 1}
{'word': '몸이', 'freq': 1, 'len': 2, 'script_num': 1}
{'word': '밖의', 'freq': 1, 'len': 2, 'script_num': 1}
{'word': '밤', 'freq': 1, 'len': 1, 'script_num': 1}
{'word': '보입니다', 'freq': 1, 'len': 4, 'script_num': 1}
{'word': '빨리', 'freq': 1, 'len': 2, 'script_num': 1}
{'word': '사흘째', 'freq': 1, 'len': 3, 'script_num': 1}
{'word': '산간지역엔', 'freq': 1, 'len': 5, 'script_num': 1}
{'word': '상암동', 'freq': 1, 'len': 3, 'script_num': 1}
{'word': '새해', 'freq': 4, 'len': 2, 'script_num': 1}
{'word': '서울도', 'freq': 1, 'len': 3, 'script_num': 1}
{'word': '서울시', 'freq': 1, 'len': 3, 'script_num': 1}
{'word': '서해상에서', 'freq': 1, 'len': 5, 'script_num': 1}
{'word': '서해안지역도', 'freq': 1, 'len': 6, 'script_num': 1}
{'word': '세찬', 'freq': 1, 'len': 2, 'script_num': 1}
{'word': '손도', 'freq': 1, 'len': 2, 'script_num': 1}
{'word': '시리고', 'freq': 2, 'len': 3, 'script_num': 1}
{'word': '시민들은', 'freq': 1, 'len': 4, 'script_num': 1}
{'word': '시작되는', 'freq': 1, 'len': 4, 'script_num': 1}
{'word': '시작했습니다', 'freq': 1, 'len': 6, 'script_num': 1}
...
{'word': '싶어요', 'freq': 1, 'len': 3, 'script_num': 1}
{'word': '쌓였는데', 'freq': 1, 'len': 4, 'script_num': 1}
{'word': '아침', 'freq': 1, 'len': 2, 'script_num': 1}
{'word': '안에', 'freq': 1, 'len': 2, 'script_num': 1}
{'word': '약화되고', 'freq': 1, 'len': 4, 'script_num': 1}
{'word': '얼굴도', 'freq': 1, 'len': 3, 'script_num': 1}
{'word': '여미고', 'freq': 1, 'len': 3, 'script_num': 1}
{'word': '영상으로', 'freq': 1, 'len': 4, 'script_num': 1}
{'word': '영하', 'freq': 3, 'len': 2, 'script_num': 1}
{'word': '영하권에', 'freq': 1, 'len': 4, 'script_num': 1}
{'word': '영향으로', 'freq': 1, 'len': 4, 'script_num': 1}
{'word': '예보없이', 'freq': 1, 'len': 4, 'script_num': 1}
{'word': '오늘', 'freq': 2, 'len': 2, 'script_num': 1}
{'word': '오르겠습니다', 'freq': 1, 'len': 6, 'script_num': 1}
{'word': '오전까지', 'freq': 1, 'len': 4, 'script_num': 1}
{'word': '올', 'freq': 1, 'len': 1, 'script_num': 1}
{'word': '옷깃을', 'freq': 1, 'len': 3, 'script_num': 1}
{'word': '왔고', 'freq': 1, 'len': 2, 'script_num': 1}
{'word': '우리나라까지', 'freq': 1, 'len': 6, 'script_num': 1}
{'word': '움츠러듭니다', 'freq': 1, 'len': 6, 'script_num': 1}
{'word': '월평동', 'freq': 1, 'len': 3, 'script_num': 1}
{'word': '이어졌습니다', 'freq': 2, 'len': 6, 'script_num': 1}
{'word': '이어질', 'freq': 1, 'len': 3, 'script_num': 1}
{'word': '이후', 'freq': 1, 'len': 2, 'script_num': 1}
{'word': '있겠고', 'freq': 1, 'len': 3, 'script_num': 1}
{'word': '있어서', 'freq': 1, 'len': 3, 'script_num': 1}
{'word': '장갑', 'freq': 1, 'len': 2, 'script_num': 1}
{'word': '적설량을', 'freq': 1, 'len': 4, 'script_num': 1}
{'word': '전국의', 'freq': 1, 'len': 3, 'script_num': 1}
{'word': '전망입니다', 'freq': 1, 'len': 5, 'script_num': 1}
{'word': '전북', 'freq': 1, 'len': 2, 'script_num': 1}
{'word': '전해드립니다', 'freq': 1, 'len': 6, 'script_num': 1}
{'word': '절로', 'freq': 1, 'len': 2, 'script_num': 1}
{'word': '점차', 'freq': 1, 'len': 2, 'script_num': 1}
{'word': '정읍엔', 'freq': 1, 'len': 3, 'script_num': 1}
{'word': '제주', 'freq': 2, 'len': 2, 'script_num': 1}
{'word': '제주도엔', 'freq': 1, 'len': 4, 'script_num': 1}
{'word': '조금', 'freq': 2, 'len': 2, 'script_num': 1}
{'word': '좋게', 'freq': 1, 'len': 2, 'script_num': 1}
{'word': '중부지방의', 'freq': 1, 'len': 5, 'script_num': 1}
{'word': '지방엔', 'freq': 1, 'len': 3, 'script_num': 1}
{'word': '집에가려고요', 'freq': 1, 'len': 6, 'script_num': 1}
{'word': '차가운', 'freq': 1, 'len': 3, 'script_num': 1}
{'word': '찬', 'freq': 1, 'len': 1, 'script_num': 1}
{'word': '챙겨보지만', 'freq': 1, 'len': 5, 'script_num': 1}
{'word': '첫', 'freq': 1, 'len': 1, 'script_num': 1}
{'word': '첫날', 'freq': 2, 'len': 2, 'script_num': 1}
{'word': '첫날부터', 'freq': 1, 'len': 4, 'script_num': 1}
{'word': '추워서', 'freq': 1, 'len': 3, 'script_num': 1}
{'word': '추위나', 'freq': 1, 'len': 3, 'script_num': 1}
{'word': '추위는', 'freq': 1, 'len': 3, 'script_num': 1}
{'word': '추위에', 'freq': 1, 'len': 3, 'script_num': 1}
{'word': '출근이', 'freq': 1, 'len': 3, 'script_num': 1}
{'word': '큰', 'freq': 2, 'len': 1, 'script_num': 1}
{'word': '풀린다고', 'freq': 1, 'len': 4, 'script_num': 1}
{'word': '하지만', 'freq': 1, 'len': 3, 'script_num': 1}
{'word': '한낮에도', 'freq': 1, 'len': 4, 'script_num': 1}
{'word': '한파가', 'freq': 1, 'len': 3, 'script_num': 1}
{'word': '한파와', 'freq': 1, 'len': 3, 'script_num': 1}
{'word': '함께', 'freq': 2, 'len': 2, 'script_num': 1}
{'word': '합니다', 'freq': 1, 'len': 3, 'script_num': 1}
{'word': '호남', 'freq': 1, 'len': 2, 'script_num': 1}
{'word': '호남과', 'freq': 1, 'len': 3, 'script_num': 1}
{'word': '호남지방과', 'freq': 1, 'len': 5, 'script_num': 1}
{'word': '확장했던', 'freq': 1, 'len': 4, 'script_num': 1}


'''

