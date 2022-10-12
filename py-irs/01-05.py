# 모듈 호출(import) 예:
import hgsysinc # {hgunicode.py} 다른 경로에 있기 때문에 경로 지정
# ㄱ)
import hgunicode as 한글코드
자모변환 = 한글코드.hgGetChoJungJongString_Char('한')
print('# ㄱ)', 자모변환)

# ㄴ)
from hgunicode import hgGetChoJungJongString_Char as 음절_자모_변환
자모변환 = 음절_자모_변환('한')
print('# ㄴ)', 자모변환)


'''
처리 결과
======================
# ㄱ) 한
# ㄴ) 한

'''
