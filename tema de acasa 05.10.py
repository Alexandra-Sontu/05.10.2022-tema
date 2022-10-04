import random

def corect(nr,baza):
    cif_mare=0
    while nr!=0:
        cifra=nr%10
        nr//=10
        if cifra>cif_mare:
            cif_mare=cifra
    if cif_mare>=baza:
        print(cif_mare)
        return False
    return True

def zecimal(nr,baza):
    nr_in_10=0
    i=0
    while nr!=0:
        cifra=nr%10
        nr//=10
        nr_in_10+=cifra*(baza**i)
        i+=1
    return nr_in_10

def adunarea(x,y,b):
    x=zecimal(x,b)
    y=zecimal(y,b)
    suma = x+y
    return zecimal_in_baza(suma,b)
def scaderea(x,y,b):
    x=zecimal(x,b)
    y=zecimal(y,b)
    if(x>y):
        scad=x-y 
        return zecimal_in_baza(scad,b)
    scad=y-x
    return zecimal_in_baza(scad,b)
def zecimal_in_baza(nr,b):
    num_final=""
    while nr!=0:
        cifra=nr%b
        nr//=b
        num_final+=str(cifra)
    num_final=num_final[::-1]
    return(int(num_final))

def inmultire(x,y,b):
    x=zecimal(x,b)
    y=zecimal(y,b)
    p=x*y
    return zecimal_in_baza(p,b)

x = random.randint(0,999)
b = random.randint(2,9)
y = random.randint(0,999)
print("Baza:",b)
print("Primul numar:",x)
print("Al doilea numar:",y)
este_corect_x=corect(x,b)
este_corect_y=corect(y,b)

if(este_corect_x and este_corect_y):
    print("Aceste numere sunt scrise corect")
    print("Numarul",x,"in zecimal:",zecimal(x,b))
    print("Numarul",y,"in zecimal:",zecimal(y,b))
    print("Suma:",adunarea(x,y,b))
    print("Diferenta:",scaderea(x,y,b))
    print("Produsul:",inmultire(x,y,b))
else:
    print("Numarul nu este scris corect")