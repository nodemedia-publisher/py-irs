# 외부 라이브러리와 함수 호출 예:
import glob
pre_pathname = './../../../../../../hgproj80/textdata'
pathname = '/kbs9news/worker/-txt_mon_all/*.txt'
pathname = pre_pathname + pathname #####
filelist = glob.glob(pathname)
print(f'filelist ({len(filelist)}):')
for fid, filename in enumerate(filelist):
    filename = filename[len(pre_pathname):] ##### 출력을 위해서 앞에 경로 일부 삭제
    print(f'{fid}:', filename)


'''
=========================
filelist (196):
0: /kbs9news/worker/-txt_mon_all\200101.txt
1: /kbs9news/worker/-txt_mon_all\200102.txt
2: /kbs9news/worker/-txt_mon_all\200103.txt
...
...
194: /kbs9news/worker/-txt_mon_all\201703.txt
195: /kbs9news/worker/-txt_mon_all\201704.txt
>>> 
'''
