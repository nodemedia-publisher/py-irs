from dict_base import 훈민정음, 훈민정음보충
# 사전(dict) 처리 예: 확장(list.extend() 비슷)
훈민정음.update(훈민정음보충) # 사전(dict) {key:value} 방식 내용 변경
print("사전(dict) update(dict):", 훈민정음)



'''

처리 결과:
=========================
사전(dict) update(dict): {'제작': '세종대왕', '반포': '1446년', '소장': '간송미술관', '창제': '1443년', '언어': '한글', '사용자': '8천만'}

'''

