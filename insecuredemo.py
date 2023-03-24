 

try:
    print(xs[7])
    print(xs[8])
except: pass
ys=[1, 2, None, None]
for y in ys:
    try:
        print(str(y+3)) #TypeErrors ahead
    except: continue #not how to handle them

#some imports
import hashlib
import telnetlib
import ftplib

s = b"I am a string"
print("SHA256: " +hashlib.sha256(s).hexdigest())