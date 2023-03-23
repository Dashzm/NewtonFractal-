import numpy as np
import math as math
import PIL.Image as im
import random as rand

def grid_gen(xmain, xmax, nx, ymain, ymax, ny):
  xstep = np.linspace(xmain, xmax, nx)
  ystep = np.linspace(ymain, ymax, ny)

  return xstep[:, None] + 1j*ystep


def f_cubic(x):
  return (x**6)-1


def fprime_cubic(x):
  return 6*x**5


def newton_iter(x, f=f_cubic, fprime=fprime_cubic):
  return x - f(x)/fprime(x)

def randColor():
  color = (rand.randint(0,255),rand.randint(0,255),rand.randint(0,255))

def classify(p):
  z0 = -1
  z1 = 1
  z2 = -(1/2) - ((1j*math.sqrt(3))/2)
  z3 = (1/2) + ((1j*math.sqrt(3))/2)
  z4 = (1/2) - ((1j*math.sqrt(3))/2)
  z5 = -(1/2) + ((1j*math.sqrt(3))/2)
  
  if np.isclose(p, z0):
    return (0xF6,0xA9,0x61)
  elif np.isclose(p, z1):
    return (0xE5,0x6B,0x5E)
  elif np.isclose(p, z2):
    return (0xBB,0x40,0x5C)
  elif np.isclose(p,z3):
    return (0x84,0x36,0x60)
  elif np.isclose(p, z4):
    return (0x58,0x31,0x68)
  elif np.isclose(p, z5):
    return (0x3A,0x22,0x5E)
  else:
    return (0, 0, 0)

def main():
  size_x = 800
  size_y = 800
  
  grid = grid_gen(-2, 2, size_x, -2, 2, size_y)

  for _ in range(100):
    grid = newton_iter(grid)

  image = im.new('RGB', (size_x, size_y))
  px = image.load()

  for i in range(size_x):
      for j in range(size_y):
        px[i, j] = classify(grid[i, j])

  image.save("fractal.png")

if __name__ == '__main__':
  main()
    
