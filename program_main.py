
import random as rd
import pandas as pd
import matplotlib as plt

import time as tm

def pre_info():
     syn = "\n\nThis is program under development \n" + tm.ctime() + "\nThe data used can be excrated in vehicles.csv FILE\n\n"
     for i in syn:
          print(i,end="")
          tm.sleep(0.02)
     
pre_info()

data_read = pd.read_csv("vehicles.csv")
print(data_read)
