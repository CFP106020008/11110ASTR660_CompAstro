def N(k, em):
    return (em/2/k)**(-2/(2*(k+1)-1))


def etot(N, k, bit):
    if bit == 32:
        em = 1e-7
    elif bit == 64:
        em = 1e-15
    else:
        print('Error!')
    return 1/N**k + N**0.5*em

print('{:.2e}'.format(N(2, 1e-7))) 
print('{:.2e}'.format(N(2, 1e-15)))
print('{:.2e}'.format(N(4, 1e-7)))
print('{:.2e}'.format(N(4, 1e-15)))

print('{:.2e}'.format(etot(N(2, 1e-7) , 2, 32)))
print('{:.2e}'.format(etot(N(2, 1e-15), 2, 64)))
print('{:.2e}'.format(etot(N(4, 1e-7) , 4, 32)))
print('{:.2e}'.format(etot(N(4, 1e-15), 4, 64)))
