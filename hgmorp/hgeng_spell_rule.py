#------------------------
#------------------------
import hgsysinc
#===============================
#===============================
eng_clitics_suffix = [ # 영어 목록:접어
    "'m", "'d", "'ll", "'re", "'s", "'t", "'ve", # 작은따옴표로 된 것(apple's->apple, can't->can)을 바꾸려고
]

eng_clitics_tail = [ # 영어 목록:접어
    "ll", "re", "ve", # 작은따옴표를 제거한 것('ll -> ll, 're -> re, 've -> ve)
    # 작은따옴표 없이 2글자로 오는 경우(불용어 처리할 때 필요)
]

eng_clitics_head = [ # 영어 목록:접어를 분리할 때 앞 부분(단어 아님)
    "ain",
    #="aren't",    # 접어를 제외한 앞 부분이 단어
    #==="can't",   # 접어를 제외한 앞 부분이 단어
    'doesn', 'don', 
    #==="else's",    # 접어를 제외한 앞 부분이 단어
    #==="get's",     # 접어를 제외한 앞 부분이 단어
    'hasn', "haven", 
    #==="he'd", "he's", "her's",    # 접어를 제외한 앞 부분이 단어
    #==="i'm", "it's",     # 접어를 제외한 앞 부분이 단어
    "isn", 
    #==="no's",    # 접어를 제외한 앞 부분이 단어
    #==="she'd", "she's",    # 접어를 제외한 앞 부분이 단어
    "shouldn", 
    #==="that's", "there's", "they'd", "they're", "they've",    # 접어를 제외한 앞 부분이 단어
    "wasn", 
    #==="we'd", "we're",    # 접어를 제외한 앞 부분이 단어
    "weren", 
    #==="who'd", "who're", "who's", "whom's",    # 접어를 제외한 앞 부분이 단어
    "wouldn", 
    #==="you'd", "you're",    # 접어를 제외한 앞 부분이 단어
]

eng_clitics_merge = [ # 영어 목록:접어와 통합된 형태
    "ain't", # ain't : am not, are not, is not, has not, have not의 축약어
    "aren't",
    "can't", "couldn't", 
    "didn't", "doesn't", "don't",
    "hadn't",
    "hasn't", "haven't", "havn't", "he'd", "he'll", "how'd",
    "i'd", "i'll", "i'm", "i've", "isn't", "it'll", 
    "mayn't", "mightn't", "musn't", "mustn't", 
    "needn't", "nobody'll",
    "oughtn't",
    "she'd", "she'll", "shouldn't",
    "that'd", "that'll", "there'd", 
        "they'd", "they'll", "they're", "they've",
    "warn't", "wasn't", 
    "we'd", "we'll", "we're", "we've", "weren't", 
        "what'll", 
        "when'd", "where'd", "who'd", "who're", 
        "won't", "wouldn't",
    "you'd", "you'll", "you're", "you've",
]

eng_clitics_merge__s = [ # 영어 목록:접어와 통합된 형태(~'s)
    "else's", "get's", "he's", "her's", "no's", "she's", "that's", "there's", 
    "we's", "what's", "where's", "who's", "whom's", "you's",
]
 
#----------
# 기본 불용어에 포함하지 않은 것: 
#----------
# "did", "does", 'doing', 'done', 
# 'exactly', "everybody", "everyman", 
# 'far', 
# 'goes', 'going', 'gone', 'gets', 'got',
# 'had', 'has', 'have', 'hi', 
# 'is', 
# 'little', 
# 'just', 
# 'made', 'make', 'makes', 'mr', 
# 'new', "nobody", 
# 'old', 
# 'really', 
# 'thing', 'things', 
#----------

stoplist_eng_basic = [ # 영어 불용어 목록
    'a', 'about', 'above', 'across', 'after', 'again', 'against', 
        'all', 'almost', 'along', 'already', 'also', 'although', 'always', 
        'am', 'among', 
        'an', 'and', 'another', 'any', 'anyone', 'anything', 'anyway', 
        'are', 'around','as', 'at', 
    'b', 'back', 'be', 'became', 'because', 'become', 'becomes', 
        'been', 'being', 'before', 'below', 'between', 'both', 'but', 'by',
    'c', 'can', 'cannot', 'could', 
    'd', 'do', 'down', 'during',
    'e', 'each', 'eight', 'either', 'else', 'enough', 'etc', 
        'even', 'ever', 'every', 'everyone', 'everything', 
        'ex', 'except', 
    'f', 'few', 'five', 'for', 'four', 'from', 'full',
    'g', 'get', 'go', 
    'h', 
        'he', 'her', 'here', 'herself', 
        'him', 'himself', 'his', 'how',  'however',
    'i', 'if', 'in','inside', 'into', 'is', 'it', 'its', 
    'j', 
    'k', 'keep',
    'l', 'last', 'least', 'less', 
    'm', 'many', 'may', 'me', 'might', 'mine', 'more', 'most', 'much', 'must', 'my', 'myself',
    'n', 'none', 'near', 'never', 'next', 
        'nine', 'no', 'nor', 'not', 'nothing', 'now',
    'o', 'of', 'off', 'often', 'on', 'once', 'one', 'only', 'onto', 'or', 
        'other', 'others', 'otherwise', 'our', 'out', 'over', 'own',
    'p', 'part', 'perhaps', 'please', 'put',
    'q',
    'r', 'rather', 'rarely', 're', 
    's', 'seem', 'seems', 'self', 'seven', 'several', 'she', "should", 'show',
        'side', 'since', 'six', 'so', 'some', 'someone', 'something', 'soon', 'still', 'such',
    't', "'the", 'take', 'taken', 'takes', 'ten', 
        'than', 'that', 
        'the', 'their', 'them', 'themselves', 'then', 'there', 'these', 
        'they', 
        'this', 'those', 'though', 'three', 'through', 'thus', 
        'to', 'too', 'took', 'twelve', 'two', 
    'u', 'under', 'until', 'up', 'upon', 'us',
    'v', 'very', 'via', 
    'w', 'was', 'we', 'well', 'were', 
        'what', 'when', 'When', 'where', 'whether', 'which', 'while', 
        'who', 'whole', 'whose', 'whom', 'why',
        'will', 'with', 'within', 'without',  'would', 
    'x', 
    'y', 'yet', 'you', 'your', 'yourself',
    'z', 
]
#
stoplist_eng = []
stoplist_eng.extend(stoplist_eng_basic)
stoplist_eng.extend(eng_clitics_suffix)
stoplist_eng.extend(eng_clitics_tail)
stoplist_eng.extend(eng_clitics_head)
stoplist_eng.extend(eng_clitics_merge)
stoplist_eng.extend(eng_clitics_merge__s)

#
eng_clitics_head_dict = { # 접어를 분리할 때 앞 부분
    #="ain":'am', # ain't : am not, are not, is not, has not, have not의 축약어
    #="aren", ?("aren't",)
    'doesn':'does', 'don':'do', 'hasn':'has', "haven":'have', "isn":'is', 
    "shouldn":'should', "wasn":'was', "weren":'were', "wouldn":'would',
}

eng_clitics_merge_dict = { # 영어 불용어 목록:접어와 통합된 형태
    "ain't":'am', # ain't : am not, are not, is not, has not, have not의 축약어
    "aren't":'are',
    "can't":'can', "doesn't":'does', "don't":'do',
    #="else's":'else', "get's":'get', # <=== {~'s} 규칙으로 처리 가능
    "hasn't":'has', "haven't":'have', "havn't":'have', 
    #="he'd":'he', # <=== {~'d} 규칙으로 처리 가능
    #="he's":'he', "her's":'her', 
    #="i'm":'i', # <=== {~'s, ~'m} 규칙으로 처리 가능
    "isn't":'is', 
    #="it's":'it', "no's":'no', # <=== {~'s} 규칙으로 처리 가능
    #="she'd":'she', "she's":'she', # <=== {~'d, ~'s} 규칙으로 처리 가능
    "shouldn't":'should',
    #="that's":'that', "there's":'there', # <=== {~'s} 규칙으로 처리 가능
    #="they'd":'they', "they're", "they've", # <=== {~'d, ~'re, ~'ve} 규칙으로 처리 가능
    #="we'd":'we', "we're":'we', # <=== {~'d, ~'re} 규칙으로 처리 가능
    "wasn't":'was', "weren't":'were', 
    #="who'd":'who', "who're":'who', "who's":'who', "whom's":'whom', # <=== {~'d, ~'re, ~'ve} 규칙으로 처리 가능
    "wouldn't":'would',
    #="you'd":'you', "you're":'you', # <=== {~'d, ~'re} 규칙으로 처리 가능
}

eng_clitics_form_dict = dict()
eng_clitics_form_dict.update(eng_clitics_head_dict)
eng_clitics_form_dict.update(eng_clitics_merge_dict)

#
stoplist_eng_raw_min1 = [ # 영어 불용어 목록
    "'m", "'d", "'re", "'s", "'t", "'ll", "'ve", # 작은따옴표로 된 것(apple's->apple, can't->can)을 바꾸려고
    'a', 'about', 'above', 'across', 'after', 'again', 'against', 'ago', "ain't",
        'all', 'almost', 'along', 'already', 'also', 'although', 'always', 
        'am', 'among', 'an', 'and', 'another', 'any',
        'are', "aren't",'around','as', 'at', 'away',
    'b', 'back', 'be', 'became', 'become', 'becomes', 'been', 'being', 'before', 'between', 'both', 'but', 'by',
    'c', 'can', "can't", 'cannot', 'could', 
    'd', 'did', 'do', "does", 'doesn', "doesn't",'doing', 'done', 'don', "don't",'down', 'during',
    'e', 'each', 'eight', 'else', "else's", 'etc', 'even', 'ever', 'ex',
    'f', 'far', 'few', 'five', 'for', 'four', 'from',
    'g', 'get', 'go', 'goes', 'going', 'gone', "get's", 'gets', 'got',
    'h', 'had', 'has', 'hasn', "hasn't", 'have', "haven't", "havn't",
        'he', "he'd", "he's", 'her', "her's", 'here', 'herself', 
        'hi', 'him', 'himself', 'his', 'how',  'however',
    'i', "i'm", 'if', 'in','inside', 'into', 'is', "isn't", 'it', "it's", 'its', 
    'j', 'just', 
    'l', 'last', 'less', 'little', 
    'm', 'made', 'make', 'makes', 'many', 'may', 'more', 'mr', 'much', 'must', 'my', 'myself',
    'n', 'near', 'never', 'new', 'nine', 'no', "no's", 'not', 'now',
    'o', 'of', 'off', 'old', 'on', 'once', 'one', 'only', 'onto', 'or', 'other', 'otherwise', 'our', 'out', 'over',
    'p',
    'q',
    'r', 'rather', 'rarely', 'really', 
    's', 's', 'self', 'seven', 'she', "she'd", "she's", "should","shouldn", "shouldn't",
        'since', 'six', 'so', 'some', 'someone', 'soon', 'still',
    't', "'the", 'take', 'taken', 'takes', 'ten', 
        'than', 'that', "that's", 
        'the', 'their', 'them', 'themselves', 'then', 'there', "there's", 'these', 
        'they', "they'd", "they're", "they've", 
        'this', 'thing', 'three', 'through',
        'to', 'too', 'took', 'twelve', 'two', 
    'u', 'under', 'until', 'up', 'upon', 'us',
    'v', 'very',
    'w', 'was', "wasn", "wasn't", 'we', "we'd", "we're", 'were', "weren", "weren't",
        'what', 'when', 'When', 'where', 'which', 'while', 
        'who', "who'd", "who're", "who's", 'whose', 'whom', "whom's", 'why',
        'will', 'with', 'within', 'without',  'would', "wouldn", "wouldn't",
    'x', 
    'y', 'yet', 'you', "you'd", "you're",'your', 'yourself',
    'z',
    #----------
    # 포함하지 않은 것: everybody, everyman, everyone, everything, nobody, nothing, someone, something
]


#===============================
#===============================
# 철자만으로 원형으로 바꿀 수 있는 것
#===============================
#===============================
# {-(e)s}를 변경하면 원형이 되는 목록
replace_end__s_dict_4 = {
    'ches':'ch', 'shes':'sh', 'bies':'by', 'cies':'cy', 'dies':'dy',
    'fies':'fy', 'gies':'gy', 'hies':'hy', 'lies':'ly', 'mies':'my',
    'nies':'ny', 'pies':'py', 'ries':'ry', 'sies':'sy', 'ties':'ty',
}
replace_end__s_dict_5 = {
    'wives':'wife',
}

# {s}를 제거하면 원형이 되는 목록(3글자 짜리)
del_end__s_list_3 = [
    'ths', 'aws', 'ews', 'ows', 'oys',
]

# {s}를 제거하면 원형이 되는 목록(4글자 짜리)
del_end__s_list_4 = [ # 300 여개(10 x 30 여개)
    #='aves', 'ives', 'oves', 'lves', # 검토가 필요하다. (~f:~ves// ~ves: ~v, ~ve)
    'aces', 'acks', 'acts', 'ades', 'afts', 'ages', 'ails', 'aims', 'ains', 'airs', 
    'aits', 'akes', 'ales', 'alks', 'alls', 'alps', 'alts', 'ambs', 'ames', 'amps', 
    'ands', 'ands', 'anks', 'ants', 'aphs', 'ards', 'arks', 'arls', 'arms', 'arts',
    'ases', 'asks', 'asts', 'ates', 'auls', 'awls', 'azes', 'bags', 'bals', 'bees', 
    'bels', 'bers', 'bets', 'bins', 'bits', 'bles', 'bors', 'cals', 'cans', 'cars', 
    'cers', 'cles', 'cons', 'curs', 'cuts', 'days', 'dels', 'dens', 'ders', 'dges', 
    'dors', 'eads', 'eaks', 'eals', 'eams', 'eans', 'ears', 'eats', 'eces', 'ecks', 
    'ects', 'edes', 'eeds', 'eeks', 'eels', 'eems', 'eens', 'eeps', 'eers', 'eets', 
    'eges', 'eins', 'ells', 'elps', 'elts', 'ends', 'ends', 'ents', 'eons', 'epts', 
    'erds', 'erns', 'erts', 'ests', 'eurs', 'exts', 'fers', 'fits', 'fles', 'fuls', 
    'gees', 'gels', 'gers', 'gets', 'gins', 'gles', 'gons', 'gots', 'gues', 'hens', 
    'hers', 'hops', 'hors', 'hots', 'ials', 'ians', 'ians', 'ibes', 'ices', 'icks', 
    'icts', 'ides', 'iefs', 'iens', 'iers', 'iffs', 'ifts', 'iges', 'ighs', 'igns', 
    'ikes', 'ilds', 'iles', 'ills', 'imes', 'inds', 'ines', 'ings', 'inks', 'ints', 
    'ions', 'ions', 'iors', 'iots', 'ipts', 'irls', 'irts', 'isms', 'ists', 'ists', 
    'izes', 'kees', 'kens', 'kers', 'kets', 'keys', 'kins', 'kles', 'lars', 'lars', 
    'lays', 'leas', 'lers', 'lets', 'leys', 'lins', 'lips', 'lops', 'lors', 'lots', 
    'mals', 'mans', 'mens', 'mers', 'mets', 'mits', 'mons', 'mpts', 'nals', 'nces', 
    'nels', 'ners', 'nets', 'neys', 'nges', 'nors', 'nuts', 'oads', 'oals', 'oars', 
    'oats', 'obes', 'ocks', 'odes', 'offs', 'oils', 'oins', 'oirs', 'olds', 'oles', 
    'olks', 'olls', 'olts', 'ombs', 'omps', 'onds', 'ones', 'ongs', 'onts', 'oods', 
    'oofs', 'ooks', 'ools', 'ooms', 'oons', 'oops', 'oots', 'ords', 'ords', 'ores', 
    'orks', 'orms', 'orns', 'orts', 'oses', 'osts', 'ouls', 'oups', 'ours', 'outs', 
    'owls', 'pays', 'pels', 'pens', 'pers', 'pets', 'pics', 'ples', 'ques', 'rals', 
    'rams', 'rays', 'rces', 'rees', 'rels', 'rers', 'rets', 'reys', 'rges', 'rics', 
    'rits', 'rols', 'rons', 'rops', 'rors', 'rots', 'rsts', 'rums', 'sals', 'says', 
    'sees', 'sels', 'sers', 'sets', 'sits', 'sons', 'sors', 'sses', 'tals', 'tans', 
    'tars', 'tays', 'tees', 'tels', 'tens', 'ters', 'tles', 'toms', 'tons', 'tors', 
    'uals', 'uces', 'udes', 'uers', 'uffs', 'ughs', 'uits', 'ulls', 'ults', 'umes', 
    'umps', 'unds', 'unks', 'unts', 'upts', 'urls', 'urts', 'usts', 'vels', 'vers', 
    'vets', 'vils', 'vors', 'ways', 'wels', 'wers', 'yers', 'zers', 'zles',
]
   
# {s}를 제거하면 원형이 되는 목록(5글자 짜리)
del_end__s_list_5 = [
    'turns', 'ships', 'umors', 'fects', 'jects', 'lects', 'pects', 
    'rects', 'sects', 'tects', 'dicts', 'licts', 'ducts', 'duets', 
    'ights', 'ughts', 'tives', 'roves', 'sives', 'vives',
]
