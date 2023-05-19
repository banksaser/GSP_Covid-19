import pandas as pd

Raw = pd.read_excel(r'District3_Raw2.xlsx')
Val = pd.read_excel(r'District_Val.xlsx')

i = 0
j = 0
error_detect = []
p1 =[]
p2 = []
correct = False

n2 = 2609
n3 = 1542
n33 = 1435

for i in range (n33) :
    correct = False
    for j in range (923) :
        a = Raw.at[i,'district']
        b = Val.at[j,'district']
        if Raw.at[i,'province'] == Val.at[j,'province']:
            if Raw.at[i,'district'] == Val.at[j,'district']:
                correct = True
                break
    if not correct :
        error_detect.append(Raw.at[i,'district'])
        p1.append(Raw.at[i,'province_of_isolation'])
        p2.append(Raw.at[i,'province'])
          
error = pd.DataFrame({'province_of_isolation':p1,'province':p2,'district':error_detect})
writer = pd.ExcelWriter('Error.xlsx', engine='xlsxwriter')
error.to_excel(writer, index = False)
writer.save()





    

