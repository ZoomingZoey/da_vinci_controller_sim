import utils as ut
class Matrix2:
  def __init__(self, a11=0, a12=0,
               a21=0, a22=0):
    
    self.mat = [
      [a11, a12],
      [a21, a22]
    ]

  def at(self, r, c):
    if (r < 0 or r >= 2) and (c < 0 or c >= 2):
      print('Matrix row or collumn index out of range')
      return
    return self.mat[r][c]
  
  def determinant(self):
    return (self.mat[0][0] * self.mat[1][1]) - (self.mat[0][1] * self.mat[1][0])
  
  def __eq__(self, other: "Matrix2") -> bool:
    return(
      ut.equal(self.mat[0][0], other.mat[0][0]) and
      ut.equal(self.mat[0][1], other.mat[0][1]) and
      ut.equal(self.mat[1][0], other.mat[1][0]) and
      ut.equal(self.mat[1][1], other.mat[1][1])
    )