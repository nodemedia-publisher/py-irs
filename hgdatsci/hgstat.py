#---
#---
import hgsysinc
#-----------------------------
#-----------------------------
def hgAvg_low(datalist):
    sum_val = 0
    for val in datalist:
        sum_val += val
    #=print(sum_val)

    avg_val = sum_val / len(datalist)
    #=print(avg_val) 

    return avg_val

def hgAvg(datalist):
    #=print(sum(datalist))
    avg_val = sum(datalist) / len(datalist)
    #=print(avg_val) 
    return avg_val

def hgAvgTable2D(Table2D):
    ''' 2차원 리스트(Table2D)에 대한 평균 구하기
    결과는 1차원 리스트    
    === Pandas.DataFrame().mean()
    '''
    #=print('Table2D:', Table2D)
    table2d_trans = hgTranspose_Lists(Table2D)
    #=print('table2d_trans:', table2d_trans)
    
    AvgList = [hgAvg(table_i) for table_i in table2d_trans]
    #=print(AvgList) 
    return AvgList

def hgGeoAvg(datalist): # geometric mean
    mul_val = 1
    for val in datalist:
        mul_val *= val
    #=print(mul_val)

    geoAvg = mul_val ** (1/len(datalist)) # **: 제곱 연산자
    #=geoAvg = pow(mul_val, (1/len(datalist))) # pow: 제곱 함수
    
    #=print(geoAvg) 

    return geoAvg

def hgCenteringTable2D(Table2D, PrintAvg=False):
    ''' 2차원 리스트(Table2D)에 대한 평균값을 빼서 중심화한다.
    '''
    #=print('Table2D:', Table2D)

    Table2D_Avg = hgAvgTable2D(Table2D) # 2차원 리스트의 평균 구하기
    if(PrintAvg == True):
        from numpy import round as np_round
        print('Table2D_Avg:')
        print(np_round(Table2D_Avg, 6))  # 보기 좋게 6자리까지만
        print(Table2D_Avg[0:5])
    #---
    #=Table2D_Avg = numpy.array(Table2D_Avg)
    #---
    Table2D_Center = Table2D - Table2D_Avg
    #=print('Table2D_Center:', Table2D_Center)
    return Table2D_Center

def hgTss_low(datalist): # 총변동: Total Sum of Squares
    dataNum = len(datalist)
    if(dataNum <= 0):
        assert False, '(dataNum <= 0)'
        return 0

    Avg = hgAvg(datalist)
    calc_val = 0 
    for val in datalist: 
        calc_val += (val - Avg)**2
    return calc_val

def hgVar_low(datalist, sampleMode=False): # variance
    dataNum = len(datalist)
    if(sampleMode == True): # 표본 표준 편차(sample standard deviation)
        dataNum -= 1
    if(dataNum <= 0):
        assert False, '(dataNum <= 0)'
        return 0
    #---1
    Avg = hgAvg(datalist)
    calc_val = 0 
    for val in datalist: 
        calc_val += (val - Avg)**2
    #---2
    #=calc_val = hgTss_low(datalist)
    #---
    calc_val /= dataNum
    return calc_val

def hgStd_low(datalist, sampleMode=False): # standard deviation
    dataNum = len(datalist)
    if(sampleMode == True): # 표본 표준 편차(sample standard deviation)
        dataNum -= 1
    if(dataNum <= 0):
        assert False, '(dataNum <= 0)'
        return 0

    ret_var = hgVar_low(datalist, sampleMode)
    ret_std = ret_var ** 0.5 # 제곱근
    return ret_std

def hgStat_low(datalist, sampleMode=False): # 
    dataNum = len(datalist)
    if(sampleMode == True): # 표본 표준 편차(sample standard deviation)
        dataNum -= 1
    if(dataNum <= 0):
        assert False, '(dataNum <= 0)'
        return 0

    Avg = hgAvg(datalist)
    calc_val = 0 
    for val in datalist: 
        calc_val += (val - Avg)**2
    calc_val /= dataNum
    ret_std = calc_val ** 0.5
    return Avg, ret_std

def hgCovariance_low(datalist1, datalist2): # Covariance
    dataNum = len(datalist1)
    if(dataNum <= 0):
        assert False, '(dataNum <= 0)'
        return 0
    if(dataNum != len(datalist2)):
        assert False, '(dataNum != len(datalist2))'
        return 0

    Avg1 = hgAvg(datalist1)
    Avg2 = hgAvg(datalist2)
    calc_val = 0 
    for i in range(0, dataNum): 
        val1 = datalist1[i]
        val2 = datalist2[i]
        calc_val += (val1 - Avg1) * (val2 - Avg2)
    ret_cov = calc_val / (dataNum - 1)
    return ret_cov

def hgCoefficient_low(datalist1, datalist2, debugPrint=False): # Correlation coefficient(Pearsons correlation)
    dataNum = len(datalist1)
    if(dataNum != len(datalist2)):
        assert False, '(dataNum != len(datalist2))'
        return 0
    #---
    Avg1 = hgAvg(datalist1)
    Avg2 = hgAvg(datalist2)
    if(debugPrint == True):
        print('Avg1: %.3f' %Avg1)
        print('Avg2: %.3f' %Avg2)
        
        # caption
        print(' ', end='\t')
        print('val1', end='\t')
        print('val2', end='\t')
        print('(val1 - Avg1)', end='\t')
        print('(val2 - Avg2)', end='\t')
        print('(val1 - Avg1)**2', end='\t')
        print('(val2 - Avg2)**2', end='\t')
        print('(val1 - Avg1) * (val2 - Avg2)')
    #---
    calc_bunja = 0 
    dif2_1 = 0
    dif2_2 = 0
    for i in range(0, dataNum): 
        val1 = datalist1[i]
        val2 = datalist2[i]

        dif2_1 += (val1 - Avg1)**2
        dif2_2 += (val2 - Avg2)**2

        bunja = (val1 - Avg1) * (val2 - Avg2)
        calc_bunja += bunja

        if(debugPrint == True):
            print(f'{i}', end='\t')
            print(f'{val1}', end='\t')
            print(f'{val2}', end='\t')
            print(f'%.1f' % (val1 - Avg1), end='\t')
            print(f'%.1f' % (val2 - Avg2), end='\t')
            print(f'%.1f' % ((val1 - Avg1)**2), end='\t')
            print(f'%.1f' % ((val2 - Avg2)**2), end='\t')
            print(f'%.1f' % bunja)
    #---
    calc_bunmo = dif2_1 * dif2_2
    sqrt_bunmo = (calc_bunmo**0.5) # square-root
    if(debugPrint == True):
        print('bunja:%.3f' %calc_bunja)
        print('sum((val1 - Avg1)**2):%.3f' % dif2_1)
        print('sum((val2 - Avg2)**2):%.3f' % dif2_2)
        print('bunmo:%.3f' %calc_bunmo)
        print('sqrt bunmo:%.3f' %sqrt_bunmo)
    #---
    if(sqrt_bunmo == 0):
        coefficient = 0;
    else:
        coefficient = calc_bunja / sqrt_bunmo
    return coefficient

def hgCoefficient_dict(dict1, dict2, datanum, debugPrint=False): 
    # Correlation coefficient(Pearsons correlation)
    dictsum1 = sum(dict1.values())
    dictsum2 = sum(dict2.values())

    Avg1 = dictsum1 / datanum
    Avg2 = dictsum2 / datanum
    if(debugPrint == True):
        print('Avg1: %.3f' %Avg1)
        print('Avg2: %.3f' %Avg2)
        
        # caption
        print(' ', end='\t')
        print('val1', end='\t')
        print('val2', end='\t')
        print('(val1 - Avg1)', end='\t')
        print('(val2 - Avg2)', end='\t')
        print('(val1 - Avg1)**2', end='\t')
        print('(val2 - Avg2)**2', end='\t')
        print('(val1 - Avg1) * (val2 - Avg2)')

    # 값이 있는 항목을 모은다.
    keylist = list(dict1.keys())
    for key in dict2.keys():
        if key not in keylist:
            keylist.append(key)
    keynum = len(keylist)
    if(debugPrint == True):
        print('keynum: {keynum}')

    # 값이 있는 항목을 먼저 계산한다.
    calc_bunja = 0 
    dif2_1 = 0
    dif2_2 = 0
    for i, key in enumerate(keylist):
        if(key not in dict1):
            val1 = 0
        else:
            val1 = dict1[key]
        if(key not in dict2):
            val2 = 0
        else:
            val2 = dict2[key]
        
        #
        dif2_1 += (val1 - Avg1)**2
        dif2_2 += (val2 - Avg2)**2

        bunja = (val1 - Avg1) * (val2 - Avg2)
        calc_bunja += bunja

        if(debugPrint == True):
            print(f'{i}', end='\t')
            print(f'{val1}', end='\t')
            print(f'{val2}', end='\t')
            print(f'%.1f' % (val1 - Avg1), end='\t')
            print(f'%.1f' % (val2 - Avg2), end='\t')
            print(f'%.1f' % ((val1 - Avg1)**2), end='\t')
            print(f'%.1f' % ((val2 - Avg2)**2), end='\t')
            print(f'%.1f' % bunja)

    # 값이 없어서 계산하지 않은 나머지 항목 추가 연산
    emptyNum = datanum - keynum
    if(emptyNum > 0):
        val1 = 0
        val2 = 0
        '''
        for i in range(0, emptyNum):
            #
            dif2_1 += (val1 - Avg1)**2
            dif2_2 += (val2 - Avg2)**2

            bunja = (val1 - Avg1) * (val2 - Avg2)
            calc_bunja += bunja

            if(debugPrint == True):
                print(f'{i}', end='\t')
                print(f'{val1}', end='\t')
                print(f'{val2}', end='\t')
                print(f'%.1f' % (val1 - Avg1), end='\t')
                print(f'%.1f' % (val2 - Avg2), end='\t')
                print(f'%.1f' % ((val1 - Avg1)**2), end='\t')
                print(f'%.1f' % ((val2 - Avg2)**2), end='\t')
                print(f'%.1f' % bunja)
        '''
        #
        dif2_1 += ((val1 - Avg1)**2) * emptyNum
        dif2_2 += ((val2 - Avg2)**2) * emptyNum

        bunja = ((val1 - Avg1) * (val2 - Avg2)) * emptyNum
        calc_bunja += bunja

    #
    calc_bunmo = dif2_1 * dif2_2
    sqrt_bunmo = (calc_bunmo**0.5)
    if(debugPrint == True):
        print('bunja:%.3f' %calc_bunja)
        print('sum((val1 - Avg1)**2):%.3f' % dif2_1)
        print('sum((val2 - Avg2)**2):%.3f' % dif2_2)
        print('bunmo:%.3f' %calc_bunmo)
        print('sqrt bunmo:%.3f' %sqrt_bunmo)
    #
    if(sqrt_bunmo == 0):
        coefficient = 0;
    else:
        coefficient = calc_bunja / sqrt_bunmo
    return coefficient

def hgLinearRegression(datalist1, datalist2):
    dataNum = len(datalist1)
    if(dataNum <= 0):
        assert False, '(dataNum <= 0)'
        return 0
    if(dataNum != len(datalist2)):
        assert False, '(dataNum != len(datalist2))'
        return 0

    SSxx = hgTss_low(datalist1)

    Avg1 = hgAvg(datalist1)
    Avg2 = hgAvg(datalist2)
    SSxy = 0 
    for i in range(0, dataNum): 
        val1 = datalist1[i]
        val2 = datalist2[i]
        SSxy += (val1 - Avg1) * (val2 - Avg2)
    if(SSxx == 0):
        slope = float('NaN') # NaN
    else:
        slope = SSxy / SSxx
    spare = Avg2 - (slope * Avg1)
    return slope, spare, Avg1, Avg2

def hgTranspose_Lists(datalists, debug=False): 
    '''# 2차원 목록(Matrix2D)에서 행과 열을 전치시킨다.'''
    #
    Matrix2D = []

    #
    listNum = len(datalists)
    if(listNum <= 0):
        #=assert False, '(listNum <= 0)'
        return Matrix2D
    #
    item_num = len(datalists[0])
    for item_c in range(0, item_num):
        row_list = []
        for list1 in datalists:
            #----- 아래 for-loop는 매우 느리다.
            #=for j, x in enumerate(list1):
            #=    if(item_c == j):
            #=        row_list.append(x)
            #-----
            x = list1[item_c]
            row_list.append(x)
        if(len(row_list) > 0):
            Matrix2D.append(row_list)

    if(debug == True):
        print(f'{len(Matrix2D)}:')
        print(*Matrix2D, sep='\n')
    #
    return Matrix2D

def hgMatrix2D__DataFrame(DataFrame, debug=False): 
    '''# {pandas.DataFrame}을 {Matrix2D}로 변환한다.
    '''
    # 
    Matrix2D = []
    row_num = DataFrame.shape[0]
    col_num = DataFrame.shape[1]
    for ri in range(row_num):
        if((debug == True) and (ri < 1)): # 첫 번째 1개만 출력해본다
            print(DataFrame.iloc[ri]), print()
        #
        datalist = []
        for ci in range(col_num):
            datalist.append(DataFrame.iloc[ri,ci])
        #
        Matrix2D.append(datalist)
    #
    return Matrix2D

def _hgRows_Lists_(datalists, debug=False): 
    '''# 2차원 목록(Matrix2D)에서 행과 열을 전치시킨다.'''
    # _hgRows_Lists_ 함수는 사용하지 않는다.
    #
    row_lists = hgTranspose_Lists(datalists, debug=debug)
    return row_lists

def _hgRows_DataFrame_(DataFrame, debug=False): 
    '''# {pandas..DataFrame}을 {Matrix2D}로 변환한다.
    '''
    # _hgRows_DataFrame_() 함수는 사용하지 않는다.
    # 참고용으로 남겨둔 것이며, 나중에 지워도 된다.
    datalists = hgMatrix2D__DataFrame(DataFrame, debug=debug)
    return datalists

def hgAnova_List(datalist1, datalist2, debug=False): # 분산 분석(analysis of variance: ANOVA)
    # var-check
    dataNum = len(datalist1)
    if(dataNum <= 0):
        assert False, '(dataNum <= 0)'
        return 0
    if(dataNum != len(datalist2)):
        assert False, '(dataNum != len(datalist2))'
        return 0
    #
    slope, spare, avg1, avg2 = hgLinearRegression(datalist1, datalist2)
    if(debug==True):
        print('slope:', slope, 'spare:', spare)
        print('avg1:', avg1, 'avg2:', avg2)
    #    
    SSR = 0 # 회귀제곱합(SSR: Resgression Sum of Squares)
    SSE = 0 # 오차제곱합(SSE: Sum of Squares Error)
    TSS = 0 # 총변동(Total Sum of Squares)
    for i in range(0, dataNum): 
        val1 = datalist1[i]
        val2 = datalist2[i]
        yi_val = (slope * val1) + spare
        
        # debug
        if(debug==True):
            yi__ymean = (yi_val - avg2)
            yi__ymean__2 = (yi_val - avg2)**2
            print('va1:', val1, 'va2:', val2, 'yi_val:', yi_val, 'yi__ymean:', yi__ymean, 'yi__ymean__2:', yi__ymean__2)
        
        #
        SSR += (yi_val - avg2)**2
        SSE += (val2 - yi_val)**2
        TSS += (val2 - avg2)**2
    if(debug==True):
        print('회귀제곱합(SSR):', SSR, '오차제곱합(SSE):', SSE, '총변동(TSS):', TSS)

    # 결정계수: coefficient of determination, R**2(R-squared)
    if(TSS == 0):
        R2 = float('NaN') # NaN
    else:
        R2 = SSR / TSS
    if(debug==True):
        print('결정계수(R2):', R2)

    # 상관계수: correlation coefficient
    r_value = R2**0.5
    if(slope < 0):
        r_value = -r_value # 음수로 전환
    if(debug==True):
        print('상관계수(r):', r_value)
    
    #
    return r_value, R2, TSS, SSE, SSR, slope, spare, avg1, avg2

def hgRValue_Lists(baselist, datalists, debugPrint=False, ProcMod=0):
    #
    rvalue_list = []

    # var-check
    dataNum = len(baselist)
    if(dataNum <= 0):
        #=assert False, '(dataNum <= 0)'
        return rvalue_list
    #
    listNum = len(datalists)
    if(listNum <= 0):
        #=assert False, '(listNum <= 0)'
        return rvalue_list
    #
    for inx, list_c in enumerate(datalists): 
        if(dataNum != len(list_c)):
            #=assert False, '(dataNum != len(list1))'
            if(debugPrint==True):
                print("error-debug: (dataNum != len(list1))")
            rvalue_list = [] # init
            return rvalue_list
        #--------
        # hgAnova_List() code
        #--------
        #=# format:
        #=# r_value, R2, TSS, SSE, SSR, slope, spare, avg1, avg2 = hgAnova_List(baselist, list1)
        #=#--------
        #=anova = hgAnova_List(baselist, list1)
        #=r_value = anova[0] # r_value
        #--------
        #--------
        r_value = hgCoefficient_low(baselist, list_c)
        if(debugPrint==True):
            #=print('anova:', anova)
            print(f'({inx}) 상관계수(r): %.4f' % r_value)
        #
        rvalue_list.append((inx, r_value)) # format: (index, r-value)
        
        # 진행 상태 출력
        if(ProcMod > 0):
            modval = inx % ProcMod
            if(modval == 0):
                perval = (inx / listNum) * 100
                print('... %.2f' % perval)
    # 정렬: rvalue_list format [(inx, r_value),...]
    rvalue_list.sort(key=lambda r: -r[1]) # 튜플 2번째 값(r-value), 큰 값 순서로 정렬
    #
    return rvalue_list

def hgRValueLists_Lists(datalists, SortFlag=False, debugPrint=False):
    #
    RValueLists = []
    for i, baselist in enumerate(datalists): 
        dataNum = len(baselist)
        if(dataNum <= 0):
            #=assert False, '(dataNum <= 0)'
            return None
        #
        RValueList_Cur = []
        for j, complist in enumerate(datalists): 
            if(i == j): # 자기 자신은 계산할 필요가 없다.
                pass
            else:
                if(dataNum != len(complist)):
                    #=assert False, '(dataNum != len(list1))'
                    if(debugPrint==True):
                        print("error-debug: (dataNum != len(list1))")
                    return None
                #--------
                # hgAnova_List() code
                #--------
                #=# format:
                #=# r_value, R2, TSS, SSE, SSR, slope, spare, avg1, avg2 = hgAnova_List(baselist, list1)
                #=#--------
                #=anova = hgAnova_List(baselist, list1)
                #=r_value = anova[0] # r_value
                #--------
                #--------
                r_value = hgCoefficient_low(baselist, complist)
                if(debugPrint==True):
                    #=print('anova:', anova)
                    print(f'({i}:{j}) 상관계수(r): %.4f' % r_value)
                #
                RValueList_Cur.append((j, r_value)) # (index, r-value)
        #
        if(SortFlag == True):
            RValueList_Cur.sort(key=lambda r : -r[1]) # 높은 값을 기준으로 정렬
        # 현재 고객에 대한 상관계수 목록을 전체 결과 목록에 추가
        RValueLists.append(RValueList_Cur)
    #
    return RValueLists

def hgRValueTable2D_Lists(datalists, debug=False):
    #
    RValueTable = []

    #
    listNum = len(datalists)
    if(listNum <= 0):
        #=assert False, '(listNum <= 0)'
        return None

    for i in range(0, listNum): 
        baselist = datalists[i]
        dataNum = len(baselist)
        if(dataNum <= 0):
            #=assert False, '(dataNum <= 0)'
            return None
        #
        AnovaList = []
        for j in range(0, listNum): 
            if(i == j): # 자기 자신
                r_value = 1
            else:
                list1 = datalists[j]
                if(dataNum != len(list1)):
                    #=assert False, '(dataNum != len(list1))'
                    if(debug==True):
                        print("error-debug: (dataNum != len(list1))")
                    return None
                #--------
                # hgAnova_List() code
                #--------
                #=# format:
                #=# r_value, R2, TSS, SSE, SSR, slope, spare, avg1, avg2 = hgAnova_List(baselist, list1)
                #=#--------
                #=anova = hgAnova_List(baselist, list1)
                #=r_value = anova[0] # r_value
                #--------
                #--------
                r_value = hgCoefficient_low(baselist, list1)
                if(debug==True):
                    #=print('anova:', anova)
                    print(f'({i}:{j}) 상관계수(r): %.4f' % r_value)
            #
            AnovaList.append(r_value)
        #
        RValueTable.append(AnovaList)
    #
    return RValueTable

def hgRValueDataFrame_Lists(datalists, debug=False):
    #
    listNum = len(datalists)
    if(listNum <= 0):
        #=assert False, '(listNum <= 0)'
        return None

    for i in range(0, listNum): 
        baselist = datalists[i]
        dataNum = len(baselist)
        if(dataNum <= 0):
            #=assert False, '(dataNum <= 0)'
            return None
    #
    import pandas as pd
    
    #
    df = pd.DataFrame(datalists).T
    RValueDataFrame = df.corr(method='pearson')

    return RValueDataFrame

def hgNonZeroCount(list):
    #=item_num = [int(x != 0) for x in list].count(1) # '0'의 아닌 것(1)의 개수
    non_zero_item_num = 0
    for x in list:
        if x != 0:
            non_zero_item_num += 1
    #=print(f'{i} ({non_zero_item_num}):', list)
    return non_zero_item_num

def get_milion_value(value):
    milion_value = value / 1000000 # 백만분의 1
    #=print('milion_value:', milion_value)
    #=print('milion_value: %.1f' % milion_value) # format print
    return milion_value

def get_histo_avg(values, counts, title=None, debugPrint=False):
    each_x_freq_sum = 0
    data_sum = 0
    for i in range(len(counts)):
        data_sum += counts[i]
        each_val = counts[i] * values[i]
        each_x_freq_sum += each_val
        if(debugPrint == True):
            print(f'c_x_v: {each_val}, counts[{i}] * values[{i}]:', counts[i], '*', values[i])
    if(data_sum == 0):
        data_avg = 0
    else:
        data_avg = each_x_freq_sum / data_sum

    if(title != None):
        print(f'{title} >> ', end='')
    if(debugPrint == True):
        print(f'data_sum {len(counts)}:', data_sum)
        print('each_x_freq_sum:', each_x_freq_sum)
        print('data_avg: %.1f' % data_avg)
        #= data_avg_str = '{:.1f}'.format(data_avg) # string 변환
        print()
    #
    return data_avg

def hgSqrt(datalist):
    '''매개변수(datalist)의 값이 바뀐다.'''
    #-----
    # '0'보다 작은 값은 제곱근을 구할 수 없기 때문에 '0'으로
    # 이렇게 하지 않으면 아래에서 (datalist_new**0.5) 를 실행하면 
    # {RuntimeWarning: invalid value encountered in sqrt} 메시지 발생.
    #-----
    for li, value in enumerate(datalist):
        if (value < 0):
            datalist[li] = 0
    datalist_sqrt = datalist**0.5 # sqrt()
    #
    return datalist_sqrt
    
#========================
#========================
#========================
def PrintMatrix2D(Matrix2D):
    JulNum = len(Matrix2D)
    for j in range(0, JulNum):
        Dis_j = Matrix2D[j]
        KanNum = len(Dis_j)
        for k in range(0, KanNum):
            print('[', j, ':', k, ']', Dis_j[k])

def GetMatrix2D_MaxMin(Matrix2D, ExcludeSelf=False):
    min_val = -1
    max_val = -1
    firstFalg = False
    JulNum = len(Matrix2D)
    for j in range(0, JulNum):
        Dis_j = Matrix2D[j]
        KanNum = len(Dis_j)
        for k in range(0, KanNum):
            if(ExcludeSelf == True): # 자기 자신은 제외
                if(j == k): 
                    continue

            if(firstFalg == False): # 맨 처음
                max_val = Dis_j[k]
                min_val = Dis_j[k]
                firstFalg = True
                continue
            
            if(min_val > Dis_j[k]):
                min_val = Dis_j[k]
            if(max_val < Dis_j[k]):
                max_val = Dis_j[k]

    MaxMin = {
        'min': min_val,
        'max': max_val,
    }
    return MaxMin

#================================
#================================
def hgStandardScaler(datalist, sampleMode=False): # 
    # 표준편차로 스케일링
    dataNum = len(datalist)
    if(sampleMode == True): # 표본 표준 편차(sample standard deviation)
        dataNum -= 1
    if(dataNum <= 0):
        assert False, '(dataNum <= 0)'
        return 0

    #
    Avg, ret_std = hgStat_low(datalist)

    #
    scalelist = []
    for val in datalist: 
        scale_val = (val - Avg) / ret_std
        scalelist.append(scale_val)
    #
    return scalelist

def hgStandardScaler_Lists(datalists, Transpose=False, debug=False):
    '''# 표준편차로 스케일링
    {from sklearn.preprocessing.StandardScaler}처럼 작동하려면 
    처리 구조가 달라서 여기서는 매개변수 {Transpose=True} 해야 한다.
    '''
    # 
    if(Transpose == True): # 전치(행렬) 변환
        #=print('datalists:', datalists)
        datalists = hgTranspose_Lists(datalists) # transpos
        #print('datalists(after transpose):', datalists)

    listNum = len(datalists)
    if(listNum <= 0):
        #=assert False, '(listNum <= 0)'
        return None
    #
    StdScaler_lists = []
    for i in range(0, listNum): 
        baselist = datalists[i]
        dataNum = len(baselist)
        if(dataNum <= 0):
            #=assert False, '(dataNum <= 0)'
            return None
        #
        scalelist = hgStandardScaler(baselist)
        StdScaler_lists.append(scalelist)
    # 
    if(Transpose == True): # 전치(행렬) 변환
        #-----
        # {원래 데이터}를 {전치(행렬) 변환} 했으면 
        # {스케일된 데이터}도 {원래 데이터}처럼 보이도록 
        # 다시 {전치(행렬) 변환} 해준다.
        #-----
        #=print('StdScaler_lists:', StdScaler_lists)
        StdScaler_lists = hgTranspose_Lists(StdScaler_lists) # transpos
        #print('StdScaler_lists(after transpose):', StdScaler_lists)
    #
    return StdScaler_lists

def StandardizDataFrame_by_sklearn(DataFrame_V, debugPrint=False):
    '''Standardize Pandas.DataFrame'''
    #-----
    from sklearn.preprocessing import StandardScaler
    StdScaler = StandardScaler()
    StdScaler.fit(DataFrame_V)
    StdScaler_DataFrame = StdScaler.transform(DataFrame_V)
    if(debugPrint == True):
        print('StdScaler_DataFrame.shape:', StdScaler_DataFrame.shape)
    return StdScaler_DataFrame

#================================
#================================
def test_coefficient_low(datalist1, datalist2, graph=False, debugPrint=False):
    hgsysinc._print_function_name_()

    #=print(datalist1)
    #=print(datalist2)
    Coefficient = hgCoefficient_low(datalist1, datalist2, debugPrint=debugPrint)
    print('상관계수:', Coefficient)
    print()

    if(graph == True):
        import matplotlib.pyplot as plt
        plt.scatter(datalist1, datalist2)
        plt.show()

def test_coefficient_numpy(datalist1, datalist2, graph=False):
    hgsysinc._print_function_name_()

    #=print(datalist1)
    #=print(datalist2)

    import numpy as np
    Coefficient = np.corrcoef(datalist1, datalist2)
    print('상관계수:', Coefficient)
    print()

    if(graph == True):
        import matplotlib.pyplot as plt
        plt.scatter(datalist1, datalist2)
        plt.show()

def test_coefficient_scipy(datalist1, datalist2, graph=False): # scipy Pearson's correlation
    hgsysinc._print_function_name_()

    #=print(datalist1)
    #=print(datalist2)

    from scipy.stats import pearsonr
    Coefficient, _ = pearsonr(datalist1, datalist2)

    print('상관계수:', Coefficient)
    print()

    if(graph == True):
        import matplotlib.pyplot as plt
        plt.scatter(datalist1, datalist2)
        plt.show()

def test_coefficient_pandas(datalist1, datalist2, graph=False):
    hgsysinc._print_function_name_()

    #=print(datalist1)
    #=print(datalist2)

    import pandas as pd
    drink_series = pd.Series(datalist1)
    weather_series = pd.Series(datalist2)
    Coefficient = drink_series.corr(weather_series)

    print('상관계수:', Coefficient)
    print()

    if(graph == True):
        import matplotlib.pyplot as plt
        plt.scatter(datalist1, datalist2)
        plt.show()

#================================
#================================
#================================
from unittest import TestCase, main
class HGTest(TestCase):
    def _test_avg_low(self):
        hgsysinc._print_function_name_()

        datalist = [a for a in range(1,11)]
        datalist = list(range(1,11))
        print(datalist)
        
        avg_ret = hgAvg_low(datalist)
        print(avg_ret)
        '''
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        5.5        
        '''

    def _test_avg_1(self):
        hgsysinc._print_function_name_()

        datalist = [a for a in range(1,11)]
        datalist = list(range(1,11))
        print(datalist)
        
        avg_ret = hgAvg(datalist)
        print(avg_ret)

        '''
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        55
        5.5
        '''

    def _test_avg_numpy11(self):
        hgsysinc._print_function_name_()

        import numpy as np
        datalist = [a for a in range(1,11)]
        avg_ret = np.mean(datalist)
        print(avg_ret)

        datalist = list(range(1,11))
        avg_ret = np.mean(datalist)
        print(avg_ret)

        datalist = np.array([a for a in range(1,11)])
        avg_ret = np.mean(datalist)
        print(avg_ret)

        datalist = np.arange(1,11)
        avg_ret = np.mean(datalist)
        print(avg_ret)

        '''
        5.5
        5.5
        5.5
        5.5
        '''

    def _test_avg_numpy21(self):
        hgsysinc._print_function_name_()

        datalist = [a for a in range(1,11)]
        print(type(datalist))
        print(datalist)

        datalist = list(range(1,11))
        print(type(datalist))
        print(datalist)

        import numpy as np
        datalist = np.array([a for a in range(1,11)])
        print(type(datalist))
        print(datalist)

        datalist = np.arange(1,11)
        print(type(datalist))
        print(datalist)

        '''
        <class 'list'>
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        <class 'list'>
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        <class 'numpy.ndarray'>
        [ 1  2  3  4  5  6  7  8  9 10]
        <class 'numpy.ndarray'>
        [ 1  2  3  4  5  6  7  8  9 10]        
        '''

    def _test_avg_numpy22(self):
        hgsysinc._print_function_name_()

        datalist = [a for a in range(1,11)]
        datalist = list(range(1,11))

        import numpy as np
        datalist = np.array([a for a in range(1,11)])
        print(datalist)
        datalist = np.arange(1,11)
        print(datalist)

        avg_ret = np.mean(datalist)
        print(avg_ret)

        '''
        [ 1  2  3  4  5  6  7  8  9 10]
        [ 1  2  3  4  5  6  7  8  9 10]
        5.5
        '''

    def _test_geo_avg_low(self):
        hgsysinc._print_function_name_()

        datalist = [a for a in range(1,11)]
        datalist = list(range(1,11))
        print(datalist)
        
        avg_ret = hgGeoAvg(datalist)
        print(avg_ret)
        '''
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        3628800
        4.528728688116765
        '''

    def _test_geo_avg_numpy(self):
        hgsysinc._print_function_name_()

        import numpy as np
        datalist = np.array([a for a in range(1,11)])
        print(datalist)
        print(datalist.prod())
        avg_ret = datalist.prod()**(1.0/len(datalist)) # **: 제곱 연산자
        avg_ret = pow(datalist.prod(), (1.0/len(datalist))) # pow: 제곱 함수
        print(avg_ret)
        print()
        '''
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        3628800
        4.528728688116765        
        '''

    def _test_get_stat_low(self):
        hgsysinc._print_function_name_()

        datalist = [a for a in range(1,11)]
        #=datalist = list(range(1,11))
        print(datalist)

        Var = hgVar_low(datalist)
        print('분산:', Var)
        Avg, Std = hgStat_low(datalist)
        #=print('평균=%.5f' %Avg)
        print('평균=%.5f 표준편차=%.5f' % (Avg, Std))
        print()

    def _test_get_stat_numpy1(self):
        hgsysinc._print_function_name_()

        import numpy as np
        datalist = [a for a in range(1,11)]
        #=datalist = list(range(1,11))
        print(datalist)

        Var = np.var(datalist)
        Avg = np.mean(datalist)
        Std = np.std(datalist)
        print('분산:', Var)
        #=print('평균=%.5f' %Avg)
        print('평균=%.5f 표준편차=%.5f' % (Avg, Std))
        print()

    def _test_get_stat_numpy2(self):
        hgsysinc._print_function_name_()

        import numpy as np
        #=datalist = [a for a in range(1,11)]
        #=datalist = list(range(1,11))
        datalist = np.array([a for a in range(1,11)])
        print(datalist)

        Avg = datalist.mean()
        Std = np.sqrt(np.mean(abs(datalist - Avg)**2))
        #=Std = np.std(datalist)
        #=print('평균=%.5f' %Avg)
        print('평균=%.5f 표준편차=%.5f' % (Avg, Std))
        print()

    def _test_get_cov_low(self):
        hgsysinc._print_function_name_()

        #
        datalist = [a for a in range(1,11)]
        #=datalist = list(range(1,11))
        datalist1 = datalist[0:11:2]
        datalist2 = datalist[1:11:2]
        print(datalist1)
        print(datalist2)

        Cov = hgCovariance_low(datalist1, datalist2)
        print('공분산:', Cov)
        print()

    def _test_get_cov_numpy(self):
        hgsysinc._print_function_name_()

        #
        import numpy as np
        datalist = [a for a in range(1,11)]
        #=datalist = list(range(1,11))
        datalist1 = datalist[0:11:2]
        datalist2 = datalist[1:11:2]
        print(datalist1)
        print(datalist2)

        Cov = np.cov(datalist1, datalist2)
        print('공분산:', Cov)
        print()
        '''
        [1, 3, 5, 7, 9]
        [2, 4, 6, 8, 10]
        공분산: [[10. 10.]
        [10. 10.]]
        '''

    def _test_get_coefficient_low(self):
        hgsysinc._print_function_name_()

        #
        datalist = [a for a in range(1,11)]
        #=datalist = list(range(1,11))
        datalist1 = datalist[0:11:2]
        datalist2 = datalist[1:11:2]
        print(datalist1)
        print(datalist2)

        Coefficient = hgCoefficient_low(datalist1, datalist2, debugPrint=False)
        print('상관계수:', Coefficient)
        print()

    def _test_get_coefficient_numpy(self):
        hgsysinc._print_function_name_()

        #
        datalist = [a for a in range(1,11)]
        #=datalist = list(range(1,11))
        datalist1 = datalist[0:11:2]
        datalist2 = datalist[1:11:2]
        print(datalist1)
        print(datalist2)

        #=from scipy.stats import pearsonr
        #=Coefficient, _ = pearsonr(datalist1, datalist2)
        import numpy as np
        Coefficient = np.corrcoef(datalist1, datalist2)
        print('상관계수:', Coefficient)
        print()

    def _test_standard_scaler(self):
        hgsysinc._print_function_name_()

        #
        from sklearn.datasets import load_breast_cancer
        raw_data = load_breast_cancer()
        # 'filename': 'C:\\~~~~\\Python\\Python38\\lib\\site-packages\\sklearn\\datasets\\data\\breast_cancer.csv'}

        import pandas as pd
        raw_data_frame = pd.DataFrame(raw_data['data'], columns = raw_data['feature_names'])
        print('raw_data_frame.shape:', raw_data_frame.shape), print()

        # {pandas.DataFrame}을 {Matrix2D}로 변환한다.
        datalists = hgMatrix2D__DataFrame(raw_data_frame)
        #-----
        # hgStandardScaler_Lists() 함수로 넘길 때 {DataFrame}과 처리 구조가 달라서 {Transpose=True} 해야 한다.
        #-----
        StandardScaler_Lists = hgStandardScaler_Lists(datalists, Transpose=True)
        print('StandardScaler:')
        #=print(StandardScaler_Lists), print()
        for ri, StandardScaler_List in enumerate(StandardScaler_Lists):
            if(ri >= 5):
                break
            print(StandardScaler_List), print()
        print()

        '''
        raw_data_frame.shape: (569, 30)

        StandardScaler:
        [ 1.09706398 -2.07333501  1.26993369  0.9843749   1.56846633  3.28351467
        2.65287398  2.53247522  2.21751501  2.25574689  2.48973393 -0.56526506
        2.83303087  2.48757756 -0.21400165  1.31686157  0.72402616  0.66081994
        1.14875667  0.90708308  1.88668963 -1.35929347  2.30360062  2.00123749
        1.30768627  2.61666502  2.10952635  2.29607613  2.75062224  1.93701461]

        [ 1.82982061e+00 -3.53632408e-01  1.68595471e+00  1.90870825e+00
        -8.26962447e-01 -4.87071673e-01 -2.38458552e-02  5.48144156e-01
        1.39236330e-03 -8.68652457e-01  4.99254601e-01 -8.76243603e-01
        2.63326966e-01  7.42401948e-01 -6.05350847e-01 -6.92926270e-01
        -4.40780058e-01  2.60162067e-01 -8.05450380e-01 -9.94437403e-02
        1.80592744e+00 -3.69203222e-01  1.53512599e+00  1.89048899e+00
        -3.75611957e-01 -4.30444219e-01 -1.46748968e-01  1.08708430e+00
        -2.43889668e-01  2.81189987e-01]

        [ 1.57988811  0.45618695  1.56650313  1.55888363  0.94221044  1.05292554
        1.36347845  2.03723076  0.93968482 -0.39800791  1.22867595 -0.78008338
        0.8509283   1.18133606 -0.29700501  0.8149735   0.21307643  1.42482747
        0.23703554  0.2935594   1.51187025 -0.02397438  1.34747521  1.45628455
        0.52740741  1.08293217  0.85497394  1.95500035  1.152255    0.20139121]

        [-0.76890929  0.25373211 -0.59268717 -0.76446379  3.28355348  3.40290899
        1.91589718  1.45170736  2.86738293  4.91091929  0.32637344 -0.11040904
        0.2865934  -0.28837815  0.68970166  2.74428041  0.81951838  1.11500701
        4.73268037  2.04751088 -0.28146446  0.13398409 -0.2499393  -0.55002123
        3.3942747   3.89339743  1.98958826  2.17578601  6.04604135  4.93501034]

        [ 1.75029663 -1.15181643  1.77657315  1.82622928  0.28037183  0.53934045
        1.37101143  1.42849277 -0.00956047 -0.56244998  1.27054278 -0.7902437
        1.27318941  1.19035676  1.48306716 -0.04851988  0.82847078  1.14420474
        -0.36109227  0.49932813  1.29857524 -1.46677038  1.33853946  1.22072425
        0.22055617 -0.31339451  0.61317876  0.72925926 -0.86835298 -0.39709962]

        '''


if __name__ == '__main__':
    main()

