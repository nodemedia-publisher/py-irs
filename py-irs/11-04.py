# 파일에서 키워드가 포함된 문장 색인
import hgsysinc
from hgfind import CatchCenterText__File
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

#===================
#===================
#=Find = 'nation'
#=Find = 'goodness'
Find = 'wonderful'
#=Find = 'loveliest'
#=Find = 'happy'
#=Find = 'lovely'

PreTextLen = 35 # 앞쪽 여백
PostTextLen = 35 # 뒤쪽 여백

#
#------------------------------------------------------
#------------------------------------------------------
#= {PrintMode = True} 방식은 함수 내부에서 print() 명령으로 직접 출력한다.
#= 이 방법은 메모리에 결과를 모으지 않지만 
#= 텍스트가 길 때는 화면 출력이 오래 걸린다.
#------------------------------------------------------
#= {PrintMode = False} 방식은 함수에서 print() 명령으로 직접 출력하지 않고 
#= 문자열로 모아서 반환한다. 이 방법은 텍스트가 길 때는 메모리를 많이 
#= 사용한다.
#------------------------------------------------------
#=PrintMode = True # print() 명령으로 직접 출력
PrintMode = False # 결과를 모아서 반환
CenterTexts, FindNum = CatchCenterText__File(Find, filename1, encoding=encoding, 
    LowerCasifyFlag=True, # 대문자를 소문자로 통합할 것인가
    PreTextLen=PreTextLen, PostTextLen=PostTextLen, 
    SepChar='', 
    WordBreak=True,
    CaptionAdd=True, # 헤더 추가 <=====
    IndexAdd=True, # 인덱스 추가 <=====
    PrintMode=PrintMode, # 직접 출력(하면 반환값 없음)
    HtmlMode=False, # 결과를 웹페이지(html) 방식으로 처리
)
print('Find Num:', FindNum)
print(CenterTexts) # PrintMode=True, # 직접 출력일 때는 반환값이 없어서 내용 없다.


'''
출력 결과:
==================================
Find Num: 26
***********************************wonderful***********************************
1            love driving. oh, it seems so wonderful that i’m going to live with you
2          don’t go far enough. oh, it was wonderful--wonderful.
3        far enough. oh, it was wonderful--wonderful.
4                            “oh, isn’t it wonderful?” she said, waving her hand
5                           “isn’t the sea wonderful?” said anne, rousing from a long,
6                                          wonderful place, all flowers and sunshine and
7          spring down in the hollow--that wonderful
8              seeing nothing save her own wonderful visions.
9                                        a wonderful sensation just to think of it. can
10                                         wonderful! it’s a ray of light which will
11                                         wonderfully twisted and folded, and a small
12              presence of mind perfectly wonderful in a child of her age. i never saw
13               anne had gone home in the wonderful, white-frosted winter morning,
14                “oh, matthew, isn’t it a wonderful morning? the world looks like
15                                         wonderful event very coolly. “you needn’t get
16         “i don’t think it’s such a very wonderful thing to walk a little, low,
17              wood were all feathery and wonderful; the birches
18        christmas, diana! and oh, it’s a wonderful christmas. i’ve
19                child don’t seem half so wonderful to you when you get them.”
20         of her lively fancy; adventures wonderful and enthralling
21         the test and i did. it’s really wonderful, marilla,
22         children. it’s nothing short of wonderful how
23                                         wonderful gown of shimmering gray stuff like
24                                     and wonderful power of expression; the audience
25                 how great and still and wonderful everything was, with the murmur of
26           in september. doesn’t it seem wonderful? i’ll





'''
