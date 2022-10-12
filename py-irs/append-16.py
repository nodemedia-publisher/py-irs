import hgsysinc
from hgwordfile import GetDictFreq_WordFreqFile2, ReadTxtFile
from hgdict_low import TransDictfreq__Stoplist
#-----------
#-----
# 어휘 빈도 사전 읽기 
#-----
#
encoding='utf-8' 
# gutenberg porject: https://www.gutenberg.org/
guten_pathname = './../ext-src/data/gutenberg/'
fileame = 'gutenberg' + '_wordfreq' + '.tpx'
read_file = guten_pathname + fileame

print('dictionary reading:', read_file)
DictFreq = GetDictFreq_WordFreqFile2(read_file, encoding)
print(f'DictFreq [{len(DictFreq)}]:')

#-----------
# 불용어 처리
#-----------
# 불용어 파일 읽기
fileame = 'gutenberg_wordfreq_quatation' + '.txt'
stop_file = guten_pathname + fileame
stopword_txt = ReadTxtFile(stop_file)
stoplist_gutenberg = stopword_txt.split()

# 불용어 제거
print('DictFreq:', len(DictFreq))
DelNum = TransDictfreq__Stoplist(DictFreq, stoplist_gutenberg)
print('DictFreq_New:', len(DictFreq))
print('stop num:', DelNum)
    
   
'''
처리 결과:
==================
dictionary reading: ./../ext-src/data/gutenberg/gutenberg_wordfreq.tpx
DictFreq [53847]:
DictFreq: 53847
DictFreq_New: 53704
stop num: 143

'''

