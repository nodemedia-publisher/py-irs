import hgsysinc
from hgstat_test_kagmov import (
    hgstat_links_kaggle,
    hgstat_get_list_set__kaggle_movies,
    hgstat_get_distance_by_inx__kagmov,
    hgstat_get_metadataId_by_movieId,
    PrintSimDoc_CosDistance__ByInx,
)
from hgwordlist import GetWordDictLists_WordLists
#-----------
#-----------
links = hgstat_links_kaggle()
overview_wordlists, overview_list, title_list, \
    release_date_list, genres_list, vote_average_list, \
    vote_count_list, belongs_to_collection, metadataId_list = \
    hgstat_get_list_set__kaggle_movies()
print(f'overview_list: {len(overview_list)}')
print(f'overview_wordlists: {len(overview_wordlists)} movies')
#=print(f'title_list: {len(title_list)}')
#=print(f'release_date_list: {len(release_date_list)}')
print()
#-----------
#-----------
# 영화 줄거리 목록을 어휘 빈도 형식의 사전 목록으로 변환
WordDicts = GetWordDictLists_WordLists(overview_wordlists, EraseNonKeyword=False)
print(f'WordDicts [{len(WordDicts)}]:')

# 영화ID를 index로 변환
movieId = 1 # 첫 번째 영화() 'Toy Story'(영화ID:1)
#=movieId = 648 # 'Mission: Impossible'(영화ID:648)
metadataId = hgstat_get_metadataId_by_movieId(movieId, links)
movieInx = metadataId_list.index(metadataId)

#======================
#======================
# 전체 영화를 대상으로 코사인 거리(텍스트 거리) 측정
SimDocInfo = hgstat_get_distance_by_inx__kagmov(WordDicts, movieInx)
PrintSimDoc_CosDistance__ByInx(SimDocInfo, movieInx, WordDicts, 
    metadataId_list, links, title_list, release_date_list, genres_list, overview_list)




'''
출력 결과
==========================
overview_list: 44493
overview_wordlists: 44493 movies

WordDicts [44493]:
==========================================================
==========================================================
==========================================================
Toy Story(movieId:1) : [1995] {'Comedy', 'Animation', 'Family'}
26 단어:  ['afraid', 'andy', 'aside', 'birthday', 'bring', 'buzz', 'circumstance', 'difference', 'duo', 'eventually', 'happily', 'heart', 'learns', 'led', 'lightyear', 'live', 'losing', 'owner', 'place', 'plot', 'put', 'room', 'scene', 'separate', 'toy', 'woody']

#-------------
# 추천 목록: (간편 출력)
#-------------
순위: (영화ID) 영화 제목 <코사인 거리(텍스트 거리)> [발표] (공통/전체){공통 단어}
1: [78499] Toy Story 3 <0.575> [2010] (4 / 21){'woody', 'buzz', 'andy', 'toy'}
2: [3114] Toy Story 2 <0.584> [1999] (7 / 32){'heart', 'toy', 'buzz', 'andy', 'owner', 'woody', 'lightyear'}
3: [35836] The 40 Year Old Virgin <0.705> [2005] (2 / 35){'andy', 'owner'}
4: [113149] Andy Hardy's Blonde Trouble <0.755> [1944] (1 / 36){'andy'}
5: [25775] The Champ <0.755> [1931] (3 / 64){'andy', 'owner', 'place'}
6: [115879] Small Fry <0.760> [2011] (2 / 14){'buzz', 'place'}
7: [171281] Andy Kaufman Plays Carnegie Hall <0.772> [1980] (1 / 73){'andy'}
8: [158145] Superstar: The Life and Times of Andy Warhol <0.788> [1990] (1 / 4){'andy'}
9: [169546] Andy Peters: Exclamation Mark Question Point <0.793> [2015] (1 / 38){'andy'}
10: [163162] Wabash Avenue <0.820> [1950] (1 / 34){'andy'}


'''

