import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import os
import cv2
import numpy as np

class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Train Data Set")

        img_top = Image.open(r"images/header1.jpg")
        img_top = img_top.resize((1530, 325), Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        f_lbl = tk.Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=0, width=1530, height=325)

        title_lbl = tk.Label(self.root, text="TRAIN DATA SET", font=("times new roman", 35, "bold"), bg="red", fg="white")
        title_lbl.place(x=0, y=0, width=1530, height=45)
        
        img_bottom = Image.open(r"images/people.jpg") 
        img_bottom = img_bottom.resize((1530, 450), Image.LANCZOS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)
        b_lbl = tk.Label(self.root, image=self.photoimg_bottom)
        b_lbl.place(x=0, y=325, width=1530, height=450)

        train_btn = tk.Button(self.root, text="TRAIN DATA", command=self.train_classifier, cursor="hand2", font=("times new roman", 30, "bold"), bg="blue", fg="white")
        train_btn.place(x=0, y=280, width=1530, height=60)

    def train_classifier(self):
        data_dir = "data"
        if not os.path.exists(data_dir):
            messagebox.showerror("Error", "Data directory not found. Please generate photo samples first.", parent=self.root)
            return

        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir) if file.endswith(".jpg")]

        faces = []
        ids = []

        for image in path:
            img = Image.open(image).convert('L') 
            image_np = np.array(img, 'uint8')
            id_str = os.path.basename(image).split('.')[1] 
            try:
                id_int = int(id_str)
            except ValueError:
                print(f"Skipping invalid ID: {id_str} from file {image}")
                continue 

            faces.append(image_np)
            ids.append(id_int)
            cv2.imshow("Training", image_np)
            cv2.waitKey(1)

        cv2.destroyAllWindows()

        if len(ids) == 0:
            messagebox.showerror("Error", "No valid face samples found for training.", parent=self.root)
            return

        ids = np.array(ids)

        classifier = cv2.face.LBPHFaceRecognizer_create()
        classifier.train(faces, ids)
        classifier.write("classifier.xml")
        
        messagebox.showinfo("Result", "Training dataset completed successfully", parent=self.root)

if __name__ == "__main__":
    root = tk.Tk()
    obj = Train(root)
    root.mainloop()