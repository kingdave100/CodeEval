import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.strip("\n").split()
    if int(test[len(test)-1]) > len(test)-1:
        continue
    else:
        print test[(len(test)-1)-int(test[len(test)-1])]