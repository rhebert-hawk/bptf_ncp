import matplotlib.pyplot as plt
import numpy as np
font = {'family': 'sans-serif',
        'color':  'black',
        'weight': 'normal',
        'size': 28,
        }
a = np.loadtxt("Nucall_dna.dat", usecols=(1), unpack=True, comments=('#','@','&'))
b = np.loadtxt("EnoBall_dna.dat", usecols=(1), unpack=True, comments=('#','@','&'))
c = np.loadtxt("Eall_dna.dat", usecols=(1), unpack=True, comments=('#','@','&'))
d = max(a)-min(a)
e = max(b)-min(b)
f = max(c)-min(c)
plt.hist(a, alpha=0.5, bins=int(d), density=True, label='NCP', histtype='step')
	#as before, alpha specifies transparency
	#bins are effectively the "resolution" of your histogram - higher bin counts should result in a smoother curve, to a point
	#density=True normalizes the data
	#histtype='step' avoids filling in the histogram color, which is the default, and only graphs the value
plt.hist(b, alpha=0.5, bins=int(e), density=True, label='PHD + NCP', histtype='step')
plt.hist(c, alpha=0.5, bins=int(f), density=True, label='BPTF + NCP', histtype='step')
plt.xlabel('Number of Hydrogen Bonds', fontdict=font)
plt.ylabel('Frequency', fontdict=font)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.title('DNA Internal Hydrogen Bonds', fontdict=font)
plt.legend(prop={'size': 15})
plt.show()
