import numpy as np
import matplotlib.pyplot as plt


def plot(signal=[-1, 0, 1]):

    i = 0

    for chip in signal:
        t = np.arange(i * 2 * np.pi, (i * 2 + 2) * np.pi, 0.01)

        if chip < 0:
            s = np.sin(t)
        elif chip > 0:
            s = np.sin(t - np.pi)
        else:
            s = np.zeros_like(t)

        plt.plot(t, s)
        i += 1

    plt.show()
    fig = plt.gcf()
    # plt.show() <- don't show window!
    return fig
