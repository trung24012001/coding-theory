import numpy as np
   
mat =[[1, 11, 12],
      [4, 23, 2],
      [17, 15, 9]]
n = 26
determinant = np.linalg.det(mat)
invert = np.linalg.inv(mat).T
cofactor = invert * determinant
print(determinant)
print(21 * cofactor % n)