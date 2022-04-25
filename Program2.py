from tkinter import *
window = Tk()

window.geometry("600x500+30+20")
window.title("Midterms in OOP")




def text_sample():
    name = name_ts.get()

    disp.insert(0,f'{name}')

name_ts = Entry(window, bd = 3, font = ("Arial",14))
name_ts.place(x=260,y=80)


lbl = Label(window, text = "Enter your Fullname",  fg="red")
lbl.place(x=80, y=80)


btn = Button(window,text = "Click to display your Fullname",  fg="red", command=text_sample)
btn.place(x=80,y=120)
btn.pack



disp = Entry(window, bd = 3, font = ("Arial",14))
disp.place(x=260,y=120)
disp.pack

name_ts.pack

window.mainloop()
