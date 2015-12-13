import sys

test_cases = open(sys.argv[1], 'r')
total = 0
for line in test_cases:
    total += int(line)
print total