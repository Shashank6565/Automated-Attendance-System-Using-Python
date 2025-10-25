import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import os
import cv2
import numpy as np
import mysql.connector

class face_recognition: 
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition")

        title_lbl = tk.Label(self.root, text="FACE RECOGNITION", font=("times new roman", 35, "bold"), bg="Blue", fg="white")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        img_top = Image.open(r"C:\Users\933si\Downloads\Gemini_Generated_Image_xmbmqmxmbmqmxmbm.png")
        img_top = img_top.resize((650, 750), Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = tk.Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=45, width=650, height=750)

        img_bottom = Image.open(r"C:\Users\933si\Downloads\Gemini_Generated_Image_nam6aynam6aynam6.png") 
        img_bottom = img_bottom.resize((900, 750), Image.LANCZOS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)
        
        b_lbl = tk.Label(self.root, image=self.photoimg_bottom)
        b_lbl.place(x=650, y=45, width=900, height=750)


        # Button
        train_btn = tk.Button(self.root, text="FACE RECOGNITION", command=self.face_recog, cursor="hand2", font=("times new roman", 30, "bold"), bg="green", fg="white")
        train_btn.place(x=800, y=600, width=500, height=40)

        train_btn = tk.Button(self.root, text="EXIT",command=self.root.destroy, cursor="hand2", font=("times new roman", 30, "bold"), bg="Red", fg="white")
        train_btn.place(x=880, y=700, width=250, height=35)

    # ======================  Face Recognition========================

    def face_recog(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray, scaleFactor, minNeighbors)
            coord = []

            for (x, y, w, h) in features:
                id, predict = clf.predict(gray[y:y + h, x:x + w])
                confidence = int(100 * (1 - predict / 300))

                conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="GEUshashanksingh6565",
                    database="college"
                )
                my_cursor = conn.cursor()

                my_cursor.execute("SELECT Name FROM student WHERE `Student ID`=%s", (id,))
                n = my_cursor.fetchone()
                n = "+".join(n) if n else "Unknown"

                my_cursor.execute("SELECT `University Roll No.` FROM student WHERE `Student ID`=%s", (id,))
                r = my_cursor.fetchone()
                r = "+".join(r) if r else "N/A"

                my_cursor.execute("SELECT Department FROM student WHERE `Student ID`=%s", (id,))
                d = my_cursor.fetchone()
                d = "+".join(d) if d else "N/A"

                my_cursor.execute("SELECT Course FROM student WHERE `Student ID`=%s", (id,))
                c = my_cursor.fetchone()
                c = "+".join(c) if c else "N/A"

                conn.close()

                if confidence > 77:
                    cv2.putText(img, f"ID: {id}", (x, y - 95), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)
                    cv2.putText(img, f"Name: {n}", (x, y - 70), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)
                    cv2.putText(img, f"Roll: {r}", (x, y - 45), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)
                    cv2.putText(img, f"Dept: {d}", (x, y - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown Face", (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)

                coord = [x, y, w, h]
            return coord

        def recognize(img, clf, faceCascade):
            coord = draw_boundary(img, faceCascade, 1.1, 10, (255, 25, 255), "Face", clf)
            return img

        # Load classifier and face detector
        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)

        while True:
            ret, img = video_cap.read()
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Face Recognition", img)

            if cv2.waitKey(1) == 13:  # Press Enter key to exit
                break

        video_cap.release()
        cv2.destroyAllWindows()




if __name__ == "__main__":
    root = tk.Tk()
    obj = face_recognition(root)
    root.mainloop()