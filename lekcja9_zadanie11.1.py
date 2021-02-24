import random
from random import randint
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

number = int(input("Wpisz ilość liczb do posortowania: "))


def podpunkt_1(n):
    return random.sample(range(n), n)


def podpunkt_2(n):
    arr = [i for i in range(n)]
    not_sorted_count = randint(2, 6)
    shuffled = set()
    while len(shuffled) < not_sorted_count:
        shuffled.add(randint(0, n-1))
    while len(shuffled) > 2:
        switch_index_one = shuffled.pop()
        switch_index_two = shuffled.pop()
        temp = arr[switch_index_two]
        arr[switch_index_two] = arr[switch_index_one]
        arr[switch_index_one] = temp
    return arr


def podpunkt_3(n):
    numbers_and_positions = dict.fromkeys(range(n), 0)
    values_ordered_list = []
    for i in range(n):
        values_ordered_list.append(i)
    for key in numbers_and_positions:
        numbers_and_positions[key] = values_ordered_list[-1]
        values_ordered_list.pop()
    return numbers_and_positions


def podpunkt_4(n):
    # szczerze mówiąc nie do końca rozumiem zadanie
    # graficzne przedstawienie rozkładu gaussowskiego, gdzie wierzchołek występuje na n/2
    sns.distplot(random.normal(loc=n/2, scale=0.01, size=(n, n)), hist=False)
    plt.show()


def podpunkt_5(n):
    numbers_and_positions = dict.fromkeys(range(n), 0)
    for key in numbers_and_positions:
        numbers_and_positions[key] = random.randint(0, n-1)
    return numbers_and_positions
