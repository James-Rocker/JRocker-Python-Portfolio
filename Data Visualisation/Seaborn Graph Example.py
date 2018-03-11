# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 16:05:55 2018

@author: james
"""

import imp, pip, time

def install_func(package):
    try:
        imp.find_module(package)
    except ImportError:
        print ('Error ' + package + ' library is missing ')
        var = input("Do you want to download and install the " + package + " library? (Note, this download and install might take a while) ")
        if var in ['no','n','No','N','NO']:
            print ('Error, '+ package + ' not installed, please install the library before attempting to run this program.')
            time.sleep(5)
            quit()
        else:
            pip.main(['install', package])
package = 'seaborn'
install_func(package)
package = 'pandas'
install_func(package)
package = 'numpy'
install_func(package)

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
#import numpy as np

example = {'Column 1' : [1,2,5,3,7],
            'Column 2' : [5,7,1,2,5],
            'Column 3' : [7,2,5,4,1]}
example = pd.DataFrame(example, index=['A','B','C','D','E'])

# Create violinplot
sns.swarmplot(x='A', y="Column 3", data=example)

# Show the plot
plt.show()