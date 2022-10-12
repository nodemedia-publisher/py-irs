#-----------------------------
# 20만 여 개의 파일명을 메모리로 읽은 후 탐색
#-----------------------------
import hgsysinc
from hgfind import FileScan
#
PrePath = ''
PrePath = './../../../../../hgproj80/textdata'
PathList = [ # 2001년 ~ 2016년
    PrePath + '/kbs9news/worker/-txt_each_all/2001/*.txt',
    PrePath + '/kbs9news/worker/-txt_each_all/2002/*.txt',
    PrePath + '/kbs9news/worker/-txt_each_all/2003/*.txt',
    PrePath + '/kbs9news/worker/-txt_each_all/2004/*.txt',
    PrePath + '/kbs9news/worker/-txt_each_all/2005/*.txt',
    PrePath + '/kbs9news/worker/-txt_each_all/2006/*.txt',
    PrePath + '/kbs9news/worker/-txt_each_all/2007/*.txt',
    PrePath + '/kbs9news/worker/-txt_each_all/2008/*.txt',
    PrePath + '/kbs9news/worker/-txt_each_all/2009/*.txt',
    PrePath + '/kbs9news/worker/-txt_each_all/2010/*.txt',
    PrePath + '/kbs9news/worker/-txt_each_all/2011/*.txt',
    PrePath + '/kbs9news/worker/-txt_each_all/2012/*.txt',
    PrePath + '/kbs9news/worker/-txt_each_all/2013/*.txt',
    PrePath + '/kbs9news/worker/-txt_each_all/2014/*.txt',
    PrePath + '/kbs9news/worker/-txt_each_all/2015/*.txt',
    PrePath + '/kbs9news/worker/-txt_each_all/2016_utf8_txt/201601/*.txt',
    PrePath + '/kbs9news/worker/-txt_each_all/2016_utf8_txt/201602/*.txt',
    PrePath + '/kbs9news/worker/-txt_each_all/2016_utf8_txt/201603/*.txt',
    PrePath + '/kbs9news/worker/-txt_each_all/2016_utf8_txt/201604/*.txt',
    PrePath + '/kbs9news/worker/-txt_each_all/2016_utf8_txt/201605/*.txt',
    PrePath + '/kbs9news/worker/-txt_each_all/2016_utf8_txt/201606/*.txt',
    PrePath + '/kbs9news/worker/-txt_each_all/2016_utf8_txt/201607/*.txt',
    PrePath + '/kbs9news/worker/-txt_each_all/2016_utf8_txt/201608/*.txt',
    PrePath + '/kbs9news/worker/-txt_each_all/2016_utf8_txt/201609/*.txt',
    PrePath + '/kbs9news/worker/-txt_each_all/2016_utf8_txt/201610/*.txt',
    PrePath + '/kbs9news/worker/-txt_each_all/2016_utf8_txt/201611/*.txt',
    PrePath + '/kbs9news/worker/-txt_each_all/2016_utf8_txt/201612/*.txt',
]
#=pathname = PrePath + '/kbs9news/worker/-txt_each_all/2009/*.txt' # 2009년 뉴스 텍스트

from unittest import TestCase, main
import glob
class HGTest(TestCase):
    def test_41(self): #=2015년 처음 출현한 단어 = {완벽주의자, 도어맨, 모노핀, 별풍선}
        #=FindWord = '완벽주의자'
        FindWord = 'KBS'
        FindWord = '별풍선'
        fileID = 1
        find_inx = (-1)
        for inx, pathname in enumerate(PathList):
            #=pathname = './../../../../../hgproj80/textdata/kbs9news/worker/-txt_each_all/2001/*.txt'
            for filename in glob.glob(pathname):
                #=print(f'{fileID}:', filename)
                find_inx = FileScan(FindWord, filename)
                if(find_inx >= 0): # 처음으로 발견, 위치를 출력하고 종료
                    print(f'{FindWord} [{fileID}]: ({find_inx})', filename)
                    break
                fileID += 1
            if(find_inx >= 0): # 발견했으면 종료
                break
# TestCase 호출
main()
#=if __name__ == '__main__':
#=    main()


'''
처리결과:
=====================================================
KBS [1]: (671) ./../../../../../hgproj80/textdata/kbs9news/worker/-txt_each_all/2001\20010101_001.txt
.
----------------------------------------------------------------------
Ran 1 test in 0.122s
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
별풍선 [177522]: (268) ./../../../../../hgproj80/textdata/kbs9news/worker/-txt_each_all/2015\20150105_2996378.txt
.
----------------------------------------------------------------------
Ran 1 test in 483.737s
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

'''
