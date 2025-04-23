import matplotlib.pyplot as plt
import numpy as np
import matplotlib
font = {'family': 'sans-serif',
        'color':  'black',
        'weight': 'bold',
        'size': 10,
        }

#x,y = np.loadtxt("NTeqrg.dat", usecols=(0,1), unpack=True, comments=('#','@','&'))

#c,d = np.loadtxt("Ebptfeqrg.dat", usecols=(0,1), unpack=True, comments=('#','@','&'))

#e,f = np.loadtxt("2f6jeqrg.dat", usecols=(0,1), unpack=True, comments=('#','@','&'))

x,y1 = np.loadtxt("Notail1_bptfradgyr.dat", usecols=(0,1), unpack=True, comments=('#','@','&'))
y2 = np.loadtxt("Notail2_bptfradgyr.dat", usecols=(1), unpack=True, comments=('#','@','&'))
y3 = np.loadtxt("Notail3_bptfradgyr.dat", usecols=(1), unpack=True, comments=('#','@','&'))
y4 = np.loadtxt("Notail4_bptfradgyr.dat", usecols=(1), unpack=True, comments=('#','@','&'))
y5 = np.loadtxt("Notail5_bptfradgyr.dat", usecols=(1), unpack=True, comments=('#','@','&'))
y0 = np.concatenate((y1[-70000:],y2[-70000:],y3[-70000:],y4[-70000:],y5[-70000:]))

c,d1 = np.loadtxt("2f6jex1_bptfradgyr.dat", usecols=(0,1), unpack=True, comments=('#','@','&'))
d2 = np.loadtxt("2f6jex2_bptfradgyr.dat", usecols=(1), unpack=True, comments=('#','@','&'))
d3 = np.loadtxt("2f6jex3_bptfradgyr.dat", usecols=(1), unpack=True, comments=('#','@','&'))
d4 = np.loadtxt("2f6jex4_bptfradgyr.dat", usecols=(1), unpack=True, comments=('#','@','&'))
d5 = np.loadtxt("2f6jex5_bptfradgyr.dat", usecols=(1), unpack=True, comments=('#','@','&'))
d0 = np.concatenate((d1[-70000:],d2[-70000:],d3[-70000:],d4[-70000:],d5[-70000:]))

e,f1 = np.loadtxt("E1_bptfradgyr.dat", usecols=(0,1), unpack=True, comments=('#','@','&'))
f2 = np.loadtxt("E2_bptfradgyr.dat", usecols=(1), unpack=True, comments=('#','@','&'))
f3 = np.loadtxt("E3_bptfradgyr.dat", usecols=(1), unpack=True, comments=('#','@','&'))
f4 = np.loadtxt("E4_bptfradgyr.dat", usecols=(1), unpack=True, comments=('#','@','&'))
f5 = np.loadtxt("E5_bptfradgyr.dat", usecols=(1), unpack=True, comments=('#','@','&'))
f0 = np.concatenate((f1[-70000:],f2[-70000:],f3[-70000:],f4[-70000:],f5[-70000:]))

plt.figure(figsize=(3.25,3.25))

plt.hist(y0, alpha=0.5, linewidth=2, density=True, bins=300, histtype='step', color='purple', label='Free')

plt.hist(d0, alpha=0.5, linewidth=2, density=True, bins=300, histtype='step', color='orange', label='+Peptide')

plt.hist(f0, alpha=0.5, bins=300, linewidth=2, density=True, histtype='step', color='olive', label='+NCP')

plt.xticks(fontsize=8)
plt.yticks(fontsize=8)

plt.xlabel('RoG ($\AA$)', fontdict=font)
plt.ylabel('Normalized Frequency', fontdict=font)

plt.title('BPTF Radius of Gyration (RoG)', fontdict=font)
plt.legend(loc='upper left', fontsize=8)

plt.tight_layout()
#plt.margins(x=0)

plt.savefig('histrg.pdf')
plt.savefig('histrg.png')
plt.savefig('histrg.svg')
plt.show()
