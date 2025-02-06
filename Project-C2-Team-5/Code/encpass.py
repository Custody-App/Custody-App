import hashlib

def hashpassword(password):
    encodedpassword = password.encode('utf-8')
    hash_obj = hashlib.sha256(encodedpassword)
    hashpassword = hash_obj.hexdigest()
    return hashpassword
