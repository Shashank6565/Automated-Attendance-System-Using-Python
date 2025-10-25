from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector 
import cv2


class student:
    def __init__(self, root):
        self.root = root
        self.root.title("Automated Attendance System")
        self.root.geometry("1530x790+0+0")
        self.root.title("Automated Attendance System")


    #==================== Variable Declaration ====================

        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_sem = StringVar()
        self.var_roll = StringVar()
        self.var_name = StringVar()
        self.var_sec = StringVar()
        self.var_phn = StringVar()
        self.var_email = StringVar()
        self.var_address = StringVar()
        self.var_searchby = StringVar()
        self.var_searchtxt = StringVar()
        self.var_photo = StringVar()
        self.var_dob = StringVar()
        self.var_id = StringVar()  

        
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
        title_lbl = Label(bg_img, text="STUDENT MANAGEMENT PORTAL", font=("times new roman", 35, "bold"), bg="yellow", fg="black")
        title_lbl.place(x=0, y=0, width=1530, height=45)


        # Frame (Main Frame)
        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=0, y=45, width=1530, height=665)


        # Left Frame
        left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Details", font=("times new roman", 12, "bold"))
        left_frame.place(x=30, y=10, width=700, height=580)


        # Image
        left_img = Image.open(r"C:\Users\933si\OneDrive\Desktop\Images for PBL\bg.jpg")
        left_img = left_img.resize((1530, 710), Image.Resampling.BICUBIC)
        self.photoleft_img = ImageTk.PhotoImage(left_img)

        f_img = Label(self.root, image=self.photoleft_img)
        f_img.place(x=40, y=215, width=690, height=120)


        # Current course information

        current_lbl = LabelFrame(left_frame, bd=2, bg="white", relief=RIDGE, text="Current Course Information", font=("times new roman", 12, "bold"))
        current_lbl.place(x=10, y=140, width=680, height=110)


        dep_lbl=Label(current_lbl, text="Department", font=("times new roman", 12, "bold"), bg="white")
        dep_lbl.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        dep_combo = ttk.Combobox(current_lbl, textvariable=self.var_dep, font=("times new roman", 12, "bold"), state="readonly")
        dep_combo['values'] = ("Select Department", "CSE", "ECE", "ME", "CE", "EE")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=10, pady=5, sticky=W)


        course_lbl = Label(current_lbl,  text="Course", font=("times new roman", 12, "bold"), bg="white")
        course_lbl.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        course_combo = ttk.Combobox(current_lbl, textvariable=self.var_course, font=("times new roman", 12, "bold"), state="readonly")
        course_combo['values'] = ("Select Course", "B.Tech", "M.Tech", "PhD")
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=10, pady=5, sticky=W)


        year_lbl = Label(current_lbl, text="Year", font=("times new roman", 12, "bold"), bg="white")
        year_lbl.grid(row=1, column=0, padx=10, pady=5, sticky=W)

        year_combo = ttk.Combobox(current_lbl, textvariable=self.var_year, font=("times new roman", 12, "bold"), state="readonly")
        year_combo['values'] = ("Select Year", "1st Year", "2nd Year", "3rd Year", "4th Year")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=10, pady=5, sticky=W)


        sem_lbl = Label(current_lbl, text="Semester", font=("times new roman", 12, "bold"), bg="white")
        sem_lbl.grid(row=1, column=2, padx=10, pady=5, sticky=W)

        sem_combo = ttk.Combobox(current_lbl, textvariable=self.var_sem, font=("times new roman", 12, "bold"), state="readonly")
        sem_combo['values'] = ("Select Semester", "Odd Semester", "Even Semester")
        sem_combo.current(0)
        sem_combo.grid(row=1, column=3, padx=10, pady=5, sticky=W)

        # Student class information

        current_class_lbl = LabelFrame(left_frame, bd=2, bg="white", relief=RIDGE, text="Student Class Information", font=("times new roman", 12, "bold"))
        current_class_lbl.place(x=10, y=240, width=680, height= 310)

        # Student ID.
        id_lbl = Label(current_class_lbl, text="Student ID", font=("times new roman", 12, "bold"), bg="white")
        id_lbl.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        id_entry = Entry(current_class_lbl, textvariable=self.var_id, font=("times new roman", 12, "bold"), bd=5, relief=GROOVE)
        id_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        # University Roll No.
        roll_lbl = Label(current_class_lbl, text="University Roll No.", font=("times new roman", 12, "bold"), bg="white")
        roll_lbl.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        roll_entry = Entry(current_class_lbl, textvariable=self.var_roll, font=("times new roman", 12, "bold"), bd=5, relief=GROOVE)
        roll_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)

        # Name.
        name_lbl = Label(current_class_lbl, text="Name", font=("times new roman", 12, "bold"), bg="white")
        name_lbl.grid(row=1, column=0, padx=10, pady=5, sticky=W)

        name_entry = Entry(current_class_lbl, textvariable=self.var_name, font=("times new roman", 12, "bold"), bd=5, relief=GROOVE)
        name_entry.grid(row=1, column=1, padx=10, pady=5, sticky=W)

        # Section.
        sec_lbl = Label(current_class_lbl, text="Section", font=("times new roman", 12, "bold"), bg="white")
        sec_lbl.grid(row=1, column=2, padx=10, pady=5, sticky=W)

        self.var_sec = StringVar()
        sec_combo= ttk.Combobox(current_class_lbl, textvariable=self.var_sec, font=("times new roman", 12, "bold"), state="readonly", width=18)
        sec_combo['values'] = ("Select Section", "A", "B", "C", "D", "E", "F", "G", "H", "AI/ML", "Data Science", "Cyber Security", "Cloud Computing", "Blockchain", "IoT")
        sec_combo.current(0)
        sec_combo.grid(row=1, column=3, padx=10, pady=5, sticky=W)


        # Phone No. 
        phn_entry = Entry(current_class_lbl, textvariable=self.var_phn, font=("times new roman", 12, "bold"), bd=5, relief=GROOVE)
        phn_lbl = Label(current_class_lbl, text="Phone No.", font=("times new roman", 12, "bold"), bg="white")
        phn_lbl.grid(row=2, column=0, padx=10, pady=5, sticky=W)
        phn_entry.grid(row=2, column=1, padx=10, pady=5, sticky=W)

        # Email.
        email_lbl = Label(current_class_lbl, text="Email", font=("times new roman", 12, "bold"), bg="white")
        email_lbl.grid(row=2, column=2, padx=10, pady=5, sticky=W)

        email_entry = Entry(current_class_lbl, textvariable=self.var_email, font=("times new roman", 12, "bold"), bd=5, relief=GROOVE)
        email_entry.grid(row=2, column=3, padx=10, pady=5, sticky=W)

        #DOB.
        dob_lbl = Label(current_class_lbl, text="DOB", font=("times new roman", 12, "bold"), bg="white")
        dob_lbl.grid(row=3, column=0, padx=10, pady=5, sticky=W)
        dob_entry = Entry(current_class_lbl, textvariable=self.var_dob, font=("times new roman", 12, "bold"), bd=5, relief=GROOVE)
        dob_entry.grid(row=3, column=1, padx=10, pady=5, sticky=W)
        
        # Address.
        address_lbl = Label(current_class_lbl, text="Address", font=("times new roman", 12, "bold"), bg="white")
        address_lbl.grid(row=3, column=2, padx=10, pady=5, sticky=W)

        address_entry = Entry(current_class_lbl, textvariable=self.var_address, font=("times new roman", 12, "bold"), bd=5, relief=GROOVE)
        address_entry.grid(row=3, column=3, padx=10, pady=5, sticky=W)

        # Radio buttons
        self.var_radio1 = StringVar()
        radio1 = ttk.Radiobutton(current_class_lbl, variable=self.var_radio1, text= "Take Photo Sample", value="Yes")
        radio1.grid(row=5, column=0, padx=10, pady=5, sticky=W)
        radio2 = ttk.Radiobutton(current_class_lbl, variable=self.var_radio1, text= "No Photo Sample", value="No")
        radio2.grid(row=5, column=1, padx=10, pady=5, sticky=W)

        # Buttons

        btn_frame = Frame(current_class_lbl, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=10, y=190, width=660, height=90)


        save_btn = Button(btn_frame, text="Save", command=self.add_data, width=17, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        save_btn.grid(row=0, column=0, padx=0, pady=5, sticky=W)

        update_btn = Button(btn_frame, text="Update", width=17, font=("times new roman", 12, "bold"), bg="blue", fg="white",  command=self.update_data)
        update_btn.grid(row=0, column=1, padx=0, pady=5, sticky=W)

        delete_btn = Button(btn_frame, text="Delete", command=self.delete_data, width=17, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        delete_btn.grid(row=0, column=2, padx=0, pady=5, sticky=W)
        
        reset_btn = Button(btn_frame, text="Reset", command=self.reset_data, width=17, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        reset_btn.grid(row=0, column=3, padx=0, pady=5, sticky=W)

        exit_btn = Button(btn_frame, text="Exit", width=17, font=("times new roman", 12, "bold"), bg="blue", fg="white", command=self.root.destroy)
        exit_btn.grid(row=1, column=0, padx=0, pady=5, sticky=W)

        update_photo_btn = Button(btn_frame, text="Update Photo", width=17, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        update_photo_btn.grid(row=1, column=1, padx=0, pady=5, sticky=W)

        take_photo_btn = Button(btn_frame, text="Take Photo",command=self.generate_dataset, width=17, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        take_photo_btn.grid(row=1, column=2, padx=0, pady=5, sticky=W)


        # Right Frame
        right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Details", font=("times new roman", 12, "bold"))
        right_frame.place(x=790, y=10, width=660, height=580)

        
        right_img = Image.open(r"C:\Users\933si\OneDrive\Desktop\Images for PBL\bg.jpg")
        right_img = right_img.resize((1530, 710), Image.Resampling.BICUBIC)
        self.photoright_img = ImageTk.PhotoImage(right_img)

        r_img = Label(self.root, image=self.photoright_img)
        r_img.place(x=800, y=215, width=650, height=120)

        #======================= Search Frame =========================
 
        right_frame_lbl = LabelFrame(right_frame, bd=2, bg="white", relief=RIDGE, text="Search Student", font=("times new roman", 12, "bold"))
        right_frame_lbl.place(x=10, y=140, width=640, height= 105)

        search_lbl= Label(right_frame_lbl, text="Search By", font=("times new roman", 12, "bold"), bg="white")
        search_lbl.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        search_combo = ttk.Combobox(right_frame_lbl, font=("times new roman", 12, "bold"), state="readonly")
        search_combo['values'] = ("Select", "Roll No.", "Phone No.")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=10, pady=5, sticky=W)


        search_entry = Entry(right_frame_lbl, font=("times new roman", 12, "bold"), bd=5, relief=GROOVE)
        search_entry.grid(row=0, column=2, padx=5, pady=5, sticky=W)

        search_btn = Button(right_frame_lbl, text="Search", width=10, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        search_btn.grid(row=0, column=3, padx=5, pady=5, sticky=W)

        show_all_btn = Button(right_frame_lbl, text="Show All", width=10, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        show_all_btn.grid(row=1, column=0, padx=5, pady=5, sticky=W)
        


        #======================= Table Frame =========================

        table_frame = Frame(right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=10, y=255, width=640, height=290)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame, columns=("id", "dep", "course", "year", "sem", "roll", "name", "sec", "phn", "email", "dob", "address", "photo"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        

        self.student_table.heading("id", text="Student ID")
        self.student_table.heading("dep", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("roll", text="Roll No.")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("sec", text="Section")
        self.student_table.heading("phn", text="Phone No.")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("dob", text="Date of Birth")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("photo", text="Photo Status")
        
        self.student_table["show"] = "headings"

        self.student_table.column("id", width=100)
        self.student_table.column("dep", width=100)
        self.student_table.column("course", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("sem", width=100)
        self.student_table.column("roll", width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("sec", width=100)
        self.student_table.column("phn", width=100)
        self.student_table.column("email", width=100)
        self.student_table.column("dob", width=100)
        self.student_table.column("address", width=100)
        self.student_table.column("photo", width=100)

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()  
        
    #======================= Function Declaration =========================

    def add_data(self):
        if self.var_dep.get() == "Select Department" or self.var_course.get() == "Select Course" or self.var_year.get() == "Select Year" or self.var_sem.get() == "Select Semester" or self.var_sec.get() == "Select Section":
            messagebox.showerror("Error", "All fields are required.", parent=self.root)
        else:
            try:

                conn= mysql.connector.connect(host="Localhost", user="root", password="GEUshashanksingh6565", database="college")
                my_cursor = conn.cursor()
                my_cursor.execute("INSERT INTO student VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (self.var_id.get(), self.var_dep.get(), self.var_course.get(), self.var_year.get(), self.var_sem.get(), self.var_roll.get(), self.var_name.get(), self.var_sec.get(), self.var_phn.get(), self.var_email.get(), self.var_dob.get(), self.var_address.get(), self.var_radio1.get()))
                conn.commit()
                self.fetch_data()  
                conn.close()
                messagebox.showinfo("Success", "Student details added successfully.", parent=self.root)
            except Exception as e:
                messagebox.showerror("Error", f"Error due to {str(e)}", parent=self.root)
                conn.rollback()
                conn.close()

    #======================= Fetch Data =========================

    def fetch_data(self):
        conn = mysql.connector.connect(host="Localhost", user="root", password="GEUshashanksingh6565", database="college")
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT * FROM student")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert("", END, values=row)
            conn.commit()
        conn.close()



    #======================= Function to open student details window =========================
     
    def get_cursor(self, event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        row = content['values']

        self.var_id.set(row[0])
        self.var_dep.set(row[1])
        self.var_course.set(row[2])
        self.var_year.set(row[3])
        self.var_sem.set(row[4])
        self.var_roll.set(row[5])
        self.var_name.set(row[6])
        self.var_sec.set(row[7])
        self.var_phn.set(row[8])
        self.var_email.set(row[9])
        self.var_dob.set(row[10])
        self.var_address.set(row[11])
        self.var_radio1.set(row[12])



    #======================= Function to Update student details =========================

    # def update_data(self):

    #     if self.var_dep.get() == "Select Department" or self.var_course.get() == "Select Course" or self.var_year.get() == "Select Year" or self.var_sem.get() == "Select Semester":
    #         messagebox.showerror("Error", "All fields are required.", parent=self.root)
    #     else:
    #         try:
    #             upadate = messagebox.askyesno("Update", "Do you want to update these details?", parent=self.root)
    #             if upadate > 0:
    #                 conn = mysql.connector.connect(host="Localhost", user="root", password="GEUshashanksingh6565", database="college")
    #                 my_cursor = conn.cursor()
    #                 my_cursor.execute("UPDATE student SET dep=%s, course=%s, year=%s, sem=%s, roll=%s, name=%s, sec=%s, phn=%s, email=%s, dob=%s, address=%s, photo=%s WHERE id=%s",(
    #                 self.var_dep.get(), self.var_course.get(), self.var_year.get(), self.var_sem.get(), self.var_roll.get(), self.var_name.get(), self.var_sec.get(), 
    #                 self.var_phn.get(), self.var_email.get(), self.var_dob.get(), self.var_address.get(), self.var_radio1.get(), self.var_id.get()))   
    #             else:
    #                 if not upadate:
    #                     return          
    #             messagebox.showinfo("Success", "Student details updated successfully.", parent=self.root)  
    #             conn.commit()
    #             self.fetch_data()
    #             conn.close()

    #         except Exception as es:
    #             messagebox.showerror("Error", f"Error due to {str(es)}", parent=self.root)


    def update_data(self):
        if self.var_dep.get() == "Select Department" or self.var_name.get() == "":
            messagebox.showerror("Error", "All fields are required.", parent=self.root)
        else:
            try:
                update = messagebox.askyesno("Update", "Do you want to update these student details?", parent=self.root)
                if update > 0:
                    conn = mysql.connector.connect(host="Localhost", user="root", password="GEUshashanksingh6565", database="college")
                    my_cursor = conn.cursor()

                    # THIS IS THE FINAL, FULLY CORRECTED SQL QUERY with exact column names from SHOW COLUMNS
                    my_cursor.execute("UPDATE student SET Department=%s, Course=%s, Year=%s, Semester=%s, `University Roll No.`=%s, Name=%s, Section=%s, `Phone No.`=%s, Email=%s, DOB=%s, Address=%s, `Photo Sample`=%s WHERE `Student ID`=%s", (
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_sem.get(),
                        self.var_roll.get(),  # This now correctly maps to `University Roll No`
                        self.var_name.get(),
                        self.var_sec.get(),
                        self.var_phn.get(),   # This now correctly maps to `Phone No`
                        self.var_email.get(),
                        self.var_dob.get(),
                        self.var_address.get(),
                        self.var_radio1.get(),
                        self.var_id.get()    # This is for the WHERE clause `Student ID`
                    ))
                else:
                    if not update:
                        return

                messagebox.showinfo("Success", "Student details updated successfully.", parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()

            except Exception as es:
                messagebox.showerror("Error", f"Error due to: {str(es)}", parent=self.root)
    
    #Delete Function

    def delete_data(self):
        if self.var_id.get() == "":
            messagebox.showerror("Error", "Student ID must be required", parent=self.root)
        else:
            try:
                delete = messagebox.askyesno("Delete", "Do you want to delete this student?", parent=self.root)
                if delete > 0:
                    conn = mysql.connector.connect(host="Localhost", user="root", password="GEUshashanksingh6565", database="college")
                    my_cursor = conn.cursor()
                    sql = "DELETE FROM student WHERE `Student ID`=%s"
                    val = (self.var_id.get(),)
                    my_cursor.execute(sql, val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete", "Successfully deleted student details", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Error due to: {str(es)}", parent=self.root)

    # Reset Function

    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_sem.set("Select Semester")
        self.var_id.set("")
        self.var_roll.set("")
        self.var_name.set("")
        self.var_sec.set("Select Section")
        self.var_phn.set("")
        self.var_email.set("")
        self.var_dob.set("")
        self.var_address.set("")
        self.var_radio1.set("")


    #======================= Generate Data Set or Take Photo Sample =========================
    def generate_dataset(self):
        if self.var_dep.get() == "Select Department" or self.var_course.get() == "Select Course" or self.var_year.get() == "Select Year" or self.var_sem.get() == "Select Semester":
            messagebox.showerror("Error", "All fields are required.", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="Localhost", user="root", password="GEUshashanksingh6565", database="college")
                my_cursor = conn.cursor()
                my_cursor.execute("SELECT * FROM student")
                myresult = my_cursor.fetchall()
                id = 0
                for x in myresult:
                    id += 1
                my_cursor.execute("UPDATE student SET Department=%s, Course=%s, Year=%s, Semester=%s, `University Roll No.`=%s, Name=%s, Section=%s, `Phone No.`=%s, Email=%s, DOB=%s, Address=%s, `Photo Sample`=%s WHERE `Student ID`=%s",(
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_sem.get(),
                    self.var_roll.get(),
                    self.var_name.get(),
                    self.var_sec.get(),
                    self.var_phn.get(),
                    self.var_email.get(),
                    self.var_dob.get(),
                    self.var_address.get(),
                    self.var_radio1.get(),
                    self.var_id.get()==id+1
                ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                # Load predefined data on face frontals from opencv
                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                    # Scaling factor = 1.3
                    # Minimum Neighbors = 5

                    for (x, y, w, h) in faces:
                        face_cropped = img[y:y+h, x:x+w]
                        return face_cropped

                cap = cv2.VideoCapture(0)
                img_id = 0
                while True:
                    ret, my_frame = cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id += 1
                        face = cv2.resize(face_cropped(my_frame), (450, 450))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        file_name_path = "data/user." + str(id) + "." + str(img_id) + ".jpg"
                        cv2.imwrite(file_name_path, face)
                        cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
                        cv2.imshow("Cropped Face", face)

                        if cv2.waitKey(1) == 13 or int(img_id) == 100:  # 13 is the Enter Key
                            break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result", "Generating data sets completed!", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Error due to: {str(es)}", parent=self.root)

if __name__ == "__main__":
    root = Tk()
    obj = student(root)
    root.mainloop()
