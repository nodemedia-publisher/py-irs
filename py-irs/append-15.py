import hgsysinc
from hgwordfile import GetDictFreq_WordFreqFile2
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
    
   
'''
처리 결과:
==================
dictionary reading: ./../ext-src/data/gutenberg/gutenberg_wordfreq.tpx
DictFreq [53847]:


'''

