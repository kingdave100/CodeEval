import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.strip("\n")
    total = 0
    for i in test:
        total += int(i)
    print total