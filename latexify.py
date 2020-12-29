import matplotlib.pyplot as plt
import numpy as np
import matplotlib
import matplotlib.ticker
import re

def latexify(fig_width=None, fig_height=None, columns=1, params = None):
    """Set up matplotlib's RC params for LaTeX plotting.
    Call this before plotting a figure.

    Parameters
    ----------
    fig_width : float, optional, inches
    fig_height : float,  optional, inches
    columns : {1, 2}
    """

    # code adapted from http://www.scipy.org/Cookbook/Matplotlib/LaTeX_Examples

    # Width and max height in inches for IEEE journals taken from
    # computer.org/cms/Computer.org/Journal%20templates/transactions_art_guide.pdf

    assert(columns in [1,2])

    if fig_width is None:
        fig_width = 3.39 if columns==1 else 6.9 # width in inches

    if fig_height is None:
        golden_mean = (np.sqrt(5)-1.0)/2.0    # Aesthetic ratio
        fig_height = fig_width*golden_mean # height in inches

    MAX_HEIGHT_INCHES = 8.0
    if fig_height > MAX_HEIGHT_INCHES:
        print("WARNING: fig_height too large:" + fig_height + 
              "so will reduce to" + MAX_HEIGHT_INCHES + "inches.")
        fig_height = MAX_HEIGHT_INCHES

    if params == None:
      params = {'backend': 'ps',
                'text.latex.preamble': r'''\usepackage{gensymb,amsfonts}''',
                'axes.labelsize': 8, # fontsize for x and y labels (was 10)
                'axes.titlesize': 8,
                # 'text.fontsize': 8, # was 10
                'legend.fontsize': 8, # was 10
                'xtick.labelsize': 8,
                'ytick.labelsize': 8,
                'text.usetex': True,
                'figure.figsize': [fig_width,fig_height],
                'font.family': 'serif'
      }
    matplotlib.rcParams.update(params)
    # plt.rc('font', family='serif')
    matplotlib.rcParams["text.latex.preamble"] += r'\DeclareMathSymbol{\minus}{\mathbin}{AMSa}{"39}'


class MyLogFormatter(matplotlib.ticker.LogFormatterMathtext):
    def __call__(self, x, pos=None):
        # call the original LogFormatter
        rv = matplotlib.ticker.LogFormatterMathtext.__call__(self, x, pos)

        # check if we really use TeX
        if matplotlib.rcParams["text.usetex"]:
            # if we have the string ^{- there is a negative exponent
            # where the minus sign is replaced by the short hyphen
            rv = re.sub(r'\^\{-', r'^{\\minus', rv)

        return rv

def _example():
  example = r'''
##### EXAMPLE #####
from latexify import latexify, MyLogFormatter, _example

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
'''
  print(example)