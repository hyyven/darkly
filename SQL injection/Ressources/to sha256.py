import hashlib

STRING = "FortyTwo"
print(hashlib.sha256(STRING.lower().encode('utf-8')).hexdigest())