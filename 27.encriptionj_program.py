import random
import string
chars=" "+string.punctuation+string.digits+string.ascii_letters
chars=list(chars)
key=chars.copy()
print(chars)
print("-------------------------------------------------------------------------------------------------------------")
random.shuffle(key)
print(key)

# encription-------------------------------------------------------------------------------------------
plain_text=input("enter a message to encript")
siper_text=""

for le in plain_text:
    index=chars.index(le)
    siper_text+=key[index]

print(plain_text)
print(siper_text)

# decript------------------------------------------------------------------------------------------
siper_text=input("enter")
plain_text=""
for le in siper_text:
    index=key.index(le)
    plain_text+=chars[index]

print(siper_text)
print(plain_text)


