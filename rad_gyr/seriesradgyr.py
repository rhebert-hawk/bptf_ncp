import matplotlib.pyplot as plt
import numpy as np
import matplotlib
font = {'family': 'sans-serif',
        'color':  'black',
        'weight': 'normal',
        'size': 28,
        }
x,y = np.loadtxt("NTrg.dat", usecols=(0,1), unpack=True, comments=('#','@','&'))
#a,b = np.loadtxt("Abptfrg.dat", usecols=(0,1), unpack=True, comments=('#','@','&'))
c,d = np.loadtxt("Ebptfrg.dat", usecols=(0,1), unpack=True, comments=('#','@','&'))
e,f = np.loadtxt("2f6jrg.dat", usecols=(0,1), unpack=True, comments=('#','@','&'))
plt.plot(x/100, y, alpha=0.5, label='isolated BPTF')
plt.plot(e/100, f, alpha=0.5, label='BPTF with H3 fragment')
#plt.plot(a/100, b, alpha=0.5, label='BPTF on NCP (I)')
plt.plot(c/100, d, alpha=0.5, label='BPTF on NCP')
plt.xlabel('Time (ns)', fontdict=font)
plt.ylabel('Distance (Angstroms)', fontdict=font)
plt.axvline(x=1000)
plt.axvline(x=2000)
plt.axvline(x=3000)
plt.axvline(x=4000)
plt.xticks(np.arange(0, 5500, step=500), fontsize=20)
plt.yticks(fontsize=20)
plt.annotate('Run 1', xy=(350,5), fontsize=20)
plt.annotate('Run 2', xy=(1350,5), fontsize=20)
plt.annotate('Run 3', xy=(2350,5), fontsize=20)
plt.annotate('Run 4', xy=(3350,5), fontsize=20)
plt.annotate('Run 5', xy=(4350,5), fontsize=20)
plt.xlim(0,5000)
plt.ylim(0,30)
plt.title('BPTF Radius of Gyration over Time', fontdict=font)
plt.legend(fontsize=14, loc='center right')
plt.margins(x=0)
plt.show()
