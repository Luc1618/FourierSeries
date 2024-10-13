__all__ = ['SFourier']

# Dependences
class SFourier:
  def __init__(self, f):
    """
    Args
    ------
    f :function
      Função que será aproximada pela soma parcial da série de Fourier.
    """
    self.f = f

### Method 1
  def fourier_cordenadas(self, L, Nsum):
    """
    Função que calcula as coordenadas da soma parcial da série fourier no intervalo [-L, L].

    Args
    ------
    L : float 
      Gera o intervalo [-L, L], em que a soma parcial será calculada.
    Nsum: int
      Número de somas parciais.

    Returns
    -------
    X : ndarray 
      Coordenadas do eixo X.
    Y: ndarray
      Coordenadas do eixo Y.
    YY: ndarray 
      Matriz de passos do somatório.
    """

    from numpy import linspace, trapz, zeros, ones, cos, sin, pi

    # Evitando alguns erros.
    L = abs(L)
    Nsum = abs(int(Nsum))

    # Vetor dominio no intervalo [-L, L].
    X = linspace(-L, L, 10000)

    # Matriz de passos ! ! !
    YY = zeros((Nsum + 1, 10000))

    # Termo inicial da série de Fourier.
    a0 = (1/L)*trapz(self.f(X), X)

    # Termo inicial da matriz de passos.
    YY[0,] = (a0/2)*ones(10000)

    # For que representa a soma do n-ésimo termo da série.
    for n in range(1, Nsum+1):
      # Funções trigonométricas.
      cos_n = lambda x: cos(n*pi*x/L)
      sen_n = lambda x: sin(n*pi*x/L)
      fcos_n = lambda x: self.f(x)*cos_n(x)
      fsen_n = lambda x: self.f(x)*sen_n(x)

      # Coeficientes de Fourier.
      # Integração de -L a L.
      an = (1/L)*trapz(fcos_n(X), X)
      bn = (1/L)*trapz(fsen_n(X), X)

      # Vetor imagem que recebe o termo do somatório.
      YY[n,] = an*cos_n(X) + bn*sen_n(X)


    # Vetor imagem da série de Fourier.
    Y = YY.sum(axis = 0)

    # Retorna as coordenadas X e Y da série.
    return X, Y, YY

### Method 2
  def plot_fourier(self, L, Nsum, plotf = True):
    """
    Plota o gráfico da soma parcial da série de fourier.

    Args
    ------
    L : float 
      Gera o intervalo [-L, L], em que a soma parcial será calculada.
    Nsum: int
      Número de somas parciais.
    plotf : bool, optional
      Se True, plota o gráfico da função original f.

    """

    from matplotlib.pyplot import figure, title, xlabel, ylabel, xlim, grid, plot, legend, show, close

    # Evitando erros.
    L = abs(L)
    Nsum = abs(int(Nsum))

    # Configurações do gráfico
    figure(figsize=(10, 7))
    title(f"Fourier series (Nsum = {Nsum})")
    xlabel('x')
    ylabel('y')
    xlim(-L, L)
    grid()

    # Cálculo da soma parcial da série de Fourier para o domínio [-L, L].
    X, Y, _ = self.fourier_cordenadas(L, Nsum)

    # Se True, plota o gráfico da função original.
    plot(X, Y, color = 'black', lw = 1.5, zorder = 2)
    if plotf:
      plot(X, self.f(X), color = 'orange', lw = 1.5, zorder = 1)
      legend(["F(x)", "f(x)"], loc = 'upper right', title = "functions")

    
    # Plot da série

    show()
    close()

    return

### Method 3
  def animation_fourier(self, L, Nsum, plotf = True, name = 'S_Fourier', fps = 30, save = True, typeSave = 'gif'):
    """
      Animação da soma parcial da série de Fourier convergindo para a função original.

      Args
      ------
      L: float
        Gera o intervalo [-L, L], em que a soma parcial será calculada.
      Nsum: int
        Número de somas parciais
      plotf: bool, optional
        Se True, plota o gráfico da função original f.
      name: string, optional
        Nome do arquivo;
      fps: int, optional
        Frames por segundo;
      save: bool, optional
        Se True, salva a animação;
      typeSave: string, optional
        Tipo de arquivo da animação, 'mp4' ou 'gif';
    """

    from matplotlib.pyplot import figure, title, xlabel, ylabel, xlim, ylim, grid, plot, legend, show, close
    from matplotlib.animation import FuncAnimation
    # Evitando alguns erros.
    L = abs(L)
    Nsum = abs(int(Nsum))

    # Define as configurações do gráfico e da animação.
    fig = figure(figsize=(10, 7))
    line, = plot([], [], lw = 1.5, color = 'black', zorder = 2)
    xlabel('x')
    ylabel('y')
    grid()

    X, _, YY = self.fourier_cordenadas(L, Nsum)

    xlim(-L, L)
    ylim(min(self.f(X)) - .5, max(self.f(X)) + .5)

    # Se True, plota o gráfico da função o original.
    if plotf:
      plot(X, self.f(X), color = 'orange', lw = 1.5, zorder = 1)
      # Exibindo legendas
      legend(["F(x)", "f(x)"], loc = 'upper right', title = 'functions')

    # Função que realiza o update na animação.
    def update(i):
      X, Y, _ = self.fourier_cordenadas(L, i)
      line.set_data(X, YY[0:i].sum(axis = 0))
      title(f'Fourier series (Nsum = {i})')
      return line,

    # Animação
    anim = FuncAnimation(fig, update, range(1, Nsum+1), blit=True)

    # Salva a animação caso queira salvar.
    if save:
      nome_arquivo = './' + str(name) + '.' + str(typeSave)
      if typeSave == 'mp4':
        anim.save(nome_arquivo, writer="ffmpeg", fps = fps)
      elif typeSave == 'gif':
        anim.save(nome_arquivo, writer="pillow", fps = fps)

    show()
    close()

    return
  
