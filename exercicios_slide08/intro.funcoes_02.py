y = 4 #variável y global

def f(x):
    print(x + 1) #variável x local

def g():
    print(y + 1) # não recebe o parâmetro pois y é uma variável global

#main 
f(3)
g()
