

import pandas as pd
import time as tm
import matplotlib.pyplot as plt

def pre_info():
     syn = "\n\nThis is program under development \n" + tm.ctime() + "\n> This Program is used to plot graph  \n > Data visulation  \n  > calcuation  \n   >  User interface for finding the required data..  \n\n"
     for i in syn:
          print(i,end="")
          tm.sleep(0.005)
          
pre_info()

def printing(a):
     for i in a:
          print(i,end = "")
          tm.sleep(0.008)
     load = "............\n\n"
     for i in load:
          print(i,end="")
          tm.sleep(0.3)


data = pd.read_csv("main-data.csv")
print(data)

printing("\n\nOpening the graph window ->>\n\n")

# Graph UNDER CONSTRUCTION
data.plot()
plt.show()
