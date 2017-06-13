import numpy as np
import matplotlib.pyplot as plt


signal = [-1, 0, 1, 1, -1, -1, 1, 0]
i = 0

for chip in signal:
    t = np.arange(i * 2 * np.pi, (i * 2 + 2) * np.pi, 0.01)
    s = np.sin(t - np.pi * (i % 2))
    plt.plot(t, s)
    i += 1

plt.show()
