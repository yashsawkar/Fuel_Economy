

import pandas as pd
import matplotlib.pyplot as plt
import time as tm

def pre_info():
     syn = "\n\nThis is program under development \n" + tm.ctime() + "\nThe program is used to execrate data from vehicles.csv  -->> main_vec.csv FILE\n\n"
     for i in syn:
          print(i,end="")
          tm.sleep(0.005)

     
pre_info()

# printing the main ^BIG^ file
big_data = pd.read_csv("vehicles.csv")
print(big_data)
print("This is all columns and they data type")
print(big_data.info())

#loading the big csv file into the data frame 
datafram = pd.DataFrame(big_data)
print(datafram)



collection = {
               "Car_type" : [],
               "Fuel_type" : [],
               "Drive" : [],
               "Fuel_consumtion" : [],
               "vehicle_brand" : [],
               "Transmission" : [],
               "cylinder" : [],
               "cubic_capacity" : []
               }

for i in datafram["VClass"]:
     print(i)
     collection["Car_type"].append(i)
     
for i in datafram["fuelType"]:
     print(i)
     collection["Fuel_type"].append(i)
     
for i in datafram['drive']:
     print(i)
     collection["Drive"].append(i)
     
for i in datafram['barrels08']:
     print(i)
     collection["Fuel_consumtion"].append(i)
     
for i in datafram['make']:
     print(i)
     collection["vehicle_brand"].append(i)
     
for i in datafram['trany']:
     print(i)
     collection["Transmission"].append(i)
     
for i in datafram["cylinders"]:
     print(i)
     collection["cylinder"].append(i)
     
for i in datafram["displ"]:
     print(i)
     collection["cubic_capacity"].append(i)
     

dataframe_collection = pd.DataFrame(collection)
print(dataframe_collection)

# Now transfering this dataframe into a main_vehicles.csv file
dataframe_collection.to_csv("main-data.csv")

# printing the csv file to conform the placement of elements in the csv file
read_data = pd.read_csv("main-data.csv")
print(read_data.to_string())










                  






