import hgsysinc
from 자모 import 자모_음절변환
from hgunicode import hgGetChoJungJongString

# (옛한글 포함) 한글 음절을 자모로 변환한 후에 다시 음절로 변환
#=string = '하ᇐ글' # 자모_음절변환()로 원래대로 복원됨
string = '百姓이 니르고져 호ᇙ배이셔도' # 자모_음절변환()로 원래대로 복원됨
print(f'입력 문자열 ({len(string)}):', string)

# 음절 문자열을 자모 문자열로 변환
string_jamo = hgGetChoJungJongString(string)
print(f'자모 문자열 변환 ({len(string_jamo)}):', string_jamo)

# 자모 문자열을 음절 문자열로 변환
string_syllable = 자모_음절변환(string_jamo)
print(f'음절 문자열 변환 ({len(string_syllable)}):', string_syllable)

if(string != string_syllable):
    print('변환 결과가 다릅니다.')


'''
처리 결과:

응용프로그램에 따라 출력 모양이 다를 수 있음.
========================================
입력 문자열 (16): 百姓이 니르고져 호ᇙ배이셔도
자모 문자열 변환 (25): 百姓이 니르고져 호ᇙ배이셔도
음절 문자열 변환 (16): 百姓이 니르고져 호ᇙ배이셔도

'''


