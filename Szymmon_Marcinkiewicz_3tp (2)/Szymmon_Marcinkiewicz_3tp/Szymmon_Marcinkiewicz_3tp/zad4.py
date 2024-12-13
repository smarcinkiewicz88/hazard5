import random

from tkinter import *


root = Tk()
root.geometry("500x500")
root.config(bg="#004B24")
root.resizable(False, False)
root.title("Ruletka")



label1 = Label(root, text="Witaj na naszej stronie Hazardowej :3", background= "#C31A17", foreground="white", width=71)
label1.pack()

def losuj():
    liczba = IntVar()
    liczba.set(int(random.randint(0,37)))


    
    czarne = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
    czerwone = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
    zielone = [0, 37]

    if liczba.get() in czarne:
        output_string.set("czarne")
    elif liczba.get() in czerwone:
        output_string.set("czerwone")
    else:
        output_string.set("zielone") 
        

    wyswietlenie_liczby.config(textvariable=liczba)

los = Button(root, text="Zagraj :3", width=10, height=3, command=losuj)
los.pack()



output_string = StringVar()
output_label = Label(root, textvariable=output_string, bg="#C31A17", fg="white")
output_label.pack()

wyswietlenie_liczby = Label(root, bg="#C31A17", fg="white")
wyswietlenie_liczby.pack()


root.mainloop()
