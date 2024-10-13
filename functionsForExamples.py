from numpy import piecewise, pi, sin, cos, exp, tanh


squareWave01 = lambda x: piecewise(x,
 [
  (-2*pi <= x) & (x < -pi),
  (-pi <= x) & (x < 0),
  (0 <= x) & (x <= pi),
  (pi < x) & (x <= 2*pi)
  ],
 [1, -1, 1, -1])

ladder = lambda x: piecewise(x,
      [(x < -10),
      (x >= -10) & (x < -5),
      (x >= -5) & (x < 0),
      (x >= 0) & (x < 5),
      (x >= 5) & (x <= 10),
      x > 10],
    [0, -5, -2.5, 2.5, 5, 10])

squareWave02 = lambda x: piecewise(x,
                        [x < -10,
                         (x >= -10) & (x < -5),
                         (x >= -5) & (x < 0),
                         (x >= 0) & (x < 5),
                         (x >= 5) & (x < 10),
                         x >= 10],
                        [-1, 1, -1, 1, -1, 1])

tower = lambda x: piecewise(x,
                        [(x < -8),
                         (x >= -8) & (x < -7),
                         (x >= -7) & (x < -6),
                         (x >= -6) & (x < -5),
                         (x >= -5) & (x < -4),
                         (x >= -4) & (x < -3),
                         (x >= -3) & (x < -2),
                         (x >= -2) & (x < -1),
                         (x >= -1) & (x < 0),
                         (x >= 0) & (x < 1),
                         (x >= 1) & (x < 2),
                         (x >= 2) & (x < 3),
                         (x >= 3) & (x < 4),
                         (x >= 4) & (x < 5),
                         (x >= 5) & (x < 6),
                         (x >= 6) & (x < 7),
                         (x >= 7) & (x < 8),
                         (x >= 8)],
                        [0, 1, 2, 3, 4, 5, 6, 7, 8, 8, 7, 6, 5, 4, 3, 2, 1, 0])

crazy = lambda x: piecewise(x,
    [(x < -5), 
    (x >= -5) & (x < 0), 
    (x >= 0) & (x < 10),  
    (x >= 10)],
    [lambda x: sin(x) + 0.1*x, 
    lambda x: cos(x) + x**2 / 10,  
    lambda x: exp(-x) * cos(x), 
    lambda x: tanh(x / 5) + sin(x / 3)])
   