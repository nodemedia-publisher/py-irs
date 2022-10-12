import hgsysinc
from hgstat_test_kagmov import (
    hgstat_metadata_kaggle,
    hgstat_links_kaggle,
    #=hgstat_get_title_kaggle_by_movieId,
    hgstat_get_metadataId_by_movieId,
    hgstat_get_title_kaggle_by_metadataId,
    hgstat_get_genres_kaggle_by_metadataId,
    hgstat_get_overview_kaggle_by_metadataId,
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
print(links)
print()

#---------------------
#---------------------
print('# 영화ID로 영화 제목, 장르, 줄거리 출력')
movieId_list = [
    1, # 'Toy Story'
    3114, # 'Toy Story 2'
    2355, # Bug's Life, A (1998)
    #=4886, # Monsters, Inc. (2001)
    #=6377, # Finding Nemo (2003)
    #=8961, # Incredibles, The (2004)
    #=4306, # Shrek (2001)
    #=260, # Star Wars: Episode IV - A New Hope (1977)
]
for li, movieId in enumerate(movieId_list):
    metadata_id = hgstat_get_metadataId_by_movieId(movieId, links)
    #=print(metadata_id)
    movie_title = hgstat_get_title_kaggle_by_metadataId(metadata_id, movies_metadata)
    if(len(movie_title) <= 0): # 제목이 없는 경우
        movie_title = '<<<영화 제목 없음>>>'

    genres_list = hgstat_get_genres_kaggle_by_metadataId(metadata_id, movies_metadata)
    if(len(genres_list) <= 0): # 장르 없는 경우
        genres_list = '<<<장르 없음>>>'

    overview = hgstat_get_overview_kaggle_by_metadataId(metadata_id, movies_metadata)
    if(len(overview) <= 0): # 줄거리 없는 경우
        overview = '<<<줄거리 없음>>>'

    #
    print(f'{li+1}\t{movieId}\t{metadata_id}\t{movie_title}\t{genres_list}\t{overview}')


'''
처리 결과: 
================================
       movieId   imdbId    tmdbId
0            1   114709     862.0
1            2   113497    8844.0
2            3   113228   15602.0
3            4   114885   31357.0
4            5   113041   11862.0
...        ...      ...       ...
45838   176269  6209470  439050.0
45839   176271  2028550  111109.0
45840   176273   303758   67758.0
45841   176275     8536  227506.0
45842   176279  6980792  461257.0

[45843 rows x 3 columns]

# 영화ID로 영화 제목, 장르, 줄거리 출력
1	1	Toy Story	['Animation', 'Comedy', 'Family']	Led by Woody, Andy's toys live happily in his room until Andy's birthday brings Buzz Lightyear onto the scene. Afraid of losing his place in Andy's heart, Woody plots against Buzz. But when circumstances separate Buzz and Woody from their owner, the duo eventually learns to put aside their differences.
2	3114	Toy Story 2	['Animation', 'Comedy', 'Family']	Andy heads off to Cowboy Camp, leaving his toys to their own devices. Things shift into high gear when an obsessive toy collector named Al McWhiggen, owner of Al's Toy Barn kidnaps Woody. Andy's toys mount a daring rescue mission, Buzz Lightyear meets his match and Woody has to decide where he and his heart truly belong.
3	2355	A Bug's Life	['Adventure', 'Animation', 'Comedy', 'Family']	On behalf of "oppressed bugs everywhere," an inventive ant named Flik hires a troupe of warrior bugs to defend his bustling colony from a horde of freeloading grasshoppers led by the evil-minded Hopper.



'''
