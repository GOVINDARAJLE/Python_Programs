# program to find the hash of a file

# import hashlib
import hashlib

def hash_file(filename):
    h = hashlib.sha1()
    with open(filename, 'rb', buffering=0) as f:
        chunk = 0
        while chunk != b'':
            chunk =file.read(1024)
            h.update(chunk)
    
    return h.hexdigest()

message = input("Enter the file name: ")
print(hash_file(message))
print(message) 