from tkinter import *
from PIL import Image, ImageTk

class Developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Developer")

        img_top = Image.open(r"images/dev.jpg")
        img_top = img_top.resize((1530, 790), Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=0, width=1530, height=790)

        main_frame = Frame(f_lbl, bd=2, bg="white")
        main_frame.place(x=1000, y=55, width=500, height=600)

        img_dev = Image.open(r"images/kiran.jpg")
        img_dev = img_dev.resize((200, 200), Image.LANCZOS)
        self.photoimg_dev = ImageTk.PhotoImage(img_dev)

        dev_lbl = Label(main_frame, image=self.photoimg_dev)
        dev_lbl.place(x=300, y=0, width=200, height=200)

        dev_label = Label(main_frame, text="Hello, my name is Kiran", font=("times new roman", 16, "bold"), bg="white")
        dev_label.place(x=0, y=5)

        dev_label_2 = Label(main_frame, text="I am a Python Developer", font=("times new roman", 16, "bold"), bg="white")
        dev_label_2.place(x=0, y=40)

        img_follow = Image.open(r"images/follow.jpg")
        img_follow = img_follow.resize((500, 390), Image.LANCZOS)
        self.photoimg_follow = ImageTk.PhotoImage(img_follow)

        follow_lbl = Label(main_frame, image=self.photoimg_follow)
        follow_lbl.place(x=0, y=210, width=500, height=390)


if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()