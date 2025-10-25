from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk

# Import your main attendance system here
from main import attendence__System   # ✅ Make sure 'main.py' is in the same folder


# Temporary user storage (replace later with database)
users = {"hello": "12345"}


class Login_Window:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1550x880+0+0")

        # Background image
        self.bg_img = Image.open(r"C:\Users\933si\Downloads\WhatsApp Image 2025-10-06 at 18.22.12.jpeg")
        self.bg_img = self.bg_img.resize((1550, 880), Image.Resampling.LANCZOS)
        self.bg = ImageTk.PhotoImage(self.bg_img)
        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

        # Frame for login form
        frame = Frame(self.root, bg="black")
        frame.place(x=610, y=170, width=340, height=450)

        # Login icon
        img_login = Image.open(r"C:\Users\933si\Downloads\WhatsApp Image 2025-10-06 at 18.22.12.jpeg")
        img_login = img_login.resize((100, 100), Image.Resampling.LANCZOS)
        self.photoimage_login = ImageTk.PhotoImage(img_login)
        lbl2 = Label(self.root, image=self.photoimage_login, bg="black", borderwidth=0)
        lbl2.place(x=730, y=175, width=100, height=100)

        # Heading
        get_str = Label(frame, text="Get Started", font=("times new roman", 20, "bold"), fg="white", bg="black")
        get_str.place(x=95, y=100)

        # Username
        username = Label(frame, text="Username", font=("times new roman", 15, "bold"), fg="white", bg="black")
        username.place(x=70, y=155)
        self.txtuser = ttk.Entry(frame, font=("times new roman", 15, "bold"))
        self.txtuser.place(x=40, y=180, width=270)

        # Password
        password = Label(frame, text="Password", font=("times new roman", 15, "bold"), fg="white", bg="black")
        password.place(x=70, y=225)
        self.txtpass = ttk.Entry(frame, font=("times new roman", 15, "bold"), show="*")
        self.txtpass.place(x=40, y=250, width=270)

        # Login button
        loginbtn = Button(frame, command=self.login, text="Login",
                          font=("times new roman", 15, "bold"), bd=3, relief=RIDGE,
                          fg="white", bg="red", activeforeground="white", activebackground="red")
        loginbtn.place(x=110, y=300, width=120, height=35)

        # Register button
        registerbtn = Button(frame, command=self.register_window, text="New User? Register",
                             font=("times new roman", 10, "bold"), borderwidth=0,
                             fg="white", bg="black", activeforeground="white", activebackground="black")
        registerbtn.place(x=15, y=350, width=160)

        # Forget password button
        forgetbtn = Button(frame, command=self.forget_password_window, text="Forget Password",
                           font=("times new roman", 10, "bold"), borderwidth=0,
                           fg="white", bg="black", activeforeground="white", activebackground="black")
        forgetbtn.place(x=15, y=370, width=160)

    # ---------------- LOGIN FUNCTION ----------------
    def login(self):
        user = self.txtuser.get()
        password = self.txtpass.get()

        if user == "" or password == "":
            messagebox.showerror("Error", "All fields are required")
        elif user in users and users[user] == password:
            messagebox.showinfo("Success", f"Welcome {user}! Logged in successfully.")
            self.open_attendance_window()  
        else:
            messagebox.showerror("Invalid", "Invalid username or password")

    # ---------------- OPEN ATTENDANCE WINDOW ----------------
    def open_attendance_window(self):
        self.new_window = Toplevel(self.root)
        self.app = attendence__System(self.new_window)

    # ---------------- REGISTER FUNCTION ----------------
    def register_window(self):
        self.new_window = Toplevel(self.root)
        self.new_window.title("Register")
        self.new_window.geometry("400x400")

        Label(self.new_window, text="Register New User", font=("times new roman", 20, "bold")).pack(pady=10)

        Label(self.new_window, text="Username", font=("times new roman", 15)).pack(pady=5)
        self.reg_username = Entry(self.new_window, font=("times new roman", 15))
        self.reg_username.pack(pady=5)

        Label(self.new_window, text="Password", font=("times new roman", 15)).pack(pady=5)
        self.reg_password = Entry(self.new_window, font=("times new roman", 15), show="*")
        self.reg_password.pack(pady=5)

        Button(self.new_window, text="Register", font=("times new roman", 15, "bold"),
               bg="green", fg="white", command=self.register_user).pack(pady=20)

    def register_user(self):
        new_user = self.reg_username.get()
        new_pass = self.reg_password.get()

        if new_user == "" or new_pass == "":
            messagebox.showerror("Error", "All fields are required", parent=self.new_window)
        elif new_user in users:
            messagebox.showerror("Error", "Username already exists", parent=self.new_window)
        else:
            users[new_user] = new_pass
            messagebox.showinfo("Success", "Registration Successful!", parent=self.new_window)
            self.new_window.destroy()

    # ---------------- FORGET PASSWORD FUNCTION ----------------
    def forget_password_window(self):
        self.forget_win = Toplevel(self.root)
        self.forget_win.title("Reset Password")
        self.forget_win.geometry("400x300")

        Label(self.forget_win, text="Reset Your Password", font=("times new roman", 20, "bold")).pack(pady=10)

        Label(self.forget_win, text="Username", font=("times new roman", 15)).pack(pady=5)
        self.forget_username = Entry(self.forget_win, font=("times new roman", 15))
        self.forget_username.pack(pady=5)

        Label(self.forget_win, text="New Password", font=("times new roman", 15)).pack(pady=5)
        self.forget_newpass = Entry(self.forget_win, font=("times new roman", 15), show="*")
        self.forget_newpass.pack(pady=5)

        Button(self.forget_win, text="Reset", font=("times new roman", 15, "bold"),
               bg="orange", fg="white", command=self.reset_password).pack(pady=20)

    def reset_password(self):
        user = self.forget_username.get()
        new_pass = self.forget_newpass.get()

        if user == "" or new_pass == "":
            messagebox.showerror("Error", "All fields are required", parent=self.forget_win)
        elif user not in users:
            messagebox.showerror("Error", "Username not found", parent=self.forget_win)
        else:
            users[user] = new_pass
            messagebox.showinfo("Success", "Password reset successfully!", parent=self.forget_win)
            self.forget_win.destroy()


if __name__ == "__main__":
    root = Tk()
    obj = Login_Window(root)
    root.mainloop()
