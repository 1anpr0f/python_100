import validators 
#from validator import validate_email
email = "derickian57@gmail.com"
if validators.email(email):
    print("email is valide")
else:
    print("bad email")
