import M2Crypto
import base64

fileName = "public_key.pub"
RSAKey = M2Crypto.RSA.gen_key(512, 3)

RSAKey.save_pub_key(fileName)
public_file = open(fileName,"r")
keyString = public_file.read().split("-----")[2].strip()
public_file.close()
keyInt = int.from_bytes(base64.b64decode(keyString),byteorder='big')
print("---- Copy N below ----")
print(keyInt)
print("---- ----")

#paste the output from encrypt.py to here
#secretMessage = 963259373376
secretMessage = int(input("Paste the secret message here in int : "))

decrypted_message = RSAKey.private_decrypt((secretMessage).to_bytes(10, byteorder='big'), M2Crypto.RSA.no_padding).decode('latin1')

print("---- Decrypted Message ----")
print(int.from_bytes(decrypted_message.encode('latin1'),byteorder='big'))
