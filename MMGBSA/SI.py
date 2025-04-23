import numpy as np
from pymbar import timeseries
from math import sqrt
import os,sys
'''This script is for determining the statistical inefficiency of a timeseries.
   It assumes that the data file is a 2 column array, where the first is some time
   value and the second column possesses the data'''
data=np.genfromtxt(sys.argv[1], dtype=float, usecols=int(sys.argv[2]))
#print data
SI=timeseries.statistical_inefficiency(data)
SP=np.floor(len(data)/SI)  # Determine the number of significant points
avg=np.average(data)
sd=np.std(data)
sem=sd/sqrt(SP)
indices = timeseries.subsample_correlated_data(data)
data_n = data[indices]
print (data_n)
print("\n\nNumber of significant points: "+str(SP)+"\n\n")
print("\n\tValue: "+str(avg)+" +/- "+str(sem))
