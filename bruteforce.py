#!/usr/bin/python3
import binascii
ux = binascii.unhexlify
hx = binascii.hexlify
import crc_ccitt
import base64
import sys

def decrypt(ciphertext, key):
    def split_key(key):
        l = []
        for i in range(8):
            l.append(key & 0xFF)
            key = key >> 8
        return l
    key = split_key(key)

    version = ciphertext[0]
    flags = ciphertext[1]
    main_ciphertext = ciphertext[2:]
    plaintext = []
    last_char = 0
    for i, enc_c in enumerate(main_ciphertext):
        dec_c = enc_c ^ last_char ^ key[i % 8]
        plaintext.append(dec_c)
        last_char = enc_c

    plaintext = bytes(plaintext)
    ignore = plaintext[0]
    message_crc = plaintext[1:3]
    real_plaintext = plaintext[3:]
    calculated_crc = crc_ccitt.qChecksum(real_plaintext).to_bytes(2, byteorder='big')
    if message_crc == calculated_crc:
        return real_plaintext, flags
    else:
        return False

if __name__ == '__main__':
    #ciphertext = ux("0302d91c2a42274b2748467f13721a10")
    #key = int("5b2e", 16)
    input_file = open(sys.argv[1]).read()
    ciphertext = base64.b64decode(input_file.split(":")[0])
    for i in range(65536):
        ret = decrypt(ciphertext, i)
        if ret != False:
            print("Solution found!")
            print("key = " + hex(i))
            print("plaintext = " + repr(ret[0]))
            print("flags = " + repr(ret[1]))
