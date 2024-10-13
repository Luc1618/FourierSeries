from functionsForExamples import tower
import sfourier as sf

F = sf.SFourier(tower)

F.plot_fourier(10, 30)