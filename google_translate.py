from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES


def change(text="type", src="English", dest="Urdu"):
    text1 = text
    src1 = src
    dest1 = dest
    trans = Translator()
    trans1 = trans.translate(text=text1, src=src1, dest=dest1)
    return trans1.text

def data():
    s = comb_sor.get()
    d = comb_dest.get()
    msg = sor_txt.get(1.0, END)
    textget = change(text=msg, src=s, dest=d)
    dest_txt.delete(1.0, END)
    dest_txt.insert(END,textget)



root = Tk()
root.title("Translator")
root.geometry("500x700")
root.config(bg='gray')

lab_txt = Label(root, text="Translator", font=("Time New Roman", 40, "bold"), bg="gray")
lab_txt.place(x=100, y=40, height=50, width=300)

frame = Frame(root).pack(side=BOTTOM)

lab_txt = Label(root, text="Source Text", font=("Time New Roman", 20, "bold"), bg="gray", fg="white")
lab_txt.place(x=100, y=100, height=20, width=300)

sor_txt = Text(frame, font=("Time New Roman", 20, "bold"), wrap=WORD)
sor_txt.place(x=10, y=130, height=150, width=480)

list_txt = list(LANGUAGES.values())

comb_sor = ttk.Combobox(frame, value=list_txt)
comb_sor.place(x=10, y=300, height=40, width=150)
comb_sor.set("english")

button_change = Button(frame, text="Translate", relief=RAISED, command=data)
button_change.place(x=170, y=300, height=40, width=150)

comb_dest = ttk.Combobox(frame, value=list_txt)
comb_dest.place(x=330, y=300, height=40, width=150)
comb_dest.set("english")

lab_txt = Label(root, text="Destination Text", font=("Time New Roman", 20, "bold"), bg="gray", fg="white")
lab_txt.place(x=100, y=360, height=20, width=300)

dest_txt = Text(frame, font=("Time New Roman", 20, "bold"), wrap=WORD)
dest_txt.place(x=10, y=400, height=150, width=480)



root.mainloop()