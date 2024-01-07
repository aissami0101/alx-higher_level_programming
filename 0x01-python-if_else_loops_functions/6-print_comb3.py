#!/usr/bin/python3
for dig in range(0, 10):
    for dig2 in range(dig + 1, 10):
        if dig == 8 and dig2 == 9:
            print("{}{}".format(dig, dig2))
        else:
            print("{}{}".format(dig, dig2), end=", ")
