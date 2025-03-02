import math
x=0.2
epsilon=0.01
p=math.sin(x)
term=p
n=1
while abs(term) >=epsilon:
        term=((-1)**n)*(math.sin(x**(n+1))/math.factorial(n+1))
        p+=term
        n+=1
print(f"p ~ {p:.4f}")



