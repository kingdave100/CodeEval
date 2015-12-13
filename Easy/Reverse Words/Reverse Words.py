import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.strip("\n").split()
    for i in reversed(test):
        print i,
    print