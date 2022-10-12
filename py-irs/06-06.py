import hgsysinc
from hgunicode import hgGetChoJungJongString, hgSyllableStr__Jamo3Str

# 한글 음절을 자모로 변환한 후에 다시 음절로 변환
string = '나랏말씀이 중국과 달라' # 유니코드 음절 문자열
print(f'입력 문자열 ({len(string)}):', string)

# 음절 문자열을 자모 문자열로 변환
string_jamo = hgGetChoJungJongString(string)
print(f'자모 문자열 변환 ({len(string_jamo)}):', string_jamo)

# 자모 문자열을 음절 문자열로 변환
string_syllable = hgSyllableStr__Jamo3Str(string_jamo)
print(f'음절 문자열 변환 ({len(string_syllable)}):', string_syllable)

if(string != string_syllable):
    print('변환 결과가 다릅니다.')




'''
처리 결과:

응용프로그램에 따라 출력 모양이 다를 수 있음.
========================================

입력 문자열 (12): 나랏말씀이 중국과 달라
자모 문자열 변환 (28): 나랏말씀이 중국과 달라
음절 문자열 변환 (12): 나랏말씀이 중국과 달라


'''

