t = 0
p = 0
o = 0
def setup ():
    size (250, 250)
def draw():
    global t
    global p
    global o
    square(t, 5, 57)
    if t > height:
       t = 0
    else:
       t = map(second(), 0, 59, 0, height)
    square(p, 80, 69)
    if p > height:
       p = 0
    else:
       p = map(minute(), 0, 59, 0, height)
    square(o, 169, 78)
    if o > height:
       o = 0
    else:
       o = map(hour(), 0, 0, 50, height)
