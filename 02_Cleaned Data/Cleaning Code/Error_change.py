import pandas as pd

Raw = pd.read_excel(r'District3_correct.xlsx')
Val = pd.read_excel(r'District3_ref2.xlsx')

i = 0
j = 0

#n2 = 2333
#n3 = 1387
n4 = 690
#n22 = 886076
#n33 = 312302
n44 = 312140

for j in range (n4):    
    b = Val.at[j,'district']
    if (j== n4-1):
        print(i)
        
    while (i<n44):
        if(Raw.at[i,'district_of_onset'] == b): 
            break
        i+=1
        
    while(Raw.at[i,'district_of_onset'] == b and Raw.at[i,'province_of_onset']== Val.at[j,'province']):
        Raw.at[i,'province_of_onset'] = Val.at[j,'province_change']
        if not isinstance(Val.at[j,'district_change'],float):
            Raw.at[i,'district_of_onset'] = Val.at[j,'district_change']
        i+=1
        if i==n44 :
            break
    
        
writer = pd.ExcelWriter('District3_correct2.xlsx', engine='xlsxwriter')
Raw.to_excel(writer, index = False)
writer.save()
