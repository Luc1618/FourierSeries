import sfourier as sf
from numpy import cos, sin, log, abs

f = lambda x: log(abs(x))

F = sf.SFourier(f)

F.plot_fourier(10, 100)