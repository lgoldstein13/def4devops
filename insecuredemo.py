

import hashlib

xs=[1,2,3,4,5,6,7,8]
try:
    print(xs[7])
    print(xs[8])
except: pass

ys=[1, 2, None, None]
for y in ys:
    try:
        if y is not None:
            print(str(y+3))
    except: continue

#some imports
import telnetlib
import ftplib

s = b"I am a string"
print("SHA256: " +hashlib.sha256(s).hexdigest())