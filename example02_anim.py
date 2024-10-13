import sfourier as sf
from functionsForExamples import crazy


F = sf.SFourier(crazy)

F.animation_fourier(
    L = 30,
    Nsum = 250,
    name = 'testeFourier02',
    fps = 20,
    save = True,
    typeSave = 'mp4'
)