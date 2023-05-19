import pandas as pd

Raw = pd.read_excel(r'Error2.xlsx')
Val = pd.read_excel(r'tambon.xlsx')

i = 0
j = 0

district_change = []
province_change= []

p1 = []
p2 = []
p3 = []
n2 = 2333
n3 = 1388
n33 = 690

while (i<n33) :    
    c = Raw.at[i,'district']
    for j in range (7436):
        check=0
        if not isinstance(Raw.at[i,'province_correct'],float):
            province_change.append(Raw.at[i,'province_correct'])
            district_change.append("")
            check =1
            i+=1
            break
        elif c == Val.at[j,'Tambon']:
            province_change.append(Val.at[j,'Province'])
            district_change.append(Val.at[j,'District'])
            i+=1
            check=1
            break
    if (check==0):
            district_change.append("")
            province_change.append("")
            i+=1
         
error = pd.DataFrame({'correct_province':province_change,'district_change':district_change})
result = Raw.join(error)
writer = pd.ExcelWriter('Error4.xlsx', engine='xlsxwriter')
result.to_excel(writer, index = False)
writer.save()
