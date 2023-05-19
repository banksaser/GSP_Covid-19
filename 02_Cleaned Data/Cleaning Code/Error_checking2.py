import pandas as pd

Raw = pd.read_excel(r'District3_Change2.xlsx')
Val = pd.read_excel(r'District_Val.xlsx')

i = 0
j = 0
error_detect_province = []
error_detect_district = []

n2 = 533
n3 = 241
while (i<n3) :
    a = Raw.at[i,'province_change']
    b = Val.at[j,'province']
    c = Raw.at[i,'district_change']
    d = Val.at[j,'district']
    if (a==b):
        if (c==d):
                i += 1
        elif (c!=d):
                check_j = j
                while(a==Val.at[check_j,'province'] and check_j<922):
                    check_j += 1
                    if c==Val.at[check_j,'district'] :
                        i += 1
                        break
                if  check_j == 922 or a != Val.at[check_j,'province'] :
                    error_detect_province.append(a)
                    error_detect_district.append(c)
                    i += 1

    else :  j += 1
         
error = pd.DataFrame({'Error_province':error_detect_province,'Error_district':error_detect_district})
writer = pd.ExcelWriter('Error2.xlsx', engine='xlsxwriter')
error.to_excel(writer, index = False)
writer.save()





    


