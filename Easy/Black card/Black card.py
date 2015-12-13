import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    count = 0
    index = 0
    test = test.split("|")
    names = test[0].split()
    blackSpot = int(test[1])
    while len(names) > 1:
        for i in names:
            count += 1
            if count == blackSpot:
                names.remove(i)
                count = 0
                break

    print names[0]
