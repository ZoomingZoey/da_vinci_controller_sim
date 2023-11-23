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

  def identity(self):
    self.mat = [
      [1, 0, 0, 0],
      [0, 1, 0, 0],
      [0, 0, 1, 0],
      [0, 0, 0, 1]
    ]

    return self.mat