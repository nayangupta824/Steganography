# Steganography

*youtube link* - https://youtu.be/gY-V5t1hHh0

Stecrypt is a GUI based application that performs steganography on image files. Stecypt takes as imput an image file and a message. Then it encrypts that message on the basis of a key provided by user and hides the encrypted message into image file using steganography techniques. Finally, it generates steganographic image containing hidden message.
Stecrypt also allows user to extract the encrypted message, hidden in steganographic image. This encypted message can be decrypted if correct key is provided.

*Features:*

1. Enrypt a message on the basis of key provide.
2. Hide the message in an image file.
3. Retrieve the text message hidden in an image file.
4. Decrypt the message when correct key is provided.

*Application Description:*

Stecrypt contains 3 main components:

Graphical User Interface
Encryption/Decryption Module
Steganography module
Requirements:

*Operating System:*
Linux

*Programming Language:*
Python 2.7

*Modules:*
pycrypto
Tkinter
steganography
PIL (or Pillow)
tkFileDialog



Installation Guide:

1. Download and extract .tar file.
2. Goto extracted directory.
3. Install requirements using:
pip install -r requirements.txt
4. Run main.py, using:
python main.py
FOR gui Run front_gui.py (but we are still working on this!!)
