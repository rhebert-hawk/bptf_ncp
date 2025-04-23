#!/usr/bin/python 

import sys
import math 
import numpy as np
import matplotlib
import matplotlib.pyplot as plt 

y,yerr = np.loadtxt("EnoB_h3_1.dat", usecols=(1,2), unpack=True, comments=('#','@','&'))
f,y1,y1err = np.loadtxt("EnoB_h3_2.dat", usecols=(0,1,2), unpack=True, comments=('#','@','&'))
x = np.array([i for i in range(0,135)])


fig,ax=plt.subplots(figsize=(8.0,4.0))
plt.plot(x, y, color = 'orange',label = "H3K4me3 (Tail1)")
plt.plot(x, y1, color = 'black', label = "H3 (Tail2)")
#plt.plot(y2, color = 'blue', label = "H3(Tail2)")

plt.fill_between(x, y-(yerr/2.2), y+(yerr/2.2),color= 'orange', antialiased='True', alpha=0.3)
plt.fill_between(x, y1-(y1err/2.2), y1+(y1err/2.2),color ='black', antialiased='True', alpha=0.3)
#plt.fill_between(x, y2-error2, y2+error2,color ='blue, antialiased='True', alpha=0.3)
ax.set_ylim(0,17)
ax.set_xlim(0,55)
plt.xticks(np.arange(55),['A1','R2','T3','K4','Q5','T6','A7','R8','K9','S10','T11','G12','G13','K14','A15','P16','R17','K18','Q19','L20','A21','T22','K23','A24','A25','R26','K27','S28','A29','P30','A31','T32','G33','G34','V35','K36','K37','P38','H39','R40','Y41','R42','P43', 'G44', 'T45', 'V46', 'A47', 'L48', 'R49', 'E50', 'I51', 'R52', 'R53', 'Y54', 'Q55' ],rotation='vertical', fontweight='bold')
ax.set_xlabel("Residue",fontsize=13, fontweight='bold')
ax.set_yticklabels([i for i in range(0,18)], fontsize=13, fontweight='bold')
plt.yticks(np.arange(1, 18, 1.0) )
ax.set_ylabel(r"RMSF ($\mathrm{\AA}$)",fontsize=13, fontweight='bold')
plt.axvline(x=36.0, color='k', linestyle='--')
bbox_props = dict(boxstyle="larrow,pad=0.3", fc="papayawhip", ec="k", lw=2)
t = ax.text(33, 8.5, "Tail ", ha="center", va="center",size=14,bbox=bbox_props)
bbox_props = dict(boxstyle="rarrow,pad=0.3", fc="papayawhip", ec="k", lw=2)
t = ax.text(39, 8.5, "Core", ha="center", va="center",size=14,bbox=bbox_props)
ax.legend(loc='upper right',labelspacing=0.1,borderpad=0.1, prop={'weight':'bold'})
plt.tight_layout()
plt.title("Nucleosome + PHD Finger (II)", fontweight='bold')
plt.savefig("EnoBh3.svg",format='svg')
plt.close()

