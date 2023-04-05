import hashlib
import os

def hash_file(filename):
    # hash object
    h = hashlib.sha1()
    # open file for reading in binary mode
    with open(filename,'rb') as file:
        # loop till the end of the file
        chunk = 0
        while chunk != b'':
            # read only 1024 bytes at a time
            chunk = file.read(1024)
            h.update(chunk)
    # return the hex representation of digest
    return h.hexdigest()

message = hash_file("/Users/lucasdevries/Documents/GVSUWinter23/CIS455/MerkleTree/Files/File1.rtf") # change to a file within the given directory
path_of_the_directory= '/Users/lucasdevries/Documents/GVSUWinter23/CIS455/MerkleTree/Files' # change to wanted path for directory
print("Files and directories in a specified path:")
files = []
for filename in os.listdir(path_of_the_directory):
    f = os.path.join(path_of_the_directory,filename)
    if os.path.isfile(f):
        split_tup = os.path.splitext(f)
        file_name = split_tup[0]
        file_extension = split_tup[1]
        if(file_extension == ".rtf"): # Filtering out the added file within this directory, only getting the file types 'rtf'
            files.append(hash_file(f))
            print("File: " + file_name + " Hash: " + hash_file(f))

def merkleRoot(leaves):
    if 0 == len(leaves):
        raise ValueError("Should not be called with an empty list")
    # If there is only one leave, we are done
    if 1 == len(leaves):
        return leaves[0]
    # If the number of leaves is odd, append the last element again
    if 1 == (len(leaves) % 2):
        leaves.append(leaves[-1])
    n = []
    for i in range(len(leaves) // 2):
        x = leaves[2*i] + leaves[2*i+1]
        n.append(hashlib.sha1(str(x).encode('utf-8')).hexdigest())
    return merkleRoot(n)

print("Root Hash: " + merkleRoot(files))