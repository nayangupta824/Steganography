from Crypto.Cipher import AES
from Crypto import Random
import base64
BS = 16
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
unpad = lambda s : s[0:-ord(s[-1])]


class AESCipher:

    def __init__( self, key ):
        self.key = key

    def encrypt( self, raw ):
        raw = pad(raw)
        iv = Random.new().read( AES.block_size )
        cipher = AES.new( self.key, AES.MODE_CBC, iv )
        return base64.b64encode( iv + cipher.encrypt( raw ) )

    def decrypt( self, enc ):
        enc = base64.b64decode(enc)
        iv = enc[:16]
        cipher = AES.new(self.key, AES.MODE_CBC, iv )
        return unpad(cipher.decrypt( enc[16:] ))


def encrypt(message , key):
	cipher = AESCipher(key)
	code = cipher.encrypt(message)
	return code
	
def decrypt(code , key):
	cipher2 = AESCipher(key)
	message = cipher2.decrypt(code)
	return message
if __name__=="__main__":
	while True:
		choice = input("choose one of following : \n1) Encryption \n2) Decryption\n3) Exit\n:")
		if choice == 1:
			message = raw_input("Enter the message to encrypt : ")
			key = raw_input("Enter the key of 16 characters long : ")
			code = encrypt(message,key)
			print "The encrypted message is : " + code
			print "**Encoded successfully**"
		elif choice == 2:
			code = raw_input("Enter the code to decrypt : ")
			key = raw_input("Enter its key : ")
			message = decrypt(code , key)
			print message
		elif choice == 3:
			break
		else:
			print "Incorrect Input"
