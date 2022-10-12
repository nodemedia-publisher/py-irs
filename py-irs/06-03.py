import hgsysinc
from hgunicode import hgGetChoJungJongString
#----------------------
#----------------------
string ='한'
string ='좋아요'
string ='사랑' # 출력했을 때 {메모장}에서 글자 모양을 구별하기 좋다.
ChoJungJongString = hgGetChoJungJongString(string, jamo=True)
print('음절 문자열:', string)
print('자모 문자열:', ChoJungJongString)
print()



'''
처리 결과

응용프로그램에 따라 출력 모양이 다를 수 있음.
=========================
음절 문자열: 사랑
자모 문자열: 사랑 <=== 자모 문자열이지만 어떤 응용 프로그램에서는 음절 상태로 보임(메모장에서는 약간 다르게 보임)


'''

