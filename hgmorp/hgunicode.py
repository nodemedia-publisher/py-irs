#---
#---
def _lline_(): # 다른 라이브러리와 함수 이름이 겹치지 않도록 'l'자를 추가
    import inspect
    return inspect.currentframe().f_back.f_lineno

#---
#---
import hgbasic
from hgbasic import get_hangul_syllable__index, PrintCodeValue_String

from hgchartype import get_script
from hgchartype import 글자상태_자모

from hgbasic import (
    __HG_SYL_NUM__, # = 11172  # (ord('힣') - ord('가') + 1)
    __HG_SYL_LEADING_DEC__, # = 44032 # ord('가')
    __HG_CHO_NUM__, # = 19 # 초성 개수
    __HG_JUNG_NUM__, # = 21 # 중성 개수
    __HG_JONG_NUM__, # = 28 # 종성 개수[종성( 27 + 채움(1)]
    __HG_JUNG_X_JONG_NUM__, # 중성 개수 x 종성 개수 = 588
)
##----------
##----------

### define
#--------------------------
# 초성, 중성, 종성 호환 자모
#--------------------------
__compa_jamo_string_4_chosung__ = 'ㄱㄲㄴㄷㄸㄹㅁㅂㅃㅅㅆㅇㅈㅉㅊㅋㅌㅍㅎ' # Hangul Compatibility Jamo (0x3131-0x314E)(ksc5601: 0xA4A1~0xA4BE)
__compa_jamo_string_4_jungsung__ = 'ㅏㅐㅑㅒㅓㅔㅕㅖㅗㅘㅙㅚㅛㅜㅝㅞㅟㅠㅡㅢㅣ' # Hangul Compatibility Jamo (0x314F-0x3163)(ksc5601:0xA4BF~0xA4D3)
__compa_jamo_string_4_jongsung__ = 'ㄱㄲㄳㄴㄵㄶㄷㄹㄺㄻㄼㄽㄾㄿㅀㅁㅂㅄㅅㅆㅇㅈㅊㅋㅌㅍㅎ' # Hangul Compatibility Jamo (ksc5601 0xA4A1 ~ 0xA4BE <= 종성부용초성)


__compa_jamo1_string_double_moum_7__ = 'ㅘㅙㅚㅝㅞㅟㅢ' #--- 중성 1글자로 표현하는 이중모음(7) # Hangul Compatibility Jamo (0x3131-ex314E)(ksc5601: 0xA4A1~0xA4D3)
__compa_jamo1_string_double_jaum_11__ = 'ㄳㄵㄶㄺㄻㄼㄽㄾㄿㅀㅄ' #--- 종성 호환 2글자 겹받침(11) # Hangul Compatibility Jamo (0x3131-ex314E)(ksc5601: 0xA4A1~0xA4D3)

#
__HangulCompatibilityJamo_Modern_51__ =  'ㄱㄲㄳㄴㄵㄶㄷㄸㄹㄺㄻㄼㄽㄾㄿㅀㅁㅂㅃㅄㅅㅆㅇㅈㅉㅊㅋㅌㅍㅎㅏㅐㅑㅒㅓㅔㅕㅖㅗㅘㅙㅚㅛㅜㅝㅞㅟㅠㅡㅢㅣ' # (51자) 현대 음절 가능한 Hangul Compatibility Jamo (0x3131-0x3163)(ksc5601: 0xA4A1~0xA4D3)
__jamo_string_modern_51__ = "ᄀᄁᆪᄂᆬᆭᄃᄄᄅᆰᆱᆲᆳᆴᆵᆶᄆᄇᄈᆹᄉᄊᄋᄌᄍᄎᄏᄐᄑ하ᅢᅣᅤᅥᅦᅧᅨᅩᅪᅫᅬᅭᅮᅯᅰᅱᅲᅳᅴᅵ" # (51자) # Hangul Jamo (0x1110-0x1175)

#--------------------------
# 초성, 중성, 종성 자모
#--------------------------
__chosung_jamo_code_list__ = [0x1100,0x1101,0x1102,0x1103,0x1104,0x1105,0x1106,0x1107,0x1108,
                            0x1109,0x110a,0x110b,0x110c,0x110d,0x110e,0x110f,0x1110,0x1111,0x1112] 
__jungsung_jamo_code_list__ = [0x1161,0x1162,0x1163,0x1164,0x1165,0x1166,0x1167,0x1168, 0x1169, 0x116a,
                            0x116b,0x116c,0x116d,0x116e,0x116f,0x1170,0x1171,0x1172, 0x1173, 0x1174,0x1175] 
__jongsung_jamo_code_list__ = [0x11a8, 0x11a9, 0x11aa,0x11ab,0x11ac,0x11ad,0x11ae,0x11af, 0x11b0,
                            0x11b1,0x11b2, 0x11b3, 0x11b4, 0x11b5, 0x11b6, 0x11b7, 0x11b8, 0x11b9, 
                            0x11ba, 0x11bb, 0x11bc, 0x11bd, 0x11be, 0x11bf, 0x11c0, 0x11c1, 0x11c2] 

#--------------------------
# 초성, 중성, 종성 자모
#--------------------------
__chosung_jamo_string__ = 'ᄀᄁᄂᄃᄄᄅᄆᄇᄈᄉᄊᄋᄌᄍᄎᄏᄐᄑᄒ'  # Hangul Jamo (0x1110-0x1112)
__jungsung_jamo_string__ = 'ᅡᅢᅣᅤᅥᅦᅧᅨᅩᅪᅫᅬᅭᅮᅯᅰᅱᅲᅳᅴᅵ'  # Hangul Jamo (0x1161-0x1175)
__jongsung_jamo_string__ = 'ᆨᆩᆪᆫᆬᆭᆮᆯᆰᆱᆲᆳᆴᆵᆶᆷᆸᆹᆺᆻᆼᆽᆾᆿᇀᇁᇂ' # Hangul Jamo (0x11A8-0x11C2)

#--------------------------
#--------------------------
# 방점
__SingleDotBangjeom = '〮' # 0x302E 	HANGUL SINGLE DOT TONE MARK
__DoubleDotBangjeom = '〯' # 0x302F 	HANGUL DOUBLE DOT TONE MARK

__HANGUL_CHOSEONG_FILLER_v__ = int('115F', 16)   # 'ᅟ'  (화면에 안 보임)
__HANGUL_CHOSEONG_FILLER__ =  'ᅟ' # 4447  0x115F # (화면에 안 보임)
__HANGUL_JUNGSEONG_FILLER_v__ = int('1160', 16) # 'ᅠ' (화면에 안 보임)
__HANGUL_JUNGSEONG_FILLER__ = 'ᅠ' # 4448  0x1160 # (화면에 안 보임)

#--------------------------
#--------------------------
#----- 전각 아스키 문자 영역
__Fullascii_Begin__ = '！' # 0xFF01
__Fullascii_End__ = '～'   # 0xFF5E

__Fullascii_Begin_v__ = ord(__Fullascii_Begin__) # '！' # 0xFF01
__Fullascii_End_v__ = ord(__Fullascii_End__) # '～'   # 0xFF5E

__Halfascii_Begin__ = '!' # 0x0021
__Halfascii_End__ = '~' # 0x007E

__Halfascii_Begin_v__ = ord(__Halfascii_Begin__) # '!' # 0x0021
__Halfascii_End_v__ = ord(__Halfascii_End__) # '~' # 0x007E

# 전각 아스키 영역과 아스키 영역 간격: 0xFEE0(65248)


#--------------------------
#-------------------------- 반각 자모 처리
__halfwidth_jamo52_list__ = 'ﾠﾡﾢﾣﾤﾥﾦﾧﾨﾩﾪﾫﾬﾭﾮﾯﾰﾱﾲﾳﾴﾵﾶﾷﾸﾹﾺﾻﾼﾽﾾￂￃￄￅￆￇￊￋￌￍￎￏￒￓￔￕￖￗￚￛￜ' # 맨 앞에 반각 채움 문자 포함, 총 52자
__compatible_jamo52_list_for_halfwidth_jamo = 'ㅤㄱㄲㄳㄴㄵㄶㄷㄸㄹㄺㄻㄼㄽㄾㄿㅀㅁㅂㅃㅄㅅㅆㅇㅈㅉㅊㅋㅌㅍㅎㅏㅐㅑㅒㅓㅔㅕㅖㅗㅘㅙㅚㅛㅜㅝㅞㅟㅠㅡㅢㅣ' # 반각자모는 맨 앞에 반각채움 문자가 있어서 쌍을 이루도록 맨 앞에 한글 채움 문자


#---------------------------------------------
#---------------------------------------------
#---------------------------------------------
def __HG_CHO_CHAR(chosung_inx, jamo=True):
    # jamo=True: Hangul Jamo, 
    # jamo=False: Hangul Compatibility Jamo
    chosung_jamo = ''
    if((chosung_inx < 0) or (chosung_inx >= __HG_CHO_NUM__)): 
        return chosung_jamo  # logic error
    if(jamo == True):
        return __chosung_jamo_string__[chosung_inx]
    else: 
        return __compa_jamo_string_4_chosung__[chosung_inx]

def __HG_JUNG_CHAR(jungsung_inx, jamo=True):
    # jamo=True: Hangul Jamo, 
    # jamo=False: Hangul Compatibility Jamo
    jungsung_jamo = ''
    if((jungsung_inx < 0) or (jungsung_inx >= __HG_JUNG_NUM__)): 
        return jungsung_jamo  # logic error
    if(jamo == True):
        return __jungsung_jamo_string__[jungsung_inx]
    else:
        return __compa_jamo_string_4_jungsung__[jungsung_inx]

def __HG_JONG_CHAR(jongsung_inx, jamo=True):
    # jamo=True: Hangul Jamo, 
    # jamo=False: Hangul Compatibility Jamo
    jongsung_jamo = ''
    if((jongsung_inx < 0) or (jongsung_inx >= __HG_JONG_NUM__)): 
        return jongsung_jamo  # logic error
    if(jongsung_inx == 0): return jongsung_jamo # fill-state
    if(jamo == True):
        return __jongsung_jamo_string__[jongsung_inx - 1]
    else:
        return __compa_jamo_string_4_jongsung__[jongsung_inx - 1]

def hgIsHangulCompatibilityJamo(hgchar):
    #=print('ord(hgchar):', hex(ord(hgchar))) #= debug
    if((ord(hgchar) >= 0x3131) and (ord(hgchar) <= 0x318E)): 
        return True # Hangul Compatibility Jamo 0x3131(ᄀ) 0x318e(ㆎ))
    return False

def hgGetChoJungJongChar__CompatibilityJamo(hgchar):
    #-----
    # (낱글자) 호환 자모를 초성,중성,종성 자모로 변환
    # 사전 순서로 된 목록의 사전 검색에서 낱글자 자음을 초성으로 변환해야 하는 경우가 있음
    # 예를 들어 "한ㄱ" 을 검색하면 추천 단어는 '한'+'ㄱ~' 으로 시작하는 것을 처리할 때
    # "한ㄱ"의 'ㄱ'은 자음이라서 초성이 아니므로 초중종 자모로 구성된 사전에서 검색 불가능
    # 이런 경우 초중종 사전에서 검색할 수 있도록 두벌식 자모 'ㄱ'를 초성 자모로 변경할 때 
    #-----
    #=print('ord(hgchar):', hex(ord(hgchar))) #= debug
    ChoJungJongChar = None
    compatible_jamo_inx = __HangulCompatibilityJamo_Modern_51__.find(hgchar)
    if(compatible_jamo_inx >= 0): # 호환 자모인 경우
        ChoJungJongChar = __jamo_string_modern_51__[compatible_jamo_inx]
        return ChoJungJongChar
    else: # 호환 자모가 아닌 경우
        return ChoJungJongChar

def hgGetChosungInx_JamoChar(JamoChar):
    jamo_inx = __chosung_jamo_string__.find(JamoChar)
    return jamo_inx

def hgGetJungsungInx_JamoChar(JamoChar):
    jamo_inx = __jungsung_jamo_string__.find(JamoChar)
    return jamo_inx

def hgGetJongsungInx_JamoChar(JamoChar):
    jamo_inx = __jongsung_jamo_string__.find(JamoChar)
    return jamo_inx

def hgGetChosungInx_Char(hgchar): # 조합 공식을 역으로 분해해서 처리
    chosung_inx = (-1)
    syllable_inx = hgGetSyllable_inx(hgchar)
    jongsung_inx = hgGetJongsungInx_Char(hgchar)
    jungsung_inx = hgGetJungsungInx_Char(hgchar)
    if((syllable_inx < 0) or (jongsung_inx < 0) or (jungsung_inx < 0)):
        return chosung_inx
    
    syl_jong_div_jong_inx= int((syllable_inx - jongsung_inx) / __HG_JONG_NUM__)
    xxx_minus_jung_inx = syl_jong_div_jong_inx - jungsung_inx
    chosung_inx = int(xxx_minus_jung_inx / __HG_JUNG_NUM__)
    return chosung_inx

def hgGetJungsungInx_Char(hgchar): # 조합 공식을 역으로 분해해서 처리
    jungsung_inx = (-1)
    syllable_inx = hgGetSyllable_inx(hgchar)
    jongsung_inx = hgGetJongsungInx_Char(hgchar)
    if((syllable_inx < 0) or (jongsung_inx < 0)):
        return jungsung_inx
    
    syl_jong_div_jong_inx= int((syllable_inx - jongsung_inx) / __HG_JONG_NUM__)
    jungsung_inx = syl_jong_div_jong_inx % __HG_JUNG_NUM__
    return jungsung_inx

def hgGetJongsungInx_Char(hgchar): # 조합 공식을 역으로 분해해서 처리
    jongsung_inx = (-1)
    syllable_inx = hgGetSyllable_inx(hgchar)
    if(syllable_inx < 0):
        return jongsung_inx

    jongsung_inx = syllable_inx % __HG_JONG_NUM__
    return jongsung_inx

def _hgGetJongsungInx_SyllableInx_del_think(syllable_inx):
    if((syllable_inx < 0) or (syllable_inx >= __HG_SYL_NUM__)):
        return (-1)
    jongsung_inx = syllable_inx % __HG_JONG_NUM__
    return jongsung_inx

def hgGetSyllable_inx(hgchar):
    syllable_inx = (-1)
    hglen = len(hgchar)
    if(hglen != 1): 
        return syllable_inx
    dec_char = ord(hgchar)
    syllable_inx = dec_char - __HG_SYL_LEADING_DEC__
    if((syllable_inx < 0) or (syllable_inx >= __HG_SYL_NUM__)): # 한글 음절 범위 초과
        syllable_inx = (-1)
    return syllable_inx

def hgGetChoJungJongInx_Char_Logic(hgchar):
    # 한글 음절에 대한 자모 인덱스 구하기: 
    # ===> 아래 코드는 깔끔해보이지만 조합 공식을 역으로 분해하는 데다가 
    # 내부에서 중복 연산하므로 비효율적이라 사용하지 않음.
    # 형식 : {'cho': chosung_inx, 'jung': jungsung_inx, 'jong':jongsung_inx}
    ChoJungJongInx = {}
    hglen = len(hgchar)
    if(hglen != 1): 
        return ChoJungJongInx

    chosung_inx = hgGetChosungInx_Char(hgchar)
    jungsung_inx = hgGetJungsungInx_Char(hgchar)
    jongsung_inx = hgGetJongsungInx_Char(hgchar)
    if((chosung_inx < 0) or (jungsung_inx < 0) or (jongsung_inx < 0)): 
        return ChoJungJongInx
    ChoJungJongInx = {'cho': chosung_inx, 'jung': jungsung_inx, 'jong':jongsung_inx}
    return ChoJungJongInx

def hgGetChoJungJongInx_Char(hgchar):
    #-----
    # 한글 음절에 대한 자모 인덱스 구하기: 
    #-----
    # 불필요한 연산을 줄이고 한꺼번에 직접 계산
    # 형식 : {'cho': chosung_inx, 'jung': jungsung_inx, 'jong':jongsung_inx}
    #-----
    ChoJungJongInx = {}
    syllable_inx = hgGetSyllable_inx(hgchar) # 음절 인덱스 구하기
    if(syllable_inx < 0):
        return ChoJungJongInx
    #-----
    # 종성 인덱스
    #-----
    jongsung_inx = syllable_inx % __HG_JONG_NUM__
    #-----
    # 중성 인덱스
    #-----
    #---a): 조합 공식을 역으로 적용한 것이지만 코드가 길어서 사용하지 않음.
    #=syl_jong_div_jong_inx= int((syllable_inx - jongsung_inx) / __HG_JONG_NUM__)
    #---b): a)처럼 {jongsung_inx}를 계산하지 않고 나누면 자동으로 잘려서 결과가 같다.
    syl_jong_div_jong_inx = int(syllable_inx / __HG_JONG_NUM__)
    jungsung_inx = syl_jong_div_jong_inx % __HG_JUNG_NUM__ # 나머지 값 구하기
    #-----
    # 초성 인덱스
    #-----
    #---a): 조합 공식을 역으로 적용한 것이지만 코드가 길어서 사용하지 않음.
    #=xxx_minus_jung_inx = syl_jong_div_jong_inx - jungsung_inx
    #=chosung_inx = int(xxx_minus_jung_inx / __HG_JUNG_NUM__)
    #---b): a)처럼 {jungsung_inx}를 계산하지 않고 나누면 자동으로 잘려서 결과가 같다.
    chosung_inx = int(syllable_inx /__HG_JUNG_X_JONG_NUM__) # 중성 개수 x 종성 개수 = 588
    #-----
    #
    ChoJungJongInx = {'cho': chosung_inx, 'jung': jungsung_inx, 'jong':jongsung_inx}
    return ChoJungJongInx

def hgGetChoJungJongInx(string):
    ChoJungJongInxList = []
    for hgchar in string:
        ChoJungJongInx = hgGetChoJungJongInx_Char(hgchar)
        ChoJungJongInxList.append(ChoJungJongInx)
    #print(ChoJungJongInxList)
    return ChoJungJongInxList

def hgGetChoJungJongString_Inx(ChoJungJongInx, jamo=True):
    '''한글 자모 인덱스로부터 한글 자모 문자열 변환
    jamo=True: Hangul Jamo, 
    jamo=False: Hangul Compatibility Jamo
    '''
    ChoJungJongString = '';
    if(ChoJungJongInx == None) or (len(ChoJungJongInx) <= 0):
        return ChoJungJongString
    #
    ChoInx = ChoJungJongInx.get('cho')
    JungInx = ChoJungJongInx.get('jung')
    JongInx = ChoJungJongInx.get('jong')
    #
    if (ChoInx != None) and (ChoInx >= 0): 
        ChoJungJongString += __HG_CHO_CHAR(ChoInx, jamo)
    if (JungInx != None) and (JungInx >= 0): 
        ChoJungJongString += __HG_JUNG_CHAR(JungInx, jamo)
    if (JongInx != None) and (JongInx >= 1):  # 0-inx, fill-code
        ChoJungJongString += __HG_JONG_CHAR(JongInx, jamo)
    return ChoJungJongString

def hgGetChoJungJongString_Char(hgchar, jamo=True):
    # 한글 음절을 초성, 중성, 종성 문자열로 변환
    # jamo=True: Hangul Jamo, 
    # jamo=False: Hangul Compatibility Jamo
    ChoJungJongString = ''
    ChoJungJongInx = hgGetChoJungJongInx_Char(hgchar)
    if(len(ChoJungJongInx) >= 1): # 한글 음절이 아닌 경우에는 길이가 없다.
        ChoJungJongString = hgGetChoJungJongString_Inx(ChoJungJongInx, jamo=jamo)
    return ChoJungJongString

def hgGetChoJungJongJamo_Inx(ChoJungJongInx):
    ChoJungJongJamo = {}
    if(ChoJungJongInx == None): 
        return ChoJungJongJamo
    if(len(ChoJungJongInx) <= 0):
        return ChoJungJongJamo

    if ChoJungJongInx.get('cho') != None:
        if(ChoJungJongInx.get('cho') >= 0): 
            ChoJungJongJamo['cho'] = __HG_CHO_CHAR(ChoJungJongInx.get('cho'), jamo=True)
    if ChoJungJongInx.get('jung') != None:
        if(ChoJungJongInx.get('jung') >= 0): 
            ChoJungJongJamo['jung'] = __HG_JUNG_CHAR(ChoJungJongInx.get('jung'), jamo=True)
    if ChoJungJongInx.get('jong') != None:
        if(ChoJungJongInx.get('jong') >= 1):  # 0-inx, fill-code
            ChoJungJongJamo['jong'] = __HG_JONG_CHAR(ChoJungJongInx.get('jong'), jamo=True)
    return ChoJungJongJamo

def hgGetChoJungJongJamo_Char(hgchar):
    ChoJungJongJamo = {}
    ChoJungJongInx = hgGetChoJungJongInx_Char(hgchar)
    if(len(ChoJungJongInx) > 0):
        ChoJungJongJamo = hgGetChoJungJongJamo_Inx(ChoJungJongInx)
    return ChoJungJongJamo

def PrintChoJungJongChar_Inx(ChoJungJongInx, jamo=True):
    if(ChoJungJongInx == None): 
        return
    if(len(ChoJungJongInx) <= 0):
        return
    print('자모:', end='')
    ChoJungJongString = hgGetChoJungJongString_Inx(ChoJungJongInx, jamo)
    print(ChoJungJongString, end='')
    print('')

def PrintChoJungJongChar(hgchar, jamo=True):
    ChoJungJongInx = hgGetChoJungJongInx_Char(hgchar)
    if(len(ChoJungJongInx) >= 1):
        PrintChoJungJongChar_Inx(ChoJungJongInx, jamo)

def hgGetChoJungJongString(string, jamo=True, CompatibleJamo2ChoJungJong=False):
    '''
    jamo=True: Hangul Jamo, 
    jamo=False: Hangul Compatibility Jamo
    '''
    #=print(string)
    ChoJungJongString = '';
    for hgchar in string:
        ChoJungJongString_Cur = hgGetChoJungJongString_Char(hgchar, jamo)
        if(len(ChoJungJongString_Cur) <= 0): # 초중종 자모로 변환되지 않은 경우
            if(jamo == True): # [jamo==True:유니코드 자모(초중종)]로 변환할 때
                if(CompatibleJamo2ChoJungJong == True):
                    # (낱글자) 호환 자모를 초성,중성 자모로 변환
                    # (사전 검색에서 낱글자 자음을 초성으로 변환해야 하는 경우가 있음)
                    # ex) "한ㄱ"을 검색하면 추천 단어는 '한'+'ㄱ~' 으로 시작하는 것을 처리할 때
                    each_jamo_char = hgGetChoJungJongChar__CompatibilityJamo(hgchar)
                    if(each_jamo_char != None):
                        ChoJungJongString += each_jamo_char
                        continue # 호환 자모를 변환했으므로 루프 처음으로 이동
            # 위에서 처리된 것이 없으면
            ChoJungJongString += hgchar # 원래 글자를 넘겨 줌
        else: # 초,중,종 자모 문자열로 변환된 경우
            ChoJungJongString += ChoJungJongString_Cur
    
    #=print(ChoJungJongString)
    return ChoJungJongString

def hgGetSyllable__Jamo3(ChoJamo, JungJamo, JongJamo=''):
    HGSyllable = ''
    #=if(isinstance(ChoJamo, str) != True): return HGSyllable
    #=if(isinstance(JungJamo, str) != True): return HGSyllable
    #=if(isinstance(JongJamo, str) != True): 
    #=    #=assert False, '(isinstance(JongJamo, str) != True)'
    #=    return HGSyllable

    #=if(len(ChoJamo) != 1): return HGSyllable
    #=if(len(JungJamo) != 1): return HGSyllable
    #
    ChoJamo_Inx = __chosung_jamo_string__.find(ChoJamo)
    if(ChoJamo_Inx <= (-1)):
        return HGSyllable
    JungJamo_Inx = __jungsung_jamo_string__.find(JungJamo)
    if(JungJamo_Inx <= (-1)):
        return HGSyllable
    JongJamo_Inx = 0
    if(len(JongJamo) > 0): # 종성-0: 종성 채움 상태
        JongJamo_Inx = __jongsung_jamo_string__.find(JongJamo)
        if(JongJamo_Inx <= (-1)):
            return HGSyllable
        JongJamo_Inx += 1 # 종성 인덱스는 채움 상태를 반영하여 [종성자모목록]에 '+1'처리

    # 현대어 음절 규칙에 맞게 음절 생성
    HGSyllable = get_hangul_syllable__index \
        (ChoJamo_Inx, JungJamo_Inx, JongJamo_Inx)
    #
    return HGSyllable

def hgSyllableStr__Jamo3Str(JamoStr): # 초중종 자모 문자열을 음절로 변환
    SyllableStr = ''
    StrLen = len(JamoStr)
    StrPos = 0
    while(StrPos < StrLen):
        Syllable = ''
        CurChar = JamoStr[StrPos]
        #디버깅출력(CurChar)
        chosung_jamo_inx = __chosung_jamo_string__.find(CurChar)
        if(chosung_jamo_inx >= 0): # 초성 자모 인가
            if((StrPos + 1) < StrLen):
                NextChar = JamoStr[StrPos+1]
                jungsung_jamo_inx = __jungsung_jamo_string__.find(NextChar)
                if(jungsung_jamo_inx >= 0): # 중성 자모인가
                    if((StrPos + 2) < StrLen):
                        NextNextChar = JamoStr[StrPos+2]
                        jongsung_jamo_inx = \
                            __jongsung_jamo_string__.find(NextNextChar)
                        if(jongsung_jamo_inx >= 0): # 종성 자모인가
                            # 초성+중성+종성
                            Syllable = get_hangul_syllable__index(chosung_jamo_inx, 
                                        jungsung_jamo_inx, (jongsung_jamo_inx + 1)) # 종성 자모 인덱스는 종성 채움을 위해서 '+1'을 한다.
                            StrPos += 3
                        else: # 초성+중성_^_자모
                            Syllable = get_hangul_syllable__index \
                                        (chosung_jamo_inx, jungsung_jamo_inx)
                            StrPos += 2
                    else: # 초성+중성__JamoStr끝
                        Syllable = get_hangul_syllable__index \
                                    (chosung_jamo_inx, jungsung_jamo_inx)
                        StrPos += 2
                else: # 초성__^_자모 => 음절 구성이 안 되므로 통과
                    pass
            else:   # 초성__문자열끝 => 음절 구성이 안 되므로 통과
                pass
        # 앞에서 음절이 생성되었으면 음절과 합치고, 아니면 현재 글자를 합친다.
        if(len(Syllable) > 0):
            SyllableStr += Syllable
        else:
            SyllableStr += CurChar
            StrPos += 1
    return SyllableStr

#---------------------------------------------
#---------------------------------------------
#---------------------------------------------
def HGGetAscii__FullwidthAscii(char):
    """전각 아스키 문자를 (반각) (기본 라틴) 아스키 문자로 변환"""
    #
    KBDChar = ''
    if(len(char) == 1):
        if((char >= __Fullascii_Begin__) and (char <= __Fullascii_End__)):
            half_ascii_v = (ord(char) - ord(__Fullascii_Begin__)) + __Halfascii_Begin_v__
            KBDChar = chr(half_ascii_v)
    #
    return KBDChar

def HGGetAsciiString__FullwidthAsciiString(string):
    """전각 아스키 문자를 (반각) (기본 라틴) 아스키 문자로 변환"""
    #
    KBDstring = ''
    for char in string:
        half_ascii = HGGetAscii__FullwidthAscii(char)
        if(half_ascii): 
            KBDstring += half_ascii # 반각 아스키 문자로 처리
        else: 
            KBDstring += char # 원래 문자로 처리
    #
    return KBDstring

def HGGetFullwidthAscii__Ascii(char):
    """(반각) (기본 라틴) 아스키 문자를 전각 아스키 문자로 변환"""
    #
    KBDChar = ''
    if(len(char) == 1):
        if((char >= __Halfascii_Begin__) and (char <= __Halfascii_End__)):
            full_ascii_v = (ord(char) - ord(__Halfascii_Begin__)) + __Fullascii_Begin_v__
            KBDChar = chr(full_ascii_v)
    #
    return KBDChar

def HGGetFullwidthAsciiString__AsciiString(string):
    """(반각) (기본 라틴) 아스키 문자를 전각 아스키 문자로 변환"""
    #
    KBDstring = ''
    for char in string:
        fill_ascii = HGGetFullwidthAscii__Ascii(char)
        if(fill_ascii): 
            KBDstring += fill_ascii # 전각 아스키 문자로 처리
        else: 
            KBDstring += char # 원래 문자로 처리
    #
    return KBDstring

#---------------------------------------------
#---------------------------------------------
#---------------------------------------------
def HGGetHalfJamo__CompatibleJamo(char):
    """호환 자모를 반각 문자로 변환"""
    #
    NewChar = ''
    char_inx = __compatible_jamo52_list_for_halfwidth_jamo.find(char)
    if(char_inx >= 0):
        NewChar = __halfwidth_jamo52_list__[char_inx]
    #
    return NewChar

def HGGetHalfJamoString__CompatibleJamoString(string):
    """호환 자모를 반각 문자로 변환"""
    #
    NewString = ''
    for char in string:
        half_char = HGGetHalfJamo__CompatibleJamo(char)
        if(half_char): 
            NewString += half_char # 반각 자모로 처리
        else: 
            NewString += char # 원래 문자로 처리
    #
    return NewString

def HGGetCompatibleJamo__HalfJamo(char):
    """반각 자모를 호환 자모로 변환"""
    #
    NewChar = ''
    char_inx = __halfwidth_jamo52_list__.find(char)
    if(char_inx >= 0):
        NewChar = __compatible_jamo52_list_for_halfwidth_jamo[char_inx]
    #
    return NewChar

def HGGetCompatibleJamoString__HalfJamoString(string):
    """반각 자모를 호환 자모로 변환"""
    #
    NewString = ''
    for char in string:
        half_char = HGGetCompatibleJamo__HalfJamo(char)
        if(half_char): 
            NewString += half_char # 호환 자모로 처리
        else: 
            NewString += char # 원래 문자로 처리
    #
    return NewString
    
#---------------------------------------------
#---------------------------------------------
#---------------------------------------------
def getSyllableSound(hgchar):
    # {닿, 홀, ㄹ} = 닿(소리), 홀(소리), ㄹ(소리)
    SylSound = ''
    ChoJungJongJamo = hgGetChoJungJongJamo_Char(hgchar)
    if(len(ChoJungJongJamo) <= 0):
        return SylSound
    if('jong' in ChoJungJongJamo):
        if(len(ChoJungJongJamo['jong']) > 0):
            if(ChoJungJongJamo['jong'] == 'ᆯ'): # 종성_ㄹ = 'ᆯ' # 4527 0x11af
                SylSound = 'ㄹ' # 키보드 입력을 고려해서 한글 호환 자모 'ㄹ' 이다.
            else:
                SylSound = '닿'
        else:
            SylSound = '닿'
    elif(len(ChoJungJongJamo['jung']) > 0):
        SylSound = '홀'
    elif(len(ChoJungJongJamo['cho']) > 0):
        SylSound = '닿'
    else:
        pass
    return SylSound

def getVoulHarmony(hgchar):
    # {양, 음} = 양(성), 음(성)
    VoulHarmony = ''
    ChoJungJongJamo = hgGetChoJungJongJamo_Char(hgchar)
    if(len(ChoJungJongJamo) <= 0):
        return VoulHarmony
    if('jung' in ChoJungJongJamo):
        if(len(ChoJungJongJamo['jung']) > 0):
            if(ChoJungJongJamo['jung'] == 'ᅡ'): # 중성_ㅏ = 'ᅡ' # 4449 0x1161'
                VoulHarmony = '양'
            elif(ChoJungJongJamo['jung'] == 'ᅩ'): # 중성_ㅗ = 'ᅩ' # 4457 0x1169'
                VoulHarmony = '양'
            elif(ChoJungJongJamo['jung'] == 'ᅪ'): # 중성_ㅘ = 'ᅪ' # 4458 0x116a'
                VoulHarmony = '양'
            else:
                VoulHarmony = '음'
    return VoulHarmony

def hgunicode_test11(string):
    # 한글 음절을 자모로 변환한 후에 다시 음절로 변환
    #=string = '나랏말씀이 중국과 달라' # 유니코드 음절 문자열
    print(f'입력 문자열 ({len(string)}):', string)

    # 음절 문자열을 자모 문자열로 변환
    string_jamo = hgGetChoJungJongString(string)
    print(f'자모 문자열 변환 ({len(string_jamo)}):', string_jamo)

    # 자모 문자열을 음절 문자열로 변환
    string_syllable = hgSyllableStr__Jamo3Str(string_jamo)
    print(f'음절 문자열 변환 ({len(string_syllable)}):', string_syllable)

    if(string != string_syllable):
        print('변환 결과가 다릅니다.')
    return string_syllable, string_jamo

#================================
#================================
#================================
from unittest import TestCase, main

class HGTest(TestCase):
    def _test_1(self):
        string = '동해물과 백두산이'
        lmt_str = hgGetChoJungJongString(string, jamo=True)
        print(lmt_str)

    def _test_2(self):
        string = '동해물과 백두산이'
        for c in string:
            PrintChoJungJongChar(c)

    def _test_3(self):
        string = '한ㄴ'
        lmt_str = hgGetChoJungJongString(string, jamo=True, CompatibleJamo2ChoJungJong=False)
        print(lmt_str)
        PrintCodeValue_String(lmt_str)
        print

        lmt_str = hgGetChoJungJongString(string, jamo=True, CompatibleJamo2ChoJungJong=True)
        print(lmt_str)
        PrintCodeValue_String(lmt_str)
        print

    def _test_4(self):
        string = '대한민국'
        lmt_str = hgGetChoJungJongString(string, jamo=True)
        print(lmt_str)
        PrintCodeValue_String(lmt_str)

    def _test_11(self):
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


if __name__ == '__main__':
    main()

