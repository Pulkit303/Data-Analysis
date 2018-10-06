#!/usr/bin/python3

import pandas as pd
import matplotlib.pyplot as plt
#Loading the dataset
df= pd.read_csv("airline-safety.csv")
#Plotting the grph between incidents and fatalities on airports
x = df["incidents_85_99"] 
x1 = df["incidents_00_14"]
y = df["fatalities_85_99"]
y1= df["fatalities_00_14"]
p1=plt.bar(x, y,  color= "m")
p2=plt.bar(x1, y1 ,color="b")
plt.xlabel('incidents') 
plt.ylabel('fatalities') 
#Giving titles to bar graph
plt.title('Fatalities per Incidents', loc='center')
#Applying legend for easy understanding
plt.legend((p1[0], p2[0]), ('1985-1999', '2000-2014'))
plt.show()
