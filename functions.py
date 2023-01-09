def suma(num,func):
    return num + func(num)
def otra_func(val):
    return val*2
resultado=suma(2,lambda x:x*4)
print(resultado)
numbers=[2,4,6,8]
valor=list(map(lambda num:int(num/2),numbers))
print(valor)
