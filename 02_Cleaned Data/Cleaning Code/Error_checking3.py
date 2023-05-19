import pandas as pd

Raw = pd.read_excel(r'District3_correct2.xlsx')
Val = pd.read_excel(r'District_Val.xlsx')


error_detect_province = []
error_detect_district = []
error_position = []

n22 = 885794
n33 = 312081


for i in range (n33) :
    a = Raw.at[i,'province_of_onset']
    c = Raw.at[i,'district_of_onset']
    check = 0
    
    if(i!=0):
        if (c==Raw.at[i-1,'district_of_onset']):
            continue

    
    for j in range(923):
        if Val.at[j,'district'] == c:
            check =1
            break
        
    if check ==0:
        error_detect_province.append(a)
        error_detect_district.append(c)            
        error_position.append(i+2)

         
error = pd.DataFrame({'Error_position':error_position,'Error_province':error_detect_province,'Error_district':error_detect_district})
writer = pd.ExcelWriter('Error4.xlsx', engine='xlsxwriter')
error.to_excel(writer, index = False)
writer.save()