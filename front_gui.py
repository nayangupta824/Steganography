from Tkinter import *
from PIL import ImageTk, Image    
import tkFileDialog
from main import Encode , Decode
from tkFileDialog import askopenfilename



def path():
     askopenfilename(filetypes=[("Image File",'.png'),("Image File", '.jpg')])


def decrypt():
         root1=Tk()
         width=root1.winfo_screenwidth()
         height=root1.winfo_screenheight()
         root1.geometry('%dx%d+0+0'%(width,height))
         Label(root1, text="Enter 16 bit Key :").grid(row=0)
         e = Entry(root1)
         e.grid(row=0, column=1)
         pbtn = Button(root1, text='Enter Image Path', command=path)#lambda:(root1.tkFileDialog.askopenfilename(filetypes=[("Image File",'.png'),("Image File", '.jpg')]))
         pbtn.grid(row=2, column=1, sticky=W, pady=4, padx=5)         
         ibtn=Button(root1, text="Decode")
         ibtn.grid(row=2, column=2, sticky=W, pady=4, padx=5)







def encrypt():
         root1=Tk()
         width=root1.winfo_screenwidth()
         height=root1.winfo_screenheight()
         root1.geometry('%dx%d+0+0'%(width,height))
         Label(root1, text="Enter 16 bit Key :").grid(row=0)
         e = Entry(root1)
         e.grid(row=0, column=1)
         Label(root1, text="Enter the message :").grid(row=2)
         e1 = Entry(root1)
         e1.grid(row=2, column=1)
         pbtn = Button(root1, text='Image Path', command=path)#lambda:(root1.tkFileDialog.askopenfilename(filetypes=[("Image File",'.png'),("Image File", '.jpg')]))
         pbtn.grid(row=4, column=1, sticky=W, pady=4, padx=5)         
         ibtn=Button(root1, text="Encode",command = Encode())
         ibtn.grid(row=4, column=2, sticky=W, pady=4, padx=5)

        
       
              

def main():
    root = Tk()
    root.geometry("300x200+300+300")
    app = (root)
    eButton = Button(root, text="ENCODE", command=encrypt)
    eButton.pack(side=LEFT, padx=5, pady=5)
    dButton = Button(root, text="DECODE", command=decrypt)
    dButton.pack(side=LEFT)
    root.mainloop()  


if __name__ == '__main__':
    main()  
