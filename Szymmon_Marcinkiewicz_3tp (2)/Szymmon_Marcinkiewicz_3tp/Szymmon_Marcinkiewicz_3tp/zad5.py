import random

kwota = int(input("ile pieniędzy wpłacasz?\n"))
wybor = int(input("Stawiasz na: \n1 - kolor \n2 - numer\n"))


stawka = 0
liczba = random.randint(0,37)
czarne = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
czerwone = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
zielone = [0, 37]

if wybor == 2:
    wyborlicz = int(input("1-36 - numer\n"))

    if wyborlicz == liczba:
            
            stawka = kwota * 36
            print("Wygrałeś", stawka)
    else:
            print("Przegrałeś :(")

elif wybor == 1:

    wyborkol = int(input("na co stawiasz: \n1 - czarne, \n2 - czerwone, \n3 - zielone\n"))

    if liczba in czarne:
        print("czarne")

        if wyborkol == 1:

            stawka = kwota * 2
            print("Wygrałeś", stawka)
        else:
            print("Przegrałeś :(")

    elif liczba in czerwone:
        print("czerwone")

        if wyborkol == 2:

            stawka = kwota * 2
            print("Wygrałeś", stawka)
        else:
            print("Przegrałeś :(")

    elif liczba in zielone:
        print("zielone")

        if wyborkol == 3:

            stawka = kwota * 36
            print("Wygrałeś", stawka)
        else:
            print("Przegrałeś :(")


print(liczba)