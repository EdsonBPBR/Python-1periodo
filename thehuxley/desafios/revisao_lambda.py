# (d, p, nome)
registros = [
    (3, 2.25, 'Coxinha'),
    (7, 3.45, 'Coca'),
    (2, 1.75, 'Lata'),
    (2, 4.56, 'Pastel'),
    (3, 1.15, 'Fanta'),
    
]

x = sorted(registros, key=lambda y: (y[0], y[1]))
print(x)