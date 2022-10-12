# 문자열에서 키워드가 포함된 문장 색인
"""
사용 함수: HGTextScanPos(), CatchCenterText__Pos()
"""
import hgsysinc
from hgfind import HGTextScanPos, CatchCenterText__Pos
from hgwordfile import ReadTxtFile
from hgcrawl import get_filename__Anne_of_Green_Gables
#-----------------------------
#-----------------------------
# 빨강 머리 앤
filename1 = get_filename__Anne_of_Green_Gables() # {빨강 머리 앤}의 파일 경로
# 해당 파일이 있는지 검사하여 없으면 다운로드한다.
from pathlib import Path
file_check = Path(filename1)
if ((file_check.is_file() == True) and (file_check.exists() == True)):
        pass
else:
    from hgcrawl import download_gutenberg_Anne_of_Green_Gables
    download_gutenberg_Anne_of_Green_Gables()
#-----
encoding='utf-8' 
booktext = ReadTxtFile(filename1, encoding=encoding)
booktext = booktext.lower() # 대문자롤 소문자로 통합하기 위해서 소문자 변환

#===================
#===================
#=Find = 'nation'
#=Find = 'romantic'
#=Find = 'sensible'
#=Find = 'ridiculous'
#=Find = 'best'
#=Find = 'loveliest'
Find = 'goodness'
print('@@@ --- HGScan Pos ---')
FindPosList = HGTextScanPos(Find, booktext) # 단어 위치 탐색
# FindPosList format: [658, 1671, 2181, 2972, 4866, 5624]
print('Find Num:', len(FindPosList))
#=print(*FindPosList, sep = '\n')

#----------
# 용례 출력
#----------
FindLen = len(Find)
PreTextLen = 35 # 앞쪽 여백
PostTextLen = (35 + FindLen) # 뒤쪽 여백

print(Find.center((PreTextLen + PostTextLen) + len(Find), '*') ) # 헤더 출력
for i, KwdPos in enumerate(FindPosList):
    #---------
    # {WordBreak=False} # 글자 단위로 처리
    #---------
    #=CenterText = CatchCenterText__Pos(booktext, KwdPos=KwdPos, KeyLen=FindLen, 
    #=    PreTextLen=PreTextLen, PostTextLen=PostTextLen) # 글자 단위로 문장 경계 처리
    #---------
    #---------
    # {WordBreak=True} # 공백문자 단위로 처리
    #---------
    CenterText = CatchCenterText__Pos(booktext, KwdPos=KwdPos, KeyLen=FindLen,
        PreTextLen=PreTextLen, PostTextLen=PostTextLen, WordBreak=True,
        HtmlMode=False, # 결과를 웹페이지(html) 방식으로 처리
        )
    #---------
    print(f'{i+1}\t{CenterText}')
print(),print(),print(),



'''
출력 결과:
==================================
@@@ --- HGScan Pos ---
Find Num: 14
***************************************goodness***************************************
1                                         “goodness, i don’t care. but where on earth
2                                      and goodness only knows what will come of it.”
3        wisdom, power, holiness, justice, goodness, and truth,’” responded anne
4        you do know something then, thank goodness! you’re not quite a
5        feelings of orphans, brought from goodness
6                            “thanks be to goodness for that,” breathed marilla in
7                                “merciful goodness!”
8             why, it’s only twilight. and goodness knows you’ve gone over
9            inveigled into the party only goodness
10            anne’s got plenty of faults, goodness knows, and far be it
11                                   anne. goodness knows what’s to be done. i suppose
12                          can. anne, for goodness sake smile a little. you know
13                                         goodness. i did make a mistake in judging
14                                         goodness we hadn’t got to that stage in




>>> 

'''
