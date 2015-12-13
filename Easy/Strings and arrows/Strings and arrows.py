import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    total = 0
    index = 0
    while index < len(test):
        index = test.find("<--<<", index)
        if index == -1: break
        index += 4
        total += 1
    index = 0
    while index < len(test):
        index = test.find(">>-->", index)
        if index == -1: break
        index += 4
        total += 1
    print total
