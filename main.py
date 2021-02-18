import random


# test Millera-Rabina
# n - liczba testowana, k - dokładność testu (l.powtórzeń, im więcej tym lepiej)
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
        a, b = b, a % b
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


# generowanie kluczy
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

# de = n*euler + 1
d = modinv(e, euler_func_n)

BLOCK_SIZE = 64


# szyfrowanie

def split_by_n(seq):
    return [seq[i:i+BLOCK_SIZE] for i in range(0, len(seq), BLOCK_SIZE)]


def encrypt_block(blok):  # szyfrowanie pojedycznego bloku
    return pow(blok, e, n)


def encrypt_message(message):  # szyfrowanie całej wiadomości
    return encrypt_block(int(message.encode('utf-8').hex(), 16))


# jest problem z szyfrowaniem długiego tekstu, dlatego dzielę tekst na mniejsze, szyfrowalne elementy
def encrypt(long_text):
    encrypted_text = ''
    for element in split_by_n(long_text):
        encrypted_text += str(encrypt_message(element))
        encrypted_text += ' '
    return encrypted_text


# deszyfrowanie

def decrypt_block(blok):  # deszyfrowanie bloku
    return pow(blok, d, n)


def decrypt_message(message):  # deszyfrowanie całej wiadomości
    return bytes.fromhex(hex(decrypt_block(message))[2:].upper()).decode('utf-8')


def decrypt(encrypted_text):
    plain_message = ''
    for element in encrypted_text[:-1].split(' '):
        plain_message += decrypt_message(int(element))
    return plain_message


input_message = input("Wpisz wiadomość: ")
print(decrypt(encrypt(input_message)))
