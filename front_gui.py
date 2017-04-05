from Tkinter import *
from PIL import ImageTk, Image    
import tkFileDialog
from main import Encode , Decode
from tkFileDialog import askopenfilename

path_to_file = []

def path():
     del path_to_file[:]
     ifile = askopenfilename(filetypes=[("Image File",'.png'),("Image File", '.jpg')])
     path_to_file.append(ifile)
     print path_to_file
     #print ifile

def decode(e1, key):
	message = Decode(path_to_file[0], key)
	e1.insert(0, message)

def decrypt():
         root1=Tk()
         width=root1.winfo_screenwidth()
         height=root1.winfo_screenheight()
         root1.geometry('%dx%d+0+0'%(width,height))
         Label(root1, text="Enter 16 bit Key :").grid(row=0)
         e = Entry(root1)
         e.grid(row=0, column=1)
         Label(root1, text="Decoded message:").grid(row=2)
         e1 = Entry(root1)
         e1.grid(row=2, column=1)
         pbtn = Button(root1, text='Enter Image Path', command = path)
         pbtn.grid(row=4, column=1, sticky=W, pady=4, padx=5)         
         ibtn=Button(root1, text="Decode",command = lambda: decode(e1, e.get()))
         ibtn.grid(row=4, column=2, sticky=W, pady=4, padx=5)


def test(kgp):
	print kgp



def encrypt():
         root1=Tk()
         width=root1.winfo_screenwidth()
         height=root1.winfo_screenheight()
         root1.geometry('%dx%d+0+0'%(width,height))
         Label(root1, text="Enter 16 bit Key :").grid(row=0)
         e = Entry(root1)
         #print e["text"]
         e.grid(row=0, column=1)
         Label(root1, text="Enter the message :").grid(row=2)
         e1 = Entry(root1)
         e1.grid(row=2, column=1)
         pbtn = Button(root1, text='Image Path', command=path)
         pbtn.grid(row=4, column=1, sticky=W, pady=4, padx=5)   
         print path_to_file      
         ibtn=Button(root1, text="Encode",command = lambda: Encode(path_to_file[0], "image/output2.jpg",e1.get(),e.get()))
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
