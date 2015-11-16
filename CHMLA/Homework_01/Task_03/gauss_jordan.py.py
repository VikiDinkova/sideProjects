def gauss_jordan(m, eps = 1.0/(10**10)):
  (height, width) = (len(m), len(m[0]))
  for y in range(0,height):
    maxrow = y
    for y2 in range(y+1, height):    # Namirane na maksimalniq element na kolonata
      if abs(m[y2][y]) > abs(m[maxrow][y]):
        maxrow = y2
    (m[y], m[maxrow]) = (m[maxrow], m[y])
    if abs(m[y][y]) <= eps:     # Matricata nqma obratna
      return False
    for y2 in range(y+1, height):    # Zanulqvane na kolonata pod glavniq diagonal
      c = m[y2][y] / m[y][y]
      for x in range(y, width):
        m[y2][x] -= m[y][x] * c
  for y in range(height-1, 0-1, -1): # Zanulqvane nad glavniq diagonal
    c  = m[y][y]
    for y2 in range(0,y):
      for x in range(width-1, y-1, -1):
        m[y2][x] -=  m[y][x] * m[y2][y] / c
    m[y][y] /= c
    for x in range(height, width):       # Normalizirane na red y
      m[y][x] /= c
  return True
 
m = [[1, 0, 2, 2], [5, 2, 2, 2], [3, -1, 4, 1]]
if not gauss_jordan(m):
  print("Matricata nqma obratna")
else:
  print("Matricata ima obratna")
  for row in m:
    print(row)