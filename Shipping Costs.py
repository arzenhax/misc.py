

def groundship_check(w):
  if w > 10:
    p = w * 4.75
    fc = 20
    return print(p + fc)
  elif (6 < w) and (w <= 10): 
    p = 4 * w
    fc = 20
    return print(p + fc)
  elif (2 < w) and (w <= 6): 
    p = 3
    fc = 20
    return print(p + fc)
  else:
    p = 1.5
    fc = 20
    return print(p + fc)
     

groundship_check(8.4)


def droneship_check(w):
  if w > 10:
    p = 14.25
    return print(p)
  elif (6 < w) and (w <= 10): 
    p = 12
    return print(p)
  elif (2 < w) and (w <= 6): 
    p = 9
    return print(p)
  else:
    p = 4.5
    return print(p)

droneship_check(22)


def pgship_check(w):
  return print(125)


pgship_check(22)

input("Press enter to continue...")