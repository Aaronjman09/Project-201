from tkinter import *
window = Tk()
window.title("BMI Calculator")
window.geometry("400x400")
window.configure(bg = "lightcyan")

heading_label = Label(window, text = "BMI Calculator", bg = "lightcyan", fg = "black", font = ("calibri, 20"), bd = 5)
name_label = Label(window, text = "Username", bg = "lightcyan", fg = "black", font = ("calibri, 12"), bd = 1)
username = Entry(window, text = "", bd = 2, width = 22)
result_frame = LabelFrame(window, text = "result", bg = "lightcyan", font = ("calibri, 12"))
result_frame.pack(padx = 20, pady = 2)

heading_label.place(x = 50, y = 20)
name_label.place(x = 20, y = 90)
username.place(x = 150, y = 92)
result_frame.place(x = 20, y = 300)

window.mainloop()