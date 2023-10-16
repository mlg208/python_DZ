import hashlib

username = "MLG"
passw = "12345678"

# hash = hashlib.md5()
# hash = hashlib.sha1()
hash = hashlib.sha512()
hash.update(username.encode('utf-8'))
hash.update(passw.encode('utf-8'))

hash_string = hash.hexdigest()
print(hash_string)