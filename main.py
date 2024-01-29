import tkinter as tk

win = tk.Tk()
canvas = tk.Canvas(win, bg="white", width=400, height=400)
for i in range(50 , 400, 50):
    canvas.create_line((i,0), (i,400), fill="black")
for g in range(0 , 400, 50):
    canvas.create_line((0,g), (400,g), fill="black")
canvas.create_oval((50,50), (100,100), fill="black")
canvas.create_oval((150,150), (100,100), fill="black")
canvas.create_oval((0,0), (50,50), fill="black")
canvas.create_oval((0,150), (50,100), fill="black")
canvas.create_oval((100,0), (150,50), fill="black")
print('a')
canvas.pack()
win.mainloop()