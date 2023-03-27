#!/usr/bin/python3
def safe_print_integer(value):
    while True:
        try:
            x = int(input("Please enter an integer value: "))
            print("{:d}".format(x))
            break
        except ValueError:
            print("False")
