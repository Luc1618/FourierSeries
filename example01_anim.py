import sfourier as sf
from functionsForExamples import squareWave01


F = sf.SFourier(squareWave01)

F.animation_fourier(
    L = 10,
    Nsum = 250,
    name = 'testeFourier',
    fps = 20,
    save = True,
    typeSave = 'mp4'
)