import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    for letter in test.strip("\n"):
        if letter.isupper():
            sys.stdout.write(letter.lower())
        elif letter.islower():
            sys.stdout.write(letter.upper())
        else:
            sys.stdout.write(letter)
    print