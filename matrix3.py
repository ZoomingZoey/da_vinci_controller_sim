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