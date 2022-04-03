#Encryption
message_list = []
secret_list = []
secret_message = ""

with open(input("Message File name: ")) as f:
    message_list = f.readlines()

with open(input("Secret Key File name: ")) as f:
    secret_list = f.readlines()

if len(message_list[0]) < len(secret_list[0]):
    for i in range(0,len(message_list[0])):
        secret_message = secret_message + chr((ord(message_list[0][i]) ^ ord(secret_list[0][i]))%128)       
else:
    print("Message cannot be smaller than the secret!")

print("Secret Message::    " + secret_message + "\n")

#Decryption
decrypted_message = ""
for i in range(0,len(secret_message)):
    decrypted_message = decrypted_message + chr((ord(secret_message[i]) ^ ord(secret_list[0][i]))%128)

print("Decrypted Message::    " + decrypted_message + "\n")
