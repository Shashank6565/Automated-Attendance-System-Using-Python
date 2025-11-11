from tkinter import *
from PIL import Image, ImageTk

class Help:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Help Desk")

        img_top = Image.open(r"images/help.jpg")
        img_top = img_top.resize((1530, 790), Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=0, width=1530, height=790)

        dev_label = Label(f_lbl, text="Email: example@gmail.com", font=("times new roman", 30, "bold"), bg="white", fg="blue")
        dev_label.place(x=550, y=220)


if __name__ == "__main__":
    root = Tk()
    obj = Help(root)
    root.mainloop()