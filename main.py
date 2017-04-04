from __future__ import absolute_import, unicode_literals
from steganography.steganography import Steganography
import encrypt_decrypt
import os

def Encode(input_path,output_path,message,key):
	#encrypting the message
	encrypted = encrypt_decrypt.encrypt(message , key)
	#steganograph the image
	Steganography.encode(input_path, output_path, encrypted)

def Decode(image_path , key):
	#steganograph the image
	message = Steganography.decode(image_path)
	#decrypting the message
	decrypted = encrypt_decrypt.decrypt(message , key)
	return decrypted

if __name__=="__main__":
	while True:
		os.system('clear')
		choice = input("CHOOSE THE OPERATION : \n1) Encode image \n2) Decode image\n3) Exit\n:")
		if choice == 1:
			os.system('clear')
			print("***********IMAGE ENCODING***********")
			input_path = raw_input("Enter the path of input image(default : image/input.jpg) : ")
			message = raw_input("Enter the message to encode : ")
			output_path = "image/output.jpg"
			key = raw_input("Enter the 16-charater long key (e.g thisismypassword): ")
			print "ENCODING ....."
			Encode(input_path,output_path,message,key)
			print "ENCODE SUCCESSFULL..."
			print "OUTPUT IMAGE AT image/output.jpg "
			print "Press enter to continue..."
			raw_input()
		elif choice == 2:
			os.system('clear')
			output_path = raw_input("Enter the path of the image to decode (default : image/output.jpg) : ")
			key = raw_input("Enter the key you have for it : ")
			print "Decoding ......"
			decrypted = Decode(output_path , key)
			print "DECODE SUCCESSFULL....."
			print "Decoded text is : " + decrypted
			print "Press enter to continue..."
			raw_input()
			
		elif choice == 3:
			os.system('clear')
			print "Press enter to exit..."
			raw_input()
			os.system('clear')
			break
		else:
			os.system('clear')
			print "Incorrect choice"
			print "Press enter to continue..."
			raw_input()
