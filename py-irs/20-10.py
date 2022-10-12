import hgsysinc
from hgstat_test_kagmov import (
    hgstat_metadata_kaggle,
    hgstat_links_kaggle,
    hgstat_collection_dict__kagmov,
    hgstat_title_dict__kagmov,
    hgstat_genres_dict__kagmov,
)
#---------------
# format: movies_metadata
#---------------
# adult,belongs_to_collection,budget,genres,homepage,id,imdb_id,original_language,original_title,overview,popularity,poster_path,production_companies,production_countries,release_date,revenue,runtime,spoken_languages,status,tagline,title,video,vote_average,vote_count
# False,"{'id': 10194, 'name': 'Toy Story Collection', 'poster_path': '/7G9915LfUQ2lVfwMEEhDsn3kT4B.jpg', 'backdrop_path': '/9FBwqcd9IRruEDUrTdcaafOMKUq.jpg'}",30000000,"[{'id': 16, 'name': 'Animation'}, {'id': 35, 'name': 'Comedy'}, {'id': 10751, 'name': 'Family'}]",http://toystory.disney.com/toy-story,862,tt0114709,en,Toy Story,"Led by Woody, Andy's toys live happily in his room until Andy's birthday brings Buzz Lightyear onto the scene. Afraid of losing his place in Andy's heart, Woody plots against Buzz. But when circumstances separate Buzz and Woody from their owner, the duo eventually learns to put aside their differences.",21.946943,/rhIRbceoE9lR4veEXuwCC2wARtG.jpg,"[{'name': 'Pixar Animation Studios', 'id': 3}]","[{'iso_3166_1': 'US', 'name': 'United States of America'}]",1995-10-30,373554033,81.0,"[{'iso_639_1': 'en', 'name': 'English'}]",Released,,Toy Story,False,7.7,5415
# False,,65000000,"[{'id': 12, 'name': 'Adventure'}, {'id': 14, 'name': 'Fantasy'}, {'id': 10751, 'name': 'Family'}]",,8844,tt0113497,en,Jumanji,"When siblings Judy and Peter discover an enchanted board game that opens the door to a magical world, they unwittingly invite Alan -- an adult who's been trapped inside the game for 26 years -- into their living room. Alan's only hope for freedom is to finish the game, which proves risky as all three find themselves running from giant rhinoceroses, evil monkeys and other terrifying creatures.",17.015539,/vzmL6fP7aPKNKPRTFnZmiUfciyV.jpg,"[{'name': 'TriStar Pictures', 'id': 559}, {'name': 'Teitler Film', 'id': 2550}, {'name': 'Interscope Communications', 'id': 10201}]","[{'iso_3166_1': 'US', 'name': 'United States of America'}]",1995-12-15,262797249,104.0,"[{'iso_639_1': 'en', 'name': 'English'}, {'iso_639_1': 'fr', 'name': 'Français'}]",Released,Roll the dice and unleash the excitement!,Jumanji,False,6.9,2413
#---------------
movies_metadata = hgstat_metadata_kaggle(AllFlag=False)
links = hgstat_links_kaggle()

#---------------------
#---------------------
belong_to_collection_dict, collection_dict = \
    hgstat_collection_dict__kagmov(movies_metadata, links)
print('belong_to_collection_dict:', len(belong_to_collection_dict))
print('collection_dict:', len(collection_dict))

print('순서\t영화ID\t시리즈')
for ti, movieId_cur in enumerate(belong_to_collection_dict):
    print(f'{ti+1}\t{movieId_cur}\t{belong_to_collection_dict[movieId_cur]}')
    if((ti + 1)>= 3):
        break
print()
print('순서\t시리즈ID\t시리즈')
for li, collectId in enumerate(collection_dict):
    print(f'{li+1}\t{collectId}\t{collection_dict[collectId]}')
    if((li + 1) >= 3):
        break
print(), print(), 

title_dict, movies_metadata_ = hgstat_title_dict__kagmov(movies_metadata, links)
genres_dict, movies_metadata_ = hgstat_genres_dict__kagmov(movies_metadata, links)


#---------------------
#---------------------
print('# 영화ID로 영화 제목, 시리즈, 장르 출력')
movieId_list = [
    1, # 'Toy Story'
    3114, # 'Toy Story 2'
    2355, # Bug's Life, A (1998)
    4886, # Monsters, Inc. (2001)
    6377, # Finding Nemo (2003)
    #=8961, # Incredibles, The (2004)
    #=4306, # Shrek (2001)
    #=260, # Star Wars: Episode IV - A New Hope (1977)
]
for li, movieId in enumerate(movieId_list):
    CollectionName = ""
    if(movieId in belong_to_collection_dict): # 시리즈 사전 탐색
        CollectionName = belong_to_collection_dict[movieId]
    #    
    movie_title = title_dict[movieId]
    genres_list = genres_dict[movieId]

    if(len(movie_title) <= 0): # 제목이 없는 경우
        movie_title = '<<<영화 제목 없음>>>'
    if(len(genres_list) <= 0): # 장르 없는 경우
        genres_list = '<<<장르 없음>>>'
    #
    print(f'{li+1}\t{movieId}\t{movie_title}\t{CollectionName}\t{genres_list}')


'''
처리 결과: 
================================
belong_to_collection_dict: 4485
collection_dict: 1695
순서	영화ID	시리즈
1	1	Toy Story Collection
2	3	Grumpy Old Men Collection
3	5	Father of the Bride Collection

순서	시리즈ID	시리즈
1	10194	Toy Story Collection
2	119050	Grumpy Old Men Collection
3	96871	Father of the Bride Collection


# 영화ID로 영화 제목, 시리즈, 장르 출력
1	1	Toy Story	Toy Story Collection	['Animation', 'Comedy', 'Family']
2	3114	Toy Story 2	Toy Story Collection	['Animation', 'Comedy', 'Family']
3	2355	A Bug's Life		['Adventure', 'Animation', 'Comedy', 'Family']
4	4886	Monsters, Inc.	Monsters, Inc. Collection	['Animation', 'Comedy', 'Family']
5	6377	Finding Nemo	Finding Nemo Collection	['Animation', 'Family']


'''

