import hgsysinc
from hgstat_test_kagmov import (
    hgstat_metadata_kaggle, 
    hgstat_links_kaggle,
    hgstat_overview_dict__kagmov,
)
from hgeng_spell_rule import stoplist_eng_raw_min1
from hgwordlist import GetWordList__Text6
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
print('# 영화ID로 영화 줄거리와 단어 목록 출력')
movieId = 1 # 'Toy Story'(영화ID:1)
#=movieId = 648 # 'Mission: Impossible'(영화ID:648)
#=movieId = 3114 # 'Toy Story 2'
#=movieId = 2355 # Bug's Life, A (1998)
#=movieId = 4886 # Monsters, Inc. (2001)
#=movieId = 6377 # Finding Nemo (2003)
#=movieId = 8961 # Incredibles, The (2004)
#=movieId = 4306 # Shrek (2001)
#=movieId = 260 # Star Wars: Episode IV - A New Hope (1977)

overview = overview_dict[movieId]
print(f'overview [{len(overview)}]:')
print(overview)
print()
#-----------
#-----------
stoplist = stoplist_eng_raw_min1 # 불용어 목록 지정
wordlist = GetWordList__Text6(overview, 
    ExcFilter=stoplist, # 불용어 처리
    LowerCase=True, # 대문자는 소문자로 변환
    CliticsModify=True, # {~'s}, {~'t}, {~'d}는 {~}로 바꾼다.
    ExcChar1=True,  # 1글자보다 작은 것은 지운다.
    ExcNumber=True, # 숫자만 있는 것은 지운다.
    UnifySpellRule=True, # 철자 규칙으로 단일화(s 제거, es 변형)
)
print(f'wordlist [{len(wordlist)}]:')
print(wordlist)
print()

#-----------
# 단어 목록을 빈도 사전으로 변환
DictFreq = GetDictFreq__WordList(wordlist, SortFlag=True, FreqOrderFlag=True) # by high freq
print(f'DictFreq [{len(DictFreq)}]:')
print(DictFreq)



'''
처리 결과:
==================
overview_dict: 44450
# 영화ID로 영화 줄거리와 단어 목록 출력
overview [303]:
Led by Woody, Andy's toys live happily ...

wordlist [32]:
['led', 'woody', 'andy', 'toy', 'live', 'happily', 'room', 'andy', 'birthday', 'bring', 'buzz', 'lightyear', 'scene', 'afraid', 'losing', 'place', 'andy', 'heart', 'woody', 'plot', 'buzz', 'circumstance', 'separate', 'buzz', 'woody', 'owner', 'duo', 'eventually', 'learns', 'put', 'aside', 'difference']

DictFreq [26]:
{'woody': 3, 'andy': 3, 'buzz': 3, 'led': 1, 'toy': 1, 'live': 1, 'happily': 1, 'room': 1, 'birthday': 1, 'bring': 1, 'lightyear': 1, 'scene': 1, 'afraid': 1, 'losing': 1, 'place': 1, 'heart': 1, 'plot': 1, 'circumstance': 1, 'separate': 1, 'owner': 1, 'duo': 1, 'eventually': 1, 'learns': 1, 'put': 1, 'aside': 1, 'difference': 1}

'''

