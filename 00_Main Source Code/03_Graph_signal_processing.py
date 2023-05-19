import numpy as np
from pygsp import graphs
import pandas as pd
import math

W_dataframe = pd.read_excel('Graph.xlsx')
x_dataframe = pd.read_excel(r'signal_normalize.xlsx')   
 
x = x_dataframe.to_numpy()
W = W_dataframe.to_numpy()

G = graphs.Graph(W)
G.compute_laplacian()
G.compute_fourier_basis()

v = G.u
vt = np.transpose(v)

filter_30_hat = np.zeros((928,928))
sm = 0.3              
for i in range(928):
    if i<=928*sm : filter_30_hat[i][i]=1
    else : filter_30_hat[i][i] = 0
    
filter_30 = np.matmul(np.matmul(v,filter_30_hat),vt)
xl = np.matmul(filter_30,x)              
         
magnitude = [0 for district in range(928)]
for i in range(928):
    magnitude[i] = math.log((sum(x[i])+500)/(sum(abs(xl[i]))+500),2)
    if magnitude[i]>1 : magnitude[i] = 1
    if magnitude[i]<-1 : magnitude[i] = -1

