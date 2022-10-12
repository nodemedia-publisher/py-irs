#-----
# re.findall("[\w]+", string) 방식은 접어(예:can't)를 분리하기 때문에 
# 온전한 접어(예:can't) 형태는 오지 않는 문제가 있다.
# 접어(예:can't)를 처리하기 위해 작은따옴표 {'}를 추가한 
# re.findall("[\w']+", string) 방식으로 처리
#-----
# 토큰 분리: re.findall("[\w']+", string)
import re
# 1. 토큰 분리
text_a2 = """
He can't do it.
I like 'python'.
"""
text_a2 = text_a2.lower() # 대문자를 소문자로 변경
WordList = re.findall("[\w']+", text_a2)
print(WordList)


'''
처리 결과:
==================
['he', "can't", 'do', 'it', 'i', 'like', "'python'"]

'''
