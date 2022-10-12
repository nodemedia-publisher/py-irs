import hgsysinc
from hgstat_test_kagmov import hgstat_metadata_kaggle
#---------------
# format: movies_metadata
#---------------
# adult,belongs_to_collection,budget,genres,homepage,id,imdb_id,original_language,original_title,overview,popularity,poster_path,production_companies,production_countries,release_date,revenue,runtime,spoken_languages,status,tagline,title,video,vote_average,vote_count
# False,"{'id': 10194, 'name': 'Toy Story Collection', 'poster_path': '/7G9915LfUQ2lVfwMEEhDsn3kT4B.jpg', 'backdrop_path': '/9FBwqcd9IRruEDUrTdcaafOMKUq.jpg'}",30000000,"[{'id': 16, 'name': 'Animation'}, {'id': 35, 'name': 'Comedy'}, {'id': 10751, 'name': 'Family'}]",http://toystory.disney.com/toy-story,862,tt0114709,en,Toy Story,"Led by Woody, Andy's toys live happily in his room until Andy's birthday brings Buzz Lightyear onto the scene. Afraid of losing his place in Andy's heart, Woody plots against Buzz. But when circumstances separate Buzz and Woody from their owner, the duo eventually learns to put aside their differences.",21.946943,/rhIRbceoE9lR4veEXuwCC2wARtG.jpg,"[{'name': 'Pixar Animation Studios', 'id': 3}]","[{'iso_3166_1': 'US', 'name': 'United States of America'}]",1995-10-30,373554033,81.0,"[{'iso_639_1': 'en', 'name': 'English'}]",Released,,Toy Story,False,7.7,5415
# False,,65000000,"[{'id': 12, 'name': 'Adventure'}, {'id': 14, 'name': 'Fantasy'}, {'id': 10751, 'name': 'Family'}]",,8844,tt0113497,en,Jumanji,"When siblings Judy and Peter discover an enchanted board game that opens the door to a magical world, they unwittingly invite Alan -- an adult who's been trapped inside the game for 26 years -- into their living room. Alan's only hope for freedom is to finish the game, which proves risky as all three find themselves running from giant rhinoceroses, evil monkeys and other terrifying creatures.",17.015539,/vzmL6fP7aPKNKPRTFnZmiUfciyV.jpg,"[{'name': 'TriStar Pictures', 'id': 559}, {'name': 'Teitler Film', 'id': 2550}, {'name': 'Interscope Communications', 'id': 10201}]","[{'iso_3166_1': 'US', 'name': 'United States of America'}]",1995-12-15,262797249,104.0,"[{'iso_639_1': 'en', 'name': 'English'}, {'iso_639_1': 'fr', 'name': 'Français'}]",Released,Roll the dice and unleash the excitement!,Jumanji,False,6.9,2413
#---------------
movies_metadata =  hgstat_metadata_kaggle() # 데이터베이스 항목 전부 읽기
print(movies_metadata)
print(f'movies_metadata.columns {(len(movies_metadata.columns.values))} :') 
print(movies_metadata.columns.values)
#=print(movies_metadata.columns.values.tolist())
print(), print(movies_metadata.iloc[0]) # 첫 번째 항목 출력


'''
처리 결과: 
================================
       adult  ... vote_count
0      False  ...     5415.0
1      False  ...     2413.0
2      False  ...       92.0
3      False  ...       34.0
4      False  ...      173.0
...      ...  ...        ...
45461  False  ...        1.0
45462  False  ...        3.0
45463  False  ...        6.0
45464  False  ...        0.0
45465  False  ...        0.0

[45466 rows x 24 columns]
movies_metadata.columns 24 :
['adult' 'belongs_to_collection' 'budget' 'genres' 'homepage' 'id'
 'imdb_id' 'original_language' 'original_title' 'overview' 'popularity'
 'poster_path' 'production_companies' 'production_countries'
 'release_date' 'revenue' 'runtime' 'spoken_languages' 'status' 'tagline'
 'title' 'video' 'vote_average' 'vote_count']
 
adult                                                                False    
belongs_to_collection    {'id': 10194, 'name': 'Toy Story Collection', ...    
budget                                                            30000000    
genres                   [{'id': 16, 'name': 'Animation'}, {'id': 35, '...    
homepage                              http://toystory.disney.com/toy-story    
id                                                                     862    
imdb_id                                                          tt0114709    
original_language                                                       en    
original_title                                                   Toy Story    
overview                 Led by Woody, Andy's toys live happily in his ...    
popularity                                                         21.9469    
poster_path                               /rhIRbceoE9lR4veEXuwCC2wARtG.jpg    
production_companies        [{'name': 'Pixar Animation Studios', 'id': 3}]    
production_countries     [{'iso_3166_1': 'US', 'name': 'United States o...    
release_date                                                    1995-10-30    
revenue                                                        3.73554e+08    
runtime                                                                 81    
spoken_languages                  [{'iso_639_1': 'en', 'name': 'English'}]    
status                                                            Released    
tagline                                                                NaN    
title                                                            Toy Story    
video                                                                False    
vote_average                                                           7.7    
vote_count                                                            5415    
Name: 0, dtype: object

'''
