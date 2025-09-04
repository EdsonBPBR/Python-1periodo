y = 5 

def f(y): #escopo local
    print(y + 1) 

def g(): #escopo global
    print(y + 1)

#main 
f(3)
g()
