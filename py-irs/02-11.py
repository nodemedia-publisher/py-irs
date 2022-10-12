import hgsysinc
from hgtest import load_dictfreq_us_president
#-----------------------------
# 접두사와 접미사 포함 어휘 목록 추출
#-----------------------------
#-----------------------------
#=print('reading texts')
Vocabulary = load_dictfreq_us_president() # 미국 대통령 취임 연설(InaugurationSpeech)
print('Dict Num:', len(Vocabulary))
#=print('Word Num:', sum([Vocabulary[dic] for dic in Vocabulary]))
#=print(Vocabulary)

print('# ㄱ) 접두사 일치 출력')
find = 'inter'
inx = 0
for word in Vocabulary:
    if word.startswith(find):
        inx += 1
        print(inx,':', word)
print(f'prefix [{find}] num:', inx)
print()
print('# ㄴ) 접미사 일치 출력')
find = 'ment'
inx = 0
for word in Vocabulary:
    if word.endswith(find):
        inx += 1
        print(inx,':', word)
print(f'suffix [{find}] num:', inx)



'''
출력 결과:
~.startswith(find)와 ~.endswith(find)의 예제가 필요해서 출력
---------------------------------------
Dict Num: 9110
# ㄱ) 접두사 일치 출력
1 : intercourse
2 : interdependence
3 : interdependent
4 : interest
5 : interested
6 : interesting
7 : interests
8 : interfere
9 : interfered
10 : interference
11 : interfering
12 : interior
13 : interlocked
14 : interlude
15 : intermission
16 : internal
17 : internally
18 : international
19 : internationality
20 : internet
21 : interoceanic
22 : interpose
23 : interposing
24 : interpret
25 : interpretation
26 : interpreted
27 : interpreters
28 : interrupted
29 : interruptions
30 : intersecting
31 : interstate
32 : interval
33 : intervals
34 : intervene
35 : intervened
36 : intervening
37 : intervention
prefix [inter] num: 37

# ㄴ) 접미사 일치 출력
1 : abandonment
2 : accomplishment
3 : achievement
4 : acknowledgment
5 : adjustment
6 : advancement
7 : aggrandizement
8 : agreement
9 : aliment
10 : amendment
11 : appeasement
12 : appointment
13 : arbitrament
14 : argument
15 : armament
16 : arraignment
17 : arrangement
18 : assignment
19 : attachment
20 : attainment
21 : augment
22 : banishment
23 : cement
24 : commencement
25 : commitment
26 : compliment
27 : concernment
28 : contentment
29 : curtailment
30 : debasement
31 : department
32 : detachment
33 : detriment
34 : development
35 : disappointment
36 : disarmament
37 : disbursement
38 : discernment
39 : discouragement
40 : document
41 : element
42 : embarrassment
43 : employment
44 : enactment
45 : encouragement
46 : enforcement
47 : enfranchisement
48 : engagement
49 : enjoyment
50 : enlargement
51 : enrichment
52 : enslavement
53 : entanglement
54 : environment
55 : equipment
56 : establishment
57 : excitement
58 : experiment
59 : extinguishment
60 : firmament
61 : fulfillment
62 : government
63 : impairment
64 : impoverishment
65 : improvement
66 : inducement
67 : instrument
68 : investment
69 : involvement
70 : judgment
71 : management
72 : moment
73 : monument
74 : movement
75 : noninvolvement
76 : ornament
77 : parchment
78 : parliament
79 : payment
80 : postponement
81 : preferment
82 : punishment
83 : readjustment
84 : reestablishment
85 : requirement
86 : resentment
87 : retirement
88 : retrenchment
89 : sentiment
90 : settlement
91 : statement
92 : supergovernment
93 : supplement
94 : testament
95 : torment
96 : treatment
97 : unemployment
suffix [ment] num: 97

'''
