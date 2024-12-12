
a = int(input("podaj pierwsza liczba: "))
b = int(input("podaj druga liczba: "))
wybor = int(input("wybierz funkcję: (1-dodawanie, 2- odejmowanie, 3- mnożenie, 4- dzielenie)"))

wynik = 0

if wybor == 2:
    wynik = a - b

elif wybor == 1:
    wynik = a + b

elif wybor == 3:
    wynik = a * b
    
else:
    if b == 0:
            print("nie dziel przez")
    else:
        wynik = a / b

print(wynik)