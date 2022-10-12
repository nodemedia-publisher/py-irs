#---
#---
def stat_graph_line(data, label=None, title=None, 
    xticks_label= None, xlabel=None, ylabel=None,
    linestyle=None, color=None,
    saveImageFile='',
    debugPrint=False,
    ):
    if(debugPrint == True):
        print('data:', len(data))
        #=print('date:', len(date))
        print('data sum:', sum(data)),print()

    #-------
    import matplotlib.pyplot as plt

    #=figsize = (15, 7)
    #=figsize = (10, 4)
    figsize = (10, 5)

    #
    plt.figure(figsize=figsize)
    #=plt.plot(date, data, label=label)
    #=plt.plot(data)
    
    if(linestyle != None):
        linestyle = linestyle
    else:
        linestyle = 'solid'
    plt.plot(data, label=label, linestyle=linestyle, color=color)

    if(label != None):
        plt.legend(loc='upper left')

    figure = plt.gcf()
    if(title != None):
        figure.canvas.set_window_title(title) # 윈도우 창에 [제목] 보이기
        #=plt.suptitle(title, fontsize=20, y=1.04) # 이미지 밖의 위쪽에 [제목] 표시
        plt.title(title, fontsize=20, y=1.04) # 이미지 밖의 위쪽에 [제목] 표시

    #
    if(xlabel != None):
        plt.xlabel(xlabel)
    if(ylabel != None):
        plt.ylabel(ylabel)

    #
    if(xticks_label != None):
        xtick_val = [n for n in range(len(data))]
        plt.xticks(xtick_val, labels=xticks_label)

    # 숫자가 클 경우에 tick 표기가 지수형(exponential)으로 바뀌지 않게
    plt.ticklabel_format(useOffset=False, style='plain', axis='y')
    
    #
    figure.tight_layout() # x,y tick 짤리지 않도록

    #
    if(saveImageFile != ''):
        # plt.savefig() 함수는 plt.show() 보다 먼저 호출해야 내용이 비어 있지 않다.
        plt.savefig(saveImageFile + '.png', bbox_inches='tight')
    else:
        plt.show()
    # 
    plt.close() # 이 함수를 호출하지 않으면 다음 호출에 이전 그림이 같이 호출됨.

def stat_graph_line_acc(data, label=None, title=None, 
    linestyle=None, color=None,
    saveImageFile='',
    debugPrint=False,
    ):
    if(debugPrint == True):
        print('data:', len(data))
        print('data sum:', sum(data)), print()

    #---------------------
    # 누적 데이터
    #---------------------
    data_acc = []
    data_sum = 0
    for value in data:
        data_sum += value
        data_acc.append(data_sum)
    if(debugPrint == True):
        print('data sum:', data_sum), print()

    #-------
    import matplotlib.pyplot as plt

    #=figsize = (15, 7)
    #=figsize = (10, 4)
    figsize = (10, 5)

    #
    plt.figure(figsize=figsize)
    #=plt.plot(date, data_acc, label=label)
    #=plt.plot(data_acc)
    
    if(linestyle != None):
        linestyle = linestyle
    else:
        linestyle = 'solid'
    plt.plot(data_acc, label=label, linestyle=linestyle, color=color)

    if(label != None):
        plt.legend(loc='upper left')

    figure = plt.gcf()
    if(title != None):
        figure.canvas.set_window_title(title) # 윈도우 창에 [제목] 보이기
        #=plt.suptitle(title, fontsize=20, y=1.04) # 이미지 밖의 위쪽에 [제목] 표시
        plt.title(title, fontsize=20, y=1.04) # 이미지 밖의 위쪽에 [제목] 표시

    # 숫자가 클 경우에 라벨 표기가 지수형(exponential)으로 바뀌지 않게
    plt.ticklabel_format(useOffset=False, style='plain', axis='y')

    #
    figure.tight_layout() # x,y tick 짤리지 않도록

    #
    if(saveImageFile != ''):
        # plt.savefig() 함수는 plt.show() 보다 먼저 호출해야 내용이 비어 있지 않다.
        plt.savefig(saveImageFile + '.png', bbox_inches='tight')
    else:
        plt.show()
    # 
    plt.close() # 이 함수를 호출하지 않으면 다음 호출에 이전 그림이 같이 호출됨.

def stat_graph_line_compare(datas, labels=None, 
    title=None, linestyles=None, saveImageFile='',
    debugPrint=False,
    ):
    if(debugPrint == True):
        for i, data in enumerate(datas):
            print(f'data{i+1}:', len(data))
        for i, data in enumerate(datas):
            print(f'data{i+1} sum:', sum(data))
        print()

    #-------
    import matplotlib.pyplot as plt

    #=figsize = (15, 7)
    #=figsize = (10, 4)
    figsize = (10, 5)

    #
    plt.figure(figsize=figsize)
    for i, data in enumerate(datas):
        if(debugPrint == True):
            print(f'data{i+1} sum:', len(data))
        label = ''
        if(labels != None):
            label = labels[i]
        if(linestyles != None):
            linestyle = linestyles[i]
        else:
            linestyle = 'solid'
        plt.plot(data, label=label, linestyle=linestyle)
    #
    plt.legend(loc='upper left')

    figure = plt.gcf()
    if(title != None):
        figure.canvas.set_window_title(title) # 윈도우 창에 [제목] 보이기
        #=plt.suptitle(title, fontsize=20, y=1.04) # 이미지 밖의 위쪽에 [제목] 표시
        plt.title(title, fontsize=20, y=1.04) # 이미지 밖의 위쪽에 [제목] 표시

    #
    figure.tight_layout() # x,y label 짤리지 않도록

    #
    if(saveImageFile != ''):
        # plt.savefig() 함수는 plt.show() 보다 먼저 호출해야 내용이 비어 있지 않다.
        plt.savefig(saveImageFile + '.png', bbox_inches='tight')
    else:
        plt.show()
    # 
    plt.close() # 이 함수를 호출하지 않으면 다음 호출에 이전 그림이 같이 호출됨.

def stat_graph_line_acc_compare(datas, labels=None, title=None, 
    linestyles=None, saveImageFile='',
    debugPrint=False,
    ):
    if(debugPrint == True):
        #=print('date:', len(date))
        for i, data in enumerate(datas):
            print(f'data{i+1}:', len(data))
        for i, data in enumerate(datas):
            print(f'data{i+1} sum:', len(data))
        print()

    #---------------------
    # 누적 데이터
    #---------------------
    data_acc = []
    for i, data in enumerate(datas):
        data_acc1 = []
        data_sum = 0
        for value in data:
            data_sum += value
            data_acc1.append(data_sum)
        data_acc.append(data_acc1)
        if(debugPrint == True):
            print(f'data{i+1} sum:', data_sum)

    #-------
    import matplotlib.pyplot as plt

    #=figsize = (15, 7)
    #=figsize = (10, 4)
    figsize = (10, 5)

    #
    plt.figure(figsize=figsize)
    #=plt.plot(date, data_acc1, label=label1)
    #=plt.plot(date, data_acc2, label=label2)
    #=plt.plot(data_acc1)
    #=plt.plot(data_acc2)
    for i, acc_data in enumerate(data_acc):
        label = ''
        if(labels != None):
            label = labels[i]
        if(linestyles != None):
            linestyle = linestyles[i]
        else:
            linestyle = 'solid'
        plt.plot(acc_data, label=label, linestyle=linestyle)

    plt.legend(loc='upper left')

    figure = plt.gcf()
    if(title != None):
        figure.canvas.set_window_title(title)
        #=plt.suptitle(title, fontsize=20, y=1.04) # 이미지 밖의 위쪽에 [제목] 표시
        plt.title(title, fontsize=20, y=1.04) # 이미지 밖의 위쪽에 [제목] 표시

    # 숫자가 클 경우에 라벨 표기가 지수형(exponential)으로 바뀌지 않게
    plt.ticklabel_format(useOffset=False, style='plain', axis='y')

    #
    figure.tight_layout() # x,y tick 짤리지 않도록

    #
    if(saveImageFile != ''):
        # plt.savefig() 함수는 plt.show() 보다 먼저 호출해야 내용이 비어 있지 않다.
        plt.savefig(saveImageFile + '.png', bbox_inches='tight')
    else:
        plt.show()
    # 
    plt.close() # 이 함수를 호출하지 않으면 다음 호출에 이전 그림이 같이 호출됨.

def stat_graph_bar2(data1, data2, label1=None, label2=None, title=None, 
    patterns=None, bar_colors=None,
    saveImageFile='',
    debugPrint=False,
    ):
    #-------
    import matplotlib.pyplot as plt

    #=figsize = (15, 7)
    #=figsize = (10, 4)
    #=figsize = (3, 4)
    #=figsize = (4, 5)
    figsize = (5, 6)

    bar_width = 0.65

    bar_data = [data1, data2]
    bar_num = [n for n in range(len(bar_data))]
    #=bar_colors = ['blue', 'orange', 'green'] # 'blue':Korea, 'orange':Japan, 'green':Italy
    x_ticks = [label1, label2]

    #
    figure = plt.figure(figsize=figsize)
    bars = plt.bar(bar_num, bar_data, width=bar_width, color=bar_colors)
    
    #
    if(patterns != None):
        #=patterns = ['/', '\\', '|', '-', '+', 'x', 'o', 'O', '.', '*']
        for i, patch in enumerate(bars.patches):
            patch.set_hatch(patterns[i])
    
    #    
    plt.xticks(bar_num, x_ticks)

    #=plt.legend(loc='upper left')

    #
    figure = plt.gcf()
    if(title != None):
        figure.canvas.set_window_title(title) # 윈도우 창에 [제목] 보이기
        #=plt.suptitle(title, fontsize=20, y=1.04) # 이미지 밖의 위쪽에 [제목] 표시
        plt.title(title, fontsize=15, y=1.04) # 이미지 밖의 위쪽에 [제목] 표시

    # 숫자가 클 경우에 라벨 표기가 지수형(exponential)으로 바뀌지 않게
    plt.ticklabel_format(useOffset=False, style='plain', axis='y')

    #
    figure.tight_layout() # x,y tick 짤리지 않도록

    #
    if(saveImageFile != ''):
        # plt.savefig() 함수는 plt.show() 보다 먼저 호출해야 내용이 비어 있지 않다.
        plt.savefig(saveImageFile + '.png', bbox_inches='tight')
    else:
        plt.show()
    # 
    plt.close() # 이 함수를 호출하지 않으면 다음 호출에 이전 그림이 같이 호출됨.

def stat_graph_bars(covid19_datas, labels=None, title=None, 
    patterns=None, bar_colors=None,
    saveImageFile='',
    debugPrint=False,
    ):
    if(debugPrint == True):
        #=print('covid19_date:', len(covid19_date))
        for i, covid19_data in enumerate(covid19_datas):
            print(f'covid19_data{i+1}:', covid19_data)
        print()

    #-------
    import matplotlib.pyplot as plt

    #=figsize = (15, 7)
    #=figsize = (10, 4)
    #=figsize = (3, 4)
    #=figsize = (4, 5)

    if(patterns != None):
        figsize = (5, 6)
        bar_width = 0.65 
    else:
        figsize = (3.6, 4.5)
        bar_width = 0.85 

    bar_num = [n for n in range(len(covid19_datas))]
    #=bar_colors = ['blue', 'orange', 'green']

    #
    plt.figure(figsize=figsize)
    bars = plt.bar(bar_num, covid19_datas, width=bar_width, color=bar_colors)

    #
    if(patterns != None):
        #=patterns = ['/', '\\', '|', '-', '+', 'x', 'o', 'O', '.', '*']
        for i, patch in enumerate(bars.patches):
            patch.set_hatch(patterns[i])
    
    #    
    plt.xticks(bar_num, labels)

    #=plt.legend(loc='upper left')

    #
    figure = plt.gcf()
    if(title != None):
        figure.canvas.set_window_title(title)
        #=plt.suptitle(title, fontsize=20, y=1.04) # 이미지 밖의 위쪽에 [제목] 표시
        #=plt.title(title, fontsize=15, y=1.04) # 이미지 밖의 위쪽에 [제목] 표시
        plt.title(title, fontsize=11, y=1.04) # 이미지 밖의 위쪽에 [제목] 표시-작은 제목

    # 숫자가 클 경우에 라벨 표기가 지수형(exponential)으로 바뀌지 않게
    plt.ticklabel_format(useOffset=False, style='plain', axis='y')

    #
    figure.tight_layout() # x,y tick 짤리지 않도록

    #
    if(saveImageFile != ''):
        # plt.savefig() 함수는 plt.show() 보다 먼저 호출해야 내용이 비어 있지 않다.
        plt.savefig(saveImageFile + '.png', bbox_inches='tight')
    else:
        plt.show()
    # 
    plt.close() # 이 함수를 호출하지 않으면 다음 호출에 이전 그림이 같이 호출됨.

def stat_graph_bar_histo(data, xticks=None, label=None, title=None, 
    xlabel=None, ylabel=None,
    ymax=None,
    horizontal_line=None, saveImageFile=''):
    #---------------------
    #---------------------
    import matplotlib.pyplot as plt

    #=figsize = (15, 7)
    #=figsize = (10, 4)
    figsize = (10, 5)

    histo_num = len(data)
    #
    plt.figure(figsize=figsize)
    #=plt.hist(data, bins=histo_num, label=label)
    bar_num = [n for n in range(len(data))]

    #
    bars = plt.bar(bar_num, height=data, label=label)
    #
    if(horizontal_line != None):
        plt.axhline(y=horizontal_line, linewidth=3, color='r')
    #
    if(xticks != None):
        plt.xticks(bar_num, xticks)
    #
    if(xlabel != None):
        plt.xlabel(xlabel, fontsize=15)
    if(ylabel != None):
        plt.ylabel(ylabel, fontsize=15)
    if(label != None):
        plt.legend(loc='upper left')

    figure = plt.gcf()
    if(title != None):
        figure.canvas.set_window_title(title) # 윈도우 창에 [제목] 보이기
        #=plt.suptitle(title, fontsize=20, y=1.04) # 이미지 밖의 위쪽에 [제목] 표시
        plt.title(title, fontsize=20, y=1.04) # 이미지 밖의 위쪽에 [제목] 표시

    # 숫자가 클 경우에 라벨 표기가 지수형(exponential)으로 바뀌지 않게
    plt.ticklabel_format(useOffset=False, style='plain', axis='y')
    #
    figure.tight_layout() # x,y tick 짤리지 않도록
    #
    if(ymax != None):
        plt.ylim(0, 1.05 * ymax)    
    #
    if(saveImageFile != ''):
        # plt.savefig() 함수는 plt.show() 보다 먼저 호출해야 내용이 비어 있지 않다.
        plt.savefig(saveImageFile + '.png', bbox_inches='tight')
    else:
        plt.show()
    # 
    plt.close() # 이 함수를 호출하지 않으면 다음 호출에 이전 그림이 같이 호출됨.

def stat_graph_scatter(data1, data2, label=None, title=None, 
    xlabel=None, ylabel=None, 
    winSquareMode=True, dotBigSize=True,
    saveImageFile='',
    ):
    #---------------------
    #---------------------
    import matplotlib.pyplot as plt

    #=figsize = (15, 7)
    #=figsize = (10, 4)
    if(winSquareMode == True):
        figsize = (6, 6) # 가로,세로 데이터 수가 같을 때
    else:
        figsize = (10, 5) # 가로 데이터가 많을 때

    if(dotBigSize == True): # 점을 크게
        dotSize = 130
    else: 
        dotSize = 50

    #
    data_num1 = len(data1)
    data_num2 = len(data2)

    #
    plt.figure(figsize=figsize)
    plt.scatter(data1, data2, s=dotSize)

    #
    if(xlabel != None):
        plt.xlabel(xlabel, fontsize=15)
    if(ylabel != None):
        plt.ylabel(ylabel, fontsize=15)

    if(label != None):
        plt.legend(loc='upper left')

    figure = plt.gcf()
    if(title != None):
        figure.canvas.set_window_title(title) # 윈도우 창에 [제목] 보이기
        #=plt.suptitle(title, fontsize=20, y=1.04) # 이미지 밖의 위쪽에 [제목] 표시
        plt.title(title, fontsize=20, y=1.04) # 이미지 밖의 위쪽에 [제목] 표시

    # 숫자가 클 경우에 라벨 표기가 지수형(exponential)으로 바뀌지 않게
    plt.ticklabel_format(useOffset=False, style='plain', axis='y')

    #
    figure.tight_layout() # x,y label 짤리지 않도록

    #
    if(saveImageFile != ''):
        # plt.savefig() 함수는 plt.show() 보다 먼저 호출해야 내용이 비어 있지 않다.
        plt.savefig(saveImageFile + '.png', bbox_inches='tight')
    else:
        plt.show()
    # 
    plt.close() # 이 함수를 호출하지 않으면 다음 호출에 이전 그림이 같이 호출됨.

def hggraph_wordfreq(word_list, freq_list, label=None, title=None, saveImageFile=''):
    #
    listnum = len(freq_list)

    #---------------------
    #---------------------
    import matplotlib.pyplot as plt

    #=figsize = (15, 7)
    #=figsize = (10, 4)
    figsize = (10, 5)
    #=figsize = (7, 7)
    #=figsize = (5, 5)

    #
    plt.figure(figsize=figsize)
    plt.bar(word_list, freq_list, color='limegreen')

    figure = plt.gcf()
    if(title != None):
        figure.canvas.set_window_title(title) # 윈도우 창에 [제목] 보이기
        #=plt.suptitle(title, fontsize=20, y=1.04) # 이미지 밖의 위쪽에 [제목] 표시
        plt.title(title, fontsize=20, y=1.04) # 이미지 밖의 위쪽에 [제목] 표시

    #
    plt.ylabel("freq")
    plt.xticks(rotation='vertical') # 단어를 세로로 출력
    
    # 숫자가 클 경우에 tick 표기가 지수형(exponential)으로 바뀌지 않게
    plt.ticklabel_format(useOffset=False, style='plain', axis='y')

    #
    figure.tight_layout() # x,y tick 짤리지 않도록
    plt.tight_layout()

    #
    if(saveImageFile != ''):
        # plt.savefig() 함수는 plt.show() 보다 먼저 호출해야 내용이 비어 있지 않다.
        plt.savefig(saveImageFile + '.png', bbox_inches='tight')
    else:
        plt.show()
    # 
    plt.close() # 이 함수를 호출하지 않으면 다음 호출에 이전 그림이 같이 호출됨.



#================================
#================================
#================================
from unittest import TestCase, main
class HGTest(TestCase):
    def test_1(self):
        import hgsysinc
        hgsysinc._print_function_name_()


if __name__ == '__main__':
    main()
