import matplotlib.pyplot as plt
import numpy as np
from matrix4 import Matrix4
from point import Point
from vector import Vector

# Y is up axis

def main():

  # create x, y, z points with a w coordinate
  p1 = Point(0.0, 0.0, 0.0)
  p2 = Point(100.0, -200.0, 0.0)
  p3 = Point(300.0, -100.0, 0.0)

  xpoints = np.array([p1.x, p2.x, p3.x])
  ypoints = np.array([p1.y, p2.y, p3.y])

  plt.plot(xpoints, ypoints)
  plt.axis('equal')  #<-- set the axes to the same scale
  plt.xlim([-500, 500]) #<-- set the x axis limits
  plt.ylim([-500, 500]) #<-- set the y axis limits
  plt.grid(which='major') #<-- plot grid lines

  my_mat = Matrix4()
  print(my_mat.identity())

  plt.show()

if __name__ == '__main__':
  main()

