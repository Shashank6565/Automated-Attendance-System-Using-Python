from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector 
import cv2


class attendance:
    def __init__(self, root):
        self.root = root
        self.root.title("Attendance Management Portal")
        self.root.geometry("1530x790+0+0")
        self.root.title("Automated Attendance System")
        # Images 1.
        img1 = Image.open(r"C:\Users\933si\OneDrive\Desktop\Images for PBL\GEU png.png")
        img1 = img1.resize((500, 130), Image.Resampling.BICUBIC)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        title_lbl = Label(self.root, image=self.photoimg1)
        title_lbl.place(x=500, y=0, width=500, height=130)

        # Images 2.
        img2 = Image.open(r"C:\Users\933si\OneDrive\Desktop\Images for PBL\GEU5.jpeg")
        img2 = img2.resize((500, 130), Image.Resampling.BICUBIC)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        title_lbl = Label(self.root, image=self.photoimg2)
        title_lbl.place(x=0, y=0, width=500, height=130) 

        # Images 3.
        img3 = Image.open(r"C:\Users\933si\OneDrive\Desktop\Images for PBL\GEU5.jpeg")
        img3 = img3.resize((500, 130), Image.Resampling.BICUBIC)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        title_lbl = Label(self.root, image=self.photoimg3)
        title_lbl.place(x=1000, y=0, width=550, height=130) 

        # Background Image
        img4 = Image.open(r"C:\Users\933si\OneDrive\Desktop\Images for PBL\bg.jpg")
        img4 = img4.resize((1530, 710), Image.Resampling.BICUBIC)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        bg_img = Label(self.root, image=self.photoimg4)
        bg_img.place(x=0, y=130, width=1530, height=710)

        # Title
        title_lbl = Label(bg_img, text="Attendance Management Portal", font=("times new roman", 35, "bold"), bg="yellow", fg="black")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # Frame (Main Frame)
        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=20, y=55, width=1480, height=600)

        # Left Frame
        left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Attendance Details", font=("times new roman", 12, "bold"))
        left_frame.place(x=30, y=10, width=700, height=580)

        # Image
        left_img = Image.open(r"C:\Users\933si\OneDrive\Desktop\Images for PBL\bg.jpg")
        left_img = left_img.resize((1530, 710), Image.Resampling.BICUBIC)
        self.photoleft_img = ImageTk.PhotoImage(left_img)

        f_img = Label(self.root, image=self.photoleft_img)
        f_img.place(x=60, y=220, width=690, height=120)

        #  left Inside Frame

        left_inside_frame = Frame(left_frame, bd=2, relief=RIDGE, bg="white")
        left_inside_frame.place(x=3, y=125, width=690, height=423)

        #===== Labels and Entries =====#
        attendance_id_label = Label(left_inside_frame, text="Attendance ID:", font=("times new roman", 12, "bold"), bg="white")
        attendance_id_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)
        attendance_id_entry = ttk.Entry(left_inside_frame, width=20, font=("times new roman", 12, "bold"))
        attendance_id_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        # name_label
        name_label = Label(left_inside_frame, text="Name:", font=("times new roman", 12, "bold"), bg="white")
        name_label.grid(row=0, column=2, padx=10, pady=15, sticky=W)
        name_entry = ttk.Entry(left_inside_frame, width=20, font=("times new roman", 12, "bold"))
        name_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)

        # roll_label
        roll_label = Label(left_inside_frame, text="Roll No:", font=("times new roman", 12, "bold"), bg="white")
        roll_label.grid(row=1, column=0, padx=10, pady=15, sticky=W)
        roll_entry = ttk.Entry(left_inside_frame, width=20, font=("times new roman", 12, "bold"))
        roll_entry.grid(row=1, column=1, padx=10, pady=5, sticky=W)

        # class_label
        class_label = Label(left_inside_frame, text="Class:", font=("times new roman", 12, "bold"), bg="white")
        class_label.grid(row=1, column=2, padx=10, pady=15, sticky=W)
        class_entry = ttk.Entry(left_inside_frame, width=20, font=("times new roman", 12, "bold"))
        class_entry.grid(row=1, column=3, padx=10, pady=15, sticky=W)

        # date_label
        date_label = Label(left_inside_frame, text="Date:", font=("times new roman", 12, "bold"), bg="white")
        date_label.grid(row=2, column=0, padx=10, pady=15, sticky=W)
        date_entry = ttk.Entry(left_inside_frame, width=20, font=("times new roman", 12, "bold"))
        date_entry.grid(row=2, column=1, padx=10, pady=15, sticky=W)

        # time_label
        time_label = Label(left_inside_frame, text="Time:", font=("times new roman", 12, "bold"), bg="white")
        time_label.grid(row=2, column=2, padx=10, pady=15, sticky=W)
        time_entry = ttk.Entry(left_inside_frame, width=20, font=("times new roman", 12, "bold"))
        time_entry.grid(row=2, column=3, padx=10, pady=15, sticky=W)

        # Department Label
        department_label = Label(left_inside_frame, text="Department:", font=("times new roman", 12, "bold"), bg="white")
        department_label.grid(row=3, column=0, padx=10, pady=15, sticky=W)
        department_entry = ttk.Entry(left_inside_frame, width=20, font=("times new roman", 12, "bold"))
        department_entry.grid(row=3, column=1, padx=10, pady=15, sticky=W)

        # Attendance Status
        attendance_status_label = Label(left_inside_frame, text="Attendance Status:", font=("times new roman", 12, "bold"), bg="white")
        attendance_status_label.grid(row=3, column=2, padx=10, pady=15, sticky=W)

        attendance_status_entry = ttk.Combobox(left_inside_frame, width=20, font=("times new roman", 12, "bold"))
        attendance_status_entry['values'] = ("Status", "Present", "Absent")
        attendance_status_entry.grid(row=3, column=3, padx=10, pady=15, sticky=W)

        # Buttons

        btn_frame = Frame(left_inside_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=10, y=300, width=660, height=90)


        save_btn = Button(btn_frame, text="Import CSV", width=17, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        save_btn.grid(row=0, column=0, padx=0, pady=5, sticky=W)

        update_btn = Button(btn_frame, text="Export CSV", width=17, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        update_btn.grid(row=0, column=1, padx=0, pady=5, sticky=W)

        delete_btn = Button(btn_frame, text="Update",  width=17, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        delete_btn.grid(row=0, column=2, padx=0, pady=5, sticky=W)
        
        reset_btn = Button(btn_frame, text="Reset",  width=17, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        reset_btn.grid(row=0, column=3, padx=0, pady=5, sticky=W)

        exit_btn = Button(btn_frame, text="Exit", width=17, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        exit_btn.grid(row=1, column=0, padx=0, pady=5, sticky=W)


        # Right Frame
        left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Attendance Details", font=("times new roman", 12, "bold"))
        left_frame.place(x=740, y=10, width=700, height=580)

        # table frame
        table_frame = Frame(left_frame, bd=2, relief=RIDGE, bg="white")
        table_frame.place(x=5, y=5, width=685, height=540)
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)
        self.attendance_table = ttk.Treeview(table_frame, column=("attendance_id", "name", "roll", "class", "date", "time", "department", "status"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.attendance_table.xview)
        scroll_y.config(command=self.attendance_table.yview)
        self.attendance_table.heading("attendance_id", text="Attendance ID")
        self.attendance_table.heading("name", text="Name")
        self.attendance_table.heading("roll", text="Roll No")
        self.attendance_table.heading("class", text="Class")
        self.attendance_table.heading("date", text="Date")
        self.attendance_table.heading("time", text="Time")
        self.attendance_table.heading("department", text="Department")
        self.attendance_table.heading("status", text="Status")
        self.attendance_table['show'] = 'headings'
        self.attendance_table.column("attendance_id", width=90)
        self.attendance_table.column("name", width=90)
        self.attendance_table.column("roll", width=90)
        self.attendance_table.column("class", width=90)
        self.attendance_table.column("date", width=90)
        self.attendance_table.column("time", width=90)
        self.attendance_table.column("department", width=90)
        self.attendance_table.column("status", width=90)
        self.attendance_table.pack(fill=BOTH, expand=1)



if __name__ == "__main__":
    root = Tk()
    obj = attendance(root)
    root.mainloop()