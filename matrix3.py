from matrix2 import Matrix2
from tuple2d import Tuple2D
import utils as ut
import math
class Matrix3:
  def __init__(self, a11: float=1, a12: float=0, a13: float=0,
                     a21: float=0, a22: float=1, a23: float=0,
                     a31: float=0, a32: float=0, a33: float=1) -> None:
    
    self.mat = [
      [a11, a12, a13],
      [a21, a22, a23],
      [a31, a32, a33]
    ]

  def at(self, row: int, col: int) -> float:
    if (row < 0 or row >= 3) and (col < 0 or col >= 3):
      print('Matrix row or collumn index out of range')
      return
    return self.mat[row][col]
  
  def submatrix(self, row: int, col: int) -> Matrix2:
    if (row < 0 or row >= 3) and (col < 0 or col >= 3):
      print('Matrix row or collumn index out of range')
      return
    
    new_values = []
    for r in range(3):
      if r == row:
        continue
      for c in range(3):
        if c == col:
          continue
        new_values.append(self.mat[r][c])

    return Matrix2(new_values[0], new_values[1],
                   new_values[2], new_values[3])
  
  def __eq__(self, other: "Matrix3") -> bool:
    return(
      ut.equal(self.mat[0][0], other.mat[0][0]) and
      ut.equal(self.mat[0][1], other.mat[0][1]) and
      ut.equal(self.mat[0][2], other.mat[0][2]) and
      ut.equal(self.mat[1][0], other.mat[1][0]) and
      ut.equal(self.mat[1][1], other.mat[1][1]) and
      ut.equal(self.mat[1][2], other.mat[1][2]) and
      ut.equal(self.mat[2][0], other.mat[2][0]) and
      ut.equal(self.mat[2][1], other.mat[2][1]) and
      ut.equal(self.mat[2][2], other.mat[2][2])
    )
  
  def minor(self, row: int, col: int) -> float:
    if (row < 0 or row >= 3) and (col < 0 or col >= 3):
      print('Matrix row or collumn index out of range')
      return
    
    M = self.submatrix(row, col)
    return M.determinant()
  
  def cofactor(self, row: int, col: int) -> float:
    if (row < 0 or row >= 3) and (col < 0 or col >= 3):
      print('Matrix row or collumn index out of range')
      return
    
    minor = self.minor(row, col)
    if (row + col) % 2 == 1:
      return -minor
    
    return minor
  
  def determinant(self) -> float:
    det = self.at(0, 0) * self.cofactor(0, 0) + \
          self.at(0, 1) * self.cofactor(0, 1) + \
          self.at(0, 2) * self.cofactor(0, 2)

    return det
  
  def matrixMultiply(self, other: "Matrix3") -> "Matrix3":
    M = Matrix3()
    for r in range(3):
      for c in range(3):
        temp = self.mat[r][0] * other.at(0, c) + \
               self.mat[r][1] * other.at(1, c) + \
               self.mat[r][2] * other.at(2, c)
        M.mat[r][c] = temp

    self.mat = M.mat
    return self
  
  def tupleMultiply(self, other: Tuple2D) -> Tuple2D:
    t = Tuple2D()
    for r in range(3):
      temp = self.mat[r][0] * other.componentAt(0) + \
              self.mat[r][1] * other.componentAt(1) + \
              self.mat[r][2] * other.componentAt(2)
      t.setComponentAt(r, temp)

    return t
  
  def identity(self) -> "Matrix3":
    identity = Matrix3()

    return self.matrixMultiply(identity)
  
  def transpose(self) -> "Matrix3":
    M = Matrix3()
    for r in range(3):
      for c in range(3):
        M.mat[c][r] = self.at(r, c)

    return M
  
  def invertible(self) -> bool:
    if self.determinant() == 0:
      return False
    
    return True
  
  def inverse(self) -> "Matrix3":
    if not self.invertible():
      return self
    
    M2 = Matrix3()
    for row in range(3):
      for col in range(3):
        cofactor = self.cofactor(row, col)

        # note that "col, row" here, instead of "row, col",
        # accomplishes the transpose operation!
        M2.mat[col][row] = cofactor / self.determinant()

    return M2
  
  def translation(self, x: float, y: float) -> "Matrix3":
    translation = Matrix3(a13=x, a23=y)

    return self.matrixMultiply(translation)
  
  def scaling(self, x: float, y: float) -> "Matrix3":
    scaling_matrix = Matrix3(a11=x, a22=y)

    return self.matrixMultiply(scaling_matrix)
  
  def reflectX(self) -> "Matrix3":
    scaling_matrix = Matrix3().scaling(-1, 1)

    return self.matrixMultiply(scaling_matrix)
  
  def reflectY(self) -> "Matrix3":
    scaling_matrix = Matrix3().scaling(1, -1)

    return self.matrixMultiply(scaling_matrix)
  
  def reflectOrigin(self) -> "Matrix3":
    scaling_matrix = Matrix3().scaling(-1, -1)

    return self.matrixMultiply(scaling_matrix)
  
  def rotationZ(self, radians: float) -> "Matrix3":
    rotation_matrix = Matrix3(a11=math.cos(radians), a12=-math.sin(radians),
                              a21=math.sin(radians), a22=math.cos(radians))

    return self.matrixMultiply(rotation_matrix)
        