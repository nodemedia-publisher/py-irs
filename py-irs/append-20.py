import hgsysinc
#-----------------------------
#-----------------------------
from pathlib import Path
from hgwordfile import GetHGTpxText_TpxFile

filepath = 'C:/Users/ia/Desktop/send/'
filename = Path(filepath + 'test12.tpx-wordlist.txt')
encoding='euckr'
HGTpxText = GetHGTpxText_TpxFile(filename, encoding=encoding)
print('HGTpxText:', HGTpxText)
    
#-----
HGTpxText.rstrip() # 문서 끝쪽에 있는 공백문자 지운다.
#print(HGTopicText)
HGTpxList = HGTpxText.split()
print('HGTpxList', HGTpxList)

#-----
WordFreq = {}
for word in HGTpxList:
    if(word in WordFreq):
        WordFreq[word] += 1
    else:
        WordFreq[word] = 1
print('WordFreq:', WordFreq)

'''
처리결과:
========================================
HGTpxText: 학교 컴퓨터  학교    언어    학교    언어    인공지능        인공지능        학교    언어
HGTpxList ['학교', '컴퓨터', '학교', '언어', '학교', '언어', '인공지능', '인공지능', '학교', '언어']
WordFreq: {'학교': 4, '컴퓨터': 1, '언어': 3, '인공지능': 2}
'''


