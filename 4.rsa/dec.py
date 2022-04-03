#Written in Python 3.9.6
#Encrypt with public key
print('"""  This will decrypt with private key  """')

n = int(input("Enter N: "))
d = int(input("Enter D: "))
message = int(input("Enter your message in integer: "))
decrypted  = pow(message,d,n)
print("Decrypted Message: ",decrypted)
