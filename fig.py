__doc__ = 'plot module'

import numpy
import scipy
import scipy.stats
import matplotlib
import matplotlib.pyplot as plt


def regressogram(x, y, bins=10, quantiles=[.05, .25, .5, .75, .95]):
    idx = x.argsort()
    x1 = x[idx]
    y1 = y[idx]
    l = len(idx)
    li = int(l / 10)
    y_plot = numpy.zeros([len(quantiles), bins])
    x_plot = numpy.zeros(bins)
    for i in range(bins-1):
        xi = x1[i * li: (i+1) * li]
        yi = y1[i * li: (i+1) * li]
        x_plot[i] = numpy.median(xi)
        y_plot[:, i] = scipy.stats.mstats.mquantiles(yi, quantiles)
    xi = x1[(bins-1) * li:]
    yi = y1[(bins-1) * li:]
    x_plot[-1] = numpy.median(xi)
    y_plot[:, -1] = scipy.stats.mstats.mquantiles(yi, quantiles)
    fig = plt.figure()
    for qi, yi in zip(quantiles, y_plot):
        plt.plot(x_plot, yi, '.-', linewidth=0.5, label=str(qi))
    plt.legend()
    return fig
