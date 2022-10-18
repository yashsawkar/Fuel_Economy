

import pandas as pd
import matplotlib.pyplot as plt
import time as tm

def pre_info():
     syn = "\n\nThis is program under development \n" + tm.ctime() + "\nThe program is used to execrate data from vehicles.csv  -->> main_vec.csv FILE\n\n"
     for i in syn:
          print(i,end="")
          tm.sleep(0.005)
     
pre_info()


## Execrate the requied data and place main_vec.csv



