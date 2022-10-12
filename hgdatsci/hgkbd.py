#---
#---
import hgsysinc # 이 파일에서는 사용하지 않더라도 이 파일을 부르는 곳에서 사용한다.

#---
#---
def _lline_(): # 다른 라이브러리와 함수 이름이 겹치지 않도록 'l'자를 추가
    import inspect
    return inspect.currentframe().f_back.f_lineno

#---
#---
from hgunicode import (
    hgGetSyllable__Jamo3, __compa_jamo_string_4_chosung__,
    __compa_jamo_string_4_jongsung__,
)
    

#---
#---
# naming
# 한글 호환 자모(Hangul Compatibility Jamo) : jaum, moum  <=== (0x3131-0x314E)(ksc5601: 0xA4A1~0xA4BE)
# 한글 자모(Hangul Jamo): {cho/jung/jong} + jamo <=== (Hangul Jamo: 0x1100 ~ 0x1112, 0x1161 ~ 0x1175, 0x11a8 ~ 0x11c2)
#---
# 두벌식 오토마타에서 자판에 있는 모음을 확인할 때 키보드에 입력 가능한 (기본) 모음 14자
__basic_moum14__ = 'ㅏㅐㅑㅒㅓㅔㅕㅖㅗㅛㅜㅠㅡㅣ' # 중성 (호환) 단자모:영문자} 14자, # Hangul Compatibility Jamo (0x3131-0x314E)(ksc5601: 0xA4A1~0xA4D3)

#---
__eng_from_chosung_inx_list__ =  [ # chosung-inx(초성 자모:19)
    'r','R','s','e','E',   'f','a','q','Q','t', # ㄱㄲㄴㄷㄸ   # ㄹㅁㅂㅃㅅ
    'T','d','w','W','c',   'z','x','v','g',]     # ㅆㅇㅈㅉㅊ   # ㅋㅌㅍㅎ
__eng_from_jungsung_inx_list__ = [ # jungsung-inx(중성 자모:21)
    'k', 'o', 'i', 'O', 'j',   'p', 'u', 'P', 'h','hk', # ㅏㅐㅑㅒㅓ   # ㅔㅕㅖㅗㅘ
    'ho','hl','y', 'n','nj',   'np','nl', 'b','m','ml',   'l'] # ㅙㅚㅛㅜㅝ   # ㅞㅟㅠㅡㅢ   # ㅣ
__eng_from_jongsung_inx_list__ = [ # jongsung-inx(종성 자모:27)
    'r',  'R','rt', 's','sw',  'sg', 'e', 'f','fr','fa', # ㄱㄲㄳㄴㄵ   # ㄶㄷㄹㄺㄻ
    'fq','ft','fx','fv','fg',  'a',  'q','qt', 't', 'T', # ㄼㄽㄾㄿㅀ   # ㅁㅂㅄㅅㅆ
    'd',  'w', 'c', 'z', 'x',  'v',  'g',] # ㅇㅈㅊㅋㅌ   # ㅍㅎ
__jaum1_from_eng2_11_dict__ = { # 2글자로 된 겹받침(11) (Hangul Compatibility Jamo)
    #--- 소문자
    'rt': 'ㄳ', 'sw': 'ㄵ', 'sg': 'ㄶ', 
    'fr': 'ㄺ', 'fa': 'ㄻ', 'fq': 'ㄼ', 'ft': 'ㄽ', 
    'fx': 'ㄾ', 'fv': 'ㄿ', 'fg': 'ㅀ', 
    'qt': 'ㅄ',
    #--- 소문자
    'rT': 'ㄳ', 'sW': 'ㄵ', 'sG': 'ㄶ', 
    'fR': 'ㄺ', 'fA': 'ㄻ', 'fQ': 'ㄼ', 'fT': 'ㄽ', 
    'fX': 'ㄾ', 'fV': 'ㄿ', 'fG': 'ㅀ', 
    'qT': 'ㅄ',
    #--- 대문자
    'RT': 'ㄳ', 'SW': 'ㄵ', 'SG': 'ㄶ', 
    'FR': 'ㄺ', 'FA': 'ㄻ', 'FQ': 'ㄼ', 'FT': 'ㄽ', 
    'FX': 'ㄾ', 'FV': 'ㄿ', 'FG': 'ㅀ', 
    'QT': 'ㅄ',
    #--- 대문자
    'Rt': 'ㄳ', 'Sw': 'ㄵ', 'Sg': 'ㄶ', 
    'Fr': 'ㄺ', 'Fa': 'ㄻ', 'Fq': 'ㄼ', 'Ft': 'ㄽ', 
    'Fx': 'ㄾ', 'Fv': 'ㄿ', 'Fg': 'ㅀ', 
    'Qt': 'ㅄ',
    } 
__moum1_from_eng2_7_dict__ = {# 2글자로 된 {조합 모음}(7) (Hangul Compatibility Jamo)
    #--- 소문자
    'hk':'ㅘ','ho':'ㅙ','hl':'ㅚ',
    'nj':'ㅝ','np':'ㅞ','nl':'ㅟ',
    'ml':'ㅢ',
    #--- 소문자
    'hK':'ㅘ','hO':'ㅙ','hL':'ㅚ',
    'nJ':'ㅝ','nP':'ㅞ','nL':'ㅟ',
    'mL':'ㅢ',
    #--- 대문자
    'HK':'ㅘ','HO':'ㅙ','HL':'ㅚ',
    'NJ':'ㅝ','NP':'ㅞ','NL':'ㅟ',
    'ML':'ㅢ',
    #--- 대문자
    'Hk':'ㅘ','Ho':'ㅙ','Hl':'ㅚ',
    'Nj':'ㅝ','Np':'ㅞ','Nl':'ㅟ',
    'Ml':'ㅢ',
    }

__jaummoum_from_eng2_dict__ = __jaum1_from_eng2_11_dict__.copy()
__jaummoum_from_eng2_dict__.update(__moum1_from_eng2_7_dict__)

__cho_jamo_from_eng_dict__ = { # 초성 19자(Hangul Jamo: 0x1100 ~ 0x1112)
    'r': 'ᄀ', 'R': 'ᄁ', 's': 'ᄂ', 'e': 'ᄃ', 'E': 'ᄄ', 
    'f': 'ᄅ', 'a': 'ᄆ', 'q': 'ᄇ', 'Q': 'ᄈ', 't': 'ᄉ', 
    'T': 'ᄊ', 'd': 'ᄋ', 'w': 'ᄌ', 'W': 'ᄍ', 'c': 'ᄎ', 
    'z': 'ᄏ', 'x': 'ᄐ', 'v': 'ᄑ', 'g': 'ᄒ',
    # 대문자와 소문자가 똑같은 한글 자모
    'S': 'ᄂ', 
    'F': 'ᄅ', 'A': 'ᄆ', 
    'D': 'ᄋ', 'C': 'ᄎ', 
    'Z': 'ᄏ', 'X': 'ᄐ', 'V': 'ᄑ', 'G': 'ᄒ',
    } 
__jung_jamo_from_eng_dict__ = { # 중성 21자(Hangul Jamo: 0x1161 ~ 0x1175)
    'k': 'ᅡ', 'o': 'ᅢ', 'i': 'ᅣ', 'O': 'ᅤ', 
    'j': 'ᅥ', 'p': 'ᅦ', 'u': 'ᅧ', 'P': 'ᅨ', 
    'h': 'ᅩ', 'hk': 'ᅪ', 'ho': 'ᅫ', 'hl': 'ᅬ', 
    'y': 'ᅭ', 'n': 'ᅮ', 'nj': 'ᅯ', 'np': 'ᅰ', 
    'nl': 'ᅱ', 'b': 'ᅲ', 'm': 'ᅳ', 'ml': 'ᅴ', 
    # 대문자와 소문자가 똑같은 한글 자모
    'l': 'ᅵ',
    'K': 'ᅡ', 'I': 'ᅣ',
    'J': 'ᅥ', 'U': 'ᅧ', 
    'H': 'ᅩ', 'HK': 'ᅪ', 'HO': 'ᅫ', 'HL': 'ᅬ', 
    'Y': 'ᅭ', 'N': 'ᅮ', 'NJ': 'ᅯ', 'NP': 'ᅰ', 
    'NL': 'ᅱ', 'B': 'ᅲ', 'M': 'ᅳ', 'ML': 'ᅴ', 
    'L': 'ᅵ',
    # {조합 모음} 소문자 확장
    'hK': 'ᅪ', 'hO': 'ᅫ', 'hL': 'ᅬ', 
    'nJ': 'ᅯ', 'nP': 'ᅰ', 'nL': 'ᅱ', 
    'mL': 'ᅴ', 
    # {조합 모음} 대문자 확장
    'Hk': 'ᅪ', 'Ho': 'ᅫ', 'Hl': 'ᅬ', 
    'Nj': 'ᅯ', 'Np': 'ᅰ', 'Nl': 'ᅱ', 
    'Ml': 'ᅴ', 
    } 
__jong_jamo_from_eng_dict__ =  { # 종성 27자(Hangul Jamo: 0x11a8 ~ 0x11c2)
    'r': 'ᆨ', 'R': 'ᆩ', 'rt': 'ᆪ', 's': 'ᆫ', 
    'sw': 'ᆬ', 'sg': 'ᆭ', 'e': 'ᆮ', 'f': 'ᆯ', 
    'fr': 'ᆰ', 'fa': 'ᆱ', 'fq': 'ᆲ', 'ft': 'ᆳ', 
    'fx': 'ᆴ', 'fv': 'ᆵ', 'fg': 'ᆶ', 'a': 'ᆷ', 
    'q': 'ᆸ', 'qt': 'ᆹ', 't': 'ᆺ', 'T': 'ᆻ', 
    'd': 'ᆼ', 'w': 'ᆽ', 'c': 'ᆾ', 'z': 'ᆿ', 
    'x': 'ᇀ', 'v': 'ᇁ', 'g': 'ᇂ',
    # 대문자와 소문자가 똑같은 한글 자모
    'RT': 'ᆪ', 'S': 'ᆫ', 
    'SW': 'ᆬ', 'SG': 'ᆭ', 'E': 'ᆮ', 'F': 'ᆯ', 
    'FR': 'ᆰ', 'FA': 'ᆱ', 'FQ': 'ᆲ', 'FT': 'ᆳ', 
    'FX': 'ᆴ', 'FV': 'ᆵ', 'FG': 'ᆶ', 'A': 'ᆷ', 
    'Q': 'ᆸ', 'QT': 'ᆹ', 
    'D': 'ᆼ', 'W': 'ᆽ', 'C': 'ᆾ', 'Z': 'ᆿ', 
    'X': 'ᇀ', 'V': 'ᇁ', 'G': 'ᇂ',
    # 겹받침 소문자 확장
    'rT': 'ᆪ',
    'sW': 'ᆬ', 'sG': 'ᆭ',
    'fR': 'ᆰ', 'fA': 'ᆱ', 'fQ': 'ᆲ', 'fT': 'ᆳ', 
    'fX': 'ᆴ', 'fV': 'ᆵ', 'fG': 'ᆶ',
    'qT': 'ᆹ', 
    # 겹받침 대문자 확장
    'Rt': 'ᆪ',
    'Sw': 'ᆬ', 'Sg': 'ᆭ',
    'Fr': 'ᆰ', 'Fa': 'ᆱ', 'Fq': 'ᆲ', 'Ft': 'ᆳ', 
    'Fx': 'ᆴ', 'Fv': 'ᆵ', 'Fg': 'ᆶ',
    'Qt': 'ᆹ', 
    }

__eng_from_cho_jaum19_dict__ = {# 초성 순서에 의한 {호환 자모:영문자} 19자, # Hangul Compatibility Jamo (0x3131-0x314E)(ksc5601: 0xA4A1~0xA4D3)
    'ㄱ':'r', 'ㄲ':'R', 'ㄴ':'s', 'ㄷ':'e', 'ㄸ':'E',
    'ㄹ':'f', 'ㅁ':'a', 'ㅂ':'q', 'ㅃ':'Q', 'ㅅ':'t', 
    'ㅆ':'T', 'ㅇ':'d', 'ㅈ':'w', 'ㅉ':'W', 'ㅊ':'c', 
    'ㅋ':'z', 'ㅌ':'x', 'ㅍ':'v', 'ㅎ':'g',} 
__eng_from_moum14_dict__ = {# 중성 {호환 단자모:영문자} 14자, # Hangul Compatibility Jamo (0x3131-0x314E)(ksc5601: 0xA4A1~0xA4D3)
    'ㅏ':'k', 'ㅐ':'o', 'ㅑ':'i', 'ㅒ':'O', 'ㅓ':'j', 
    'ㅔ':'p', 'ㅕ':'u', 'ㅖ':'P', 'ㅗ':'h', 'ㅛ':'y', 
    'ㅜ':'n', 'ㅠ':'b', 'ㅡ':'m', 'ㅣ':'l',} 
__eng_from_moum21_dict__ = {# 중성 순서에 의한 {호환 자모:영문자} 21자, # Hangul Compatibility Jamo (0x3131-0x314E)(ksc5601: 0xA4A1~0xA4D3)
    'ㅏ':'k',  'ㅐ':'o',  'ㅑ':'i', 'ㅒ':'O', 'ㅓ':'j', 
    'ㅔ':'p',  'ㅕ':'u',  'ㅖ':'P', 'ㅗ':'h', 'ㅘ':'hk', 
    'ㅙ':'ho', 'ㅚ':'hl', 'ㅛ':'y', 'ㅜ':'n', 'ㅝ':'nj', 
    'ㅞ':'np', 'ㅟ':'nl', 'ㅠ':'b', 'ㅡ':'m', 'ㅢ':'ml', 
    'ㅣ':'l',} 
__eng_from_jong_jaum27_dict__ = {# 종성 순서에 의한 {호환 자모:영문자} 27자
    'ㄱ': 'r',  'ㄲ': 'R',  'ㄳ': 'rt', 'ㄴ': 's',  'ㄵ': 'sw', 
    'ㄶ': 'sg', 'ㄷ': 'e',  'ㄹ': 'f',  'ㄺ': 'fr', 'ㄻ': 'fa', 
    'ㄼ': 'fq', 'ㄽ': 'ft', 'ㄾ': 'fx', 'ㄿ': 'fv', 'ㅀ': 'fg', 
    'ㅁ': 'a',  'ㅂ': 'q',  'ㅄ': 'qt', 'ㅅ': 't',  'ㅆ': 'T', 
    'ㅇ': 'd',  'ㅈ': 'w',  'ㅊ': 'c',  'ㅋ': 'z',  'ㅌ': 'x', 
    'ㅍ': 'v',  'ㅎ': 'g',}
__eng_from_double_jaum11_dict__ = {# 종성 겹받침 {호환 자모:영문자} 11자, Hangul Compatibility Jamo (0x3131-0x314E)(ksc5601: 0xA4A1~0xA4D3)
    'ㄳ':'rt', 'ㄵ':'sw', 'ㄶ':'sg',
    'ㄺ':'fr', 'ㄻ':'fa', 'ㄼ':'fq', 'ㄽ':'ft', 'ㄾ':'fx', 'ㄿ':'fv', 'ㅀ':'fg',
    'ㅄ':'qt'} # 
#-----
# 두벌식 자판으로 입력 가능한 51개의 자모에 대응하는 영문자로 변환 테이블이 없는 이유:
# 51개의 {자모:영문자} 변환 테이블을 사용하는 것이 훨씬 간단하지만
# 여러 군데서 51개의 호환 자모 중에서 일부를 분활하여 사용하므로 
# 중복되는 부분이 생기지 않도록
# 부분적으로 나눠서 변환 테이블을 만들었다.
# 되레 이것 때문에 51개의 {자모:영문자} 변환 테이블 선언은 
# 다소 복잡해졌다.
#-----
__eng_from_jaummoum51_dict__ = __eng_from_cho_jaum19_dict__.copy() #- 초성 자모(19)
__eng_from_jaummoum51_dict__.update(__eng_from_moum21_dict__)  #- 중성 자모(21)
__eng_from_jaummoum51_dict__.update(__eng_from_double_jaum11_dict__)  #- 겹받침(11)

#
__moum1_from_moum2_7_dict__ =  {#--- 중성 2글자 {조합 모음}(7)
                            'ㅗㅏ':'ㅘ', 'ㅗㅐ':'ㅙ', 'ㅗㅣ':'ㅚ',
                            'ㅜㅓ':'ㅝ', 'ㅜㅔ':'ㅞ', 'ㅜㅣ':'ㅟ',
                            'ㅡㅣ':'ㅢ',
                            } # Hangul Compatibility Jamo (0x3131-ex314E)(ksc5601: 0xA4A1~0xA4D3)

__jaum1_from_jaum2_11_dict__ =  {#--- 종성 호환 2글자 겹받침(11)
    'ㄱㅅ': 'ㄳ', 'ㄴㅈ': 'ㄵ', 
    'ㄴㅎ': 'ㄶ', 'ㄹㄱ': 'ㄺ', 'ㄹㅁ': 'ㄻ', 
    'ㄹㅂ': 'ㄼ', 'ㄹㅅ': 'ㄽ', 'ㄹㅌ': 'ㄾ', 'ㄹㅍ': 'ㄿ', 'ㄹㅎ': 'ㅀ', 
    'ㅂㅅ': 'ㅄ', } # Hangul Compatibility Jamo (0x3131-0x314E)(ksc5601: 0xA4A1~0xA4D3)

__lead_moum_from_moum2_7_dict__ =  {#--- 중성 2글자 {조합 모음}(7)이 될 수 있는 첫 번째 모음
                            'ㅗ':'ㅘㅙㅚ',
                            'ㅜ':'ㅝㅞㅟ',
                            'ㅡ':'ㅢ',
                            } # Hangul Compatibility Jamo (0x3131-ex314E)(ksc5601: 0xA4A1~0xA4D3)

__lead_jaum_from_jaum2_11_dict__ =  {#--- 종성 호환 2글자 조합 자음(겹받침(11))이 될 수 있는 첫 번째 자음
    'ㄱ': 'ㄳ', 
    'ㄴ': 'ㄵㄶ', 
    'ㄹ': 'ㄺㄻㄼㄽㄾㄿㅀ', 
    'ㅂ': 'ㅄ', } # Hangul Compatibility Jamo (0x3131-0x314E)(ksc5601: 0xA4A1~0xA4D3)


# 1글자로 자모를 2글자 자모로 변환
__moum2_from_moum1_7_dict__ =  {#--- 1글자로 된 {조합 모음}을 2글자로 변환(7)
    'ㅘ':'ㅗㅏ', 'ㅙ':'ㅗㅐ', 'ㅚ':'ㅗㅣ',   
    'ㅝ':'ㅜㅓ', 'ㅞ':'ㅜㅔ', 'ㅟ':'ㅜㅣ',   
    'ㅢ':'ㅡㅣ',
} # Hangul Compatibility Jamo (0x3131-0x314E)(ksc5601: 0xA4A1~0xA4D3)
__jaum2_from_jaum1_11_dict__ =  {#--- 1글자로 된 겹받침을 2글자로 변환(11)
    'ㄳ':'ㄱㅅ', 'ㄵ':'ㄴㅈ', 
    'ㄶ':'ㄴㅎ', 'ㄺ':'ㄹㄱ', 'ㄻ':'ㄹㅁ', 
    'ㄼ':'ㄹㅂ', 'ㄽ':'ㄹㅅ', 'ㄾ':'ㄹㅌ', 'ㄿ':'ㄹㅍ', 'ㅀ':'ㄹㅎ', 
    'ㅄ':'ㅂㅅ', 
} # Hangul Compatibility Jamo (0x3131-0x314E)(ksc5601: 0xA4A1~0xA4D3)
__double_jamo_from_single_jamo_18_dict__ = __moum2_from_moum1_7_dict__.copy() # {조합 모음}(7)
__double_jamo_from_single_jamo_18_dict__.update(__jaum2_from_jaum1_11_dict__) # 겹받침(11)

#-----
#-----
__jaummoum_from_eng_low_dict__ = {
    'a': 'ㅁ', 'b': 'ㅠ', 'c': 'ㅊ', 'd': 'ㅇ', 'e': 'ㄷ', 
    'f': 'ㄹ', 'g': 'ㅎ', 'h': 'ㅗ', 'i': 'ㅑ', 'j': 'ㅓ', 
    'k': 'ㅏ', 'l': 'ㅣ', 'm': 'ㅡ', 'n': 'ㅜ', 'o': 'ㅐ', 
    'p': 'ㅔ', 'q': 'ㅂ', 'r': 'ㄱ', 's': 'ㄴ', 't': 'ㅅ', 
    'u': 'ㅕ', 'v': 'ㅍ', 'w': 'ㅈ', 'x': 'ㅌ', 'y': 'ㅛ', 'z': 'ㅋ', }
__jaummoum_from_eng_cap_dict__ = {
    'A': 'ㅁ', 'B': 'ㅠ', 'C': 'ㅊ', 'D': 'ㅇ', 'E': 'ㄸ', 
    'F': 'ㄹ', 'G': 'ㅎ', 'H': 'ㅗ', 'I': 'ㅑ', 'J': 'ㅓ', 
    'K': 'ㅏ', 'L': 'ㅣ', 'M': 'ㅡ', 'N': 'ㅜ', 'O': 'ㅒ', 
    'P': 'ㅖ', 'Q': 'ㅃ', 'R': 'ㄲ', 'S': 'ㄴ', 'T': 'ㅆ', 
    'U': 'ㅕ', 'V': 'ㅍ', 'W': 'ㅉ', 'X': 'ㅌ', 'Y': 'ㅛ', 'Z': 'ㅋ',}

#-----------------------
#-----------------------
__kbd_jamo_from_chosung_inx_list__ =  [ # chosung-inx (호환 자모 글자:19)
    'ㄱ','ㄲ','ㄴ','ㄷ','ㄸ',    'ㄹ','ㅁ','ㅂ','ㅃ','ㅅ',
    'ㅆ','ㅇ','ㅈ','ㅉ','ㅊ',    'ㅋ','ㅌ','ㅍ','ㅎ',
]
__kbd_jamo_from_jungsung_inx_list__ = [ # jungsung-inx (호환 자모 글자:21)
    'ㅏ','ㅐ','ㅑ','ㅒ','ㅓ',         'ㅔ','ㅕ','ㅖ','ㅗ','ㅗㅏ',
    'ㅗㅐ','ㅗㅣ','ㅛ','ㅜ','ㅜㅓ',    'ㅜㅔ','ㅜㅣ','ㅠ','ㅡ','ㅡㅣ',
    'ㅣ',
]
__kbd_jamo_from_jongsung_inx_list__ = [ # jongsung-inx (호환 자모 글자:27)
    'ㄱ','ㄲ','ㄱㅅ','ㄴ','ㄴㅈ',       'ㄴㅎ','ㄷ','ㄹ','ㄹㄱ','ㄹㅁ',
    'ㄹㅂ','ㄹㅅ','ㄹㅌ','ㄹㅍ','ㄹㅎ',  'ㅁ','ㅂ','ㅂㅅ','ㅅ','ㅆ',
    'ㅇ','ㅈ','ㅊ','ㅋ','ㅌ',           'ㅍ','ㅎ',
]


#----------
#----------
__jaummoum_from_eng52_dict__ = __jaummoum_from_eng_low_dict__.copy()
__jaummoum_from_eng52_dict__.update(__jaummoum_from_eng_cap_dict__)
#----------
#----------

#----------------------- 호환 자모에서 초,중,종 자모로 변환하기 위한 사전
__jamo_from_cho_jaum19_dict__ =  {#--- 초성 호환 자모(19)에 대응하는 초성 자모, 
    # key: Hangul Compatibility Jamo (0x3131-0x314E)(ksc5601: 0xA4A1~0xA4D3)
    # value: Hangul Jamo (0x1110-0x1112)
    'ㄱ':'ᄀ','ㄲ':'ᄁ','ㄴ':'ᄂ','ㄷ':'ᄃ','ㄸ':'ᄄ',
    'ㄹ':'ᄅ','ㅁ':'ᄆ','ㅂ':'ᄇ','ㅃ':'ᄈ','ㅅ':'ᄉ','ㅆ':'ᄊ',
    'ㅇ':'ᄋ','ㅈ':'ᄌ','ㅉ':'ᄍ','ㅊ':'ᄎ','ㅋ':'ᄏ','ㅌ':'ᄐ','ㅍ':'ᄑ','ㅎ':'ᄒ', 
}
__jamo_from_jung_moun21_dict__ = {#--- 중성 호환 자모(21)에 대응하는 중성 자모
    # key: Hangul Compatibility Jamo (0x314F-0x3163)(ksc5601:0xA4BF~0xA4D3)
    # value: Hangul Jamo (0x1161-0x1175)
    'ㅏ':'ᅡ','ㅐ':'ᅢ','ㅑ':'ᅣ','ㅒ':'ᅤ',
    'ㅓ':'ᅥ','ㅔ':'ᅦ','ㅕ':'ᅧ','ㅖ':'ᅨ',
    'ㅗ':'ᅩ','ㅘ':'ᅪ','ㅙ':'ᅫ','ㅚ':'ᅬ',
    'ㅛ':'ᅭ','ㅜ':'ᅮ','ㅝ':'ᅯ','ㅞ':'ᅰ',
    'ㅟ':'ᅱ','ㅠ':'ᅲ','ㅡ':'ᅳ','ㅢ':'ᅴ','ㅣ':'ᅵ', # 
}
__jamo_from_jong_jaum27_dict__ =  {#--- 종성 호환 자모(27)에 대응하는 종성 자모
    # key: Hangul Compatibility Jamo (0x3131-0x314E)(ksc5601 0xA4A1 ~ 0xA4D3 <= 종성부용초성)
    # value: Hangul Jamo (0x11A8-0x11C2)
    'ㄱ':'ᆨ','ㄲ':'ᆩ','ㄳ':'ᆪ','ㄴ':'ᆫ','ㄵ':'ᆬ','ㄶ':'ᆭ',
    'ㄷ':'ᆮ','ㄹ':'ᆯ','ㄺ':'ᆰ','ㄻ':'ᆱ','ㄼ':'ᆲ','ㄽ':'ᆳ',
    'ㄾ':'ᆴ','ㄿ':'ᆵ','ㅀ':'ᆶ','ㅁ':'ᆷ','ㅂ':'ᆸ','ㅄ':'ᆹ',
    'ㅅ':'ᆺ','ㅆ':'ᆻ','ㅇ':'ᆼ','ㅈ':'ᆽ','ㅊ':'ᆾ','ㅋ':'ᆿ',
    'ㅌ':'ᇀ','ㅍ':'ᇁ','ㅎ':'ᇂ', 
}


#---------------------------
#---- 전각(Fullwidth) 아스키 영문자를 두벌식(키보드) 자모로 변환하기 위한 사전
#---------------------------
__jaummoum_from_full_eng_low_dict__ = { # 블록 안에 있는 영문자는 전각 아스키
    'ａ':'ㅁ', 'ｂ':'ㅠ', 'ｃ':'ㅊ', 'ｄ':'ㅇ', 'ｅ':'ㄷ', 
    'ｆ':'ㄹ', 'ｇ':'ㅎ', 'ｈ':'ㅗ', 'ｉ':'ㅑ', 'ｊ':'ㅓ', 
    'ｋ':'ㅏ', 'ｌ':'ㅣ', 'ｍ':'ㅡ', 'ｎ':'ㅜ', 'ｏ':'ㅐ', 
    'ｐ':'ㅔ', 'ｑ':'ㅂ', 'ｒ':'ㄱ', 'ｓ':'ㄴ', 'ｔ':'ㅅ', 
    'ｕ':'ㅕ', 'ｖ':'ㅍ', 'ｗ':'ㅈ', 'ｘ':'ㅌ', 'ｙ':'ㅛ', 'ｚ':'ㅋ', }
__jaummoum_from_full_eng_cap_dict__ = { # 블록 안에 있는 영문자는 전각 아스키
    'Ａ':'ㅁ', 'Ｂ':'ㅠ', 'Ｃ':'ㅊ', 'Ｄ':'ㅇ', 'Ｅ':'ㄸ', 
    'Ｆ':'ㄹ', 'Ｇ':'ㅎ', 'Ｈ':'ㅗ', 'Ｉ':'ㅑ', 'Ｊ':'ㅓ', 
    'Ｋ':'ㅏ', 'Ｌ':'ㅣ', 'Ｍ':'ㅡ', 'Ｎ':'ㅜ', 'Ｏ':'ㅒ', 
    'Ｐ':'ㅖ', 'Ｑ':'ㅃ', 'Ｒ':'ㄲ', 'Ｓ':'ㄴ', 'Ｔ':'ㅆ', 
    'Ｕ':'ㅕ', 'Ｖ':'ㅍ', 'Ｗ':'ㅉ', 'Ｘ':'ㅌ', 'Ｙ':'ㅛ', 'Ｚ':'ㅋ',}

__jaummoum_from_full_eng52_dict__ = __jaummoum_from_full_eng_low_dict__.copy()
__jaummoum_from_full_eng52_dict__.update(__jaummoum_from_full_eng_cap_dict__)
#----------
#----------

#---------------------------
#- 반각(Halfwidth) 자모를 두벌식(키보드) 자모로 변환하기 위한 사전
#---------------------------
__jaummoum_from_half_jamo_dict__ = { # 반각 자모(51자)에 대응하는 두벌식(키보드) 자모
    'ﾡ': 'ㄱ', 'ﾢ': 'ㄲ', 'ﾣ': 'ㄱㅅ', 'ﾤ': 'ㄴ', 
    'ﾥ': 'ㄴㅈ', 'ﾦ': 'ㄴㅎ', 'ﾧ': 'ㄷ', 'ﾨ': 'ㄸ', 
    'ﾩ': 'ㄹ', 'ﾪ': 'ㄹㄱ', 'ﾫ': 'ㄹㅁ', 'ﾬ': 'ㄹㅂ', 
    'ﾭ': 'ㄹㅅ', 'ﾮ': 'ㄹㅌ', 'ﾯ': 'ㄹㅍ', 'ﾰ': 'ㄹㅎ', 
    'ﾱ': 'ㅁ', 'ﾲ': 'ㅂ', 'ﾳ': 'ㅃ', 'ﾴ': 'ㅂㅅ', 'ﾵ': 'ㅅ', 
    'ﾶ': 'ㅆ', 'ﾷ': 'ㅇ', 'ﾸ': 'ㅈ', 'ﾹ': 'ㅉ', 
    'ﾺ': 'ㅊ', 'ﾻ': 'ㅋ', 'ﾼ': 'ㅌ', 'ﾽ': 'ㅍ', 'ﾾ': 'ㅎ', 
    #-----
    'ￂ': 'ㅏ', 'ￃ': 'ㅐ', 'ￄ': 'ㅑ', 'ￅ': 'ㅒ', 'ￆ': 'ㅓ', 
    'ￇ': 'ㅔ', 'ￊ': 'ㅕ', 'ￋ': 'ㅖ', 'ￌ': 'ㅗ', 
    'ￍ': 'ㅗㅏ', 'ￎ': 'ㅗㅐ', 'ￏ': 'ㅗㅣ', 'ￒ': 'ㅛ', 'ￓ': 'ㅜ', 
    'ￔ': 'ㅜㅓ', 'ￕ': 'ㅜㅔ', 'ￖ': 'ㅜㅣ', 
    'ￗ': 'ㅠ', 'ￚ': 'ㅡ', 'ￛ': 'ㅡㅣ', 'ￜ': 'ㅣ',}
#----------
#----------


#---------------------------
#- 초,중,종 자모(Hangul Jamo)를 두벌식(키보드) 자모로 변환하기 위한 사전
#---------------------------
___cho_jaum_from_cho_jamo19_dict__ = { # 초성 자모(19)에 대응하는 두벌식(키보드) 자모 사전:
    # key: Hangul Jamo (0x1110-0x1112)
    # value: Hangul Compatibility Jamo (0x3131-0x314E)(ksc5601: 0xA4A1~0xA4D3)
    'ᄀ': 'ㄱ', 'ᄁ': 'ㄲ', 'ᄂ': 'ㄴ', 'ᄃ': 'ㄷ', 'ᄄ': 'ㄸ', 'ᄅ': 'ㄹ', 'ᄆ': 'ㅁ', 
    'ᄇ': 'ㅂ', 'ᄈ': 'ㅃ', 'ᄉ': 'ㅅ', 'ᄊ': 'ㅆ', 'ᄋ': 'ㅇ', 'ᄌ': 'ㅈ', 'ᄍ': 'ㅉ', 
    'ᄎ': 'ㅊ', 'ᄏ': 'ㅋ', 'ᄐ': 'ㅌ', 'ᄑ': 'ㅍ', 'ᄒ': 'ㅎ',
}
__jung_moun_from_jung_jamo21_dict__ = { # 중성 자모(21)에 대응하는 두벌식(키보드) 자모 사전:
    # key: Hangul Jamo (0x1110-0x1112)
    # value: Hangul Compatibility Jamo (0x3131-0x314E)(ksc5601: 0xA4A1~0xA4D3)
    'ᅡ': 'ㅏ', 'ᅢ': 'ㅐ', 'ᅣ': 'ㅑ', 'ᅤ': 'ㅒ', 'ᅥ': 'ㅓ', 'ᅦ': 'ㅔ', 'ᅧ': 'ㅕ', 
    'ᅨ': 'ㅖ', 'ᅩ': 'ㅗ', 'ᅪ': 'ㅗㅏ', 'ᅫ': 'ㅗㅐ', 'ᅬ': 'ㅗㅣ', 'ᅭ': 'ㅛ', 'ᅮ': 'ㅜ', 
    'ᅯ': 'ㅜㅓ', 'ᅰ': 'ㅜㅔ', 'ᅱ': 'ㅜㅣ', 'ᅲ': 'ㅠ', 'ᅳ': 'ㅡ', 'ᅴ': 'ㅡㅣ', 'ᅵ': 'ㅣ',
}
__jong_jaum_from_jong_jamo27_dict__ = { # 종성 자모(27)에 대응하는 두벌식(키보드) 자모 사전:
    # key: Hangul Jamo (0x1110-0x1112)
    # value: Hangul Compatibility Jamo (0x3131-0x314E)(ksc5601: 0xA4A1~0xA4D3)
    'ᆨ': 'ㄱ', 'ᆩ': 'ㄲ', 'ᆪ': 'ㄱㅅ', 'ᆫ': 'ㄴ', 'ᆬ': 'ㄴㅈ', 'ᆭ': 'ㄴㅎ', 'ᆮ': 'ㄷ', 
    'ᆯ': 'ㄹ', 'ᆰ': 'ㄹㄱ', 'ᆱ': 'ㄹㅁ', 'ᆲ': 'ㄹㅂ', 'ᆳ': 'ㄹㅅ', 'ᆴ': 'ㄹㅌ', 'ᆵ': 'ㄹㅍ', 
    'ᆶ': 'ㄹㅎ', 'ᆷ': 'ㅁ', 'ᆸ': 'ㅂ', 'ᆹ': 'ㅂㅅ', 'ᆺ': 'ㅅ', 'ᆻ': 'ㅆ', 'ᆼ': 'ㅇ', 
    'ᆽ': 'ㅈ', 'ᆾ': 'ㅊ', 'ᆿ': 'ㅋ', 'ᇀ': 'ㅌ', 'ᇁ': 'ㅍ', 'ᇂ': 'ㅎ',
}
# 초중종 자모를 두벌식(키보드) 자모로 변환 사전
__jaummoum_from_hangul_jamo_dict_ = ___cho_jaum_from_cho_jamo19_dict__.copy()
__jaummoum_from_hangul_jamo_dict_.update(__jung_moun_from_jung_jamo21_dict__)
__jaummoum_from_hangul_jamo_dict_.update(__jong_jaum_from_jong_jamo27_dict__)
#----------
#----------

#---------------------------
#- 반각(Halfwidth) 자모를 영문자로 변환하기 위한 사전
#---------------------------
__eng_from_half_jamo_dict__ = { # 반각 자모(51자)에 대응하는 영문자
    'ﾡ': 'r', 'ﾢ': 'R', 'ﾣ': 'rt', 'ﾤ': 's', 'ﾥ': 'sw', 'ﾦ': 'sg', 'ﾧ': 'e', 'ﾨ': 'E', 'ﾩ': 'f', 'ﾪ': 'fr', 
    'ﾫ': 'fa', 'ﾬ': 'fq', 'ﾭ': 'ft', 'ﾮ': 'fx', 'ﾯ': 'fv', 'ﾰ': 'fg', 'ﾱ': 'a', 'ﾲ': 'q', 'ﾳ': 'Q', 'ﾴ': 'qt', 
    'ﾵ': 't', 'ﾶ': 'T', 'ﾷ': 'd', 'ﾸ': 'w', 'ﾹ': 'W', 'ﾺ': 'c', 'ﾻ': 'z', 'ﾼ': 'x', 'ﾽ': 'v', 'ﾾ': 'g', 
    #-----
    'ￂ': 'k', 'ￃ': 'o', 'ￄ': 'i', 'ￅ': 'O', 'ￆ': 'j', 'ￇ': 'p', 'ￊ': 'u', 'ￋ': 'P', 'ￌ': 'h', 'ￍ': 'hk', 'ￎ': 'ho', 
    'ￏ': 'hl', 'ￒ': 'y', 'ￓ': 'n', 'ￔ': 'nj', 'ￕ': 'np', 'ￖ': 'nl', 'ￗ': 'b', 'ￚ': 'm', 'ￛ': 'ml', 'ￜ': 'l',
    }

#---------------------------
#- 영문자를 반각(Halfwidth) 자모로 변환하기 위한 사전
#---------------------------
__half_jamo_from_eng_low_dict__ = { # 영문 소문자에 대응하는 반각 자모(char_num: 26):
    'a': 'ﾱ', 'b': 'ￗ', 'c': 'ﾺ', 'd': 'ﾷ', 'e': 'ﾧ',
    'f': 'ﾩ', 'g': 'ﾾ', 'h': 'ￌ', 'i': 'ￄ', 'j': 'ￆ',
    'k': 'ￂ', 'l': 'ￜ', 'm': 'ￚ', 'n': 'ￓ', 'o': 'ￃ',
    'p': 'ￇ', 'q': 'ﾲ', 'r': 'ﾡ', 's': 'ﾤ', 't': 'ﾵ',
    'u': 'ￊ', 'v': 'ﾽ', 'w': 'ﾸ', 'x': 'ﾼ', 'y': 'ￒ',
    'z': 'ﾻ',
}
__half_jamo_from_eng_cap_dict__ = { # 영문 대문자에 대응하는 반각 자모(char_num: 26):
    'A': 'ﾱ', 'B': 'ￗ', 'C': 'ﾺ', 'D': 'ﾷ', 'E': 'ﾨ',
    'F': 'ﾩ', 'G': 'ﾾ', 'H': 'ￌ', 'I': 'ￄ', 'J': 'ￆ',
    'K': 'ￂ', 'L': 'ￜ', 'M': 'ￚ', 'N': 'ￓ', 'O': 'ￅ', 
    'P': 'ￋ', 'Q': 'ﾳ', 'R': 'ﾢ', 'S': 'ﾤ', 'T': 'ﾶ',
    'U': 'ￊ', 'V': 'ﾽ', 'W': 'ﾹ', 'X': 'ﾼ', 'Y': 'ￒ',
    'Z': 'ﾻ',
}
__half_jamo_from_eng52_dict__ = __half_jamo_from_eng_low_dict__.copy()
__half_jamo_from_eng52_dict__.update(__half_jamo_from_eng_cap_dict__)

__half_jaum1_from_eng2_11_dict__ = { # 2글자로 된 겹받침(11) 영문자에 대응하는 반각 자모(char_num: 44{11x4}):
    #--- 소문자
    'rt': 'ﾣ', 'sw': 'ﾥ', 'sg': 'ﾦ', 
    'fr': 'ﾪ', 'fa': 'ﾫ', 'fq': 'ﾬ', 'ft': 'ﾭ', 'fx': 'ﾮ', 'fv': 'ﾯ', 'fg': 'ﾰ',
    'qt': 'ﾴ', 
    #--- 소문자
    'rT': 'ﾣ', 'sW': 'ﾥ', 'sG': 'ﾦ', 
    'fR': 'ﾪ', 'fA': 'ﾫ', 'fQ': 'ﾬ', 'fT': 'ﾭ', 'fX': 'ﾮ', 'fV': 'ﾯ', 'fG': 'ﾰ', 
    'qT': 'ﾴ', 
    #--- 대문자
    'RT': 'ﾣ', 'SW': 'ﾥ', 'SG': 'ﾦ',
    'FR': 'ﾪ', 'FA': 'ﾫ', 'FQ': 'ﾬ', 'FT': 'ﾭ', 'FX': 'ﾮ', 'FV': 'ﾯ', 'FG': 'ﾰ', 
    'QT': 'ﾴ', 
    #--- 대문자
    'Rt': 'ﾣ', 'Sw': 'ﾥ', 'Sg': 'ﾦ', 
    'Fr': 'ﾪ', 'Fa': 'ﾫ', 'Fq': 'ﾬ', 'Ft': 'ﾭ', 'Fx': 'ﾮ', 'Fv': 'ﾯ', 'Fg': 'ﾰ', 
    'Qt': 'ﾴ', 
}
__half_moum1_from_eng2_7_dict__ = { # 2글자로 된 {조합 모음}(7) 영문자에 대응하는 반각 자모(char_num: 28{7x4}):
    #--- 소문자
    'hk': 'ￍ', 'ho': 'ￎ', 'hl': 'ￏ', 
    'nj': 'ￔ', 'np': 'ￕ', 'nl': 'ￖ', 
    'ml': 'ￛ', 
    #--- 소문자
    'hK': 'ￍ', 'hO': 'ￎ', 'hL': 'ￏ',
    'nJ': 'ￔ', 'nP': 'ￕ', 'nL': 'ￖ', 
    'mL': 'ￛ', 
    #--- 대문자
    'HK': 'ￍ', 'HO': 'ￎ', 'HL': 'ￏ', 
    'NJ': 'ￔ', 'NP': 'ￕ', 'NL': 'ￖ',
    'ML': 'ￛ', 
    #--- 대문자
    'Hk': 'ￍ', 'Ho': 'ￎ', 'Hl': 'ￏ', 
    'Nj': 'ￔ', 'Np': 'ￕ', 'Nl': 'ￖ', 
    'Ml': 'ￛ',
}
__half_jamo_from_eng2_dict__ = __half_jaum1_from_eng2_11_dict__.copy()
__half_jamo_from_eng2_dict__.update(__half_moum1_from_eng2_7_dict__)


#---------------------------
#---- 전각(Fullwidth) 아스키 영문자를 반각 자모로 변환하기 위한 사전
#---------------------------
__half_jamo_from_full_eng_low_dict__ = { # 블록 안에 있는 영문자는 전각 아스키
    'ａ': 'ﾱ', 'ｂ': 'ￗ', 'ｃ': 'ﾺ', 'ｄ': 'ﾷ', 'ｅ': 'ﾧ',
    'ｆ': 'ﾩ', 'ｇ': 'ﾾ', 'ｈ': 'ￌ', 'ｉ': 'ￄ', 'ｊ': 'ￆ',
    'ｋ': 'ￂ', 'ｌ': 'ￜ', 'ｍ': 'ￚ', 'ｎ': 'ￓ', 'ｏ': 'ￃ',
    'ｐ': 'ￇ', 'ｑ': 'ﾲ', 'ｒ': 'ﾡ', 'ｓ': 'ﾤ', 'ｔ': 'ﾵ',
    'ｕ': 'ￊ', 'ｖ': 'ﾽ', 'ｗ': 'ﾸ', 'ｘ': 'ﾼ', 'ｙ': 'ￒ', 'ｚ': 'ﾻ',}
__half_jamo_from_full_eng_cap_dict__ = { # 블록 안에 있는 영문자는 전각 아스키
    'Ａ': 'ﾱ', 'Ｂ': 'ￗ', 'Ｃ': 'ﾺ', 'Ｄ': 'ﾷ', 'Ｅ': 'ﾨ',
    'Ｆ': 'ﾩ', 'Ｇ': 'ﾾ', 'Ｈ': 'ￌ', 'Ｉ': 'ￄ', 'Ｊ': 'ￆ',
    'Ｋ': 'ￂ', 'Ｌ': 'ￜ', 'Ｍ': 'ￚ', 'Ｎ': 'ￓ', 'Ｏ': 'ￅ',
    'Ｐ': 'ￋ', 'Ｑ': 'ﾳ', 'Ｒ': 'ﾢ', 'Ｓ': 'ﾤ', 'Ｔ': 'ﾶ', 
    'Ｕ': 'ￊ', 'Ｖ': 'ﾽ', 'Ｗ': 'ﾹ', 'Ｘ': 'ﾼ', 'Ｙ': 'ￒ', 'Ｚ': 'ﾻ',}

__half_jamo_from_full_eng52_dict__ = __half_jamo_from_full_eng_low_dict__.copy()
__half_jamo_from_full_eng52_dict__.update(__half_jamo_from_full_eng_cap_dict__)


#---
#---
def HGGetSyllable_KBDEngJamo3(KBDEng_Cho, KBDEng_Jung, KBDEng_Jong=''):
    '''초성, 중성, 종성에 대응하는 영문자를 매개변수로 받음.
    '''
    hgSyllable = ''

    ChoJamo = __cho_jamo_from_eng_dict__.get(KBDEng_Cho)
    JungJamo = __jung_jamo_from_eng_dict__.get(KBDEng_Jung)
    JongJamo = ''
    if(KBDEng_Jong != ''):
        JongJamo = __jong_jamo_from_eng_dict__.get(KBDEng_Jong)
    if((ChoJamo == None) or (JungJamo == None) or (JongJamo == None)):
        #-----
        # 여기서는 오류나 경고 처리를 하지 말고 그냥 종료해야 한다.
        # 현대어 음절의 경우에는 이쪽으로 올 수 없지만 옛한글일 경우에는 
        # 이쪽으로 넘어올 수 있기 때문에 여기서 엄격하게 검사하여 중단시키면 
        # 옛한글 처리와 혼용할 수 없으므로 
        # 여기서는 오류나 경고 처리를 하지 말고 그냥 종료해야 한다.
        #-----
        return hgSyllable 
    #
    hgSyllable = hgGetSyllable__Jamo3(ChoJamo, JungJamo, JongJamo)
    return hgSyllable

def HGGetSyllable_JaumMoum3(JaumMoum_Cho, JaumMoum_Jung, JaumMoum_Jong=''):
    '''초성, 중성, 종성에 대응하는 호환 자모를 매개변수로 받음.
    '''
    hgSyllable = ''

    ChoJamo = __jamo_from_cho_jaum19_dict__.get(JaumMoum_Cho)
    JungJamo = __jamo_from_jung_moun21_dict__.get(JaumMoum_Jung)
    JongJamo = JaumMoum_Jong
    if(JaumMoum_Jong != ''):
        JongJamo = __jamo_from_jong_jaum27_dict__.get(JaumMoum_Jong)
    if((ChoJamo == None) or (JungJamo == None) or (JongJamo == None)):
        #-----
        # 여기서는 오류나 경고 처리를 하지 말고 그냥 종료해야 한다.
        # 현대어 음절의 경우에는 이쪽으로 올 수 없지만 옛한글일 경우에는 
        # 이쪽으로 넘어올 수 있기 때문에 여기서 엄격하게 검사하여 중단시키면 
        # 옛한글 처리와 혼용할 수 없으므로 
        # 여기서는 오류나 경고 처리를 하지 말고 그냥 종료해야 한다.
        #-----
        return hgSyllable 
    #        
    hgSyllable = hgGetSyllable__Jamo3(ChoJamo, JungJamo, JongJamo)
    return hgSyllable

class HGAutom():
    #===========================
    #===========================
    # 두벌식 조합 오토마타 보충 설명:
    # HGAutom 클래스는 다른 응용 프로그램과 알고리즘 호환성을 유지하도록 설계했지만 
    # 한 가지 다른 점이 있다.
    # 일반적인 한글 입력기(오토마타)는 백스페이스(Backspace) 키를 입력 받도록 설계되었지만 
    # HGAutom 클래스는 백스페이스(Backspace) 키를 처리하는 부분을 반영하지 않았다.
    # 그 이유는 HGAutom은 실제 입력기로 사용하지 않고 두벌식 자모 문자열을 음절 문자열로 
    # 변환할 목적으로 사용하므로 입력 문자에 백스페이스(Backspace) 키 문자가 
    # 없기 때문이다.
    # 
    # 한글 입력기에서는 조합 중간에 백스페이스(Backspace) 키를 치면 이전 조합 상태로 
    # 되돌아가는데, 이로 인하여 음절이 조합이 완전히 끝났음에도 음절을 완성하지 않고 
    # 대기(wait) 상태로 머문다. 이 부분이 논리적으로 불완전한 부분이다.
    #
    # 자음 상태(자음, 자음+자음, 초성+중성+종성1[자음], 초성+중성+종성2[자음+자음])에서는 
    # 다음에 모음이 입력될 경우를 대비해서 대기(wait) 상태로 있는 것이 맞지만 
    # 조합 모음을 만들지 않는 모음(11자:ㅏ,ㅐ,ㅑ,ㅒ,ㅓ,ㅔ,ㅕ,ㅖ,ㅛ,ㅠ,ㅣ)과 
    # 조합 모음(7자:ㅘ, ㅙ, ㅚ, ㅝ, ㅞ, ㅟ, ㅢ)은 다음 입력과 무관하게 
    # 조합이 끝난 것이므로 더 이상 대기(wait) 상태로 있을 필요가 없다. 
    # 그런데 이 때 대부분의 한글 입력기가 음절을 완성하지 않고 
    # 다음 입력을 기다리는 대기(wait) 상태로 있다.
    # 특히 조합 모음(7자:ㅘ, ㅙ, ㅚ, ㅝ, ㅞ, ㅟ, ㅢ)으로 대기 상태일 때 
    # 백스페이스(Backspace) 키가 입력되면 조합 모음을 만드는 모음(3자:ㅗ,ㅜ,ㅡ)으로 
    # 바뀌고 모음 상태로 대기(wait)한다.
    # 만약 이 때 대기 상태로 처리하지 않으면 백스페이스(Backspace) 키가 입력되면 
    # 조합 모음을 만드는 모음(3자:ㅗ,ㅜ,ㅡ)으로 바뀌는 것이 아니라 
    # 조합 모음(7자:ㅘ, ㅙ, ㅚ, ㅝ, ㅞ, ㅟ, ㅢ)가 통채로 지워지기 때문에 
    # 대기(wait) 상태로 두는 것이 타당해 보인다.
    # 하지만 조합 모음을 만들지 않는 모음(11자:ㅏ,ㅐ,ㅑ,ㅒ,ㅓ,ㅔ,ㅕ,ㅖ,ㅛ,ㅠ,ㅣ)의 경우에는 
    # 대기(wait) 상태로 두거나, 안 두거나 백스페이스(Backspace) 키가 입력되면 
    # 결과가 똑같기 때문에 굳이 대기(wait) 상태로 둘 필요가 없는데도 
    # 대기(wait) 상태로 두는 것은 알고리즘 관점에서 불필요한 부분이다.
    #
    # 만약 두벌식 자모 문자열을 음절 문자열로 변환할 목적이라면 
    # 조합 모음을 만들지 않는 모음(11자:ㅏ,ㅐ,ㅑ,ㅒ,ㅓ,ㅔ,ㅕ,ㅖ,ㅛ,ㅠ,ㅣ)과 
    # 조합 모음(7자:ㅘ, ㅙ, ㅚ, ㅝ, ㅞ, ㅟ, ㅢ)을 대기(wait) 상태로 두는 것이 
    # 불필요하지만 다른 응용 프로그램과 알고리즘 호환성을 유지하도록 
    # HGAutom 클래스도 논리적으로 조합이 끝난 모음 상태에서도 
    # 음절을 완성하지 않고 대기(wait) 상태로 둔다.
    #
    # 조합 모음을 만들지 않는 모음 11자: ㅏ,ㅐ,ㅑ,ㅒ,ㅓ,ㅔ,ㅕ,ㅖ,ㅛ,ㅠ,ㅣ
    # 조합 모음을 만드는 모음 3자: ㅗ,ㅜ,ㅡ
    # 조합 모음 7자: ㅘ, ㅙ, ㅚ, ㅝ, ㅞ, ㅟ, ㅢ
    #
    # 한편 옛한글 입력을 지원하는 문서처리기에서는 
    # 조합 모음을 만들지 않는 모음 11자(ㅏ,ㅐ,ㅑ,ㅒ,ㅓ,ㅔ,ㅕ,ㅖ,ㅛ,ㅠ,ㅣ)과 
    # 조합 모음 7자(ㅘ, ㅙ, ㅚ, ㅝ, ㅞ, ㅟ, ㅢ)은 이후에 모음이 올 경우에 
    # 모음 3개를 조합하는 경우도 있고, 자음이 올 경우에는 종성으로 
    # 처리해야 하므로 다음 입력을 기다려야 한다.
    # 
    # 또한 PC 윈도우(메모장, 웹브라우저)와 Mac(메모, 웹브라우저)에서는 
    # 차이가 없지만 특이하게도 아이폰 계열은 약간의 차이가 있다.
    # [메모장]: 가나 ---> Backspace ---> 가ㄴ
    # [아이폰]: 가나 ---> Backspace ---> 간
    #===========================
    #===========================
    # automata
    _syl_init_ = 0 # 초기 상태
    _syl_cho_ = 1  # 초성 상태
    _syl_jung_ = 2 # 중성 상태
    _syl_jung2_ = 3 # 조합 모음 상태
    _syl_jong_ = 4  # 종성 상태
    _syl_jong2_ = 5 # 조합 자음(겹받침) 상태

    def __init__(self):
        #
        self.reset()

    def reset(self):
        #
        self.cho = ''
        self.jung1 = ''
        self.jung2 = ''
        self.jong1 = ''
        self.jong2 = ''
        self.automata_state = self._syl_init_

    def GetSyllable(self, reset=False):
        # 오토마타에서 '초성, 중성, 종성'을 읽어 음절로 변한한다.
        cho_v = self.cho
        jung_v = self.jung1
        if(self.jung2 != ''):
            #=jung_v += self.jung2
            jung_v = __moum1_from_moum2_7_dict__.get(self.jung1 + self.jung2)
        jong_v = self.jong1
        if(self.jong2 != ''):
            #=jong_v += self.jong2
            jong_v = __jaum1_from_jaum2_11_dict__.get(self.jong1 + self.jong2)

        #=print(type(self).__name__, ':', 'cho:', cho_v, 'jung:', jung_v, 'jong:', jong_v)
        if(reset == True):
            self.reset()

        # '초성, 중성, 종성'을 음절로 변환한다.
        if(cho_v ==''): # [초성]이 없는 경우
            if(jung_v ==''): # [중성]이 없는 경우
                if(jong_v): # [초성], [중성]이 없는데 종성이 있는 경우 - 오류 상태
                    assert False
            else: 
                if(jong_v): # [중성]은 있는데 [종성]이 있는 경우 - 오류 상태
                    assert False
                else: # [중성]만 있는 경우 - 낱글자 [모음]
                    return jung_v
        else: # [초성]이 있는 경우
            if(jung_v ==''): # [초성]은 있고, [중성]이 없는 경우
                if(jong_v): # [초성]있어도, [중성]이 없는데 [종성]이 있는 경우 - 오류 상태
                    assert False
                else: # [초성]만 있는 경우 - 낱글자 [자음]
                    return cho_v
            else: # [초성/중성] 모두 있는 경우 - 음절 조합
                hgSyllable = HGGetSyllable_JaumMoum3(cho_v, jung_v, jong_v)
                return hgSyllable

    def PressChar(self, PressChar):
        #
        hgSyllable = ''
        #--------------------------------------------
        # 자음 처리
        #--------------------------------------------
        if(PressChar in __compa_jamo_string_4_chosung__): # 키보드 자음()
            if(self.automata_state == self._syl_init_): # 시작 + [자음] -> 초성
                self.automata_state = self._syl_cho_
                self.cho = PressChar
            elif(self.automata_state == self._syl_cho_): # 초성 + [자음] -> 1. 겹받침 2.초성 자음 + 초성 자음
                # 1. 조합 자음(겹받침) 검사
                TwoChar = self.cho + PressChar
                TwoJaum = __jaum1_from_jaum2_11_dict__.get(TwoChar)
                if(TwoJaum):
                    self.cho = TwoJaum # 초성에 겹받침
                else:
                    #. 2 초성(자음) + 초성(자음) ===> 자음 낱글자 + 새로운 초성
                    hgSyllable = self.cho
                    self.cho = PressChar
                # 
                self.automata_state = self._syl_cho_ # 이미 이 상태라서 필요없지만 로직을 구분하기 위해서 넣어 둔다.
            elif((self.automata_state == self._syl_jung_) or # 중성1 + [자음]
                (self.automata_state == self._syl_jung2_)):  # 중성2 + [자음]
                # 초성 검사
                if(self.cho == ''): # [초성]없이 [중성] 낱글자만 있는 경우 => 중성 낱글자 ++ 새로운 초성
                    #. [중성] 낱글자 완성
                    hgSyllable = self.GetSyllable(reset=True)
                    #. 새로운 초성
                    self.cho = PressChar
                    self.automata_state = self._syl_cho_
                else: # [초성]^[중성]++[자음]
                    # 1. (중성+)종성 검사
                    if(PressChar in __compa_jamo_string_4_jongsung__): # 자음이 종성인 경우
                        self.jong1 = PressChar # 종성
                        self.automata_state = self._syl_jong_
                    else: # 자음이 종성이 아닌 경우
                        #. 2 중성 + 초성(자음) ===> 음절 완성 + 새로운 초성
                        hgSyllable = self.GetSyllable(reset=True)
                        #
                        self.cho = PressChar
                        self.automata_state = self._syl_cho_
            elif(self.automata_state == self._syl_jong_): # 종성 + [자음] -> 1. 종성+종성 2. 중성 + 초성 자음
                # 1. 종성+종성 검사
                if(self.jong2 != ''): # [종성]상태이므로 [종성2]는 값이 없음. 논리적 오류
                    assert False
                
                # 종성-종성이 온 경우 = 겹받침 검사
                TwoChar = self.jong1 + PressChar
                TwoJaum = __jaum1_from_jaum2_11_dict__.get(TwoChar)
                if(TwoJaum): # 자음이 겹받침인 경우
                    self.jong2 = PressChar # 종성
                    self.automata_state = self._syl_jong2_
                else: # 자음이 겹받침이 아닌 경우
                    #. 종성 + 초성(자음) ===> 음절 완성 + 새로운 초성
                    hgSyllable = self.GetSyllable(reset=True)
                    #
                    self.cho = PressChar
                    self.automata_state = self._syl_cho_
            elif(self.automata_state == self._syl_jong2_): # 종성+[자음]->종성+초성 자음
                if(self.jong2 == ''): #[종성+종성]상태,[종성2]는 값이 있어야 함.논리적 오류
                    assert False
                # [종성1+종성2++자음] => 음절 완성 ++ 초성
                hgSyllable = self.GetSyllable(reset=True)
                #
                self.cho = PressChar
                self.automata_state = self._syl_cho_
            else:
                assert False
            #=self.Print()
        #--------------------------------------------
        # 모음 처리
        #--------------------------------------------
        elif(PressChar in __basic_moum14__): # 키보드 [모음]
            if(self.automata_state == self._syl_init_): # 시작++[모음] -> 중성 낱글자
                self.jung1 = PressChar
                self.automata_state = self._syl_jung_
            elif(self.automata_state == self._syl_cho_): # 초성++[모음] -> 1.초성++중성 2. 자음 낱글자++초성+중성
                TwoJaum = __jaum2_from_jaum1_11_dict__.get(self.cho)
                if(TwoJaum): # 초성이 겹받침인 경우: [ㄺ++ㅏ] -> [ㄹ++가]
                    # 2. [자음1+자음2++모음] => 자음 낱글자 ++ 초성 + 중성
                    hgSyllable = TwoJaum[0] # 겹받침을 분리하여 첫 글자를 낱글자 자음
                    self.cho = TwoJaum[1] # 겹받침을 분리하여 두 번째 글자를 초성으로
                    self.jung1 = PressChar
                else: # 초성++중성
                    self.jung1 = PressChar
                self.automata_state = self._syl_jung_
            elif(self.automata_state == self._syl_jung_): # 중성++[모음] -> 1. 중성++중성 2. 중성++중성 낱글자
                if(self.jung2 != ''): # [중성]상태, [중성2]는 값이 없어야 함. 논리적 오류
                    assert False
                # 중성++중성
                TwoChar = self.jung1 + PressChar
                TwoMoum = __moum1_from_moum2_7_dict__.get(TwoChar)
                if(TwoMoum): # 모음이 {조합 모음}인 경우
                    self.jung2 = PressChar # 중성
                    self.automata_state = self._syl_jung2_
                else: # 모음이 {조합 모음}이 아닌 경우
                    #. 중성++중성 낱글자 ===> 음절 완성++새로운 중성
                    hgSyllable = self.GetSyllable(reset=True)

                    # 새로운 중성
                    self.jung1 = PressChar
                    #
                    self.automata_state = self._syl_jung_
            elif(self.automata_state == self._syl_jung2_): # 중성++[모음] -> 1. 중성++중성 2. 중성++중성 낱글자
                if(self.jung2 == ''): #[중성+중성]상태,[중성2]는 값이 있어야 함.논리적 오류
                    assert False
                # 중성^중성++중성 ==> 음절 완성++새로운 중성
                hgSyllable = self.GetSyllable(reset=True)
                self.jung1 = PressChar
                #
                self.automata_state = self._syl_jung_
            elif(self.automata_state == self._syl_jong_): # 종성++[모음] -> 초성++중성
                # 종성++모음 검사
                if(self.jong2 != ''): # [종성]상태, [종성2]는 값이 없어야 함. 논리적 오류
                    assert False
                # 종성-모음이 온 경우 => 음절 완성++초성+중성(모음)
                # 종성을 다음 글자 초성으로 옮기고, 초기화한다.
                NewCho = self.jong1
                self.jong1 = '' # 종성 초기화
                hgSyllable = self.GetSyllable(reset=True)

                # 새 음절 구성
                self.cho = NewCho
                self.jung1 = PressChar
                #
                self.automata_state = self._syl_jung_
            elif(self.automata_state == self._syl_jong2_): # 종성++[모음] -> 초성++중성
                # 종성+종성++모음 검사
                if(self.jong2 == ''): #[종성+종성]상태,[종성2]는 값이 있어야 함.논리적 오류
                    assert False
                # [종성1+종성2++모음] => (종성1)음절 완성++(종성2)초성+중성(모음)
                NewCho = self.jong2
                self.jong2 = '' # 종성2 초기화
                hgSyllable = self.GetSyllable(reset=True)

                # 새 음절 구성
                self.cho = NewCho
                self.jung1 = PressChar
                #
                self.automata_state = self._syl_jung_
            else:
                assert False
            #=self.Print()
        #--------------------------------------------
        #--------------------------------------------
        else: # 두벌식 기본 [자모](33자)가 아닌 경우, 조합 중인 자모가 있으면 음절 완성.
            if(self.automata_state != self._syl_init_): # 음절 조합이 끝나지 않은 나머지 처리
                hgSyllable = self.GetSyllable(reset=True)
            #
            hgSyllable += PressChar
        #--------------------------------------------
        #--------------------------------------------
        return hgSyllable
    
    def EndAutomata(self):
        hgSyllable = ''
        #=print(self.State())
        if(self.automata_state != self._syl_init_): # 음절 조합이 끝나지 않은 나머지 처리
            hgSyllable = self.GetSyllable(reset=True)
        #
        return hgSyllable

    def Print(self):
        print(type(self).__name__, ':', 
            'cho:', self.cho, 
            'jung1:', self.jung1, 'jung2:', self.jung2, 
            'jong1:', self.jong1, 'jong2:', self.jong2)
        self.State(PrintFlag=True)

    def State(self, PrintFlag=False):
        stmsg = 'automata_state:' + str(self.automata_state)
        if(PrintFlag == True):
            print(stmsg)
        else:
            return stmsg

#==========================
#==========================
#==========================
def HGGetJaumMoum__EngChar(char, FullwidthAsciiTrans=True):
    """FullwidthAsciiTrans: 전각 영문자를 처리할 것인가"""
    HngKBDChar = ''
    if(len(char) == 1):
        # 아스키 영문자 확인
        HngKBDChar =  __jaummoum_from_eng52_dict__.get(char) # 아스키 영문자 대응 테이블
        if(HngKBDChar is None): # 두벌식(키보드) 자모에 해당하지 않는 경우
            if(FullwidthAsciiTrans == True): # 전각 영문자를 처리하는 경우
                # 전각 영문자 확인
                HngKBDChar =  __jaummoum_from_full_eng52_dict__.get(char) # 전각 영문자 대응 테이블
        #
        if(HngKBDChar is None): # 두벌식(키보드) 자모에 해당하지 않는 경우
            HngKBDChar = char # 원래 문자를 전달
    elif(len(char) == 2): # 글자가 2자 - {조합 모음}, {조합 자음:겹받침} 확인
        HngKBDChar =  __jaummoum_from_eng2_dict__.get(char)
        #-----
        # 아래 부분을 지원하지 않고 가상 코드만 남겨둔다.
        # {__jaummoum_from_full_eng2_dict__} 변수는 생성하지 않았다.
        # 현실적으로 전각 영문자 2글자로 반각 자모 1글자로 변환하는 상황은 없어서 검토가 필요.
        #-----
        #=if(HngKBDChar is None): # 두벌식(키보드) 자모에 해당하지 않는 경우
        #=    if(FullwidthAsciiTrans == True): # 전각 영문자를 처리하는 경우
        #=        HngKBDChar =  __jaummoum_from_full_eng2_dict__.get(char) # 전각 영문자 (2:1) 대응 테이블
        #-----
        #        
        if(HngKBDChar is None): # 두벌식(키보드) 자모에 해당하지 않는 경우
            HngKBDChar = char # 원래 문자를 전달
    elif(len(char) == 0):
        pass
    else: 
        assert False, f'{char}:{len(char)}'
    #
    return HngKBDChar

def HGGetJaumMoum__EngString(string, FullwidthAsciiTrans=True):#영문자->두벌식 자모
    """FullwidthAsciiTrans: 전각 영문자를 처리할 것인가"""
    HngKBDCharString = ''
    for char in string:
        HngKBDCharString += HGGetJaumMoum__EngChar(char, FullwidthAsciiTrans)
    return HngKBDCharString

def Eng2JaumMoum_Simple(EngString):
    #----------
    # 이 함수는 1글자 단위로 영문자를 두벌식 자모로 변환한다.
    # 이 함수는 알고리즘을 설명하기 위한 것이라서 {__jaummoum_from_eng52_dict__}변수에서 
    # 직접 1:1로 변환한다. 알고리즘 설명할 때 말고는 사용하지 않는다.
    #
    # 되도록이면 HGGetJaumMoum__EngString() 함수를 사용해야 한다.
    # HGGetJaumMoum__EngString() 함수는 HGGetJaumMoum__EngChar() 함수를 호출하며, 
    # HGGetJaumMoum__EngChar() 함수는 {조합 모음}과 겹받침도 변환할 수 있도록 1~2글자 단위로 처리한다.
    #----------
    # [영문자 -> 자음/모음]
    #=string = 'gks'
    #=EngString = 'gksrnr'  # 한글 자모: ㅎㅏㄴㄱㅜㄱ <==> '한국'
    HngKBDCharString = ''
    for EngChar in EngString:
        HngKBDChar =  __jaummoum_from_eng52_dict__.get(EngChar)
        if(HngKBDChar): 
            HngKBDCharString += HngKBDChar
        else: # 영문자에 해당하는 자모가 아닌 경우
            HngKBDCharString += EngChar # 원래 문자를 전달
    #
    return HngKBDCharString

def HGTransHalfJamo2Eng(string):
    """반각 자모를 영문자로 변환"""
    # HGTransString2EngString() 함수에서도 
    # {HalfJamoTrans=True} 상태이면 반각 자모를 영문자로 변환해주고,
    # {ChoJungJongJamoTrans=True} 상태이면 초중종 자모를 영문자로 변환하지만 
    # 다른 기능이랑 혼용하므로 
    # {반각 자모를 영문자로 변환} 기능만 수행하는 독립된 함수를 만든다.
    KBDCharString = ''
    for hgchar in string:
        Eng4JaumMoum = __eng_from_half_jamo_dict__.get(hgchar)
        if(Eng4JaumMoum is not None): # [반각 자모인 경우]
            KBDCharString += Eng4JaumMoum
        else: # 영문자로 바뀌지 않은 경우
            KBDCharString += hgchar # 원래 문자를 전달
    #
    return KBDCharString

def HGTransHalfJamo2KBDJamo(string):
    """반각 자모를 두벌식 자모로 변환"""
    # HGTransString2KBDJamo() 함수에서도 
    # {HalfJamoTrans=True} 상태이면 반각 자모를 영문자로 변환해주고,
    # {ChoJungJongJamoTrans=True} 상태이면 초중종 자모를 영문자로 변환하지만 
    # 다른 기능이랑 혼용하므로 
    # {반각 자모를 두벌식 자모로 변환} 기능만 수행하는 독립된 함수를 만든다.
    KBDCharString = ''
    for hgchar in string:
        JaumMoum = __jaummoum_from_half_jamo_dict__.get(hgchar)
        if(JaumMoum is not None): # [반각 자모인 경우]
            KBDCharString += JaumMoum
        else: # 자음/모음 낱글자로 바뀌지 않은 경우
            KBDCharString += hgchar # 원래 문자를 전달
    #
    return KBDCharString

def HGTransChoJungJongJamo2KBDJamo(string):
    """초중종 자모를 두벌식 자모로 변환"""
    # HGTransString2KBDJamo() 함수에서도 
    # {HalfJamoTrans=True} 상태이면 반각 자모를 영문자로 변환해주고,
    # {ChoJungJongJamoTrans=True} 상태이면 초중종 자모를 영문자로 변환하지만 
    # 다른 기능이랑 혼용하므로 
    # {초중종 자모를 두벌식 자모로 변환} 기능만 수행하는 독립된 함수를 만든다.
    KBDCharString = ''
    for hgchar in string:
        JaumMoum = __jaummoum_from_hangul_jamo_dict_.get(hgchar)
        if(JaumMoum is not None): # [초중종 자모인 경우]
            KBDCharString += JaumMoum
        else: # 자음/모음 낱글자로 바뀌지 않은 경우
            KBDCharString += hgchar # 원래 문자를 전달
    #
    return KBDCharString

def HGTransString2KBDJamo_by2step(string, HalfJamoTrans=True, ChoJungJongJamoTrans=True):
    #-----
    # 이 함수는 나중에 사용하는 곳이 없으면 폐기한다.
    #-----
    # HalfJamoTrans: 반각 자모를 두벌식 자모로 변환
    # ChoJungJongJamoTrans: 초중종 자모를 두벌식 자모로 변환
    #-----
    from hgunicode import hgGetChoJungJongInx
    #
    KBDCharString = ''
    ChoJungJongInxes = hgGetChoJungJongInx(string)
    # 형식 : {'cho': chosung_inx, 'jung': jungsung_inx, 'jong':jongsung_inx}
    #=print(ChoJungJongInxes)

    for i, cjj_n in enumerate(ChoJungJongInxes):
        #=print(cjj_n)
        if(len(cjj_n) > 0):
            #=print('cho:', cjj_n['cho'])
            #=print('jung:', cjj_n['jung'])
            KBDCharString += __kbd_jamo_from_chosung_inx_list__[cjj_n['cho']]
            KBDCharString += __kbd_jamo_from_jungsung_inx_list__[cjj_n['jung']]
            if(cjj_n['jong'] >= 1): # jonugsung-0: filler
                jongsung_inx = (cjj_n['jong'] - 1)
                KBDCharString += __kbd_jamo_from_jongsung_inx_list__[jongsung_inx]
        else: # 한글 음절이 아님: [초/중/종성]인덱스 없음(한글 낱글자[호환 자모]도 이쪽으로)
            # 조합 모음(7)과 조합 자음(겹받침)(11)은 1글자를 2글자 자모로 바꿈
            hgchar = string[i]
            JaumMoum = __double_jamo_from_single_jamo_18_dict__.get(hgchar)
            if(JaumMoum): # 자음/모음 낱글자 확인
                KBDCharString += JaumMoum
            # 추가 확인
            if(JaumMoum is None): # 자음/모음 낱글자로 바뀌지 않은 경우
                if(HalfJamoTrans == True): # 반각 자모를 두벌식 자모로 변환
                    JaumMoum = __jaummoum_from_half_jamo_dict__.get(hgchar)
                    if(JaumMoum): # 반각 자모 확인
                        KBDCharString += JaumMoum
            # 추가 확인
            if(JaumMoum is None): # 자음/모음 낱글자로 바뀌지 않은 경우
                if(ChoJungJongJamoTrans == True): # 초중종 자모를 두벌식 자모로 변환
                    JaumMoum = __jaummoum_from_hangul_jamo_dict_.get(hgchar)
                    if(JaumMoum): # [초중종 자모인 경우]
                        KBDCharString += JaumMoum
            # 추가 확인
            if(JaumMoum is None): # 자음/모음 낱글자로 바뀌지 않은 경우
                KBDCharString += hgchar # 원래 문자를 전달
    #
    return KBDCharString

def HGTransString2KBDJamo(string, HalfJamoTrans=True, ChoJungJongJamoTrans=True):
    # HalfJamoTrans: 반각 자모를 두벌식 자모로 변환
    # ChoJungJongJamoTrans: 초중종 자모를 두벌식 자모로 변환
    from hgunicode import hgGetChoJungJongInx_Char
    #
    KBDCharString = ''
    for hgchar in string:
        CJJ_Inx = hgGetChoJungJongInx_Char(hgchar)
        # 형식 : {'cho': chosung_inx, 'jung': jungsung_inx, 'jong':jongsung_inx}
        #=print(CJJ_Inx)
        if(len(CJJ_Inx) > 0): # [음절인 경우]
            #=print('cho:', CJJ_Inx['cho'])
            #=print('jung:', CJJ_Inx['jung'])
            KBDCharString += __kbd_jamo_from_chosung_inx_list__[CJJ_Inx['cho']]
            KBDCharString += __kbd_jamo_from_jungsung_inx_list__[CJJ_Inx['jung']]
            if(CJJ_Inx['jong'] >= 1): # jonugsung-0: filler
                jongsung_inx = (CJJ_Inx['jong'] - 1)
                KBDCharString += __kbd_jamo_from_jongsung_inx_list__[jongsung_inx]
        else: # 한글 음절이 아님: [초/중/종성]인덱스 없음(한글 낱글자[호환 자모]도 이쪽으로)
            # 조합 모음(7)과 조합 자음(겹받침)(11)은 1글자를 2글자 자모로 바꿈
            JaumMoum = __double_jamo_from_single_jamo_18_dict__.get(hgchar)
            if(JaumMoum): # [조합 모음이거나 조합 자음인 경우]
                KBDCharString += JaumMoum 
            # 추가 확인
            if(JaumMoum is None): # 자음/모음 낱글자로 바뀌지 않은 경우
                if(HalfJamoTrans == True): # 반각 자모를 두벌식 자모로 변환
                    JaumMoum = __jaummoum_from_half_jamo_dict__.get(hgchar)
                    if(JaumMoum): # [반각 자모인 경우]
                        KBDCharString += JaumMoum
            # 추가 확인
            if(JaumMoum is None): # 자음/모음 낱글자로 바뀌지 않은 경우
                if(ChoJungJongJamoTrans == True): # 초중종 자모를 두벌식 자모로 변환
                    JaumMoum = __jaummoum_from_hangul_jamo_dict_.get(hgchar)
                    if(JaumMoum): # [초중종 자모인 경우]
                        KBDCharString += JaumMoum
            # 추가 확인
            if(JaumMoum is None): # 자음/모음 낱글자로 바뀌지 않은 경우
                KBDCharString += hgchar # 원래 문자를 전달
    #
    return KBDCharString

def HGTransString2EngString_by2step(string, HalfJamoTrans=True, ChoJungJongJamoTrans=True):
    # HalfJamoTrans: 반각 자모를 영문자로 변환
    from hgunicode import hgGetChoJungJongInx
    #
    EngKBDCharString = ''
    ChoJungJongInxes = hgGetChoJungJongInx(string)
    # 형식 : {'cho': chosung_inx, 'jung': jungsung_inx, 'jong':jongsung_inx}
    #=print(ChoJungJongInxes)

    for i, cjj_n in enumerate(ChoJungJongInxes):
        #=print(cjj_n)
        if(len(cjj_n) > 0):
            EngKBDCharString += __eng_from_chosung_inx_list__[cjj_n['cho']]
            EngKBDCharString += __eng_from_jungsung_inx_list__[cjj_n['jung']]
            if(cjj_n['jong'] >= 1): # jonugsung-0: filler
                jongsung_inx = (cjj_n['jong'] - 1)
                EngKBDCharString += __eng_from_jongsung_inx_list__[jongsung_inx]                
        else: # 한글 음절이 아니라서 [초-중-종성]값이 없는 경우
            hgchar = string[i]
            Eng4JaumMoum = __eng_from_jaummoum51_dict__.get(hgchar)
            if(Eng4JaumMoum): # 자음/모음 낱글자 확인
                EngKBDCharString += Eng4JaumMoum
            # 추가 확인
            if(Eng4JaumMoum is None): # 영문자로 바뀌지 않은 경우
                if(HalfJamoTrans == True): # 반각 자모를 영문자로 변환
                    Eng4JaumMoum = __eng_from_half_jamo_dict__.get(hgchar)
                    if(Eng4JaumMoum): # 반각 자모인 경우
                        EngKBDCharString += Eng4JaumMoum
            # 추가 확인
            if(Eng4JaumMoum is None): # 영문자로 바뀌지 않은 경우
                if(ChoJungJongJamoTrans == True): # 초중종 자모를 영문자로 변환
                    JaumMoum = __jaummoum_from_hangul_jamo_dict_.get(hgchar) # 초중종 자모에 대응하는 두벌식 자모
                    if(JaumMoum is not None): # [초중종 자모인 경우]
                        Eng4JaumMoum = __eng_from_jaummoum51_dict__.get(JaumMoum) # 두벌식 자모에 대응하는 영문자 확인
                        if(Eng4JaumMoum): # 두벌식 자모인 경우
                            EngKBDCharString += Eng4JaumMoum
            # 추가 확인
            if(Eng4JaumMoum is None): # 영문자로 바뀌지 않은 경우
                EngKBDCharString += hgchar # 원래 문자를 전달
    #    
    return EngKBDCharString

def HGTransString2EngString(string, HalfJamoTrans=True, ChoJungJongJamoTrans=True):
    """
    HalfJamoTrans: 반각 자모를 영문자로 변환
    ChoJungJongJamoTrans: 초중종 자모를 영문자로 변환
    """
    from hgunicode import hgGetChoJungJongInx_Char
    #
    EngKBDCharString = ''
    for hgchar in string:
        CJJ_Inx = hgGetChoJungJongInx_Char(hgchar)
        # 형식 : {'cho': chosung_inx, 'jung': jungsung_inx, 'jong':jongsung_inx}
        #=print(CJJ_Inx)
        if(len(CJJ_Inx) > 0):
            EngKBDCharString += __eng_from_chosung_inx_list__[CJJ_Inx['cho']]
            EngKBDCharString += __eng_from_jungsung_inx_list__[CJJ_Inx['jung']]
            if(CJJ_Inx['jong'] >= 1): # jonugsung-0: filler
                jongsung_inx = (CJJ_Inx['jong'] - 1)
                EngKBDCharString += __eng_from_jongsung_inx_list__[jongsung_inx]
        else: # 한글 음절이 아니라서 [초-중-종성]값이 없는 경우
            Eng4JaumMoum = __eng_from_jaummoum51_dict__.get(hgchar)
            if(Eng4JaumMoum): # 자음/모음 낱글자 확인
                EngKBDCharString += Eng4JaumMoum
            # 추가 확인
            if(Eng4JaumMoum is None): # 영문자로 바뀌지 않은 경우
                if(HalfJamoTrans == True): # 반각 자모를 영문자로 변환
                    Eng4JaumMoum = __eng_from_half_jamo_dict__.get(hgchar)
                    if(Eng4JaumMoum): # 반각 자모인 경우
                        EngKBDCharString += Eng4JaumMoum
            # 추가 확인
            if(Eng4JaumMoum is None): # 영문자로 바뀌지 않은 경우
                if(ChoJungJongJamoTrans == True): # 초중종 자모를 영문자로 변환
                    JaumMoum = __jaummoum_from_hangul_jamo_dict_.get(hgchar) # 초중종 자모에 대응하는 두벌식 자모
                    if(JaumMoum is not None): # [초중종 자모인 경우]
                        Eng4JaumMoum = __eng_from_jaummoum51_dict__.get(JaumMoum) # 두벌식 자모에 대응하는 영문자 확인
                        if(Eng4JaumMoum): # 두벌식 자모인 경우
                            EngKBDCharString += Eng4JaumMoum
            # 추가 확인
            if(Eng4JaumMoum is None): # 영문자로 바뀌지 않은 경우
                EngKBDCharString += hgchar # 원래 문자를 전달
    #    
    return EngKBDCharString

def HGGetSyllable_JaumMoumString(JaumMoumString, debugPrint=False):
    if(debugPrint == True): # caption 출력
        print_cap = ['순서', '자모', '입력 전 상태', '입력 반환 글자', 
                        '입력 후 상태', '입력 후 오토마타 상태']
        print(*print_cap, sep='\t')
        #
        hgSyllable = ''
        curHng = HGAutom() # 한글 오토마타 생성
        for jamo_i, jamoChar in enumerate(JaumMoumString):
            BeforeInnerSyllable = curHng.GetSyllable()
            CurChar = curHng.PressChar(jamoChar)
            AfterInnerSyllable = curHng.GetSyllable()
            hgSyllable += CurChar
            print(f'{jamo_i}\t{jamoChar}\t{BeforeInnerSyllable}\t', end='')
            print(f'{CurChar}\t{AfterInnerSyllable}\t{curHng.State()}')
        #
        BeforeInnerSyllable = curHng.GetSyllable()
        CurChar = curHng.EndAutomata() # 음절 조합이 끝나지 않은 나머지 처리
        AfterInnerSyllable = curHng.GetSyllable()
        hgSyllable += CurChar
        print(f'End\t\t{BeforeInnerSyllable}\t', end='')
        print(f'{CurChar}\t{AfterInnerSyllable}\t{curHng.State()}')
        #    
        return hgSyllable
    else:
        #
        hgSyllable = ''
        curHng = HGAutom() # 한글 오토마타 생성
        for jamoChar in JaumMoumString:
            #=BeforeInnerSyllable = curHng.GetSyllable() # 입력 전 조합 상태
            hgSyllable += curHng.PressChar(jamoChar)
            #=AfterInnerSyllable = curHng.GetSyllable() # 입력 후 조합 상태
            #=CurState = curHng.State()
        #
        hgSyllable += curHng.EndAutomata() # 음절 조합이 끝나지 않은 나머지 처리
        #    
        return hgSyllable

def HGGetSyllable__EngString(string, FullwidthAsciiTrans=True, debugPrint=False):
    """FullwidthAsciiTrans: 전각 영문자를 처리할 것인가"""
    JaumMoumString = HGGetJaumMoum__EngString(string, 
                        FullwidthAsciiTrans=FullwidthAsciiTrans)
    if(debugPrint == True):
        print(f'{string}\t--->\t{JaumMoumString}\t')
    HGSyllable = HGGetSyllable_JaumMoumString(JaumMoumString, debugPrint=debugPrint)
    return HGSyllable

#------------------
#------------------
#------------------
def HGGetHalfJamo__EngChar(char, FullwidthAsciiTrans=True):
    """FullwidthAsciiTrans: 전각 영문자를 처리할 것인가"""
    HngKBDChar = ''
    if(len(char) == 1):
        HngKBDChar =  __half_jamo_from_eng52_dict__.get(char) # 아스키 영문자 대응 테이블
        if(HngKBDChar is None): # 반각 자모에 해당하지 않는 경우
            if(FullwidthAsciiTrans == True): # 전각 영문자를 처리하는 경우
                HngKBDChar =  __half_jamo_from_full_eng52_dict__.get(char) # 전각 영문자 대응 테이블
        #
        if(HngKBDChar is None): # 반각 자모에 해당하지 않는 경우
            HngKBDChar = char # 원래 문자를 전달
    elif(len(char) == 2): # 글자가 2자 - {조합 모음}, {조합 자음:겹받침} 확인
        HngKBDChar =  __half_jamo_from_eng2_dict__.get(char)
        #-----
        # 아래 부분을 지원하지 않고 가상 코드만 남겨둔다.
        # {__half_jamo_from_full_eng2_dict__} 변수는 생성하지 않았다.
        # 현실적으로 전각 영문자 2글자로 반각 자모 1글자로 변환하는 상황은 없어서 검토가 필요.
        #-----
        #=if(HngKBDChar is None): # 반각 자모에 해당하지 않는 경우
        #=    if(FullwidthAsciiTrans == True): # 전각 영문자를 처리하는 경우
        #=        HngKBDChar =  __half_jamo_from_full_eng2_dict__.get(char) # 전각 영문자 대응 테이블
        #-----
        if(HngKBDChar is None): # 반각 자모에 해당하지 않는 경우
            HngKBDChar = char # 원래 문자를 전달
    elif(len(char) == 0):
        pass
    else: 
        assert False, f'{char}:{len(char)}'
    #
    return HngKBDChar

def HGGetHalfJamo__EngString(string, FullwidthAsciiTrans=True):#영문자->반각 자모
    """FullwidthAsciiTrans: 전각 영문자를 처리할 것인가"""
    #------
    # 이 함수는 1단계(영문자->반각 자모)로 처리하지만 
    # HGGetHalfJamo__EngString2() 함수는 2단계(영문자->두벌식 자모->반각 자모)로 처리한다.
    #------
    HngKBDCharString = ''
    for char in string:
        HngKBDCharString += HGGetHalfJamo__EngChar(char, FullwidthAsciiTrans)
    return HngKBDCharString

def HGGetHalfJamo__EngString2(string, FullwidthAsciiTrans=True, debugPrint=False):
    """FullwidthAsciiTrans: 전각 영문자를 처리할 것인가"""
    #------
    # 이 함수는 2단계(영문자->두벌식 자모->반각 자모)로 처리하지만 
    # HGGetHalfJamo__EngString()함수는 1단계(영문자->반각 자모)로 처리한다.
    #------
    from hgunicode import HGGetHalfJamoString__CompatibleJamoString
    # 영문자를 두벌식 자모로 변환
    JaumMoumString = HGGetJaumMoum__EngString(string, 
                        FullwidthAsciiTrans=FullwidthAsciiTrans)
    #
    if(debugPrint == True):
        print(f'{string}\t--->\t{JaumMoumString}\t')
    # 두벌식 자모를 반각 자모로 변환
    HalfJamo = HGGetHalfJamoString__CompatibleJamoString(JaumMoumString) 
    return HalfJamo


#================================
#================================
#================================
from unittest import TestCase, main

class HGTest(TestCase):
    def test_11(self):
        print()
        print()
        string = '가'
        EngKBDCharString = HGTransString2EngString(string)
        print(string, ':', EngKBDCharString)
        HngKBDChar = HGGetJaumMoum__EngString(EngKBDCharString)
        print(string, ':', HngKBDChar)

        string = '닫'
        EngKBDCharString = HGTransString2EngString(string)
        print(string, ':', EngKBDCharString)
        HngKBDChar = HGGetJaumMoum__EngString(EngKBDCharString)
        print(string, ':', HngKBDChar)

        string = '동해물과 백두산이'
        for ch in string:
            EngKBDCharString = HGTransString2EngString(ch)
            HngKBDChar = HGGetJaumMoum__EngString(EngKBDCharString)
            print(f'{ch} : {EngKBDCharString} === {HngKBDChar}')


        string = 'ㄱㄲㄴㄷㅏㅑㅓㅙㄳㄶ'


    def test_12(self):
        print()
        print()
        print(HGGetSyllable_KBDEngJamo3('a', 'k'))
        print(HGGetSyllable_KBDEngJamo3('a', 'k', 'R'))

    def _test_spare(self):
        #=print(HGGetJaumMoum__EngChar('r'))
        #=print(HGGetSyllable_JaumMoum3('ㄱ', 'ㅏ', 'ㄱ'))
        pass


if __name__ == '__main__':
    main()

