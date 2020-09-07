def encode(key): 
    encoded_str = ""
    for char in key:
        ascii_chr = ord(char)
        encoded_str += chr(ascii_chr + 2)
    return encoded_str

def decode(key):
    decoded_str = ""
    for char in key:
        ascii_chr = ord(char)
        decoded_str += chr(ascii_chr - 2)
    return decoded_str


def main():
    key = raw_input("Enter something to encode:")
    encoded_str = encode(key)
    decoded_str = decode(encoded_str)
    if decoded_str != key:
        print "key is not decoded"
    else:
        print "key is decoded, key:%s encoded str:%s, decoded string:%s" % \
              (key, encoded_str, decoded_str)

if __name__ == "__main__":
    main()    
