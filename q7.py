import re

email = input("Enter Email : ")
parts = "(\w+)@(\w+\.)+(com)"
name = re.match(parts,email)
print(name.group(1))