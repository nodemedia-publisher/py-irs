import hgsysinc
from hgcrawl import get_filename__Anne_of_Green_Gables
# 빨강 머리 앤
filename1 = get_filename__Anne_of_Green_Gables() # {빨강 머리 앤}의 파일 경로
# 해당 파일이 있는지 검사하여 없으면 다운로드한다.
from pathlib import Path
file_check = Path(filename1)
if ((file_check.is_file() == True) and (file_check.exists() == True)):
        pass
else:
    from hgcrawl import download_gutenberg_Anne_of_Green_Gables
    download_gutenberg_Anne_of_Green_Gables()
#-----
encoding='utf-8' 
#----------
#----------
import hgsysinc
from hgwordlist import GetKeywordList_File
from hgwordlist import GetWordDictList_WordList
from hgwordlist import GetWordDictList_FreqListInfo
from hgwordlist import PrintWordDictListInfo
#----------
#----------
KeywordList = GetKeywordList_File(filename1, encoding=encoding)
#=WordDictList = GetWordDictList_WordList(KeywordList)
WordDictList = GetWordDictList_WordList(KeywordList, LowerCasifyFlag=True) # 대문자를 소문자로 통합
FreqListInfo = GetWordDictList_FreqListInfo(WordDictList)
PrintWordDictListInfo(FreqListInfo)


'''
처리 결과:
==================================

List Num: 224 List Sum: 7598  <=== 대문자를 소문자로 통합 결과
Total Freq: 106775
Len Filter: 0
{'freq': 1, 'count': 3488}
{'freq': 2, 'count': 1248}
{'freq': 3, 'count': 613}
{'freq': 4, 'count': 377}
{'freq': 5, 'count': 238}
{'freq': 6, 'count': 214}
{'freq': 7, 'count': 160}
{'freq': 8, 'count': 118}
{'freq': 9, 'count': 100}
{'freq': 10, 'count': 77}
{'freq': 11, 'count': 72}
{'freq': 12, 'count': 72}
{'freq': 13, 'count': 49}
{'freq': 14, 'count': 44}
{'freq': 15, 'count': 43}
{'freq': 16, 'count': 42}
{'freq': 17, 'count': 30}
{'freq': 18, 'count': 29}
{'freq': 19, 'count': 20}
{'freq': 20, 'count': 26}
{'freq': 21, 'count': 23}
{'freq': 22, 'count': 16}
{'freq': 23, 'count': 11}
{'freq': 24, 'count': 25}
{'freq': 25, 'count': 14}
{'freq': 26, 'count': 12}
{'freq': 27, 'count': 10}
{'freq': 28, 'count': 14}
{'freq': 29, 'count': 11}
{'freq': 30, 'count': 5}
{'freq': 31, 'count': 6}
{'freq': 32, 'count': 9}
{'freq': 33, 'count': 10}
{'freq': 34, 'count': 9}
{'freq': 35, 'count': 4}
{'freq': 36, 'count': 7}
{'freq': 37, 'count': 8}
{'freq': 38, 'count': 1}
{'freq': 39, 'count': 7}
{'freq': 40, 'count': 10}
{'freq': 41, 'count': 8}
{'freq': 42, 'count': 4}
{'freq': 43, 'count': 3}
{'freq': 44, 'count': 9}
{'freq': 45, 'count': 5}
{'freq': 46, 'count': 5}
{'freq': 47, 'count': 3}
{'freq': 48, 'count': 1}
{'freq': 49, 'count': 7}
{'freq': 50, 'count': 7}
{'freq': 51, 'count': 5}
{'freq': 52, 'count': 6}
{'freq': 53, 'count': 2}
{'freq': 54, 'count': 5}
{'freq': 55, 'count': 2}
{'freq': 56, 'count': 2}
{'freq': 57, 'count': 4}
{'freq': 58, 'count': 3}
{'freq': 59, 'count': 1}
{'freq': 60, 'count': 4}
{'freq': 61, 'count': 2}
{'freq': 62, 'count': 4}
{'freq': 63, 'count': 3}
{'freq': 64, 'count': 2}
{'freq': 65, 'count': 5}
{'freq': 66, 'count': 1}
{'freq': 67, 'count': 2}
{'freq': 68, 'count': 3}
{'freq': 69, 'count': 1}
{'freq': 70, 'count': 1}
{'freq': 71, 'count': 4}
{'freq': 72, 'count': 2}
{'freq': 73, 'count': 3}
{'freq': 74, 'count': 4}
{'freq': 75, 'count': 5}
{'freq': 76, 'count': 2}
{'freq': 77, 'count': 3}
{'freq': 78, 'count': 3}
{'freq': 79, 'count': 1}
{'freq': 80, 'count': 2}
{'freq': 81, 'count': 1}
{'freq': 82, 'count': 4}
{'freq': 83, 'count': 1}
{'freq': 86, 'count': 2}
{'freq': 87, 'count': 5}
{'freq': 88, 'count': 2}
{'freq': 89, 'count': 2}
{'freq': 90, 'count': 1}
{'freq': 91, 'count': 3}
{'freq': 92, 'count': 1}
{'freq': 93, 'count': 3}
{'freq': 94, 'count': 1}
{'freq': 95, 'count': 1}
{'freq': 96, 'count': 1}
{'freq': 99, 'count': 3}
{'freq': 100, 'count': 2}
{'freq': 101, 'count': 4}
{'freq': 104, 'count': 2}
{'freq': 106, 'count': 2}
{'freq': 107, 'count': 2}
{'freq': 108, 'count': 1}
{'freq': 109, 'count': 2}
{'freq': 110, 'count': 1}
{'freq': 112, 'count': 1}
{'freq': 113, 'count': 1}
{'freq': 114, 'count': 2}
{'freq': 115, 'count': 1}
{'freq': 116, 'count': 2}
{'freq': 118, 'count': 1}
{'freq': 119, 'count': 2}
{'freq': 120, 'count': 1}
{'freq': 121, 'count': 3}
{'freq': 124, 'count': 1}
{'freq': 125, 'count': 1}
{'freq': 129, 'count': 2}
{'freq': 130, 'count': 1}
{'freq': 132, 'count': 2}
{'freq': 133, 'count': 1}
{'freq': 134, 'count': 2}
{'freq': 136, 'count': 2}
{'freq': 137, 'count': 1}
{'freq': 139, 'count': 1}
{'freq': 140, 'count': 1}
{'freq': 143, 'count': 2}
{'freq': 145, 'count': 1}
{'freq': 146, 'count': 1}
{'freq': 148, 'count': 1}
{'freq': 150, 'count': 1}
{'freq': 153, 'count': 5}
{'freq': 155, 'count': 1}
{'freq': 161, 'count': 1}
{'freq': 163, 'count': 1}
{'freq': 165, 'count': 1}
{'freq': 166, 'count': 1}
{'freq': 168, 'count': 1}
{'freq': 169, 'count': 1}
{'freq': 172, 'count': 1}
{'freq': 173, 'count': 1}
{'freq': 174, 'count': 1}
{'freq': 176, 'count': 1}
{'freq': 177, 'count': 1}
{'freq': 182, 'count': 1}
{'freq': 185, 'count': 1}
{'freq': 200, 'count': 1}
{'freq': 210, 'count': 1}
{'freq': 211, 'count': 1}
{'freq': 216, 'count': 1}
{'freq': 217, 'count': 1}
{'freq': 219, 'count': 1}
{'freq': 220, 'count': 1}
{'freq': 222, 'count': 1}
{'freq': 223, 'count': 1}
{'freq': 226, 'count': 1}
{'freq': 227, 'count': 1}
{'freq': 228, 'count': 1}
{'freq': 230, 'count': 1}
{'freq': 236, 'count': 2}
{'freq': 239, 'count': 1}
{'freq': 245, 'count': 1}
{'freq': 247, 'count': 1}
{'freq': 259, 'count': 2}
{'freq': 270, 'count': 1}
{'freq': 272, 'count': 1}
{'freq': 275, 'count': 1}
{'freq': 279, 'count': 1}
{'freq': 280, 'count': 1}
{'freq': 281, 'count': 2}
{'freq': 285, 'count': 1}
{'freq': 289, 'count': 1}
{'freq': 294, 'count': 1}
{'freq': 295, 'count': 1}
{'freq': 300, 'count': 1}
{'freq': 305, 'count': 1}
{'freq': 309, 'count': 2}
{'freq': 316, 'count': 1}
{'freq': 318, 'count': 1}
{'freq': 319, 'count': 1}
{'freq': 325, 'count': 1}
{'freq': 326, 'count': 1}
{'freq': 332, 'count': 1}
{'freq': 344, 'count': 1}
{'freq': 358, 'count': 1}
{'freq': 362, 'count': 1}
{'freq': 363, 'count': 1}
{'freq': 382, 'count': 1}
{'freq': 397, 'count': 1}
{'freq': 406, 'count': 1}
{'freq': 415, 'count': 1}
{'freq': 441, 'count': 1}
{'freq': 444, 'count': 1}
{'freq': 455, 'count': 1}
{'freq': 457, 'count': 1}
{'freq': 466, 'count': 1}
{'freq': 490, 'count': 1}
{'freq': 535, 'count': 1}
{'freq': 544, 'count': 2}
{'freq': 566, 'count': 1}
{'freq': 577, 'count': 1}
{'freq': 616, 'count': 1}
{'freq': 638, 'count': 1}
{'freq': 640, 'count': 1}
{'freq': 734, 'count': 1}
{'freq': 772, 'count': 1}
{'freq': 790, 'count': 1}
{'freq': 791, 'count': 1}
{'freq': 820, 'count': 1}
{'freq': 849, 'count': 1}
{'freq': 851, 'count': 1}
{'freq': 1151, 'count': 1}
{'freq': 1189, 'count': 1}
{'freq': 1207, 'count': 1}
{'freq': 1315, 'count': 1}
{'freq': 1364, 'count': 1}
{'freq': 1371, 'count': 1}
{'freq': 1479, 'count': 1}
{'freq': 1519, 'count': 1}
{'freq': 1700, 'count': 1}
{'freq': 1914, 'count': 1}
{'freq': 2098, 'count': 1}
{'freq': 2226, 'count': 1}
{'freq': 3042, 'count': 1}
{'freq': 3265, 'count': 1}
{'freq': 3395, 'count': 1}
{'freq': 3925, 'count': 1}

'''
