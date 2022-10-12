#------------------------
#------------------------
from unittest import TestCase, main

#------------------------
#------------------------
import hgsysinc
from hgtest import load_dictfreq_kbs_2009
from hgtest import load_dictfreq_kbs_01_16

from hgkbd import HGTransString2KBDJamo

from hgworddistance import AddNGramVocabulary__WordWeight

#------------------------
#------------------------
def load_kbs_16_and_trans_ngram(NGram=None):
    #-----------------------
    # [KBS 9시 뉴스]
    #-----------------------
    #=print('reading texts')
    #=Vocabulary = load_dictfreq_kbs_2009() # [KBS 9시 뉴스: 2009년]
    Vocabulary = load_dictfreq_kbs_01_16()  # [KBS 9시 뉴스: 16년치(2001~2016)]
    print('Dict Num:', len(Vocabulary))
    #=print('Word Num:', sum([Vocabulary[dic] for dic in Vocabulary]))
    #=print(Vocabulary)

    #=print_vocaburary = True
    print_vocaburary = False
    if print_vocaburary == True:
        from hgdict import PrintDictFreq
        PrintDictFreq(Vocabulary, PrintNum=20, PrintGuide=True)

    #-----------------------------
    # make n-gram
    #-----------------------------
    ngram_k = 5
    if(NGram != None): # 외부에서 값을 주면 그것을 사용한다.
        ngram_k = NGram
    #=NGramVocabulary = MakeNGramVocabulary__DictFreq(Vocabulary, NGram=ngram_k)
    NGramVocabulary = {}
    for CurWord in Vocabulary:
        CurWord_Low = CurWord.lower() # 소문자 변환
        WordFreq = Vocabulary[CurWord]
        KBDCharString = HGTransString2KBDJamo(CurWord_Low) # 한글->두벌식 자모
        AddNGramVocabulary__WordWeight(NGramVocabulary, KBDCharString, 
            RealWord=CurWord, Weight=WordFreq, NGram=ngram_k)
    print('NGram Dict Num:', len(NGramVocabulary))
    #=PrintNGramVocabulary(NGramVocabulary, PrintNum=0, PrintVocabularyList=False)
    #=WeightNGramVocabulary(NGramVocabulary) # 가중치(빈도) 순으로 정렬(탐색시간 단축 위해)

    # 
    return Vocabulary, NGramVocabulary

class HGTest(TestCase):
    
    def setUp(self):
        self.a = 'test setup'

    def _test_run(self):
        print('test: ok')
    def test_run_1(self):
        load_kbs_16_and_trans_ngram()

if __name__ == '__main__':
    main()

