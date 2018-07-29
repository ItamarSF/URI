def calcula(expressao):
    n = expressao.split("+")
    r = n[0]
    l, j = n[1].split("=")
    if r == 'R':
        return int(j) - int(l)
    elif l == 'L':
        return int(j) - int(r)
    else:
        return int(r) + int(l)

while True:
    try:
        expressao = input() 
        print(calcula(expressao)) 
    except EOFError:
        break
