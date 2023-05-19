import pandas as pd

case = pd.read_excel(r'District_correct.xlsx')
pop = pd.read_excel(r'District_pop.xlsx')

signal_daily = [[0 for day in range(273)] for district in range(928)]

N = case.shape[0]

for i in range (N):
    for j in range (928):
            if pop.at[j,'District'] == case.at[i,'district_of_onset'] :
                    if pop.at[j,'Province']== case.at[i,'province_of_onset']:
                        posDis = j
                        break
    signal_daily[posDis][case.at[i,'announce_date']-44287] += 1

signal_weekly = [[0 for week in range(39)] for district in range(928)]

for i in range(928):
    for j in range(39):
        signal_weekly[i][j] = round(sum(signal_daily[i][j*7:j*7+7]))

for i in range(928):
    for j in range(39):
        signal_weekly[i][j] = signal_weekly[i][j]*100000/pop.at[i,'Pop']
        
signal_Frame = pd.DataFrame(signal_weekly)
writer = pd.ExcelWriter('signal_weekly.xlsx', engine='xlsxwriter')
signal_Frame.to_excel(writer, index = False)
writer.save()