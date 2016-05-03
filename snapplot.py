import numpy as np
import matplotlib.pyplot as plt 

def snapplot(t, x, a):
    fig = plt.figure(figsize=(15, 4))
    axes = plt.gca()
    axes.set_xlim([np.amin(t), np.amax(t)])
    axes.set_ylim([np.amin(x) - 0.5, np.amax(x) + 0.5])
    plt.plot(t, x, 'k', lw=2)
    plt.xticks(np.arange(np.amin(t), np.amax(t) + 1, 1.0))
    plt.xlabel('t (sec)')
    plt.grid()
    plt.title(a)
