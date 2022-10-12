#====================================
#====================================
#====================================
#---------------
# src: https://atfis.or.kr/article/M001050000/view.do?articleId=358&boardId=3&page=5&searchKey=&searchString=&searchCategory=
# [가공식품 세분화 시장 현황조사, 농수산물유통공사] 54쪽, 57쪽
# 원자료: 통계청, KOSIS, http://kosis.kr, 광업제조업동향조사
#---------------
kosos_drink_2010 = { # 혼합음료 생산량(단위: kl) [가공식품 세분화 시장 현황조사, 농수산물유통공사] 54쪽,
    '2010.01': 32122,
    '2010.02': 36529,
    '2010.03': 52409,
    '2010.04': 63650,
    '2010.05': 72324,
    '2010.06': 72228,
    '2010.07': 71971,
    '2010.08': 69514,
    '2010.09': 56564,
    '2010.10': 53861,
    '2010.11': 45193,
}

kosos_soymilk_2010 = { # 두유 생산량(단위: kl) [가공식품 세분화 시장 현황조사, 농수산물유통공사] 57쪽,
    '2010.01': 13572,
    '2010.02': 14704,
    '2010.03': 18620,
    '2010.04': 16186,
    '2010.05': 16245,
    '2010.06': 16373,
    '2010.07': 16270,
    '2010.08': 17443,
    '2010.09': 17917,
    '2010.10': 20272,
    '2010.11': 19655,
}

kosos_carbonated_drink_2010 = { # 탄산 음료 생산량(단위: kl)
    '2010.01': 96183,
    '2010.02': 95203,
    '2010.03': 103457,
    '2010.04': 99790,
    '2010.05': 108743,
    '2010.06': 108056,
    '2010.07': 111109,
    '2010.08': 103147,
    '2010.09': 91561,
    '2010.10': 98696,
    '2010.11': 80454,
}



#---------------
# src: https://data.kma.go.kr/stcs/grnd/grndTaList.do?pgmNo=70
# [기상청 2010년 월별 날씨]
#---------------
kma_weather_2010 = { # '년월': '평균기온(℃)'
    '2010.01': -1.7,
    '2010.02': 2.3,
    '2010.03': 5.5,
    '2010.04': 9.9,
    '2010.05': 17.1,
    '2010.06': 22.3,
    '2010.07': 25.4,
    '2010.08': 26.9,
    '2010.09': 21.8,
    '2010.10': 14.5,
    '2010.11': 7.1,
    #='2010.12': 0.9,   # 위에 음표 생산에서 12월이 없어서 막는다.
}

#================================
#================================
#---------------------
#---------------------
# 인구순 나라 목록: 2021.01.23
# 참고: https://ko.wikipedia.org/wiki/%EC%9D%B8%EA%B5%AC%EC%88%9C_%EB%82%98%EB%9D%BC_%EB%AA%A9%EB%A1%9D
#---------------------
# 3 	미국 	332,915,074 	2020 	공식 인구시계
# 11 	일본 	125,960,000 	2020
# 21 	영국 	66,830,229 	2018 	공식 연간 추계치
# 22 	프랑스 	65,712,057 	2019 	월간 추계치
# 24 	이탈리아 	59,575,231 	2018 	월간 추계치
# 28 	대한민국 	51,821,669 	2020 	연간 장래인구추계
# 30 	스페인 	46,733,038 	2019
#---------------------
# GDP 순위
# 소스: https://ko.wikipedia.org/wiki/%EB%AA%85%EB%AA%A9_%EA%B5%AD%EB%82%B4_%EC%B4%9D%EC%83%9D%EC%82%B0%EC%88%9C_%EB%82%98%EB%9D%BC_%EB%AA%A9%EB%A1%9D
# 1 	미국 	20,807,269
# — 	유럽 연합[5][n 1] 	14,926,538
# 2 	중화인민공화국 	14,860,775
# 3 	일본 	4,910,580
# 4 	독일 	3,780,553
# 5 	영국 	2,638,296
# 6 	인도 	2,592,583
# 7 	프랑스 	2,551,451
# 8 	이탈리아 	1,848,222
# 9 	캐나다 	1,600,264
# 10 	대한민국 	1,586,786
# 11 	러시아 	1,464,078
# 12 	브라질 	1,363,767
# 13 	오스트레일리아 	1,334,688
# 14 	스페인 	1,247,464
# 15 	인도네시아 	1,088,768
# 16 	멕시코 	1,040,373
# 17 	네덜란드 	886,339
#18 	스위스 	707,868
#---------------------
# 1인당 GDP 순위
# 소스: https://ko.wikipedia.org/wiki/%EC%9D%BC%EC%9D%B8%EB%8B%B9_%EB%AA%85%EB%AA%A9_%EA%B5%AD%EB%82%B4_%EC%B4%9D%EC%83%9D%EC%82%B0%EC%88%9C_%EB%82%98%EB%9D%BC_%EB%AA%A9%EB%A1%9D
# 1 	룩셈부르크의 기 룩셈부르크 	113,196
# 2 	스위스의 기 스위스 	83,717
# — 	마카오의 기 마카오 	81,151
# 3 	노르웨이의 기 노르웨이 	77,975
# 4 	아일랜드의 기 아일랜드 	77,771
# 5 	카타르의 기 카타르 	69,688
# 6 	아이슬란드의 기 아이슬란드 	67,037
# 7 	미국의 기 미국 	65,112
# 8 	싱가포르의 기 싱가포르 	63,987
# 9 	덴마크의 기 덴마크 	59,795
# 10 	오스트레일리아의 기 오스트레일리아 	53,825
# 11 	네덜란드의 기 네덜란드 	52,368
# 12 	스웨덴의 기 스웨덴 	51,242
# 13 	오스트리아의 기 오스트리아 	50,023
#— 	홍콩의 기 홍콩 	49,334
# 14 	핀란드의 기 핀란드 	48,869
# 16 	독일의 기 독일 	46,564
# 17 	캐나다의 기 캐나다 	46,213
# 18 	벨기에의 기 벨기에 	45,176
# 19 	이스라엘의 기 이스라엘 	42,823
# 20 	프랑스의 기 프랑스 	41,761
# 21 	영국의 기 영국 	41,030
# 22 	일본의 기 일본 	40,847
# 23 	뉴질랜드의 기 뉴질랜드 	40,634
# 24 	아랍에미리트의 기 아랍에미리트 	37,750
# 26 	이탈리아의 기 이탈리아 	32,947
# — 	푸에르토리코의 기 푸에르토리코 	31,538
# 27 	대한민국의 기 대한민국 	31,431
# 29 	스페인의 기 스페인 	29,961
# 35 	중화민국의 기 중화민국 	24,878
#---------------------




#================================
#================================
#---------------------
#---------------------
# src: Worldometer's COVID-19 data
# https://www.worldometers.info/coronavirus/country/south-korea/
# begin: "20.02.15",
# end: "21.01.21",
#---------------------
covid19_date = [ # total: 342개, 2020.02.15 ~ 2021.01.21
    "20.02.15","20.02.16","20.02.17","20.02.18","20.02.19","20.02.20","20.02.21","20.02.22","20.02.23","20.02.24","20.02.25","20.02.26","20.02.27","20.02.28","20.02.29",
    "20.03.01","20.03.02","20.03.03","20.03.04","20.03.05","20.03.06","20.03.07","20.03.08","20.03.09","20.03.10","20.03.11","20.03.12","20.03.13","20.03.14","20.03.15","20.03.16","20.03.17","20.03.18","20.03.19","20.03.20","20.03.21","20.03.22","20.03.23","20.03.24","20.03.25","20.03.26","20.03.27","20.03.28","20.03.29","20.03.30","20.03.31",
    "20.04.01","20.04.02","20.04.03","20.04.04","20.04.05","20.04.06","20.04.07","20.04.08","20.04.09","20.04.10","20.04.11","20.04.12","20.04.13","20.04.14","20.04.15","20.04.16","20.04.17","20.04.18","20.04.19","20.04.20","20.04.21","20.04.22","20.04.23","20.04.24","20.04.25","20.04.26","20.04.27","20.04.28","20.04.29","20.04.30",
    "20.05.01","20.05.02","20.05.03","20.05.04","20.05.05","20.05.06","20.05.07","20.05.08","20.05.09","20.05.10","20.05.11","20.05.12","20.05.13","20.05.14","20.05.15","20.05.16","20.05.17","20.05.18","20.05.19","20.05.20","20.05.21","20.05.22","20.05.23","20.05.24","20.05.25","20.05.26","20.05.27","20.05.28","20.05.29","20.05.30","20.05.31",
    "20.06.01","20.06.02","20.06.03","20.06.04","20.06.05","20.06.06","20.06.07","20.06.08","20.06.09","20.06.10","20.06.11","20.06.12","20.06.13","20.06.14","20.06.15","20.06.16","20.06.17","20.06.18","20.06.19","20.06.20","20.06.21","20.06.22","20.06.23","20.06.24","20.06.25","20.06.26","20.06.27","20.06.28","20.06.29","20.06.30",
    "20.07.01","20.07.02","20.07.03","20.07.04","20.07.05","20.07.06","20.07.07","20.07.08","20.07.09","20.07.10","20.07.11","20.07.12","20.07.13","20.07.14","20.07.15","20.07.16","20.07.17","20.07.18","20.07.19","20.07.20","20.07.21","20.07.22","20.07.23","20.07.24","20.07.25","20.07.26","20.07.27","20.07.28","20.07.29","20.07.30","20.07.31",
    "20.08.01","20.08.02","20.08.03","20.08.04","20.08.05","20.08.06","20.08.07","20.08.08","20.08.09","20.08.10","20.08.11","20.08.12","20.08.13","20.08.14","20.08.15","20.08.16","20.08.17","20.08.18","20.08.19","20.08.20","20.08.21","20.08.22","20.08.23","20.08.24","20.08.25","20.08.26","20.08.27","20.08.28","20.08.29","20.08.30","20.08.31",
    "20.09.01","20.09.02","20.09.03","20.09.04","20.09.05","20.09.06","20.09.07","20.09.08","20.09.09","20.09.10","20.09.11","20.09.12","20.09.13","20.09.14","20.09.15","20.09.16","20.09.17","20.09.18","20.09.19","20.09.20","20.09.21","20.09.22","20.09.23","20.09.24","20.09.25","20.09.26","20.09.27","20.09.28","20.09.29","20.09.30",
    "20.10.01","20.10.02","20.10.03","20.10.04","20.10.05","20.10.06","20.10.07","20.10.08","20.10.09","20.10.10","20.10.11","20.10.12","20.10.13","20.10.14","20.10.15","20.10.16","20.10.17","20.10.18","20.10.19","20.10.20","20.10.21","20.10.22","20.10.23","20.10.24","20.10.25","20.10.26","20.10.27","20.10.28","20.10.29","20.10.30","20.10.31",
    "20.11.01","20.11.02","20.11.03","20.11.04","20.11.05","20.11.06","20.11.07","20.11.08","20.11.09","20.11.10","20.11.11","20.11.12","20.11.13","20.11.14","20.11.15","20.11.16","20.11.17","20.11.18","20.11.19","20.11.20","20.11.21","20.11.22","20.11.23","20.11.24","20.11.25","20.11.26","20.11.27","20.11.28","20.11.29","20.11.30",
    "20.12.01","20.12.02","20.12.03","20.12.04","20.12.05","20.12.06","20.12.07","20.12.08","20.12.09","20.12.10","20.12.11","20.12.12","20.12.13","20.12.14","20.12.15","20.12.16","20.12.17","20.12.18","20.12.19","20.12.20","20.12.21","20.12.22","20.12.23","20.12.24","20.12.25","20.12.26","20.12.27","20.12.28","20.12.29","20.12.30","20.12.31",
    "21.01.01","21.01.02","21.01.03","21.01.04","21.01.05","21.01.06","21.01.07","21.01.08","21.01.09","21.01.10","21.01.11","21.01.12","21.01.13","21.01.14","21.01.15","21.01.16","21.01.17","21.01.18","21.01.19","21.01.20","21.01.21",
]
covid19_korea_data = [ # total: 73890건(342개), 2020.02.15 ~ 2021.01.21
0,1,1,1,27,53,98,227,166,231,144,284,505,571,813,586,599,851,435,663,309,448,272,165,35,242,114,110,107,76,74,84,93,152,87,147,98,64,76,100,104,91,146,105,78,125,101,89,86,94,81,47,47,53,39,27,30,32,25,27,27,22,22,18,8,13,9,11,8,6,10,10,10,14,9,4,9,6,13,8,3,2,4,12,18,34,35,27,26,29,27,19,13,15,13,32,12,20,23,25,16,19,40,79,58,39,27,35,38,49,39,39,51,57,38,38,50,45,56,48,34,36,34,43,59,49,67,48,17,46,51,28,39,51,62,42,43,50,54,63,63,61,46,44,62,50,45,35,44,62,33,39,61,60,39,34,26,45,63,59,41,113,58,25,28,48,18,36,31,30,23,34,33,43,20,43,36,28,34,54,56,103,166,279,197,246,297,288,324,332,397,266,280,320,441,371,323,299,248,235,267,195,198,168,167,119,136,156,155,176,136,121,109,106,113,153,126,110,82,70,61,110,125,114,61,95,50,38,113,77,63,75,64,73,75,114,69,54,72,58,97,102,73,110,47,73,91,76,58,91,119,155,77,61,119,88,103,125,114,126,124,97,75,118,125,145,89,143,126,100,146,143,191,205,208,223,229,313,343,363,386,330,271,349,382,583,569,488,449,377,451,511,540,629,583,631,615,585,670,682,688,950,1030,718,880,1075,1014,1064,1053,1095,926,867,1090,985,1237,1132,970,808,1045,1048,967,1029,818,657,1020,715,839,868,672,641,665,450,537,553,524,513,579,520,389,386,403,400]
# 인구 백만명당 확진자(대한민국): 1,456
data_korea_pop = int('51,821,669'.replace(',',''))
#---------------------
covid19_japan_data = [ # total: 345168(342개), 2020.02.15 ~ 2021.01.21
0,6,7,8,10,10,15,25,12,13,2,11,42,19,8,15,18,19,38,33,56,41,41,28,57,52,52,43,70,29,17,28,36,29,64,47,47,27,65,114,80,112,194,173,87,225,206,233,318,204,515,252,351,410,680,658,743,622,248,267,741,605,556,509,501,338,377,438,418,344,519,218,165,122,159,193,217,266,306,201,175,0,224,98,88,114,70,121,81,71,83,34,48,20,62,18,39,89,23,14,31,42,28,32,36,85,47,33,46,56,32,46,39,38,33,36,41,41,40,50,47,73,85,41,40,72,59,65,52,52,56,86,87,100,93,86,117,130,151,194,214,240,253,206,193,197,348,410,373,366,352,288,382,583,659,510,454,640,567,726,927,830,596,607,972,940,1148,1323,1464,853,1998,1171,1271,1134,1552,1624,1344,1207,938,1282,937,1070,1360,1137,953,1018,865,951,1220,1012,1014,760,614,701,846,905,850,841,601,527,609,598,669,608,543,437,378,492,495,680,643,674,439,301,490,561,485,579,584,483,298,330,273,456,558,635,441,363,516,553,652,553,571,400,308,496,477,619,594,679,435,326,467,570,721,632,593,471,353,453,591,614,697,699,540,424,618,736,770,770,754,667,468,619,938,944,1132,1172,998,899,1173,1555,1587,1685,1694,1459,1190,1489,2151,2301,2398,2514,2179,1571,1471,1861,2230,2577,2585,2107,1934,1692,2441,2405,2442,2424,1969,1862,1911,2733,2969,2757,2988,2366,2217,2172,3061,3035,2893,2849,2643,2135,2455,3026,3841,3567,3765,2924,2884,3476,3708,4091,3617,2942,2893,4113,4357,6076,6906,7855,7621,5977,5460,5103,5308,6591,6696,6386,5998,6034,5446,5447]
# 인구 백만명당 확진자(일본): 2,780
data_japan_pop = int('125,960,000'.replace(',',''))

#--- italy
covid19_italy_data = [ # total: 2428218건(342개), 2020.02.15 ~ 2021.01.21
0,0,0,0,0,1,17,58,78,72,94,147,185,234,239,574,336,466,588,769,778,1247,1494,1799,977,2313,2653,2548,3499,3593,3235,3527,4208,5324,5988,6554,5560,4783,5240,5198,6202,5907,5973,5215,4047,4053,4783,4669,4585,4807,4318,3599,3037,3834,4204,3950,4697,4094,3153,2973,2666,3787,3494,3492,3047,2251,2727,3370,2644,3022,2357,2325,1738,2092,2086,1872,1966,1900,1389,1222,1075,1445,1402,1328,1083,802,745,1403,888,993,789,875,675,451,813,665,643,653,670,532,300,397,585,594,517,417,334,200,319,322,177,519,270,197,280,283,202,380,163,347,337,301,210,329,332,251,264,224,221,113,190,296,255,175,174,126,142,182,201,223,235,192,208,137,193,214,276,188,234,169,114,162,230,231,249,218,190,128,280,306,252,273,252,170,181,289,382,379,295,238,159,190,384,401,552,347,463,259,412,476,522,574,627,479,320,401,642,840,947,1071,1209,952,876,1365,1409,1462,1444,1365,999,984,1332,1402,1738,1700,1303,1107,1366,1434,1597,1616,1499,1458,1008,1229,1450,1585,1906,1638,1587,1349,1392,1640,1786,1912,1869,1766,1493,1647,1851,2548,2498,2844,2578,2257,2676,3678,4458,5372,5724,5456,4616,5901,7331,8803,10010,10925,11704,9335,10874,15198,16079,19139,19644,21268,17007,21991,24989,26826,31082,31756,29907,22250,28242,30547,34498,37807,39809,32614,25263,35098,32960,37978,40896,37253,33977,27354,32188,34283,36173,37239,34767,28334,22925,23231,25851,28993,28344,26321,20647,16253,19143,20495,22950,23826,20844,18674,13598,14706,12626,16860,18516,19702,17795,11949,14681,17400,18107,17959,16267,15074,10860,13294,14521,18040,19037,10429,8909,8583,11212,16202,23476,22205,12227,14243,10797,15373,20331,18016,17531,19976,18625,12532,14241,15771,17244,16146,16309,12545,8824,10494,13548,14078]
# 인구 백만명당 확진자(이탈리아): 41,151
data_italy_pop = int('59,575,231'.replace(',',''))

#================================
#================================
#================================
# {컴퓨터과학}
cb_buydata_111 = {'고객ID':111, '구입목록': ['C언어', '파이썬', '자료구조', '파일처리', '운영체제', '논리회로', '데이터베이스', '인공지능', '네트워크', '영상처리','정보검색', 'Window 프로그래밍', 'iOS 프로그래밍', '자바 프로그래밍']}
cb_buydata_112 = {'고객ID':112, '구입목록': ['C언어', '파이썬', '자료구조', '파일처리',]}
cb_buydata_113 = {'고객ID':113, '구입목록': ['C언어', '파이썬', '자료구조', '파일처리', '운영체제', '논리회로', '데이터베이스', ]}
cb_buydata_114 = {'고객ID':114, '구입목록': ['C언어', '자료구조', '파일처리', '데이터베이스', '정보검색', 'Window 프로그래밍', 'iOS 프로그래밍', '자바 프로그래밍']}
cb_buydata_115 = {'고객ID':115, '구입목록': ['C언어', '자료구조', '파일처리', '데이터베이스', '정보검색', 'Window 프로그래밍', '자바 프로그래밍']}
cb_buydata_116 = {'고객ID':116, '구입목록': ['C언어', '자료구조', '파일처리', '데이터베이스', '네트워크', '정보검색', '언어학','자바 프로그래밍']}
cb_buydata_117 = {'고객ID':117, '구입목록': ['C언어', '파이썬', '자료구조', '파일처리', 'Window 프로그래밍', 'iOS 프로그래밍', '자바 프로그래밍']}
cb_buydata_118 = {'고객ID':118, '구입목록': ['C언어', '파이썬', '자료구조', '파일처리', '운영체제', 'Window 프로그래밍', 'iOS 프로그래밍', '자바 프로그래밍']}
cb_buydata_119 = {'고객ID':119, '구입목록': ['파이썬', '자료구조', '인공지능', '영상처리',]}
# {한국어정보처리}
cb_buydata_131 = {'고객ID':131, '구입목록': ['파이썬', '자료구조', '인공지능', '언어학', ]}
cb_buydata_132 = {'고객ID':132, '구입목록': ['파이썬', '자료구조', '파일처리', '데이터베이스', '인공지능', '언어학', '형태론', '통사론', '음성학', '의미론']}
cb_buydata_133 = {'고객ID':133, '구입목록': ['파이썬', '자료구조', '파일처리', '데이터베이스', '인공지능', '언어학', '음성학',]}
cb_buydata_134 = {'고객ID':134, '구입목록': ['파이썬', '자료구조', '파일처리', '데이터베이스', '인공지능', '언어학', '형태론', '통사론', '의미론']}
cb_buydata_135 = {'고객ID':135, '구입목록': ['C언어', '파이썬', '자료구조', '파일처리', '인공지능', '언어학', '형태론', '통사론', '음성학', '의미론']}
# {언어학}
cb_buydata_211 = {'고객ID':211, '구입목록': ['언어학', '형태론', '통사론', '음성학', '의미론', '표준국어문법', '심리언어학', '신경언어학', '언어병리학']}
cb_buydata_212 = {'고객ID':212, '구입목록': ['언어학', '통사론', '음성학',]}
cb_buydata_213 = {'고객ID':213, '구입목록': ['언어학', '형태론', '통사론', '음성학', '의미론', '표준국어문법', '심리언어학',]}
# {언어교육}
cb_buydata_221 = {'고객ID':221, '구입목록': ['언어학', '통사론', '음성학', '의미론', '표준국어문법', '교육학', '교육행정', '교육심리', '교육상담']}
cb_buydata_222 = {'고객ID':222, '구입목록': ['언어학', '통사론', '음성학', '의미론', '표준국어문법', '교육학', '교육행정',]}
# {교육학}
cb_buydata_311 = {'고객ID':311, '구입목록': ['교육학', '교육행정', '교육심리', '교육상담', '교육철학']}
cb_buydata_312 = {'고객ID':312, '구입목록': ['교육학', '교육행정', '교육심리', '교육철학']}

cb_buydatas = [
    cb_buydata_111,cb_buydata_112,cb_buydata_113,cb_buydata_114,cb_buydata_115,cb_buydata_116,cb_buydata_117,cb_buydata_118,cb_buydata_119,
    cb_buydata_131,cb_buydata_132,cb_buydata_133,cb_buydata_134,cb_buydata_135,
    cb_buydata_211,cb_buydata_212,cb_buydata_213,
    cb_buydata_221,cb_buydata_222,
    cb_buydata_311,cb_buydata_312,
]

#================================
# 위 구매 데이터에서 구매 항목을 목록으로 변환
# itemlist (28) : ['C언어', '파이썬', '자료구조', '파일처리', '운영체제', '논리회로', '데이터베이스', '인공지능', '네트워크', '영상처리', '정보검색', 'Window 프로그래밍', 'iOS 프로그래밍', '자바 프로그래밍', '언어학', '형태론', '통사론', '음성학', '의미론', '표준국어문법', '심리언어학', '신경언어학', '언어병리학', '교육학', '교육행정', '교육심리', '교육상담', '교육철학']
# 21 : ['C언어', '파이썬', '자료구조', '파일처리', '데이터베이스', '인공지능', '네트워크', '영상처리', '정보검색', 'Window 프로그래밍', 'iOS 프로그래밍', '자바 프로그래밍', '언어학', '형태론', '통사론', '음성학', '의미론', '교육학', '교육행정', '교육심리', '교육상담']
#================================

#================================
# 위 구매 데이터를 구매 테이블로 변환
#================================
# {1: 'C언어', 2: '파이썬', 3: '자료구조', 4: '파일처리', 
# 5: '운영체제', 6: '논리회로', 7: '데이터베이스', 8: '인공지능', 9: '네트워크', 
# 10: '영상처리', 11: '정보검색', 12: 'Window 프로그래밍', 13: 'iOS 프로그래밍', 
# 14: '자바 프로그래밍', 15: '언어학', 16: '형태론', 17: '통사론', 18: '음성학', 
# 19: '의미론', 20: '표준국어문법', 21: '심리언어학', 22: '신경언어학', 23: '언어병리학', 
# 24: '교육학', 25: '교육행정', 26: '교육심리', 27: '교육상담', 28: '교육철학'}
#================================
cb_buy_item_list = [ # {28}개
    'C언어', '파이썬', '자료구조', '파일처리', '운영체제', 
    '논리회로', '데이터베이스', '인공지능', '네트워크', '영상처리', 
    '정보검색', 'Window 프로그래밍', 'iOS 프로그래밍', '자바 프로그래밍', '언어학', 
    '형태론', '통사론', '음성학', '의미론', '표준국어문법', 
    '심리언어학', '신경언어학', '언어병리학', '교육학', '교육행정', 
    '교육심리', '교육상담', '교육철학',
]

# 위 구매 데이터에서 구매자를 목록으로 변환
# {1: 111, 2: 112, 3: 113, 4: 114, 5: 115, 6: 116, 7: 117, 
# 8: 118, 9: 119, 10: 131, 11: 132, 12: 133, 13: 134, 14: 135, 
# 15: 211, 16: 212, 17: 213, 18: 221, 19: 222, 20: 311, 21: 312}
cb_buy_person_list =    [111, 112, 113, 114, 115, 116, 117, 118, 119, 131, 132, 133, 134, 135, 211, 212, 213, 221, 222, 311, 312] # {21}개

#
cb_person_id_list_by_item_key = {
    'C언어': [111, 112, 113, 114, 115, 116, 117, 118, 135], 
    'Window 프로그래밍': [111, 114, 115, 117, 118], 
    'iOS 프로그래밍': [111, 114, 117, 118], 
    '교육상담': [221, 311], 
    '교육심리': [221, 311, 312], 
    '교육철학': [311, 312], 
    '교육학': [221, 222, 311, 312], 
    '교육행정': [221, 222, 311, 312], 
    '네트워크': [111, 116], 
    '논리회로': [111, 113], 
    '데이터베이스': [111, 113, 114, 115, 116, 132, 133, 134], 
    '신경언어학': [211], 
    '심리언어학': [211, 213], 
    '언어병리학': [211], 
    '언어학': [116, 131, 132, 133, 134, 135, 211, 212, 213, 221, 222], 
    '영상처리': [111, 119], 
    '운영체제': [111, 113, 118], 
    '음성학': [132, 133, 135, 211, 212, 213, 221, 222], 
    '의미론': [132, 134, 135, 211, 213, 221, 222], 
    '인공지능': [111, 119, 131, 132, 133, 134, 135], 
    '자료구조': [111, 112, 113, 114, 115, 116, 117, 118, 119, 131, 132, 133, 134, 135], 
    '자바 프로그래밍': [111, 114, 115, 116, 117, 118], 
    '정보검색': [111, 114, 115, 116], 
    '통사론': [132, 134, 135, 211, 212, 213, 221, 222], 
    '파이썬': [111, 112, 113, 117, 118, 119, 131, 132, 133, 134, 135], 
    '파일처리': [111, 112, 113, 114, 115, 116, 117, 118, 132, 133, 134, 135], 
    '표준국어문법': [211, 213, 221, 222], 
    '형태론': [132, 134, 135, 211, 213],
}    

cb_buy_item_by_person_inx_list = {
    'C언어': [0, 1, 2, 3, 4, 5, 6, 7, 13],
    'Window 프로그래밍': [0, 3, 4, 6, 7],
    'iOS 프로그래밍': [0, 3, 6, 7],
    '교육상담': [17, 19],
    '교육심리': [17, 19, 20],
    '교육철학': [19, 20],
    '교육학': [17, 18, 19, 20],
    '교육행정': [17, 18, 19, 20],
    '네트워크': [0, 5],
    '논리회로': [0, 2],
    '데이터베이스': [0, 2, 3, 4, 5, 10, 11, 12],
    '신경언어학': [14],
    '심리언어학': [14, 16],
    '언어병리학': [14],
    '언어학': [5, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18],
    '영상처리': [0, 8],
    '운영체제': [0, 2, 7],
    '음성학': [10, 11, 13, 14, 15, 16, 17, 18],
    '의미론': [10, 12, 13, 14, 16, 17, 18],
    '인공지능': [0, 8, 9, 10, 11, 12, 13],
    '자료구조': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
    '자바 프로그래밍': [0, 3, 4, 5, 6, 7],
    '정보검색': [0, 3, 4, 5],
    '통사론': [10, 12, 13, 14, 15, 16, 17, 18],
    '파이썬': [0, 1, 2, 6, 7, 8, 9, 10, 11, 12, 13],
    '파일처리': [0, 1, 2, 3, 4, 5, 6, 7, 10, 11, 12, 13],
    '표준국어문법': [14, 16, 17, 18],
    '형태론': [10, 12, 13, 14, 16],
}

cb_person_lists_by_item_inx = { # (21)
    '111': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], # (14)
    '112': [0, 1, 2, 3], # (4)
    '113': [0, 1, 2, 3, 4, 5, 6], # (7)
    '114': [0, 2, 3, 6, 10, 11, 12, 13], # (8)
    '115': [0, 2, 3, 6, 10, 11, 13], # (7)
    '116': [0, 2, 3, 6, 8, 10, 14, 13], # (8)
    '117': [0, 1, 2, 3, 11, 12, 13], # (7)
    '118': [0, 1, 2, 3, 4, 11, 12, 13], # (8)
    '119': [1, 2, 7, 9], # (4)
    '131': [1, 2, 7, 14], # (4)
    '132': [1, 2, 3, 6, 7, 14, 15, 16, 17, 18], # (10)
    '133': [1, 2, 3, 6, 7, 14, 17], # (7)
    '134': [1, 2, 3, 6, 7, 14, 15, 16, 18], # (9)
    '135': [0, 1, 2, 3, 7, 14, 15, 16, 17, 18], # (10)
    '211': [14, 15, 16, 17, 18, 19, 20, 21, 22], # (9)
    '212': [14, 16, 17], # (3)
    '213': [14, 15, 16, 17, 18, 19, 20], # (7)
    '221': [14, 16, 17, 18, 19, 23, 24, 25, 26], # (9)
    '222': [14, 16, 17, 18, 19, 23, 24], # (7)
    '311': [23, 24, 25, 26, 27], # (5)
    '312': [23, 24, 25, 27], # (4)
}

# 구매자 별 구매항목 벡터화 => ['C언어',                                                   ,'교육상담']
cb_buy_data_1  = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] # 111
cb_buy_data_2  = [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] # 112
cb_buy_data_3  = [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] # 113
cb_buy_data_4  = [1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] # 114
cb_buy_data_5  = [1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] # 115
cb_buy_data_6  = [1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] # 116
cb_buy_data_7  = [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] # 117
cb_buy_data_8  = [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] # 118
cb_buy_data_9  = [0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] # 119
cb_buy_data_10 = [0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] # 131
cb_buy_data_11 = [0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0] # 132
cb_buy_data_12 = [0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] # 133
cb_buy_data_13 = [0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0] # 134
cb_buy_data_14 = [1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0] # 135
cb_buy_data_15 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0] # 211
cb_buy_data_16 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] # 212
cb_buy_data_17 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0] # 213
cb_buy_data_18 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0] # 221
cb_buy_data_19 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0] # 222
cb_buy_data_20 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1] # 311
cb_buy_data_21 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1] # 312

# 상품 별 구매자(상태) 항목 벡터화 => ['111',                                            ,'312']
cb_sell_data_vecor_1  = [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
cb_sell_data_vecor_2  = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]
cb_sell_data_vecor_3  = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]
cb_sell_data_vecor_4  = [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]
cb_sell_data_vecor_5  = [1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
cb_sell_data_vecor_6  = [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
cb_sell_data_vecor_7  = [1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0]
cb_sell_data_vecor_8  = [1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]
cb_sell_data_vecor_9  = [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
cb_sell_data_vecor_10 = [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
cb_sell_data_vecor_11 = [1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
cb_sell_data_vecor_12 = [1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
cb_sell_data_vecor_13 = [1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
cb_sell_data_vecor_14 = [1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
cb_sell_data_vecor_15 = [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0]
cb_sell_data_vecor_16 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0]
cb_sell_data_vecor_17 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0]
cb_sell_data_vecor_18 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0]
cb_sell_data_vecor_19 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0]
cb_sell_data_vecor_20 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0]
cb_sell_data_vecor_21 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0]
cb_sell_data_vecor_22 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
cb_sell_data_vecor_23 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
cb_sell_data_vecor_24 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1]
cb_sell_data_vecor_25 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1]
cb_sell_data_vecor_26 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1]
cb_sell_data_vecor_27 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0]
cb_sell_data_vecor_28 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1]



#================================
#================================
from unittest import TestCase, main

class HGTest(TestCase):
    def _test_datashow2(self): # 구매 데이터 변환용
        import hgsysinc
        hgsysinc._print_function_name_()

        #
        person_id_list = [item['고객ID'] for item in cb_buydatas]
        buy_lists = [item['구입목록'] for item in cb_buydatas]
        itemlist = []
        for list in buy_lists:
            for item in list:
                if item not in itemlist:
                    itemlist.append(item)
        #
        #------------------
        #------------------
        print(f'person_id_list ({len(person_id_list)}) ', person_id_list)
        print()

        print(f'buy_lists ({len(buy_lists)}):')
        print(*buy_lists, sep='\n')
        print()

        print(f'itemlist ({len(itemlist)}) :', itemlist)
        print()

        #------------------
        # make person dict
        #------------------
        buy_person_id_dict = {}
        for pi, person_id in enumerate(person_id_list):
            buy_person_id_dict[pi+1] = person_id
        print('buy_person_id_dict:', buy_person_id_dict)
        print()

        #------------------
        # make item dict
        #------------------
        person_id_list_by_item_key = {}
        buy_item_by_person_inx_list = {}
        buy_item_dict_by_order = {}
        for i, item in enumerate(itemlist):
            person_id_list_by_item_key[item] = []
            buy_item_by_person_inx_list[item] = []
            buy_item_dict_by_order[i+1] = item
        print('buy_item_dict_by_order:', buy_item_dict_by_order)
        print()
        
        #------------------
        # make 
        #------------------
        for item in itemlist:
            for linx, buylist in enumerate(buy_lists):
                if item in buylist:
                    buy_item_list = person_id_list_by_item_key[item]
                    buy_item_list.append(person_id_list[linx])

                    buy_item_list_by_person_inx = buy_item_by_person_inx_list[item]
                    buy_item_list_by_person_inx.append(linx)
        print('person_id_list_by_item_key:', person_id_list_by_item_key)
        print()
        print('buy_item_by_person_inx_list:', buy_item_by_person_inx_list)
        print()

        person_id_list_by_item_key__s = sorted(person_id_list_by_item_key)
        person_id_list_by_item_key_sort = {}
        for key in person_id_list_by_item_key__s:
            person_id_list_by_item_key_sort[key] = person_id_list_by_item_key[key]
        print('person_id_list_by_item_key_sort:', person_id_list_by_item_key_sort)
        print()
        

        buy_item_by_person_inx_list__s = sorted(buy_item_by_person_inx_list)
        buy_item_by_person_inx_list_sort = {}
        for key in buy_item_by_person_inx_list__s:
            buy_item_by_person_inx_list_sort[key] = buy_item_by_person_inx_list[key]
        print('buy_item_by_person_inx_list_sort:', buy_item_by_person_inx_list_sort)
        print()

        #------------------
        # make 2d-buy-list dict
        #------------------
        list_table = [[]] * len(person_id_list)
        for person in person_id_list:
            person_buy_list = [0 for a in range(0,len(itemlist))]

            #=print('person:', person)
            person_data = []
            for buydata in cb_buydatas:
                if (buydata['고객ID'] == person):
                    person_data = buydata['구입목록']
                    break
            #=print(person_data)
            #=print()
            if(len(person_data) <= 0):
                assert False

            for item_name in person_data:
                #=print(item_name)
                if item_name in itemlist:
                    item_index = itemlist.index(item_name)
                    person_buy_list[item_index] = 1 # 1: 구매

            person_index = person_id_list.index(person)
            list_table[person_index] = person_buy_list

        print()
        print(f'list table({len(list_table)}):', list_table)
        print(f'list table({len(list_table)}):', *list_table, sep='\n')


        #------------------
        # make buy-list dict
        #------------------
        person_lists_by_item_inx = [[]] * len(person_id_list)
        for person in person_id_list:
            person_buy_list = []

            #=print('person:', person)
            person_data = []
            for buydata in cb_buydatas:
                if (buydata['고객ID'] == person):
                    person_data = buydata['구입목록']
                    break
            #=print(person_data)
            #=print()
            if(len(person_data) <= 0):
                assert False

            for item_name in person_data:
                #=print(item_name)
                if item_name in itemlist:
                    item_index = itemlist.index(item_name)
                    person_buy_list.append(item_index)

            person_index = person_id_list.index(person)
            person_lists_by_item_inx[person_index] = person_buy_list

        print()
        print(f'person_lists_by_item_inx({len(person_lists_by_item_inx)}):', person_lists_by_item_inx)

        for pi, plist in enumerate(person_lists_by_item_inx):
            print(f"'{person_id_list[pi]}': {plist}, # ({len(plist)})")

        #=print(f'person_lists_by_item_inx({len(person_lists_by_item_inx)}):', *person_lists_by_item_inx, sep='\n')
        print('index\t', '고객ID\t', '항목수\t', '항목 리스트(항목 inx)')
        for pi, plist in enumerate(person_lists_by_item_inx):
            print(f'{pi}\t{person_id_list[pi]}\t{len(plist)}\t{plist}')


    def _test_covid19(self):
        print('data:', len(covid19_korea_data))
        #=print('date:', len(covid19_date))

        #
        import matplotlib.pyplot as plt

        figsize = (15, 7)
        figsize = (10, 4)

        #=plt.figure(figsize)
        #=plt.scatter(covid19_date, covid19_korea_data)
        #=plt.show()


        #
        plt.figure(figsize=figsize)
        #=plt.plot(covid19_date, covid19_korea_data)
        plt.plot(covid19_korea_data)
        plt.show()


#---------------------
#---------------------
if __name__ == '__main__':
    main()

