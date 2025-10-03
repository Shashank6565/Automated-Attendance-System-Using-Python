from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk, ImageDraw
from student import student
from tkinter import Button

class attendence__System:
    def __init__(self, root):
        self.root = root
        self.root.title("Automated Attendance System")
        self.root.geometry("1530x790+0+0")
        self.root.title("Automated Attendance System")

        # Images 1.
        img1 = Image.open(r"C:\Users\933si\OneDrive\Desktop\Images for PBL\GEU png.png")
        img1 = img1.resize((500, 130), Image.Resampling.BICUBIC)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        title_lbl = Label(self.root, image=self.photoimg1)
        title_lbl.place(x=500, y=0, width=500, height=130)

        # Images 2.
        img2 = Image.open(r"C:\Users\933si\OneDrive\Desktop\Images for PBL\GEU2 logo.jpg")
        img2 = img2.resize((500, 130), Image.Resampling.BICUBIC)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        title_lbl = Label(self.root, image=self.photoimg2)
        title_lbl.place(x=0, y=0, width=500, height=130) 

        # Images 3.
        img3 = Image.open(r"C:\Users\933si\OneDrive\Desktop\Images for PBL\GEU3.jpg")
        img3 = img3.resize((500, 130), Image.Resampling.BICUBIC)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        title_lbl = Label(self.root, image=self.photoimg3)
        title_lbl.place(x=1000, y=0, width=550, height=130) 



        # Background Image
        img4 = Image.open(r"C:\Users\933si\OneDrive\Desktop\Images for PBL\bg2.jpg")
        img4 = img4.resize((1530, 710), Image.Resampling.BICUBIC)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        bg_img = Label(self.root, image=self.photoimg4)
        bg_img.place(x=0, y=130, width=1530, height=710)


        # Title
        title_lbl = Label(bg_img, text="AUTOMATED ATTENDENCE SYSTEM", font=("times new roman", 35, "bold"), bg="white", fg="black")
        title_lbl.place(x=0, y=0, width=1530, height=45)


        # student button
        img5 = Image.open(r"C:\Users\933si\OneDrive\Desktop\Images for PBL\student btn.png")
        img5 = img5.resize((220, 220), Image.Resampling.BICUBIC)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b1 = Button(bg_img, image=self.photoimg5, command=self.student_details, cursor="hand2")
        b1.place(x=200, y=150, width=220, height=220)


        # Attendance button
        img7 = Image.open(r"C:\Users\933si\OneDrive\Desktop\Images for PBL\atdn btn.png")
        img7 = img7.resize((220, 220), Image.Resampling.BICUBIC)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b3 = Button(bg_img, image=self.photoimg7, cursor="hand2")
        b3.place(x=800, y=150, width=220, height=220)


        # Face Recognition button
        img6 = Image.open(r"C:\Users\933si\OneDrive\Desktop\Images for PBL\face btn.png")
        img6 = img6.resize((220, 220), Image.Resampling.BICUBIC)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b2 = Button(bg_img, image=self.photoimg6, cursor="hand2")
        b2.place(x=500, y=150, width=220, height=220)


        # Help button
        img8= Image.open(r"C:\Users\933si\OneDrive\Desktop\Images for PBL\help btn.png")
        img8= img8.resize((220, 220), Image.Resampling.BICUBIC)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b4 = Button(bg_img, image=self.photoimg8, cursor="hand2")
        b4.place(x=1100, y=150, width=220, height=220)



        # Photos button
        img9= Image.open(r"C:\Users\933si\OneDrive\Desktop\Images for PBL\photo btn.png")
        img9= img9.resize((220, 220), Image.Resampling.BICUBIC)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b5 = Button(bg_img, image=self.photoimg9, cursor="hand2")
        b5.place(x=250, y=400, width=220, height=220)


        # Help button
        img10= Image.open(r"C:\Users\933si\OneDrive\Desktop\Images for PBL\developer btn.png")
        img10= img10.resize((220, 220), Image.Resampling.BICUBIC)
        self.photoimg10 = ImageTk.PhotoImage(img10)

        b6 = Button(bg_img, image=self.photoimg10, cursor="hand2")
        b6.place(x=625, y=400, width=220, height=220)


        # Exit button
        img11= Image.open(r"C:\Users\933si\OneDrive\Desktop\Images for PBL\Exit btn.png")
        img11= img11.resize((220, 220), Image.Resampling.BICUBIC)
        self.photoimg11 = ImageTk.PhotoImage(img11)

        b7 = Button(bg_img, image=self.photoimg11, cursor="hand2", command=self.root.destroy)
        b7.place(x=1000, y=400, width=220, height=220)



    #======================= Function buttons =========================
    
    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = student(self.new_window)
        self.new_window.title("Student Details")
        self.new_window.geometry("1530x790+0+0")
        self.new_window.resizable(False, False)


if __name__ == "__main__":
    root = Tk()
    obj = attendence__System(root)
    root.mainloop()
    

        