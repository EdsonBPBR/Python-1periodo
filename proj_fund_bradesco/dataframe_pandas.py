import pandas as pd

disciplinas = {
    'cursos' : ['Fundamentos', 'Direito Digital', 'Cálculo', 'Programação I'],
    'créditos' : [90,50,80,40],
    'requisito' : [True, False, False, True]
}

data = pd.DataFrame(disciplinas)
print(f'{data}')