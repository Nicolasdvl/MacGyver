def pos(i, s, w):
    x = i * s - ((i - (i % 15))/15 * w)
    y = (i - (i % 15)) / 15 * s
    print(x)
    print(y)


pos(1, 50, 750)
pos(68, 50, 750)