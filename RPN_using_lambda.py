tokeny = []
operacje = {
    '+': lambda x,y: x+y,
    '-': lambda x,y: y-x,
    '*': lambda x,y: x*y,
    '/': lambda x,y: y/x,
    '^': lambda x,y: x**y
}

for znak in '2 7 + 3 / 14 3 - 4 * + 2 /'.split():
    if znak in operacje: tokeny.append(operacje[znak](tokeny.pop(), tokeny.pop()))
    else: tokeny.append(float(znak))
    print(tokeny)
