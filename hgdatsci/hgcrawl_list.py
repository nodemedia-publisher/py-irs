import hgsysinc

#---
Anne_of_Green_Gables = "Anne of Green Gables" # 빨강 머리 앤
Anne_of_Green_Gables_Address = 'https://www.gutenberg.org/cache/epub/45/pg45.txt'
Alice_Adventures = "Alice’s Adventures" # 이상한 나라의 앨리스
Alice_Adventures_Address = 'https://www.gutenberg.org/files/11/11-0.txt'

gutenberg_list = [ # format: [(작품명, 주소),...]
    #-----------
    # gutenberg porject: https://www.gutenberg.org/
    #-----------
    (Alice_Adventures, Alice_Adventures_Address),
    (Anne_of_Green_Gables, Anne_of_Green_Gables_Address),
]

president_list = [ # format: [(order, year, president, address),...]
    #-----------
    # https://en.wikipedia.org/wiki/United_States_presidential_inauguration
    #-----------
    #==========================
    #= 60개가 있지만 트럼프까지 59개 문서만 처리, 순서(order)는 {01, 02, ~}로 저장해야 wild-card(*)로 파일 읽을 때 순서가 일치
    #= 47대 대통령 취임사는 "Gerald Ford"(1974년)를 포함하여 2개이다.
    #==========================
    ("01", 1789, "First inauguration of George Washington", "https://en.wikisource.org/wiki/George_Washington%27s_First_Inaugural_Address"),
    #==========
]

#-----
#-----
#-----




