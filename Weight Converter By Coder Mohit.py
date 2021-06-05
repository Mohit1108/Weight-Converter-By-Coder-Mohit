from tkinter import *
window = Tk()
window.title('Weight converter By Coder Mohit ')
def from_kg():
    Gram = float(e2_value.get())*1000
    Miligram = float(e2_value.get())*1000000
    Microgram = float(e2_value.get())*1000000000
    Tone = float(e2_value.get())/1000
    Pound = float(e2_value.get())*2.205
    ounce = float(e2_value.get())*35.274
    t1.delete("1.0",END)
    t1.insert(END, Gram)
    t2.delete("1.0",END)
    t2.insert(END, Miligram)
    t3.delete("1.0",END)
    t3.insert(END, Microgram)
    t4.delete("1.0",END)
    t4.insert(END, Tone)
    t5.delete("1.0",END)
    t5.insert(END, Pound)
    t6.delete("1.0",END)
    t6.insert(END, ounce)
def website():
    import webbrowser
    url = 'https://codermohit.com'
    webbrowser.open(url)
def youtube():
    import webbrowser
    url = 'https://www.youtube.com/channel/UCaqKx5W0cSS0l2i2GgKQw9g?sub_confirmation=1'
    webbrowser.open(url)

def exit():
    window.destroy()
e1 = Label(window, text="Input the weight in KG",font=('Courier',15,'bold'))
e2_value = StringVar()
e2 = Entry(window, textvariable=e2_value,font=('Courier',15,))

e3 = Label(window, text="Gram",font=('Courier',15,))
e4 = Label(window, text="Miligram",font=('Courier',15,))
e5 = Label(window, text="Microgram",font=('Courier',15,))
e6 = Label(window, text="Tone",font=('Courier',15,))
e7 = Label(window, text="Pound",font=('Courier',15,))
e8 = Label(window, text="Ounce",font=('Courier',15,))

t1 = Text(window, height=7, width=30)
t2 = Text(window, height=7, width=30)
t3 = Text(window, height=7, width=30)
t4 = Text(window, height=7, width=30)
t5 = Text(window, height=7, width=30)
t6 = Text(window, height=7, width=30)
b1 = Button(window, text="Convert",font=('Courier',15,'bold'), command=from_kg,fg='white')
b2 = Button(window, text="Exit",font=('Courier',15,'bold'), command=exit,fg='white')
b3 = Button(window, text="Website",font=('Courier',15,'bold'), command=website,fg='white')
b4 = Button(window, text="YouTube",font=('Courier',15,'bold'), command=youtube,fg='white')

e1.grid(row=0, column=0)
e2.grid(row=0, column=1)
e3.grid(row=1, column=0)
e4.grid(row=1, column=1)
e5.grid(row=1, column=2)
e6.grid(row=3, column=0)
e7.grid(row=3, column=1)
e8.grid(row=3, column=2)
t1.grid(row=2, column=0)
t2.grid(row=2, column=1)
t3.grid(row=2, column=2)
t4.grid(row=4, column=0)
t5.grid(row=4, column=1)
t6.grid(row=4, column=2)
b1.grid(row=0, column=2)
b1.config(bg='green')


b2.grid(row=5, column=2)
b2.config(bg='#8B0000')

b3.grid(row=5, column=0)
b3.config(bg='#fb2056')

b4.grid(row=5, column=1)
b4.config(bg='#c4302b')
window.mainloop()
