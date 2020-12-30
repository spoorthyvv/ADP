import re
s1="Phone number is 8105136046,994569963"
x=re.search("[6-9]\d{9}",s1)
print(x.group())
e='^[a-zA-Z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,6}$'
def check(email):
	if(re.search(e,email)):
		print("Valid")
	else:
		print("Invalid")

check("​ spoorthy.osb@gmail.com​ ")
