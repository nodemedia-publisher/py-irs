#------------------------
#------------------------
from pathlib import Path
import os
import sys
filePath = Path(__file__).parent # file-path
parentPath = filePath.parent     # file-path-parent
#print(parentPath)
parent2Path = parentPath.parent     # file-path-parent-parent
#print(parent2Path)
parent3Path = parent2Path.parent     # file-path-parent-parent-parent
#=#print(parent2Path)

#--------------
# {parent2Path}
#--------------
# append relative path
newPath = os.path.join(parent2Path, 'hgmorp')
sys.path.append(newPath)
#print(sys.path)

# append relative path
newPath = os.path.join(parent2Path, 'hgdatsci')
sys.path.append(newPath)
#print(sys.path)

# append relative path
newPath = os.path.join(parent2Path, 'hggraph')
sys.path.append(newPath)
#print(sys.path)

#--------------
# {parent3Path}
#--------------
# append relative path
newPath = os.path.join(parent3Path, 'hgmorp')
sys.path.append(newPath)
#print(sys.path)

# append relative path
newPath = os.path.join(parent3Path, 'hgdatsci')
sys.path.append(newPath)
#print(sys.path)

# append relative path
newPath = os.path.join(parent3Path, 'hggraph')
sys.path.append(newPath)
#print(sys.path)

#--------------
# {parentPath}
#--------------
# append relative path
newPath = os.path.join(parentPath, 'hgmorp')
sys.path.append(newPath)
#print(sys.path)

# append relative path
newPath = os.path.join(parentPath, 'hgdatsci')
sys.path.append(newPath)
#print(sys.path)

# append relative path
newPath = os.path.join(parentPath, 'hggraph')
sys.path.append(newPath)
#print(sys.path)

#------------------------
# append relative path
newPath = os.path.join(parent3Path, '')
sys.path.append(newPath)
#print(sys.path)

# append relative path
newPath = os.path.join(parent2Path, '')
sys.path.append(newPath)
#print(sys.path)

# append relative path
newPath = os.path.join(parentPath, '')
sys.path.append(newPath)
#print(sys.path)

#------------------------
# append relative path
newPath = os.path.join(parent3Path, './')
sys.path.append(newPath)
#print(sys.path)

# append relative path
newPath = os.path.join(parent2Path, './')
sys.path.append(newPath)
#print(sys.path)

# append relative path
newPath = os.path.join(parentPath, './')
sys.path.append(newPath)
#print(sys.path)

#--------------
# {subPath}
#--------------
# append relative path
newPath = os.path.join(filePath, 'basic')
sys.path.append(newPath)
#print(sys.path)


#------------------------
#------------------------

def _print_function_name_(prelinefeed=0):
    if(prelinefeed > 0): # 함수 이름을 출력하기 전에 줄바꿈을 할 것인가?
        for i in range(prelinefeed):
            print()
            if(i >= 20): # '20'번 이상은 줄바꿈을 하지 않는다.
                break
    #
    import sys
    print(sys._getframe(1).f_code.co_name,'()') # 이 함수를 호출한 함수 이름
    #=print(sys._getframe(0).f_code.co_name,'()') # 현재 여기 함수 이름

