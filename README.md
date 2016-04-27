# HourglassBreaker

This is a python program that can open files encrypted by [Hourglass](https://github.com/NateBrune/Hourglass) by bruteforcing the key protecting the file.

It does not matter how many iterations you've set in Hourglass, because the underlying encryption is only 16-bit.

A test vector is included. HourglassBreaker works best on medium length messages. If it's too short, then the CRC isn't effective, and multiple keys produce a file that checksums correctly. The longer the file is, the longer HB will take.

## Example usage

$ time ./bruteforce.py todecrypt
Solution found!
key = 0x2a4f
plaintext = b'Lorem ipsum dolor sit amet, consectetur adipiscing elit.\n'
flags = 2

real	0m3.239s
user	0m3.240s
sys	0m0.000s

## License

GPLv3
