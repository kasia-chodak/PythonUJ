x = int(input("Wpisz liczbę x: "))
y = int(input("Wpisz liczbę y: "))
z = int(input("Wpisz liczbę z: "))
n = int(input("Wpisz liczbę n: "))

i = 0
j = 0
k = 0
coord_list = []

for coord1 in range(x + 1) :
    for coord2 in range(y + 1) :
        for coord3 in range(z + 1) :
            if (i + j + k) != n :
                coord_list.append([i, j, k])
            k += 1
        j += 1
        k = 0
    i +=1
    j = 0
    k = 0

print(coord_list)