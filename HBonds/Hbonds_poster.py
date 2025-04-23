import matplotlib.pyplot as plt
import numpy as np

font = {'family': 'sans-serif',
        'color':  'black',
        'weight': 'bold',
        'size': 24,
        }
        
label = ['NCP', 'PHD + NCP', 'BPTF + NCP']
h3 = np.array([49.1, 41.37, 41.02])
h4=np.array([25.9, 23, 23.41])
h2a = np.array([30.52, 25.57, 24.63])
h2b = np.array([29.59, 25.57, 25.43])


h3_sd = np.array([2.56, 2.33, 2.39])
h4_sd = np.array([1.65,1.73,1.75])
h2a_sd = np.array([1.97,2.17,1.90])
h2b_sd = np.array([2.14, 2.10, 1.94])

width = 0.35       # the width of the bars: can also be len(x) sequence


plt.figure(figsize=(8.5,6.47))


plt.bar(label, h4, width, yerr=h4_sd, capsize = 3, bottom=h2a+h2b+h3, label='H4', color='green')
plt.bar(label, h3, width, yerr=h3_sd, capsize = 3, bottom=h2a+h2b, label='H3', color='blue')
plt.bar(label, h2b, width, yerr=h2b_sd, capsize = 3, bottom=h2a, label='H2b', color='red')
plt.bar(label, h2a, width, yerr=h2a_sd, capsize = 3, label="H2a", color='yellow')
plt.ylabel('Hydrogen Bonds', fontdict=font)
plt.title('Histone Hydrogen Bonds with DNA', fontdict=font)
plt.xticks(fontsize=18, fontweight='bold')
plt.yticks(fontsize=18, fontweight='bold')
plt.legend(bbox_to_anchor=(1.0, 0.75), fontsize=18)
plt.tight_layout()

plt.savefig('Hbonds_poster.png')
plt.savefig('Hbonds_poster.pdf')
plt.show()






#import matplotlib.pyplot as plt
#import numpy as np

#font = {'family': 'sans-serif',
#        'color':  'black',
#        'weight': 'bold',
#        'size': 24,
#        }

#label = ['NCP', 'PHD + NCP', 'BPTF + NCP']
#y = np.array([587, 601, 671])
#yalt=np.array([587, 588, 603])
#a = np.array([0, 13, 68])
#y1 = np.array([68, 64, 66])
#y2 = np.array([135, 115, 118])
#y3 = np.array([0, 1, 1])
#y4 = np.array([0, 5, 6])

#internal_sd = np.array([7, 8, 9])
#yalt_sd = np.array([7,8,8])
#bptf_sd = np.array([0,1,3])
#interhistone_sd = np.array([3, 3, 3])
#dna_histone_sd = np.array([4, 4, 4])
#dna_tf_sd = np.array([0, 1, 1])
#histone_tf_sd = np.array([0, 1, 1])

#width = 0.35       # the width of the bars: can also be len(x) sequence

#plt.figure(figsize=(6.29,6.47))
#fig, ax = plt.subplots()
#ax.bar(label, y, width, yerr=internal_sd, label="Internal bonds")
#ax.bar(label, y1, width, yerr=interhistone_sd,label='Interhistone bonds')
#ax.bar(label, y2, width, yerr=dna_histone_sd, capsize=3, label='DNA-Histone bonds')
#ax.bar(label, y3, width, yerr=dna_tf_sd, bottom=y1+y2, label='DNA-Reader bonds')
#ax.bar(label, y4, width, yerr=histone_tf_sd, capsize=3, bottom=y2, label='Histone-Reader bonds')


#ax.set_ylabel('Hydrogen Bonds', fontdict=font)
#ax.set_title('Differences in Hydrogen Bonds', fontdict=font)
#plt.xticks(fontsize=18, fontweight='bold')
#plt.yticks(fontsize=18, fontweight='bold')
#ax.legend(loc='upper right', fontsize=18)

#plt.savefig('Hbonds_dif.pdf')
#plt.show()
#plt.tight_layout()
#This one appears to be the most useful


