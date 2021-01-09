#pierwsza część zadania
list1 = [1, 2, [3, 4, [5, 6], 5], 3, 4]

#lista   1 2 lista[]
#pozycje 0 1   2
#lista[] 3 4 lista[[]]
#pozycje 0 1   2

list1[2][2].append(7)
print(list1)

#druga część zadania

def getMostNestedList(list1) :
    while True :
        i = 0
        while i < len(list1) :
            if isinstance(list1[i], list):
                list1 = list1[i]
                break
            else:
                i = i + 1
        if i == len(list1) :
            return list1


nested = getMostNestedList(list1)
number = 1
if len(nested) > 0 :
    number = nested[-1] + 1
nested.append(number)
print(list1)
