from Tkinter import * 
root = Tk()
canvas = Canvas(root, width=475, height=475)
canvas.pack()
img = PhotoImage(file="Images/Bulbasau.png")
canvas.create_image(250,250, image=img)
root.mainloop()