#------------------------
#------------------------
from pathlib import Path
import os
import sys
filePath = Path(__file__).parent # file-path
parentPath = filePath.parent     # file-path-parent
#print(parentPath)

# append relative path
newPath = os.path.join(parentPath, 'hgdatsci')
sys.path.append(newPath)
#print(sys.path)
#------------------------
#------------------------
