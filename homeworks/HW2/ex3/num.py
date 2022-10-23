def N(k, em):
    return (2*k/em)**(2/(2*(k+1)-1))


def etot(N, k, bit):
    if bit == 32:
        em = 1e-7
    elif bit == 64:
        em = 1e-15
    else:
        print('Error!')
    return 1/N**k + N**0.5*em

print('Mid/Trap N32 = ', '{:.2e}'.format(N(2, 1e-7))) 
print('Mid/Trap N64 = ', '{:.2e}'.format(N(2, 1e-15)))
print('Simpsons N32 = ', '{:.2e}'.format(N(4, 1e-7)))
print('Simpsons N64 = ', '{:.2e}'.format(N(4, 1e-15)))

print('Mid/Trap e32 = ', '{:.2e}'.format(etot(N(2, 1e-7) , 2, 32)))
print('Mid/Trap e64 = ', '{:.2e}'.format(etot(N(2, 1e-15), 2, 64)))
print('Simpsons e32 = ', '{:.2e}'.format(etot(N(4, 1e-7) , 4, 32)))
print('Simpsons e64 = ', '{:.2e}'.format(etot(N(4, 1e-15), 4, 64)))
