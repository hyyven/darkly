import hashlib

STRING = "albatroz"
print(hashlib.sha256(STRING.lower().encode('utf-8')).hexdigest())