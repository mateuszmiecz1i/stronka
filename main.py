def f(x):
    if x == 0:
        return 0
    else:
        return 2 + f(x // 2)
       
 x = 0
 minX = 0
 maxX = 0
 osiemnastki = []
 
 while x > 19:
     if x == 18:
         x osiemnastki.append