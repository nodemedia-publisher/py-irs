import hgsysinc
from hgcrawl_list import (
    gutenberg_list, president_list,
    Anne_of_Green_Gables, Anne_of_Green_Gables_Address, 
    Alice_Adventures, Alice_Adventures_Address,
)

#-----
#-----
#-----
def get_gutenberg_textbook(UrlAddress, PureText=True):
    #-----------
    # gutenberg porject: https://www.gutenberg.org/
    #-----------
    from urllib.request import Request, urlopen # https://docs.python.org/ko/3/howto/urllib2.html
    from bs4 import BeautifulSoup # https://beautiful-soup-4.readthedocs.io/en/latest/
    #---
    booktext = ''
    #-----
    # request & response
    #-----
    req = Request(UrlAddress)
    response = urlopen(req)
    if(response.status != 200):
        print('response_code:', response.status)
        return booktext
    
    #-----
    # html parsing
    #-----
    soup = BeautifulSoup(response, "html.parser")
    booktext = soup.get_text()
    #=print('text len:', len(booktext))
    #=print(booktext[:1500])
    #
    if(PureText == True):
        booktext_pure = get_gutenberg_pure_text(booktext)
        #=print('pure text len:', len(booktext_pure))
        booktext = booktext_pure
    #
    return booktext
    
def get_gutenberg_pure_text(gutenberg_text):
    # Gutenberg Project 텍스트에서 본문과 관련 없는 정보 영역을 제거한다.
    """
    Gutenberg Project 텍스트에서 본문과 관련 없는 정보 영역을 제거한다.
    ~~~
    ~~~
    type1: *** START OF THE PROJECT GUTENBERG EBOOK ~~~ ***
    type2: *** START OF THIS PROJECT GUTENBERG EBOOK ~~~ ***
    ~~~
    ~~~
    type1: End of the Project Gutenberg EBook   @@@ <=== 순서상 먼저 오는 책이 있다.
    type2: *** END OF THE PROJECT GUTENBERG EBOOK ~~~ ***
    type3: *** END OF THIS PROJECT GUTENBERG EBOOK ~~~ ***
    ~~~
    ~~~
    """
    texts = gutenberg_text.splitlines(keepends=True) # 문단 구분 문자 유지 분리
    pure_text = ""
    find_body = False
    for text in texts:
        # 순수한 책 내용 시작 확인
        if(text.find("START OF THE PROJECT GUTENBERG EBOOK") >= 0): # 시작 부분
            find_body = True
            continue
        if(text.find("START OF THIS PROJECT GUTENBERG EBOOK") >= 0): # 시작 부분
            find_body = True
            continue
        
        # 순수한 책 내용 끝 확인
        if(text.find("End of the Project Gutenberg EBook") >= 0): # 끝 부분
            break # 책 위치 순서 위의 내용이 먼저 위치하는 경우 있음
        if(text.find("END OF THE PROJECT GUTENBERG EBOOK") >= 0): # 끝 부분
            break # 본문을 모두 처리했으므로 종료
        if(text.find("END OF THIS PROJECT GUTENBERG EBOOK") >= 0): # 끝 부분
            break # 본문을 모두 처리했으므로 종료
        #
        if(find_body == True):
            # 미세한 조정
            text_strip = text.strip()
            if(len(text_strip) <= 0):
                continue
            
            # 시작 부분에 내용과 관련 없는 부분을 포함한 것 확인
            if(text_strip.startswith("Produced by") == True):
                continue # 관련 없으므로 다음 문장으로
            
            # 책 본문 합치기
            pure_text += text
    #
    return pure_text

def get_gutenberg_text_folder(printPath=False):
    #-----: {./../ext-src/data/gutenberg/text}
    from pathlib import Path
    import os
    #-----
    filePath = Path(__file__).parent # file-path == os.getcwd()
    parentPath = filePath.parent     # file-path-parent
    #-----
    if(printPath == True):
        print('filePath:', filePath)
        print('parentPath:', parentPath)

    # ext-src folder
    ExtSrcPath = os.path.join(parentPath, 'ext-src')
    #=if(printPath == True):
    #=    print(ExtSrcPath)
    if(os.path.exists(ExtSrcPath) == False):
        os.makedirs(ExtSrcPath)
        if(printPath == True):
            print('make new folder:', ExtSrcPath)
    else:
        if(printPath == True):
            print('exist folder:', ExtSrcPath)

    # dada folder
    DataPath = os.path.join(ExtSrcPath, 'data')
    #=if(printPath == True):
    #=    print(DataPath)
    if(os.path.exists(DataPath) == False):
        os.makedirs(DataPath)
        if(printPath == True):
            print('make new folder:', DataPath)
    else:
        if(printPath == True):
            print('exist folder:', DataPath)

    # gutenberg folder
    GutenbergPath = os.path.join(DataPath, 'gutenberg')
    #=if(printPath == True):
    #=    print(GutenbergPath)
    if(os.path.exists(GutenbergPath) == False):
        os.makedirs(GutenbergPath)
        if(printPath == True):
            print('make new folder:', GutenbergPath)
    else:
        if(printPath == True):
            print('exist folder:', GutenbergPath)

    # text folder
    TextPath = os.path.join(GutenbergPath, 'text')
    #=if(printPath == True):
    #=    print(TextPath)
    if(os.path.exists(TextPath) == False):
        os.makedirs(TextPath)
        if(printPath == True):
            print('make new folder:', TextPath)
    else:
        if(printPath == True):
            print('exist folder:', TextPath)
    #---
    # pc 윈도우에서 (제목에 'u'문자로 시작하는 경우) 제목을 파일명과 합쳐서 코멘트에 남겨두면 
    # 다시 실행할 {/U} 제어 문자로 인식해서 오류가 발생한다.
    # 이를 방지하기 위해 폴더 구분 문자('\\')를 '/'문자로 변경
    #---
    TextPath = TextPath.replace("\\", "/")
    #---
    return TextPath

def download_gutenberg_text(gutenberg_url, file_title, down_pathname="", PureText=True):
    # download
    booktext = get_gutenberg_textbook(gutenberg_url, PureText=PureText)

    # {title}을 파일 이름에 적합하도록 변경
    from hgbasic import get_filename_from_title
    filename = get_filename_from_title(file_title)
    
    # filename
    guten_file = filename + '.txt'
    if (down_pathname != ""):
        import os
        save_file = os.path.join(down_pathname, guten_file)
    else:
        save_file = guten_file
    #---
    # pc 윈도우에서 (제목에 'u'문자로 시작하는 경우) 제목을 파일명과 합쳐서 코멘트에 남겨두면 
    # 다시 실행할 {/U} 제어 문자로 인식해서 오류가 발생한다.
    # 이를 방지하기 위해 폴더 구분 문자('\\')를 '/'문자로 변경
    #---
    save_file = save_file.replace("\\", "/")
    #
    print(f'[{len(booktext)}]:', save_file)

    # writing
    file = open(save_file, "w", encoding='utf-8')
    file.write(booktext)
    file.close()

def download_gutenberg_Alice_Adventures():
    # {이상한 나라의 앨리스} 텍스트 다운로드
    gutenberg_url = Alice_Adventures_Address
    file_title = Alice_Adventures
    guten_pathname = get_gutenberg_text_folder()
    download_gutenberg_text(gutenberg_url, file_title, 
            down_pathname=guten_pathname, PureText=True)

def download_gutenberg_Anne_of_Green_Gables():
    # {빨강 머리 앤} 텍스트 다운로드
    gutenberg_url = Anne_of_Green_Gables_Address
    file_title = Anne_of_Green_Gables
    guten_pathname = get_gutenberg_text_folder()
    download_gutenberg_text(gutenberg_url, file_title, 
            down_pathname=guten_pathname, PureText=True)
    
def get_filename__Alice_Adventures():
    # {이상한 나라의 앨리스}의 파일 경로
    import os
    from hgbasic import get_filename_from_title
    # 이상한 나라의 앨리스
    gutenberg_path = get_gutenberg_text_folder()
    work_file = get_filename_from_title(Alice_Adventures) # 이상한 나라의 앨리스
    txt_file = work_file + ".txt"
    real_file = os.path.join(gutenberg_path, txt_file)
    #
    return real_file

def get_filename__Anne_of_Green_Gables():
    # {빨강 머리 앤}의 파일 경로
    import os
    from hgbasic import get_filename_from_title
    # 빨강 머리 앤
    gutenberg_path = get_gutenberg_text_folder()
    work_file = get_filename_from_title(Anne_of_Green_Gables) # 빨강 머리 앤
    txt_file = work_file + ".txt"
    real_file = os.path.join(gutenberg_path, txt_file)
    #
    return real_file

#-----
#-----
#-----
def get_inauguration(UrlAddress, debugPrint=False):
    #-----------
    #  https://en.wikipedia.org/wiki/United_States_presidential_inauguration
    #-----------
    from urllib.request import Request, urlopen # https://docs.python.org/ko/3/howto/urllib2.html
    from bs4 import BeautifulSoup # https://beautiful-soup-4.readthedocs.io/en/latest/
    #---
    speechtext = ''
    #-----
    # request & response
    #-----
    req = Request(UrlAddress)
    response = urlopen(req)
    #=print(response.status)
    if(response.status != 200):
        print('response_code:', response.status)
        #=exit()
        return speechtext
    
    #-----
    # xml parsing
    #-----
    soup = BeautifulSoup(response, "lxml")
    #=content = soup.find('div', {'id': 'content'})
    #=content = soup.find('div', {'id': 'mw-content-text'})
    #=print(content)

    #-----
    # 본문 중간에 있는 삽입 내용은 추출에 방행되므로 제거
    #-----
    # {2009, "Barack Obama"} <div class="thumb tleft">
    # {1861, "Abraham Lincoln"} <div class="thumb tright">
    # {1861, "Abraham Lincoln"} <div class="tiInherit" ~
    # {1861, "Abraham Lincoln"} <div class="__nop wst-nop"> html src에서는 <div class="&#95;_nop wst-nop"> 이다.
    #-----
    while(True):
        find = soup.find('div', {'class': 'thumb tleft'})
        if(find is not None): # {2009, "Barack Obama"} <div class="thumb tleft">
            find.extract()
        else:
            break
    #-----
    while(True):
        find = soup.find('div', {'class': 'thumb tright'})
        if(find is not None): # {1861, "Abraham Lincoln"} <div class="thumb tright">
            find.extract()
        else:
            break
    #-----
    while(True):
        find = soup.find('div', {'class': 'tiInherit'})
        if(find is not None): # {1861, "Abraham Lincoln"} <div class="tiInherit" ~
            find.extract()
        else:
            break
    #-----
    while(True):
        find = soup.find('div', {'class': '__nop wst-nop'})
        if(find is not None): # {1861, "Abraham Lincoln"} <div class="__nop wst-nop">
            find.extract()
        else:
            break

    #-----
    # 연설 내용으로 이동
    #-----
    ws_data = soup.find('div', {'id': 'ws-data'})
    #=print(ws_data)

    # real speech area
    next_tag = ws_data.find_next('p')
    while(True):
        if((next_tag.name == 'p') or
            (next_tag.name == 'br')): # ex: <p><br />
            #=print(next_tag.text)
            speechtext += next_tag.text
        elif(next_tag.name == 'a'): # 본문 중간 무시 태그 <a href= >
            pass
        elif(next_tag.name == 'span'): # 본문 중간 무시 태그 <span id="Money"></span>
            pass
        elif(next_tag.name == 'sup'): # 본문 중간 무시 태그 <sup id="cite_ref-1" >
            pass
        elif(next_tag.name == 'i'): # 본문 중간 무시 태그 <i>
            pass        
        elif(next_tag.name == 'dl'): # 본문 중간 무시 태그 <dl>
            pass        
        elif(next_tag.name == 'dd'): # <dl>에 텍스트가 있는 경우가 있음
            #=print(next_tag.text)
            speechtext += next_tag.text
        # 
        else: # 취임사 텍스트가 아니면 루프 탈출
            break
        # next
        next_tag = next_tag.find_next()
    #
    if(debugPrint == True):
        print(f'escape tag [{len(next_tag.name)}]:', next_tag.name)
        print(next_tag)
    #
    return speechtext

def get_inauguration_text_folder():
    #-----: {./../ext-src/data/inauguration/text}
    from pathlib import Path
    import os
    #-----
    filePath = Path(__file__).parent # file-path == os.getcwd()
    parentPath = filePath.parent     # file-path-parent
    #-----
    print('filePath:', filePath)
    print('parentPath:', parentPath)

    # ext-src folder
    ExtSrcPath = os.path.join(parentPath, 'ext-src')
    #=print(ExtSrcPath)
    if(os.path.exists(ExtSrcPath) == False):
        os.makedirs(ExtSrcPath)
        print('make new folder:', ExtSrcPath)
    else:
        print('exist folder:', ExtSrcPath)

    # dada folder
    DataPath = os.path.join(ExtSrcPath, 'data')
    #=print(DataPath)
    if(os.path.exists(DataPath) == False):
        os.makedirs(DataPath)
        print('make new folder:', DataPath)
    else:
        print('exist folder:', DataPath)

    # inauguration folder
    InaugurationPath = os.path.join(DataPath, 'inauguration')
    #=print(InaugurationPath)
    if(os.path.exists(InaugurationPath) == False):
        os.makedirs(InaugurationPath)
        print('make new folder:', InaugurationPath)
    else:
        print('exist folder:', InaugurationPath)

    # text folder
    TextPath = os.path.join(InaugurationPath, 'text')
    #=print(TextPath)
    if(os.path.exists(TextPath) == False):
        os.makedirs(TextPath)
        print('make new folder:', TextPath)
    else:
        print('exist folder:', TextPath)
    
    #---
    # pc 윈도우에서 (제목에 'u'문자로 시작하는 경우) 제목을 파일명과 합쳐서 코멘트에 남겨두면 
    # 다시 실행할 {/U} 제어 문자로 인식해서 오류가 발생한다.
    # 이를 방지하기 위해 폴더 구분 문자('\\')를 '/'문자로 변경
    #---
    TextPath = TextPath.replace("\\", "/")
    #---
    return TextPath

def download_inauguration_text(inauguration_url, file_title, down_pathname="", debugPrint=False):
    # download
    speech = get_inauguration(inauguration_url, debugPrint=debugPrint)

    # {title}을 파일 이름에 적합하도록 변경
    from hgbasic import get_filename_from_title
    filename = get_filename_from_title(file_title)
    
    # filename
    path_file = filename + '.txt'
    if (down_pathname != ""):
        import os
        save_file = os.path.join(down_pathname, path_file)
    else:
        save_file = path_file
    #---
    # pc 윈도우에서 (제목에 'u'문자로 시작하는 경우) 제목을 파일명과 합쳐서 코멘트에 남겨두면 
    # 다시 실행할 {/U} 제어 문자로 인식해서 오류가 발생한다.
    # 이를 방지하기 위해 폴더 구분 문자('\\')를 '/'문자로 변경
    #---
    save_file = save_file.replace("\\", "/")
    #
    print(f'[{len(speech)}]:', save_file)

    # writing
    file = open(save_file, "w", encoding='utf-8')
    file.write(speech)
    file.close()

#================================
#================================
#================================
from unittest import TestCase, main

class HGTest(TestCase):
    #================================
    #================================
    #================================
    def _test_1(self):
        gutenberg_list.sort()
        print('gutenberg_list:', len(gutenberg_list))
        print(*gutenberg_list, sep='\n')
        '''
        '''

if __name__ == '__main__':
    main()





