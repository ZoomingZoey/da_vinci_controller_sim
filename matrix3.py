from matrix2 import Matrix2
import utils as ut
class Matrix3:
  def __init__(self, a11=0, a12=0, a13=0,
               a21=0, a22=0, a23=0,
               a31=0, a32=0, a33=0):
    
    self.mat = [
      [a11, a12, a13],
      [a21, a22, a23],
      [a31, a32, a33]
    ]

  def at(self, r, c):
    if (r < 0 or r >= 3) and (c < 0 or c >= 3):
      print('Matrix row or collumn index out of range')
      return
    return self.mat[r][c]
  
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
  
  def minor(self, row: int, col: int):
    if (row < 0 or row >= 3) and (col < 0 or col >= 3):
      print('Matrix row or collumn index out of range')
      return
    
    M = self.submatrix(row, col)
    return M.determinant()
  
  def cofactor(self, row: int, col: int):
    if (row < 0 or row >= 3) and (col < 0 or col >= 3):
      print('Matrix row or collumn index out of range')
      return
    
    minor = self.minor(row, col)
    if row + col % 2 == 1:
      return -minor
    
    return minor
        