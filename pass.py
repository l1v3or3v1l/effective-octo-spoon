import re

password = input("Enter password : ")

if re.search('^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[$#@])[A-Za-z0-9$#@]{6,}$', password):
	print("Password Valid")
else:
	print("Password Invalid")