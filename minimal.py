#!/usr/bin/env python
# coding: utf-8

import matplotlib.pyplot as plt
import numpy as np
import csv
from latexify import latexify, MyLogFormatter, _example



##### EXAMPLE #####

w = 8./2.54
aspectRatio = 3./4.5
latexify(w, aspectRatio*w) # fig_width=None, fig_height=None

#init
fig, ax = plt.subplots()

#axis configuration
ax.set_xscale("linear") # before the logformatter
ax.set_yscale("log")
# for the ticks
ax.minorticks_on()
ax.tick_params(axis='y', which='minor', direction = 'out',left=True)
ax.tick_params(axis='x', which='minor', direction = 'out', bottom=True)

#format the log axis if used
ax.yaxis.set_major_formatter(MyLogFormatter())
# ax.xaxis.set_major_formatter(MyLogFormatter())

#labels. USE \minus for the minus sign in the exponents
ax.set_xlabel(r'x label')
ax.set_ylabel(r'$f(z)$ (Gpc$^{\minus 3}$ year$^{\minus 1}$)')
#ax.set_title('Merger rate of binaries. $m = 30$ , $\beta = 1$')

#the plots
x = np.linspace(0,5,100)
y = np.exp(-x + 2*np.cos(x) + 2)
ax.plot(x,y,color='C0',linewidth=1,label=r'$f=10^{\minus 2}$')


#the legend
leg = ax.legend(fontsize = 8,loc=3) #, prop={'size': 8})# borderaxespad=0.1)

#save the figure in pdf
fig.tight_layout()
fig.savefig("plot.pdf",bbox_inches='tight',format='pdf')


print(_example())

