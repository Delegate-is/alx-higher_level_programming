#!/usr/bin/python3
#prints the ASCII alphabet, in lowercase, not followed by a new line

for n in range(ord('a'), ord('z') + 1):
    if chr(n) != 'q' and chr(n) != 'e':
            print("{}".format(chr(n)), end="")
