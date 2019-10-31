# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 23:03:54 2019

@author: sai teja
"""


"out liers"
What is an outlier?
outlier is something which is separate/different from the crowd.

import numpy as np
import matplotlib.pyplot as plt
​
import numpy as np
import matplotlib.pyplot as plt
#What are the criteria to identify an outlier?
1)Data point that falls outside of 1.5 times of an interquartile range above the 3rd quartile and below the 1st quartile

2)Data point that falls outside of 3 standard deviations. we can use a z score and if the z score falls outside of 2 standard deviation

#What is the reason for an outlier to exists in a dataset?
Variability in the data An experimental measurement error

#What are the impacts of having outliers in a dataset?¶
1.It causes various problems during our statistical analysis

2.It may cause a significant impact on the mean and the standard deviation

#finding the outlier.
1.Box plot

2.Scatter plot

3.Using IQR(Inter Quantile Range)

dataset= [11,10,12,14,12,15,14,13,15,102,12,14,17,19,107, 10,13,12,14,12,108,12,11,14,13,15,10,15,12,10,14,13,15,10]

#Detecting outlier using Z score
Formula for Z score = (Observation — Mean)/Standard Deviation

z = (X — μ) / σ

outliers=[]
def detect_outliers(data):
    
    threshold=3
    mean = np.mean(data)
    std =np.std(data)
    
    
    for i in data:
        z_score= (i - mean)/std 
        if np.abs(z_score) > threshold:
            outliers.append(y)
    return outliers
outlier_pt=detect_outliers(dataset)
outlier_pt
[102, 107, 108]

InterQuantile Range
75%- 25% values in a dataset

Steps
Arrange the data in increasing order
Calculate first(q1) and third quartile(q3)
Find interquartile range (q3-q1)
4.Find lower bound q1*1.5

5.Find upper bound q3*1.5

Anything that lies outside of lower and upper bound is an outlier

## Perform all the steps of IQR
sorted(dataset)
[10,
 10,
 10,
 10,
 10,
 11,
 11,
 12,
 12,
 12,
 12,
 12,
 12,
 12,
 13,
 13,
 13,
 13,
 14,
 14,
 14,
 14,
 14,
 14,
 15,
 15,
 15,
 15,
 15,
 17,
 19,
 102,
 107,
 108]
quantile1, quantile3= np.percentile(dataset,[25,75])
print(quantile1,quantile3)
​
12.0 15.0
##find iqr
​
iqr_value=quantile3-quantile1
print(iqr_value)
3.0
## Find the lower bound value and the higher bound value
​
lower_bound_val = quantile1 -(1.5 * iqr_value) 
upper_bound_val = quantile3 +(1.5 * iqr_value)
print(lower_bound_val,upper_bound_val)
7.5 19.5

