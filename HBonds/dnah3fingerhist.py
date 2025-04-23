import matplotlib.pyplot as plt
import numpy as np
font = {'family': 'sans-serif',
        'color':  'black',
        'weight': 'normal',
        'size': 28,
        }
#x = np.loadtxt("NoTailnoB.dat", usecols=(1), unpack=True, comments=('#','@','&'))
	#The only difference this time is since we are plotting histograms, we only need one data column
y = np.loadtxt("EnoBall_dnah3bptf.dat", usecols=(1), unpack=True, comments=('#','@','&'))
z = np.loadtxt("Eall_dnah3bptf.dat", usecols=(1), unpack=True, comments=('#','@','&'))
#plt.hist(x, alpha=0.5, bins=300, density=True, label='NCP', histtype='step')
	#as before, alpha specifies transparency
	#bins are effectively the "resolution" of your histogram - higher bin counts should result in a smoother curve, to a point
	#density=True normalizes the data
	#histtype='step' avoids filling in the histogram color, which is the default, and only graphs the value
plt.hist(y, alpha=0.5, bins=109, density=True, label='PHD + NCP', histtype='step')
plt.hist(z, alpha=0.5, bins=126, density=True, label='BPTF + NCP', histtype='step')
plt.xlabel('Number of Hydrogen Bonds', fontdict=font)
plt.ylabel('Frequency', fontdict=font)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.title('DNA, H3 and PHD Finger Hydrogen Bonds', fontdict=font)
plt.legend(prop={'size': 15})
plt.show()
