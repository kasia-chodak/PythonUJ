def fun(N):
    length = len(bin(N))
    binarnie = bin(N)[2:length]
    przerwy = []
    przerwa = 0
    binary = list(binarnie)
    for bit in binary :
        if int(bit) == 0 :
            przerwa += 1
        else :
            przerwy.append(przerwa)
            przerwa = 0
    przerwy.append(przerwa)
    return max(przerwy)

N = int(input("Wpisz liczbę w systemie dziesiętnym: "))
print(fun(N))