

import random as rd
import pandas as pd
import matplotlib.pyplot as plt


import time as tm

def pre_info():
     syn = "\n\nThis is program under development \n" + tm.ctime() + "\nThe data used can be excrated in vehicles.csv FILE\n\n"
     for i in syn:
          print(i,end="")
          tm.sleep(0.005)
     
pre_info()

# Holds whole data 
data = pd.read_csv("vehicles.csv")

# Holds only the segements of different data holding
data_segments = data.dropna() 


# Standard procedure
# Removing the unwanted data segements


# Considering only first 10 elements as preview 
print(data.head(5))

# Graph representation
data.plot()
plt.show()














