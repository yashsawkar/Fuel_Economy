

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
collection = {
               "Car_type" : [6,5,4],
               "Mileage" : [14,16,18],
               "Distance" : [40,5,76]
               }

data_collection = pd.DataFrame(collection)
print(data_collection)

data_collection.to_csv("main_vec.csv")

print("\nThe csv file is holding the folloing data for testing purposes : \n")

# print the new csv file
data =pd.read_csv("main_vec.csv")
print(data)
print("\n\n")


# printing the main file
big_data = pd.read_csv("vehicles.csv")
print(big_data)
print("This is all columns and they data type")
print(big_data.info())





                  






