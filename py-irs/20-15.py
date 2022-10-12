import hgsysinc
from hgstat_test_kagmov import (
    hgstat_metadata_kaggle,
    hgstat_links_kaggle,
    hgstat_overview_dict__kagmov,
)
from hgeng_spell_rule import stoplist_eng_raw_min1
from hgwordlist import GetWordList__Text6
from hgdistance import GetDictFreq_CosDistance
from hgdict import GetDictFreq__WordList
#---------------
# format: movies_metadata
#---------------
# adult,belongs_to_collection,budget,genres,homepage,id,imdb_id,original_language,original_title,overview,popularity,poster_path,production_companies,production_countries,release_date,revenue,runtime,spoken_languages,status,tagline,title,video,vote_average,vote_count
# False,"{'id': 10194, 'name': 'Toy Story Collection', 'poster_path': '/7G9915LfUQ2lVfwMEEhDsn3kT4B.jpg', 'backdrop_path': '/9FBwqcd9IRruEDUrTdcaafOMKUq.jpg'}",30000000,"[{'id': 16, 'name': 'Animation'}, {'id': 35, 'name': 'Comedy'}, {'id': 10751, 'name': 'Family'}]",http://toystory.disney.com/toy-story,862,tt0114709,en,Toy Story,"Led by Woody, Andy's toys live happily in his room until Andy's birthday brings Buzz Lightyear onto the scene. Afraid of losing his place in Andy's heart, Woody plots against Buzz. But when circumstances separate Buzz and Woody from their owner, the duo eventually learns to put aside their differences.",21.946943,/rhIRbceoE9lR4veEXuwCC2wARtG.jpg,"[{'name': 'Pixar Animation Studios', 'id': 3}]","[{'iso_3166_1': 'US', 'name': 'United States of America'}]",1995-10-30,373554033,81.0,"[{'iso_639_1': 'en', 'name': 'English'}]",Released,,Toy Story,False,7.7,5415
# False,,65000000,"[{'id': 12, 'name': 'Adventure'}, {'id': 14, 'name': 'Fantasy'}, {'id': 10751, 'name': 'Family'}]",,8844,tt0113497,en,Jumanji,"When siblings Judy and Peter discover an enchanted board game that opens the door to a magical world, they unwittingly invite Alan -- an adult who's been trapped inside the game for 26 years -- into their living room. Alan's only hope for freedom is to finish the game, which proves risky as all three find themselves running from giant rhinoceroses, evil monkeys and other terrifying creatures.",17.015539,/vzmL6fP7aPKNKPRTFnZmiUfciyV.jpg,"[{'name': 'TriStar Pictures', 'id': 559}, {'name': 'Teitler Film', 'id': 2550}, {'name': 'Interscope Communications', 'id': 10201}]","[{'iso_3166_1': 'US', 'name': 'United States of America'}]",1995-12-15,262797249,104.0,"[{'iso_639_1': 'en', 'name': 'English'}, {'iso_639_1': 'fr', 'name': 'Français'}]",Released,Roll the dice and unleash the excitement!,Jumanji,False,6.9,2413
#---------------
movies_metadata = hgstat_metadata_kaggle(AllFlag=False)
links = hgstat_links_kaggle()
overview_dict, movies_metadata_ = hgstat_overview_dict__kagmov(movies_metadata, links)
print(f'overview_dict: {len(overview_dict)}')
#-----------
#-----------
print('# 영화ID로 영화 줄거리(텍스트) 유사도 측정')
movieId_base = 1 # 'Toy Story'
movieId_comp = 3114 # 'Toy Story 2'
#=movieId_comp = 78499 # 'Toy Story 3'
#=movieId = 2355 # Bug's Life, A (1998)
#=movieId = 4886 # Monsters, Inc. (2001)
#=movieId = 6377 # Finding Nemo (2003)
#=movieId = 8961 # Incredibles, The (2004)
#=movieId = 4306 # Shrek (2001)
#=movieId = 260 # Star Wars: Episode IV - A New Hope (1977)
#-----------
#-----------
overview_base = overview_dict[movieId_base]
overview_comp = overview_dict[movieId_comp]
#-----------
#-----------
stoplist = stoplist_eng_raw_min1 # 불용어 목록 지정
wordlist_base = GetWordList__Text6(overview_base, ExcFilter=stoplist, LowerCase=True, 
    CliticsModify=True, ExcChar1=True, ExcNumber=True, UnifySpellRule=True)
wordlist_comp =GetWordList__Text6(overview_comp, ExcFilter=stoplist, LowerCase=True, 
    CliticsModify=True, ExcChar1=True, ExcNumber=True, UnifySpellRule=True)

# 단어 목록을 빈도 사전으로 변환
DictFreq_base = GetDictFreq__WordList(wordlist_base)
DictFreq_comp = GetDictFreq__WordList(wordlist_comp)

# 코사인 거리(Text Distance) 측정(= 1 - 텍스트 유사도)
CosDistance = GetDictFreq_CosDistance(DictFreq_base, DictFreq_comp)

#
print(f'{movieId_base}   <=== >   {movieId_comp}')
print(f'[{movieId_base}] DictFreq_base [{len(DictFreq_base)}]:',
    f' <=== wordlist_base [{len(wordlist_base)}]')
print(f'[{movieId_comp}] DictFreq_comp [{len(DictFreq_comp)}]:',
    f' <=== wordlist_comp [{len(wordlist_comp)}]')
print(f'CosDistance: %.3f' %CosDistance)

#-----------
#-----------
# 두 영화에 공통으로 일치하는 단어 목록 출력
wordset_base = set(wordlist_base)
wordset_comp = set(wordlist_comp)
wordset_common = wordset_base.intersection(wordset_comp)
print(f'wordset_common ({len(wordset_common)}) :', wordset_common)

'''
처리 결과:
==================
overview_dict: 44450
# 영화ID로 영화 줄거리(텍스트) 유사도 측정
1   <=== >   3114
[1] DictFreq_base [26]:  <=== wordlist_base [32]
[3114] DictFreq_comp [32]:  <=== wordlist_comp [38]
CosDistance: 0.584
wordset_common (7) : {'buzz', 'toy', 'lightyear', 'heart', 'owner', 'andy', 'woody'}

'''

