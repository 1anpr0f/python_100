import random 

print("enter your password:  ")

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()"
   
password = ''
for x in range(16):
     password+= random.choice(chars)


print(password)