import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.strip("\n").split(" ")
    for i in range(1,int(test[2])+1):
        out = ""
        if i % int(test[0]) == 0:
            out += "F"
        if i % int(test[1]) == 0:
            out += "B"
        if out == "":
            out = str(i)
        print out,
    print
