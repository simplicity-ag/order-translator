import tkinter as tk 

def window():
    root = tk.Tk()
    root.geometry("550x200")
    root.title("Happy Birthday")

    nameL = tk.Label(text="Youre Name")
    nameL.pack()
    name = tk.Entry()
    name.pack()

    ageL = tk.Label(text="The Age")
    ageL.pack()
    age = tk.Entry()
    age.pack()

    namePL = tk.Label(text="the Person Birthday")
    namePL.pack()
    name2 = tk.Entry()
    name2.pack()

    def textmaker():
        yname = name.get()
        ageY = age.get()
        nameB = name2.get()
        textF.config(text="Hallo lieber "+ nameB +" Du wirst "+ ageY + " Ich wünsche dir alles gute lass dich feiern liebe grüsse "+ yname)

    text = tk.Button(text="Make", command=textmaker)
    text.pack()

    textF = tk.Label(text="Birthday text")
    textF.pack()

    root.mainloop()
window()