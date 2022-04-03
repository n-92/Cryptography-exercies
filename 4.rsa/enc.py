#Written in Python 3.9.6
#Encrypt with public key
print('"""  This will encrypt with public key  """')

n = int(input("Enter N: "))
e = int(input("Enter E: "))

message = int(input("Enter your message in integer: "))
while(True):    
    if (message >= n):
        message = int(input("Enter your message less than N (in integer): "))
    else:
        break
encrypted  = pow(message,e,n)
print("Encrypted Message: ",encrypted)
