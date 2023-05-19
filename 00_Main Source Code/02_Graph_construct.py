import pandas as pd
import math
import numpy as np

distance = pd.read_excel('distance.xlsx')
distance_arr = distance.to_numpy()

Graph = [[0 for column in range(928)] for row in range(928)] 

for i in range(928):    
    row = np.array(distance_arr[i])   
    min_r = min(row[row != 0])    
    for j in range(928):
        if distance_arr[i][j] == 0 : 
            continue
        else :
            if distance_arr[i][j]>= 4*min_r : Graph[i][j] = 0
            else :
                Graph[i][j] = 1-math.log(distance_arr[i][j]/min_r,4)  

graph_Frame = pd.DataFrame(Graph)
writer = pd.ExcelWriter('Graph.xlsx', engine='xlsxwriter') 
graph_Frame.to_excel(writer, index = False)
writer.save()
