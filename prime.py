import random
from math import log

def miller_rabin(n, k=40):
    if n == 2:
        return True

    if n % 2 == 0:
        return False

    r = 0
    s = n - 1
    while s % 2 == 0:
        r += 1
        s //= 2
    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def generate_prime(n):
    tries = 0
    while True:
        tries += 1
        x = random.randint(n, 10*n)
        # if x % 2 == 0 or x % 3 == 0: continue
        if miller_rabin(x):
            break
    return tries

def xor(a, b):
    res = ''
    for i in range(0, len(a)):
       res += str(int(a[i] != b[i]))
    return res

def myhash(x):
    if len(x) == 256:
        return x
    l = int(len(x)/2)
    print()
    print('l=',conv(b=x[:l]))
    print('r=',conv(b=x[l:]))
    x = xor(x[:l], x[l:])
    print('x=',conv(b=x))
    return myhash(x)

def conv(b=None, h=None):
    if b is None:
        return bin(int(h, 16))[2:]
    return hex(int(b, 2))[2:]


# bits = 256
# n = 2 ** bits
# digits = 100
# n = 10 ** digits
# print('digits=', log(n))
# print('bits=', log(n) / log(2))
# print('expected tries:', )
# s = 0
# for i in range(0,25):
#     s += generate_prime(n)
#
# print('actual tries:', s/25)
s = ''
for i in range(0, 256):
    s += str(random.randint(0, 1))
# s = input('enter string: ')

# print('\n\nThe hash is ', conv(b=myhash(s)))
print('\n\nThe hash is ', s)
print('\n\nThe hash is ', myhash(s))
# x = x.rjust(24, '0')
# print(myhash(x))
# print(xor(x[:19], x[19:]))