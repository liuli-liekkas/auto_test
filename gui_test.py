import tkinter as tk
import tkinter.messagebox

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
# window = tk.Tk()
# window.title('My Window')
# window.geometry('500x300')
# l = tk.Label(window, bg='yellow', width=20, text='empty')
# l.pack()
# def print_selection():
#     if (var1.get() == 1) & (var2.get() == 0):
#         l.config(text='I love only Python')
#     elif (var1.get() == 0) & (var2.get() == 1):
#         l.config(text='I love only C++')
#     elif (var1.get() == 0) & (var2.get() == 0):
#         l.config(text='I do not love either')
#     else:
#         l.config(text='I love both')
# var1 = tk.IntVar()
# var2 = tk.IntVar()
# c1 = tk.Checkbutton(window, text='Python', variable=var1, onvalue=1, offvalue=0, command=print_selection)
# c1.pack()
# c2 = tk.Checkbutton(window, text='C++', variable=var2, onvalue=1, offvalue=0, command=print_selection)
# c2.pack()


# Scale
# window = tk.Tk()
# window.title('My Window')
# window.geometry('500x300')
# l = tk.Label(window, bg='yellow', width=20, text='empty')
# l.pack()
# def print_selection(v):
#     l.config(text='you have selected' + v)
# s = tk.Scale(window, label='try me', from_=0, to=10, orient=tk.HORIZONTAL, length=200, showvalue=0, tickinterval=2, resolution=0.01, command=print_selection)
# s.pack()


# Canvas
# window = tk.Tk()
# window.title('My Window')
# window.geometry('500x300')
# canvas = tk.Canvas(window, bg='green', height=200, width=500)
# image_file = tk.PhotoImage(file='pic.gif')
# image = canvas.create_image(250, 0, anchor='n', image=image_file)
# x0, y0, x1, y1 = 100, 100, 150, 150
# line = canvas.create_line(x0-50, y0-50, x1-50, y1-50)
# oval = canvas.create_oval(x0+120, y0+50, x1+120, y1+50, fill='yellow')
# arc = canvas.create_arc(x0, y0+50, x1, y1+50, start=0, extent=180)
# rect = canvas.create_rectangle(330, 30, 330+20, 30+20)
# canvas.pack()
# def moveit():
#     canvas.move(line, 2, 10)
# b = tk.Button(window, text='move item', command=moveit)
# b.pack()


# Menu
# window = tk.Tk()
# window.title('My Window')
# window.geometry('500x300')
# l = tk.Label(window, text='        ', bg='green')
# l.pack()
# counter = 0
# def do_job():
#     global counter
#     l.config(text='do' + str(counter))
#     counter += 1
# menubar = tk.Menu(window)
# filemenu = tk.Menu(menubar, tearoff=0)
# menubar.add_cascade(label='File', menu=filemenu)
# filemenu.add_command(label='New', command=do_job)
# filemenu.add_command(label='Open', command=do_job)
# filemenu.add_command(label='Save', command=do_job)
# filemenu.add_separator()
# filemenu.add_command(label='Exit', command=window.quit)
# editmenu = tk.Menu(menubar, tearoff=0)
# menubar.add_cascade(label='Edit', menu=editmenu)
# editmenu.add_command(label='Cut', command=do_job)
# editmenu.add_command(label='Copy', command=do_job)
# editmenu.add_command(label='Paste', command=do_job)
# submenu = tk.Menu(filemenu)
# filemenu.add_cascade(label='Import', menu=submenu, underline=0)
# submenu.add_command(label='Submenu_1', command=do_job)
# window.config(menu=menubar)


# Frame
# window = tk.Tk()
# window.title('My Window')
# window.geometry('500x300')
# l = tk.Label(window, text='on the window', bg='red', font=('Arial', 16))
# l.pack()
# frame = tk.Frame(window)
# frame.pack()
# frame_l = tk.Frame(frame)
# frame_r = tk.Frame(frame)
# frame_l.pack(side='left')
# frame_r.pack(side='right')
# tk.Label(frame_l, text='on the frame_l1', bg='green').pack()
# tk.Label(frame_l, text='on the frame_l2', bg='green').pack()
# tk.Label(frame_l, text='on the frame_l3', bg='green').pack()
# tk.Label(frame_r, text='on the frame_r1', bg='yellow').pack()
# tk.Label(frame_r, text='on the frame_r2', bg='yellow').pack()
# tk.Label(frame_r, text='on the frame_r3', bg='yellow').pack()


# MessageBox
window = tk.Tk()
window.title('My Window')
window.geometry('500x300')
def hit_me():
    # tkinter.messagebox.showinfo(title='Hi', message='你好！')
    # tkinter.messagebox.showwarning(title='Hi', message='有警告！')
    # tkinter.messagebox.showerror(title='Hi', message='出错了！')
    # tkinter.messagebox.askquestion(title='Hi', message='你好！')
    # tkinter.messagebox.askyesno(title='Hi', message='你好！')
    tkinter.messagebox.askokcancel(title='Hi', message='你好！')
tk.Button(window, text='hit me', bg='green', font=('Arial', 14), command=hit_me).pack()


window.mainloop()
