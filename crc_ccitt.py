#!/usr/bin/python3

# This bit is pretty much taken from qbytearray.cpp then ported to python.
# No idea if it implements CRC-CCITT correctly; I think it doesn't.
crc_tbl = [
    0x0000, 0x1081, 0x2102, 0x3183,
    0x4204, 0x5285, 0x6306, 0x7387,
    0x8408, 0x9489, 0xa50a, 0xb58b,
    0xc60c, 0xd68d, 0xe70e, 0xf78f
]

def qChecksum(data):
    crc = 0xffff;
    for i in range(len(data)):
        c = data[i]
        crc = ((crc >> 4) & 0x0fff) ^ crc_tbl[((crc ^ c) & 0x0f)];
        c >>= 4;
        crc = ((crc >> 4) & 0x0fff) ^ crc_tbl[((crc ^ c) & 0x0f)];
    return ~crc & 0xffff;

#print(hex(qChecksum("A".encode('ascii'))))
#print(hex(qChecksum([104, 101, 108, 108, 111, 32, 98, 108, 97, 104, 10])))
