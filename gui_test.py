import tkinter as tk

# Label
# window = tk.Tk()
# window.title('My Window')
# window.geometry('500x300')
# l = tk.Label(window, text='你好！this is Tkinter', bg='green', font=('Arial', 12), width=30, height=2)
# l.pack()


# Button
# window = tk.Tk()
# window.title('My Window')
# window.geometry('500x300')
# var = tk.StringVar()
# l = tk.Label(window, textvariable=var, bg='green', fg='white', font=('Arial', 12), width=30, height=2)
# l.pack()
# on_hit = False
# def hit_me():
#     global on_hit
#     if on_hit ==False:
#         on_hit = True
#         var.set('you hit me')
#     else:
#         on_hit = False
#         var.set('')
# b = tk.Button(window, text='hit me', font=('Arial', 12), width=10, height=1, command=hit_me)
# b.pack()


# Entry
# window = tk.Tk()
# window.title('My Window')
# window.geometry('500x300')
# e1 = tk.Entry(window, show=None, font=('Arial', 14))
# e2 = tk.Entry(window, show='*', font=('Arial', 14))
# e1.pack()
# e2.pack()


# Text
# window = tk.Tk()
# window.title('My Window')
# window.geometry('500x300')
# e = tk.Entry(window, show=None)
# e.pack()
# def insert_point():
#     var = e.get()
#     t.insert('insert', var)
# def insert_end():
#     var = e.get()
#     t.insert('end', var)
# b1 = tk.Button(window, text='insert point', width=10, height=2, command=insert_point)
# b1.pack()
# b2 = tk.Button(window, text='insert end', width=10, height=2, command=insert_end)
# b2.pack()
# t = tk.Text(window, height=3)
# t.pack()


# Listbox
# window = tk.Tk()
# window.title('My Window')
# window.geometry('500x300')
# var1 = tk.StringVar()
# l = tk.Label(window, bg='green', fg='yellow', font=('Arial', 12), width=10, textvariable=var1)
# l.pack()
# def print_selection():
#     value = lb.get(lb.curselection())
#     var1.set(value)
# b1 = tk.Button(window, text='print selection', width=15, height=2, command=print_selection)
# b1.pack()
# var2 = tk.StringVar()
# var2.set((1, 2, 3, 4))
# lb = tk.Listbox(window, listvariable=var2)
# list_items = [11, 22, 33, 44]
# for item in list_items:
#     lb.insert('end', item)
# lb.insert(1, 'first')
# lb.insert(2, 'second')
# lb.delete(2)
# lb.pack()


# RadioButton
# window = tk.Tk()
# window.title('My Window')
# window.geometry('500x300')
# var = tk.StringVar()
# l = tk.Label(window, bg='yellow', width=20, text='empty')
# l.pack()
# def print_selection():
#     l.config(text='you have selected' + var.get())
# r1 = tk.Radiobutton(window, text='Option A', variable=var, value='A', command=print_selection)
# r1.pack()
# r2 = tk.Radiobutton(window, text='Option B', variable=var, value='B', command=print_selection)
# r2.pack()
# r3 = tk.Radiobutton(window, text='Option C', variable=var, value='C', command=print_selection)
# r3.pack()


# Checkbutton
window = tk.Tk()
window.title('My Window')
window.geometry('500x300')


window.mainloop()