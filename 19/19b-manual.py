f = 10551264

a = 0
b = 1
while True:
    d = 1
    while True:
        c = b * d
        if c == f:
            a = a + b
        d = d + 1
        if d > f:
            b = b + 1
            if b > f:
                KONIEC
            else:
                continue
