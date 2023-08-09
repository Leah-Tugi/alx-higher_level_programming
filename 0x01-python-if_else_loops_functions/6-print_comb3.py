#!/usr/bin/python3
# 6-print_comb3.py
# Leah M Mutugi 

"""Print all possible different combinations of two digits in ascending order.

    The two digits must be different - 01 and 10 are considered identical.
    """
for dig1 in range(0, 10):
    for dig2 in range(dig1 + 1, 10):
        if dig1 == 8 and dig2 == 9:
            print("{}{}".format(dig1, dig2))
        else:
            print("{}{}".format(dig1, dig2), end=", ")
