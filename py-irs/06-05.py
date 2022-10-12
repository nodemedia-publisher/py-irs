import hgsysinc
from hgunicode import hgGetSyllable__Jamo3
from 자모 import (
    초성_ㄱ, 초성_ㅎ, 
    중성_ㅏ,
    종성_ㄲ, 종성_ㄴ,
)

# 초중종 자모로 한글 음절 조합
음절1 = hgGetSyllable__Jamo3(초성_ㄱ, 중성_ㅏ) # ᄀᅠᅟᅡ
print('변환 결과 1:', 음절1)

음절2 = hgGetSyllable__Jamo3(초성_ㄱ, 중성_ㅏ, 종성_ㄲ) # ᄀᅠᅟᅡᅟᅠᆩ
print('변환 결과 2:', 음절2)

음절3 = hgGetSyllable__Jamo3(초성_ㅎ, 중성_ㅏ, 종성_ㄴ) # ᄒᅠᅟᅡᅟᅠᆫ
print('변환 결과 3:', 음절3)


'''
처리 결과
=========================
변환 결과 1: 가
변환 결과 2: 갂
변환 결과 3: 한

'''


