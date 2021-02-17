import random

#test Millera-Rabina
#n - liczba testowana, k - dokładność testu (l.powtórzeń, im więcej tym lepiej)
def check_if_prime(n, k):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False

    a = 0
    b = n - 1
    while b % 2 == 0:
        a += 1
        b = b // 2
    for accuracy in range(k):
        e = random.randrange(2, n - 1)
        f = pow(e, b, n)
        if f == 1 or f == n - 1:
            continue
        for every in range(a - 1):
            f = pow(f, 2, n)
            if f == n - 1:
                break
        else:
            return False
    return True


def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

def modpow(base, exp, mod):
    base %= mod
    for _ in range(exp):
        base *= base % mod
    return base


def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = extended_gcd(b % a, a)
        return g, x - (b // a) * y, y


def modinv(t, s):
    g, x, y = extended_gcd(t, s)
    if g != 1:
        raise Exception("Nie istnieje odwrotność modulo")
    else:
        return x % s


def gen_rand_int():
    return random.randint(10**60, 10**100)

def split_by_n(seq, n):
    return [(seq[i:i+n]) for i in range(0, len(seq), n)]

#generowanie kluczy
p = gen_rand_int()
q = gen_rand_int()
while not check_if_prime(p, 100):
    p = gen_rand_int()
while not check_if_prime(q, 100) and abs(p - q) > 10**80:
    q = gen_rand_int()


n = p * q
euler_func_n = (p - 1)*(q - 1)
e = random.randint(1, euler_func_n)
while not gcd(e, euler_func_n) == 1:
    e = random.randint(1, euler_func_n - 1)

#de = n*euler + 1
d = modinv(e, euler_func_n)

print(p, q, n, e, euler_func_n, d)

# szyfrowanie
def split_by_n(seq):
    return ([(seq[i:i+n]) for i in range(0, len(seq), 64)])

def encrypt_block(blok):  # szyfrowanie pojedycznego bloku
    return pow(blok, e, n)


def encrypt_message(message):  # szyfrowanie całej wiadomości
    return encrypt_block(int(message.encode('utf-8').hex(), 16))

def encryptuje(splitted):
    for element in splitted:
        encrypt_message(element)

# deszyfrowanie

def decrypt_block(blok):  # deszyfrowanie bloku
    return pow(blok, d, n)


def decrypt_message(message):  # deszyfrowanie całej wiadomości
    return bytes.fromhex(hex(decrypt_block(message))[2:].upper()).decode('utf-8')


input_message = input("Wpisz wiadomość: ")

for word in ['test', 'ziom', 'ims', 'super-tajny', 'lubielody', 'wdi']:
    print(decrypt_message(encrypt_message(word)))
#print(decrypt_message(encrypt_message(input_message)))
#print(decrypt_message(encryptuje(split_by_n(input_message))))