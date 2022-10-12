# gutenberg porject scraping
import hgsysinc
from hgcrawl import get_gutenberg_text_folder, gutenberg_list, download_gutenberg_text
import time
#-----------
from datetime import datetime
time_beg = datetime.now() # 시작 시각
#-----------
# gutenberg porject: https://www.gutenberg.org/
#-----------
guten_pathname = get_gutenberg_text_folder()

for inx, cur_book in enumerate(gutenberg_list):
    print(f'{inx+1}', end=' ')
    
    title = cur_book[0]
    gutenberg_url = cur_book[1]
    download_gutenberg_text(gutenberg_url, title, down_pathname=guten_pathname)
    
    # 다운로드 후 대기(서버 부하를 줄이기 위해)
    if((inx + 1) < len(gutenberg_list)):
        time.sleep(5) # 5초 대기

#-----------
time_end = datetime.now() # 종료 시각
elapsed = time_end - time_beg # 경과 시간
print('시작 시각:', time_beg)
print('종료 시각:', time_end)
print('경과 시간(Elapsed):', elapsed)


'''
처리 결과:
---------------- 
43개 파일을 5초 간격으로 거의 5분 걸림.
(42번의) 대기 시간 {210}초를 제외하면 실제로 {90}초 정도 걸림.
작품 당 2.1 초 걸림.

==================
filePath: ./../pyexam/hgdatsci
parentPath: ./../pyexam
exist folder: ./../pyexam/ext-src
exist folder: ./../pyexam/ext-src/data
exist folder: ./../pyexam/ext-src/data/gutenberg
exist folder: ./../pyexam/ext-src/data/gutenberg/text
1 [160793]: /ext-src/data/gutenberg/text/A_Christmas_Carol.txt
2 [144713]: /ext-src/data/gutenberg/text/A_Doll_House.txt
3 [578503]: /ext-src/data/gutenberg/text/Adventures_of_Huckleberry_Finn.txt
4 [146210]: /ext-src/data/gutenberg/text/Alice_Adventures.txt
5 [1988720]: /ext-src/data/gutenberg/text/Anna_Karenina.txt
6 [567679]: /ext-src/data/gutenberg/text/Anne_of_Green_Gables.txt
7 [373495]: /ext-src/data/gutenberg/text/Around_the_World_in_Eighty_Days.txt
8 [1114793]: /ext-src/data/gutenberg/text/Ben_Hur.txt
9 [1148994]: /ext-src/data/gutenberg/text/Crime_and_Punishment.txt
10 [856785]: /ext-src/data/gutenberg/text/Dracula.txt
11 [891651]: /ext-src/data/gutenberg/text/Emma.txt
12 [443904]: /ext-src/data/gutenberg/text/Frankenstein.txt
13 [590372]: /ext-src/data/gutenberg/text/Gulliver_Travels.txt
14 [1034782]: /ext-src/data/gutenberg/text/Jane_Eyre.txt
15 [3264882]: /ext-src/data/gutenberg/text/Les_Misérables.txt
16 [1019360]: /ext-src/data/gutenberg/text/Little_Women.txt
17 [1234816]: /ext-src/data/gutenberg/text/Moby_Dick.txt
18 [903834]: /ext-src/data/gutenberg/text/Oliver_Twist.txt
19 [258353]: /ext-src/data/gutenberg/text/Peter_Pan.txt
20 [765087]: /ext-src/data/gutenberg/text/Pride_and_Prejudice.txt
21 [190357]: /ext-src/data/gutenberg/text/Pygmalion.txt
22 [343039]: /ext-src/data/gutenberg/text/Robin_Hood.txt
23 [485786]: /ext-src/data/gutenberg/text/Tarzan_of_the_Apes.txt
24 [687761]: /ext-src/data/gutenberg/text/The_Odyssey.txt
25 [568908]: /ext-src/data/gutenberg/text/The_Adventures_of_Sherlock_Holmes.txt
26 [396910]: /ext-src/data/gutenberg/text/The_Adventures_of_Tom_Sawyer.txt
27 [1959710]: /ext-src/data/gutenberg/text/The_Brothers_Karamazov.txt
28 [2656314]: /ext-src/data/gutenberg/text/The_Count_of_Monte_Cristo.txt
29 [273684]: /ext-src/data/gutenberg/text/The_Great_Gatsby.txt
30 [1118354]: /ext-src/data/gutenberg/text/The_Iliad__by_Homer.txt
31 [277001]: /ext-src/data/gutenberg/text/The_Jungle_Book.txt
32 [70783]: /ext-src/data/gutenberg/text/The_Legend_of_Sleepy_Hollow.txt
33 [629924]: /ext-src/data/gutenberg/text/The_Life_and_Adventures_of_Robinson_Crusoe.txt
34 [429395]: /ext-src/data/gutenberg/text/The_Lost_World.txt
35 [1005759]: /ext-src/data/gutenberg/text/The_Man_in_the_Iron_Mask.txt
36 [498610]: /ext-src/data/gutenberg/text/The_Scarlet_Letter.txt
37 [182075]: /ext-src/data/gutenberg/text/The_Time_Machine.txt
38 [145467]: /ext-src/data/gutenberg/text/Romeo_and_Juliet.txt
39 [341709]: /ext-src/data/gutenberg/text/The_War_of_the_Worlds.txt
40 [210069]: /ext-src/data/gutenberg/text/The_Wonderful_Wizard_of_Oz.txt
41 [368573]: /ext-src/data/gutenberg/text/Treasure_Island.txt
42 [1017675]: /ext-src/data/gutenberg/text/Uncle_Tom_Cabin.txt
43 [3246345]: /ext-src/data/gutenberg/text/War_and_Peace.txt

시작 시각: 2022-03-24 22:22:21.025157
종료 시각: 2022-03-24 22:27:20.257022
경과 시간(Elapsed): 0:04:59.23186


'''

