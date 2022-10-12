# Request & BeautifulSoup
from urllib.request import Request, urlopen # https://docs.python.org/ko/3/howto/urllib2.html
from bs4 import BeautifulSoup # https://beautiful-soup-4.readthedocs.io/en/latest/
#-----
# request & response
#-----
# "First_inauguration_of_George_Washington"
url = "https://en.wikisource.org/wiki/George_Washington%27s_First_Inaugural_Address" # "First_inauguration_of_George_Washington"
req = Request(url)
response = urlopen(req)
#=print(response.status)
if(response.status != 200):
    print('response_code:', response.status)
    exit()
#-----
# xml parsing
#-----
soup = BeautifulSoup(response, "lxml")

# go to real speech area
ws_data = soup.find('div', {'id': 'ws-data'}) # <div class="ws-noexport" id="ws-data" 
#=print(ws_data)

# next : real speech area
speech = ""
next_tag = ws_data.find_next('p')
while(next_tag.name == 'p'):
    #=print(next_tag.text)
    speech += next_tag.text
    next_tag = next_tag.find_next()
print('speech:', len(speech))

# writing
save_file = "___First_inauguration_of_George_Washington" + '.txt'
file = open(save_file, "w", encoding='utf-8')
file.write(speech)
file.close()
print('writing:', save_file)


'''
처리 결과:
==================
speech: 8616
writing: ___First_inauguration_of_George_Washington.txt

'''


