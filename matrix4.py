import utils as ut
import tuple as tp
class Matrix4:
  def __init__(self, a11=0, a12=0, a13=0, a14=0,
               a21=0, a22=0, a23=0, a24=0,
               a31=0, a32=0, a33=0, a34=0,
               a41=0, a42=0, a43=0, a44=0):
    
    self.mat = [
      [a11, a12, a13, a14],
      [a21, a22, a23, a24],
      [a31, a32, a33, a34],
      [a41, a42, a43, a44]
    ]

  def at(self, row, collumn):
    if (row < 0 or row >= 4) and (collumn < 0 or collumn >= 4):
      print('Matrix row or collumn index out of range')
      return
    return self.mat[row][collumn]

  def identity(self):
    self.mat = [
      [1, 0, 0, 0],
      [0, 1, 0, 0],
      [0, 0, 1, 0],
      [0, 0, 0, 1]
    ]

    return self
  
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

    return M
  
  def tupleMultiply(self, other: tp.Tuple) -> tp.Tuple:
    t = tp.Tuple()
    for r in range(4):
      temp = self.mat[r][0] * other.componentAt(0) + \
              self.mat[r][1] * other.componentAt(1) + \
              self.mat[r][2] * other.componentAt(2) + \
              self.mat[r][3] * other.componentAt(3)
      t.setComponentAt(r, temp)

    return t
  
  def transpose(self):
    M = Matrix4()
    for r in range(4):
      for c in range(4):
        M.mat[c][r] = self.at(r, c)

    return M