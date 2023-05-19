import pandas as pd
import matplotlib.pyplot as plt
import numpy
from matplotlib.pyplot import figure


'''#daily
signal = pd.read_excel(r'signal4_2.xlsx')
signal_array = pd.DataFrame(signal).to_numpy()

x_corr = numpy.array([i for i in range (1,275)])
figure(figsize=(60, 15), dpi=250)

for i in range(928):
    plt.plot(x_corr, signal_array[i],linewidth=0.15)

plt.savefig('line_plot_daily.png')
'''

#weekly
signal = pd.read_excel(r'signal4_3.xlsx')
signal_array = pd.DataFrame(signal).to_numpy()

x_corr = numpy.array([i for i in range (1,40)])
figure(figsize=(20, 16), dpi=250)

for i in range(928):
    plt.plot(x_corr, signal_array[i],linewidth=0.35)
plt.rc('xtick', labelsize=30)    # fontsize of the tick labels
plt.rc('ytick', labelsize=30) 
plt.savefig('line_plot_weekly.png')


'''
signal = pd.read_excel(r'signal4_2.xlsx')
signal_array = pd.DataFrame(signal).to_numpy()

x_corr = numpy.array([i for i in range (1,8)])
figure(figsize=(15, 7), dpi=250)

for j in range(275//7) :
    for i in range(928):    
        plt.plot(x_corr, signal_array[i][j*7:j*7+7],linewidth=0.5)
    plt.savefig('line_plot_week'+str(j)+'.png')
    plt.clf()
'''