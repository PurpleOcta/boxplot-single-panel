#!/usr/bin/env python3


import matplotlib
import matplotlib.pyplot as plt
import numpy as np


# Data. Assign one flat NumPy array per method. Keys will be used as labels.
# For best results, scale values to 1-2 significant digits and adjust the
# y-axis label accordingly.
rand = np.random.default_rng(1234)
data = {
    'Test 1': rand.normal(size=20) * 3 - 1.1,
    'Test 2': rand.normal(size=20) * 2 + 9.2,
    'Test 3': rand.normal(size=20) * 2 + 2.3,
    'Test 4': rand.normal(size=20) * 4,
    'Test 5': rand.normal(size=20) * 2 + 4.1,
    'Test 6': rand.normal(size=20) * 5,
}


# Settings. Set y-axis limit to None for new data, adjust later. For best
# results, use 5-7 y-ticks and set the y-axis limits to values on or half-way
# between grid lines. It is acceptable if some long tails are out-of-range.
ylim = (-10, 15)  # Set to None for new data, adjust later.
ytickmult = 5  # Horizontal grid-line interval.
ytickstart = 0  # Horizontal grid-line start.

linewidth = 1.5
matplotlib.rcParams['axes.linewidth'] = linewidth
matplotlib.rcParams['lines.linewidth'] = linewidth
matplotlib.rcParams['grid.linewidth'] = linewidth
matplotlib.rcParams['xtick.major.width'] = linewidth
matplotlib.rcParams['ytick.major.width'] = linewidth
matplotlib.rcParams['xtick.minor.width'] = linewidth
matplotlib.rcParams['ytick.minor.width'] = linewidth

# Comment the last two lines for a sans-serif font.
matplotlib.rcParams['pdf.fonttype'] = 42  # Remove Type-3 fonts.
matplotlib.rcParams['font.size'] = 7
matplotlib.rcParams['font.family'] = 'serif'
matplotlib.rcParams['mathtext.fontset'] = 'dejavuserif'


# Figure. Optimized to span one column of two-column papers. A temporary
# background color like 'silver' can help visualize margins. Adjust the axis
# offset and dimensions to your data, where 1 is the extent of the figure.
fig = plt.figure(figsize=(3.5, 1.5), facecolor='silver', dpi=300)
ax = fig.add_axes((0.14, 0.13, 0.85, 0.82))  # Left, bottom, width, height.


# Abscissa.
methods = data.keys()
n_methods = len(methods)
xticks = np.arange(1, n_methods + 1)


# Boxplots.
y = np.asarray([d for d in data.values()]).T
handles = ax.boxplot(y)


# Boxplot settings.
plt.setp(handles['boxes'], linewidth=linewidth)
plt.setp(handles['medians'], linewidth=linewidth)
plt.setp(handles['medians'], color='magenta')
plt.setp(handles['whiskers'], linewidth=linewidth)
plt.setp(handles['caps'], linewidth=linewidth)
plt.setp(handles['fliers'], markeredgewidth=linewidth)
plt.setp(handles['fliers'], markeredgecolor='gray')
plt.setp(handles['fliers'], markersize=4)


# Axis settings.
ax.grid(axis='y')
ax.set_ylabel(r'Accuracy ($10^{-3}$)')
ax.set_xticks(xticks)
ax.set_xticklabels(data)
ax.set_xlim(0.5, n_methods + 0.5)

if ytickmult is not None:
    ygrid = matplotlib.ticker.MultipleLocator(ytickmult, offset=ytickstart)
    ax.yaxis.set_major_locator(ygrid)

if ylim is not None:
    ax.set_ylim(ylim)


# Save figure in PDF, SVG, or PNG format. PDF works best for LaTeX. Use
# 300-600 DPI for high-quality PNG exports.
fig.savefig('figure.pdf', facecolor='white', dpi=300)
