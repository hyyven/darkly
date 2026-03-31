import hashlib

STRING = "true"
print(hashlib.md5(STRING.encode('utf-8')).hexdigest())
