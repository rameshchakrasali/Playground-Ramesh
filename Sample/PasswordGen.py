import random
import string

strupr = string.ascii_uppercase
strlwr = string.ascii_lowercase
strltr = string.ascii_letters
strdgt = string.digits
strsym = string.punctuation

print("Enter the length of password: ")
length=int(input())

all = strupr+strlwr+strltr+strdgt+strsym
out = random.sample(all,length)
password = "".join(out)
print(password)

