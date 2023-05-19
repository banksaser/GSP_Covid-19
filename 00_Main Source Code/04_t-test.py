import numpy as np
from pygsp import graphs
import pandas as pd
from scipy.stats import t
import matplotlib.pyplot as plt
import math

magnitude_square = [ magnitude[i]**2 for i in range (928)]
group_1 = np.argpartition(magnitude_square, 100)[:100]   
group_2 = np.argpartition(magnitude, 100)[:100]       
group_3 = np.argpartition(magnitude, -100)[-100:]    


def TV_r(district) :
        TV_r = 0
        for k in range(39):
            for j in range(928):
                if i!= j and W[i][j]!=0:
                        TV_r += W[i][j]*abs(math.log((x[i][k]+1)/(x[j][k]+1),2))
        return TV_r

var_district_G1 = []
var_district_G2 = []   
var_district_G3 = []           

for i in range(100):
    var_district_G1.append(TV_r[group_1[i]])
    var_district_G2.append(TV_r[group_2[i]])
    var_district_G3.append(TV_r[group_3[i]])

mean_G1 = np.mean(var_district_G1)
sd_G1   = np.std(var_district_G1)
mean_G2 = np.mean(var_district_G2)
sd_G2   = np.std(var_district_G2)
mean_G3 = np.mean(var_district_G3)
sd_G3   = np.std(var_district_G3)

t_value = (mean_G1-mean_G2)/(np.sqrt(sd_G1**2/100+sd_G2**2/100))    
t_test = t.cdf(t_value,99)*2
result_1v2 = t_test<0.05

t_value = (mean_G1-mean_G3)/(np.sqrt(sd_G1**2/100+sd_G3**2/100))    
t_test = t.cdf(t_value,99)*2
result_1v3 = t_test<0.05



avg_G1 = []
avg_G2 = []
avg_G3 = []

for i in range(100):
    avg_G1.append(np.average(x_raw[group_1[i]]))   
    avg_G2.append(np.average(x_raw[group_2[i]]))   
    avg_G3.append(np.average(x_raw[group_3[i]]))   

mean_G1 = np.mean(avg_G1)
sd_G1   = np.std(avg_G1)
mean_G2 = np.mean(avg_G2)
sd_G2   = np.std(avg_G2)
mean_G3 = np.mean(avg_G3)
sd_G3   = np.std(avg_G3)

t_value = (mean_G1-mean_G2)/(np.sqrt(sd_G1**2/100+sd_G2**2/100))    
t_test = t.cdf(t_value,99)*2
result_1v2 = t_test<0.05

t_value = (mean_G1-mean_G3)/(np.sqrt(sd_G1**2/100+sd_G3**2/100))    
t_test = t.cdf(t_value,99)*2
result_1v3 = t_test<0.05
