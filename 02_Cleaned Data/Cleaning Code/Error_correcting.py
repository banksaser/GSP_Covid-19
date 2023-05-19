import pandas as pd

Raw = pd.read_excel(r'Error.xlsx')
Val = pd.read_excel(r'District_Val.xlsx')


i = 0
j = 0
p1 =[]
error_detect_province = []
error_detect_district = []
province_change = []
n2 = 2333
n3 = 1388
n33 = 690

while (i<n33) :
    p1.append(Raw.at[i,'province_of_isolation'])    
    a = Raw.at[i,'province']
    c = Raw.at[i,'district']
    for j in range (923):
        b = Val.at[j,'province']
        d = Val.at[j,'district']
        if (c==d):
            if a!=b : 
                error_detect_province.append(a)
                error_detect_district.append(c)
                province_change.append(b)
            i += 1
            check = 0
            break
        check=1
    if (check==1):
        province_change.append("")
        error_detect_province.append(a)
        error_detect_district.append(c)
        
        i += 1


         
error = pd.DataFrame({'province_of_isolation':p1,'province':error_detect_province,'district':error_detect_district,'province_correct':province_change})
writer = pd.ExcelWriter('Error2.xlsx', engine='xlsxwriter')
error.to_excel(writer, index = False)
writer.save()