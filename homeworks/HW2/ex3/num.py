def etot(N, k, bit):
    if bit == 32:
        em = 1e-7
    elif bit == 64:
        em = 1e-15
    else:
        print('Error!')
    return 1/N**k + N**0.5*em

print(etot(1100, 2, 32))
print(etot(1.7e6, 2, 64))
print(etot(50, 4, 32))
print(etot(3000, 4, 64))
