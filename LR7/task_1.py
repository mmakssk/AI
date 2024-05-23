import numpy as np
import matplotlib.pyplot as pl

x = np.linspace(-500, 500, 10000)

fig, plot_one = pl.subplots()
plot_one.plot(x, 5 * (x ** 2) - 2 * x + 8, color="#80AC55", ls="-", label="5x^2 - 2x + 8", alpha=0.69)
plot_one.legend(loc=3)
plot_one.set_xlabel('X')
plot_one.set_ylabel('Y')
plot_one.set_xlim([-25,50])
plot_one.set_ylim([-10,50])

pl.show()
