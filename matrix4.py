import utils as ut
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

  def at(self, r, c):
    if (r < 0 or r >= 4) and (c < 0 or c >= 4):
      print('Matrix row or collumn index out of range')
      return
    return self.mat[r][c]

  def identity(self):
    self.mat = [
      [1, 0, 0, 0],
      [0, 1, 0, 0],
      [0, 0, 1, 0],
      [0, 0, 0, 1]
    ]

    return self.mat
  
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