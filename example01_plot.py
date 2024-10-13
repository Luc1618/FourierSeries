import sfourier as sf
from numpy import cos, sin, log, abs

def f(x):
    return x**3

F = sf.SFourier(f)

F.plot_fourier(20, 100)