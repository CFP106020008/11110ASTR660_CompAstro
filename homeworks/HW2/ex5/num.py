'''
EX5
'''

def etot(h, em, method):
    if method == 'CD':
        Etot = h**2/24 + em/h
    else:
        Etot = h/2 + em/h
    return Etot

print(etot(4.5e-8, 1e-15, 'FD'))
print(etot(2.3e-5, 1e-15, 'CD'))

