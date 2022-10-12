# request & response
from urllib.request import Request, urlopen # https://docs.python.org/ko/3/howto/urllib2.html
#-----
# request & response
#-----
# "First_inauguration_of_George_Washington"
url = "https://en.wikisource.org/wiki/George_Washington%27s_First_Inaugural_Address" # "First_inauguration_of_George_Washington"
req = Request(url)
response = urlopen(req)
#=print(response.status)
if(response.status != 200):
    print('response.status:', response.status)
    exit()
# get web-page-src
responseString = response.read()
print(f'responseString [{len(responseString)}]:', type(responseString)) # bytes:byte-string
#=print(responseString), print()

#-----
# convert & save
#-----
# convert bytes to string
htmlString = responseString.decode('utf-8') # convert bytes to string
print(f'htmlString [{len(htmlString)}]', type(htmlString))
#=print(htmlString), print()

# writing
save_file = "___First_inauguration_of_George_Washington" + '.html'
file = open(save_file, "w", encoding='utf-8')
file.write(htmlString)
file.close()
print('writing:', save_file)


'''
처리 결과:
==================
responseString [45651]: <class 'bytes'>
htmlString [45609] <class 'str'>
writing: ___First_inauguration_of_George_Washington.html

'''

