import matplotlib.pyplot as plt
import numpy as np
import utils as ut
from matrix3 import Matrix3
from matrix4 import Matrix4
from point2d import Point2D
from vector2d import Vector2D
from point3d import Point3D
from vector3d import Vector3D

# Y is up axis

def main():

  # create 2D points with a w homogenous coordinate
  # p1 = Point2D(0.0, 0.0)
  # p2 = Point2D(100.0, -200.0)
  # p3 = Point2D(300.0, -100.0)
  p1 = Point2D(0, 10)
  p2 = Point2D(10, 0)
  xpoints = np.array([p1.x, p2.x])
  ypoints = np.array([p1.y, p2.y])

  plt.plot(xpoints, ypoints)
  plt.plot(xpoints, ypoints, 'ok')
  plt.axis('equal')  #<-- set the axes to the same scale
  plt.xlim([-10, 10]) #<-- set the x axis limits
  plt.ylim([-10, 10]) #<-- set the y axis limits
  plt.grid(which='major') #<-- plot grid lines

  plt.show()

if __name__ == '__main__':
  main()

