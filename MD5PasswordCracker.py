import hashlib

flag = 0

hash_type = input("Enter a hashing type (Only MD5/md5 is available for now, I apologize): ")

def md5Crack(pass_file, flag):
    for word in pass_file:
        
        enc_wrd = word.encode('utf-8')
        digest = hashlib.md5(enc_wrd.strip()).hexdigest() 

        if (digest == pass_hash):
            print(f"Password Found: {word}")
            flag = 1
            break

    if (flag == 0):
        print("Password is not in the list.")

if (hash_type == "md5" or hash_type == "MD5"):
    pass_hash = input("Enter MD5 Hash: ")

    wordlist = input("File name: ")

    try:
        pass_file = open(wordlist, "r")
    except:
        print("No file found.")
        quit()
    
    md5Crack(pass_file, flag)
