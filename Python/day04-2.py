''' What is the lowest positive number that produces the MD5 hash with 6 zeroes? '''
import hashlib

def get_hash_number(secret_key):
    num = 1
    md5_hash = hashlib.md5(secret_key + str(num)).hexdigest()
    while md5_hash[:6] != "000000":
        num += 1
        md5_hash = hashlib.md5(secret_key + str(num)).hexdigest()
    return num
