import utils as ut
from tuple3d import Tuple3D
from matrix3 import Matrix3
class Matrix4:
  def __init__(self, a11: float=1, a12: float=0, a13: float=0, a14: float=0,
                     a21: float=0, a22: float=1, a23: float=0, a24: float=0,
                     a31: float=0, a32: float=0, a33: float=1, a34: float=0,
                     a41: float=0, a42: float=0, a43: float=0, a44: float=1):
    
    self.mat = [
      [a11, a12, a13, a14],
      [a21, a22, a23, a24],
      [a31, a32, a33, a34],
      [a41, a42, a43, a44]
    ]

  def at(self, row: int, col: int) -> float:
    if (row < 0 or row >= 4) and (col < 0 or col >= 4):
      print('Matrix row or collumn index out of range')
      return
    return self.mat[row][col]

  def identity(self) -> "Matrix4":
    identity = Matrix4()

    return self.matrixMultiply(identity)
  
  def __eq__(self, other: "Matrix4") -> bool:
    return(
      ut.equal(self.mat[0][0], other.mat[0][0]) and
      ut.equal(self.mat[0][1], other.mat[0][1]) and
      ut.equal(self.mat[0][2], other.mat[0][2]) and
      ut.equal(self.mat[0][3], other.mat[0][3]) and
      ut.equal(self.mat[1][0], other.mat[1][0]) and
      ut.equal(self.mat[1][1], other.mat[1][1]) and
      ut.equal(self.mat[1][2], other.mat[1][2]) and
      ut.equal(self.mat[1][3], other.mat[1][3]) and
      ut.equal(self.mat[2][0], other.mat[2][0]) and
      ut.equal(self.mat[2][1], other.mat[2][1]) and
      ut.equal(self.mat[2][2], other.mat[2][2]) and
      ut.equal(self.mat[2][3], other.mat[2][3]) and
      ut.equal(self.mat[3][0], other.mat[3][0]) and
      ut.equal(self.mat[3][1], other.mat[3][1]) and
      ut.equal(self.mat[3][2], other.mat[3][2]) and
      ut.equal(self.mat[3][3], other.mat[3][3])
    )
  
  def matrixMultiply(self, other: "Matrix4") -> "Matrix4":
    M = Matrix4()
    for r in range(4):
      for c in range(4):
        temp = self.mat[r][0] * other.at(0, c) + \
               self.mat[r][1] * other.at(1, c) + \
               self.mat[r][2] * other.at(2, c) + \
               self.mat[r][3] * other.at(3, c)
        M.mat[r][c] = temp

    self.mat = M.mat
    return self
  
  def tupleMultiply(self, other: Tuple3D) -> Tuple3D:
    t = Tuple3D()
    for r in range(4):
      temp = self.mat[r][0] * other.componentAt(0) + \
              self.mat[r][1] * other.componentAt(1) + \
              self.mat[r][2] * other.componentAt(2) + \
              self.mat[r][3] * other.componentAt(3)
      t.setComponentAt(r, temp)

    return t
  
  def transpose(self) -> "Matrix4":
    M = Matrix4()
    for r in range(4):
      for c in range(4):
        M.mat[c][r] = self.at(r, c)

    return M
  
  def submatrix(self, row: int, col: int) -> Matrix3:
    if (row < 0 or row >= 4) and (col < 0 or col >= 4):
      print('Matrix row or collumn index out of range')
      return
    
    new_values = []
    for r in range(4):
      if r == row:
        continue
      for c in range(4):
        if c == col:
          continue
        new_values.append(self.mat[r][c])

    return Matrix3(new_values[0], new_values[1], new_values[2],
                   new_values[3], new_values[4], new_values[5],
                   new_values[6], new_values[7], new_values[8])
  
  def minor(self, row: int, col: int) -> float:
    M = self.submatrix(row, col)
    return M.determinant()
  
  def cofactor(self, row: int, col: int):  
    minor = self.minor(row, col)
    if (row + col) % 2 == 1:
      return -minor
    
    return minor
  
  def determinant(self) -> float:
    det = self.at(0, 0) * self.cofactor(0, 0) + \
          self.at(0, 1) * self.cofactor(0, 1) + \
          self.at(0, 2) * self.cofactor(0, 2) + \
          self.at(0, 3) * self.cofactor(0, 3)

    return det
  
  def invertible(self) -> bool:
    if self.determinant() == 0:
      return False
    
    return True
  
  def inverse(self) -> "Matrix4":
    if not self.invertible():
      return self
    
    M2 = Matrix4()
    for row in range(4):
      for col in range(4):
        c = self.cofactor(row, col)

        # note that "col, row" here, instead of "row, col",
        # accomplishes the transpose operation!
        M2.mat[col][row] = c / self.determinant()

    return M2
  
  def translation(self, x: float, y: float, z: float) -> "Matrix4":
    translation = Matrix4(a14=x, a24=y, a34=z)

    return self.matrixMultiply(translation)
  
  def scaling(self, x: float, y: float, z: float) -> "Matrix4":
    scaling_matrix = Matrix4(a11=x, a22=y, a33=z)

    return self.matrixMultiply(scaling_matrix)
  
  def reflectX(self) -> "Matrix4":
    scaling_matrix = Matrix4().scaling(-1, 1, 1)

    return self.matrixMultiply(scaling_matrix)
  
  def reflectY(self) -> "Matrix4":
    scaling_matrix = Matrix4().scaling(1, -1, 1)

    return self.matrixMultiply(scaling_matrix)
  
  def reflectZ(self) -> "Matrix4":
    scaling_matrix = Matrix4().scaling(1, 1, -1)

    return self.matrixMultiply(scaling_matrix)
  
  def reflectOrigin(self) -> "Matrix4":
    scaling_matrix = Matrix4().scaling(-1, -1, -1)

    return self.matrixMultiply(scaling_matrix)

    
    