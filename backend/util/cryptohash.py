import hashlib #it is library that includes the sha256 function 
import json

def crypto_hash(*args):
    """
    This function will return SHA-256 hash of the given arguments.
    """
    stringed_args =  sorted(map(lambda data: json.dumps(data),args)) #Lambda functions can have any number of arguments but only one expression. The expression is evaluated and returned. Lambda functions can be used wherever function objects are required.

    joined_data = ''.join(stringed_args)
    return hashlib.sha256(joined_data.encode('utf-8')).hexdigest() #here only encoded data can be hashed so we are encoding it into utf-8

def main():
    print(f"crypto_hash(one ,2, 3): {crypto_hash('test',2,3)}")
    print(f"crypto_hash(2 ,one, 3): {crypto_hash(2,'test',3)}")

if  __name__=='__main__':
    main()