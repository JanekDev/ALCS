import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
viols=[[],[],[]]
for x in range(1,4):
    with open(f'output{x}.txt') as file:
        for line in file:
            if '[LOG]' in line:
                viols[x-1].append(float(line.split()[-1]))
#create violin plots for each of the three files
fig,ax=plt.subplots()
ax.violinplot(viols)
#add labels
ax.set_xticks([1,2,3])
ax.set_xticklabels(['default','modification 1','modification 2'])
red_patch=mpatches.Patch(color='red',label='Violin 1')
blue_patch=mpatches.Patch(color='blue',label='Violin 2')
green_patch=mpatches.Patch(color='green',label='Violin 3')
plt.show()


