import pandas as pd
import math

pos = pd.read_excel(r'District_Pos.xlsx')


graph_dis = [[0 for column in range(928)]for row in range(928)]

for i in range (928):
    for j in range(i,928):
        graph_dis[i][j] = math.dist([pos.at[i,'LAT'],pos.at[i,'LONG']],[pos.at[j,'LAT'],pos.at[j,'LONG']])
        
graph_Frame = pd.DataFrame(graph_dis)
writer = pd.ExcelWriter('graph_dis.xlsx', engine='xlsxwriter')
graph_Frame.to_excel(writer, index = False)
writer.save()
