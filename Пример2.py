maska = ""
for i in range(ord('0'), ord('9') + 1):
    maska += chr(i)
for i in range(ord('A'), ord('Z') + 1):
    maska += chr(i)
 
def konwersja(liczba, dlugosc):
    roznica = dlugosc - len(liczba)
    return ('0'*roznica) + liczba
 
def dodaj(a, b, system):
    wynik = ""
    dl = max(len(a), len(b))
    L1 = konwersja(a, dl)
    L2 = konwersja(b, dl)
    p = 0
    z = ''
    if op == '-' :
        if L1 < L2 :
            L1, L2 = L2, L1
            z = '-'
        tmp = L2
        for i in tmp :
            L2 += maska[sys - 1 - maska.find(i)]
        p = 1
    for i in range(-1, -dl-1, -1):
        suma = maska.find(L1[i]) + maska.find(L2[i]) + p
        p = suma//system
        cyfra = suma % system
        wynik += maska[cyfra]
    if p:
        wynik += maska[p]
    wynik = z + wynik[:dl][::-1]
    
    return wynik
 
 
A = input()
B = input()
sys = 8
 
print(dodaj(A,B,sys, '-'))


from Lab6 import show_size
loc = locals().copy()
show_size(loc)