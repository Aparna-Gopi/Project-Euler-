for a in xrange(500, 1, -1):
     for b in xrange(500, a , -1):
         c = 1000 - a - b
         if c > 0:
             if c*c == a*a + b*b:
                 print a * b * c
                 break
