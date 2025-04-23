import matplotlib.pyplot as plt
import numpy as np
import sys
font = {'family': 'sans-serif',
        'color':  'black',
        'weight': 'normal',
        'size': 28,
        }
x = np.loadtxt("Nucmsurfall.dat", usecols=(1), unpack=True, comments=('#','@','&'))
	#The only difference this time is since we are plotting histograms, we only need one data column
#y = np.loadtxt("Adna.dat", usecols=(1), unpack=True, comments=('#','@','&'))
z = np.loadtxt("NucEsurfall.dat", usecols=(1), unpack=True, comments=('#','@','&'))
#a = np.loadtxt("anobdna.dat", usecols=(1), unpack=True, comments=('#','@','&'))
b = np.loadtxt("EnoBsurfall.dat", usecols=(1), unpack=True, comments=('#','@','&'))
plt.hist(x, alpha=0.5, bins=300, density=True, linewidth=3, label='H3K4me3 Nucleosome', histtype='step')
	#as before, alpha specifies transparency
	#bins are effectively the "resolution" of your histogram - higher bin counts should result in a smoother curve
	#density=True normalizes the data
	#histtype='step' avoids filling in the histogram color, which is the default, and only graphs the value
#plt.hist(y, alpha=0.5, bins=300, density=True, linewidth=3, label='BPTF on NCP (I)', histtype='step')
plt.hist(z, alpha=0.5, bins=300, density=True, linewidth=3, label='BPTF on NCP', histtype='step')
#plt.hist(a, alpha=0.5, bins=300, density=True, linewidth=3, label='PHD Finger on NCP (I)', histtype='step')
plt.hist(b, alpha=0.5, bins=300, density=True, linewidth=3, label='PHD Finger on NCP', histtype='step')
plt.xlabel('Solvent Accessible Surface Area ($\AA^2$)', fontdict=font)
plt.ylabel('Frequency', fontdict=font)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.title('H3k4me3 Solvent Accessible Surface Area', fontdict=font)
plt.legend(prop={'size': 15})
plt.show()
