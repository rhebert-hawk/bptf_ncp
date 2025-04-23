##### Use syntax: python $Scripts/rmsffill.py data1.dat data2.dat data3.dat plot_name dataname1.dat dataname2.dat dataname3.dat ########

import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import matplotlib.legend_handler
import sys
font = {'family': 'sans-serif',
        'color':  'black',
        'weight': 'normal',
        'size': 28,
        }
x,y,yerr = np.loadtxt("Nucm_h3_1.dat", usecols=(0,1,2), unpack=True, comments=('#','@','&'))
f,y1,y1err = np.loadtxt("Nucm_h3_2.dat", usecols=(0,1,2), unpack=True, comments=('#','@','&'))
#a,b,berr= np.loadtxt("NucE_h3_2.dat", usecols=(0,1,2), unpack=True, comments=('#','@','&'))
#c = np.loadtxt("h3_1.pdb", usecols=(3), unpack=True, dtype='str')

fig, ax = plt.subplots()
ax.set_title('H3 histone RMSF', fontdict=font)
plt.plot(x, y, alpha=0.5, marker=".", lw=2, label='NCP', color='black')
plt.plot(x, g, alpha=0.5, marker="s", lw=2, label='NCP+BPTF', color='orange')
plt.fill_between(x, y-(yerr/2.2), y+(yerr/2.2), alpha=0.3, color='gray')
plt.fill_between(x, g-(gerr/2.2), g+(gerr/2.2), alpha=0.3, color='orange')
ax.xaxis.set_ticks(plt.index)
ax.xaxis.set_ticklabels(c)
leg = ax.legend(prop={'size': 10}, loc='best')
plt.ylabel('RMSF (Angstroms)', fontdict=font)
plt.xlabel('Residue Number', fontdict=font)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.margins(x=0)


plt.show()
