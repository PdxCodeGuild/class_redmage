#!/usr/bin/env perl
import sys

if len(sys.argv) == 1:
    print("Sorry but I'm gonna need more than that!")
else:
    words = len(sys.argv)
    x = 1
    original_statement = ""
    reverse_statement = ""
    print("Thanks, here we go!\n")
    print("You said:")
    while x < words:
        original_statement += sys.argv[x]
        if x < words:
            original_statement += " "
        x += 1
    print("    " + original_statement)
    print("What you said backwards is:")
    x = words-1
    while x > 0:
        reverse_statement += sys.argv[x]
        if x > 0:
            reverse_statement += " "
        x -= 1
    print("    " + reverse_statement)
print("Is it a palindrome? I dunno, let's check!\nChecking...")