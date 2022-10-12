#-----------------------------
# 파일 192개로 탐색(# 2001년 ~ 2016년 월 단위 텍스트 파일)
#-----------------------------
# 파일 목록 구하기
import glob
PrePath = ''
PrePath = './../../../../../hgproj80/textdata'
pathname = PrePath + '/kbs9news/worker/-txt_mon_all/*.txt'
filelist = glob.glob(pathname)
#=print(f'@@@ filelist ({len(filelist)}):', filelist)
#---------------------------
# 파일 열어두기(DB open 효과)
#---------------------------
from pathlib import Path
filehandles = []
for filename in filelist:
    real_filename = Path(filename)
    file = open(real_filename, 'r', encoding='cp949')
    filehandles.append(file)
#---------------------------
# 검색
#---------------------------
import hgsysinc
from hgfind import FileScan
from unittest import TestCase, main
class HGTest(TestCase):
    def test_41(self): #=2015년 처음 출현한 단어 = {완벽주의자, 도어맨, 모노핀, 별풍선}
        #=FindWord = '완벽주의자'
        #=FindWord = 'KBS'
        FindWord = '별풍선'
        find_inx = (-1)
        for fileID, file in enumerate(filehandles):
            texts = file.read()
            find_inx = texts.find(FindWord) 
            #=print(f'{fileID}:', filelist[fileID])
            if(find_inx >= 0): # 처음으로 발견, 위치를 출력하고 종료
                print(f'{FindWord} [{fileID+1}]: ({find_inx})', filelist[fileID])
                break
#---------------------------
# TestCase 호출
#---------------------------
main()
#=if __name__ == '__main__':
#=    main()
#---------------------------
# 파일 닫기(DB close 효과)
#---------------------------
for file in filehandles:
    file.close()


'''
처리결과:
=====================================================
KBS [1]: (671) ./../../../../../hgproj80/textdata/kbs9news/worker/-txt_mon_all\200101.txt
.
----------------------------------------------------------------------
Ran 1 test in 0.023s
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
별풍선 [169]: (104153) ./../../../../../hgproj80/textdata/kbs9news/worker/-txt_mon_all\201501.txt
.
----------------------------------------------------------------------
Ran 1 test in 2.053s
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

'''