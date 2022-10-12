import hgsysinc
from hgtest import load_dictfreq_kbs_2009
from hgtest import load_dictfreq_kbs_01_16
from datetime import datetime
#-----------------------------
print('주제어 파일을 읽고 검색어 사전으로 변환')
#=Vocabulary = load_dictfreq_kbs_2009() # [KBS 9시 뉴스: 2009년]
Vocabulary = load_dictfreq_kbs_01_16()  # [KBS 9시 뉴스: 16년치(2001~2016)]
print('Dict Num:', len(Vocabulary))
print('Word Num:', sum([Vocabulary[dic] for dic in Vocabulary]))
#-----------------------------
#=2015년 처음 출현한 단어 = {완벽주의자, 느릎나무, 도어맨, 모노핀, 별풍선
# 검색
time_beg = datetime.now() # 검색 시작 시각
#=FindWord = '완벽주의자' # 2015년 처음 출현한 단어
FindWord = '별풍선' # 2015년 처음 출현한 단어
WordFreq = Vocabulary.get(FindWord) # foramt: {'word': freq}
time_end = datetime.now() # 검색 종료 시각
if(WordFreq):
    print(f'{FindWord}:', WordFreq)
# 경과 시간 출력
elapsed = time_end - time_beg
print('Elapsed:', elapsed)



'''
출력 결과:
Dict Num: 413165
Word Num: 26707228
별풍선: 12
Elapsed: 0:00:00.009482

'''


