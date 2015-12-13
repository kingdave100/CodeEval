import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    changeCase = True
    for character in test:
        if character.isalpha() and changeCase == True:
            sys.stdout.write(character.upper())
            changeCase = False
        elif character.isalpha():
            sys.stdout.write(character)
            changeCase = True
        else:
            sys.stdout.write(character)