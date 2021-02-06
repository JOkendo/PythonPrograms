"""Checks the equality of floating numbers"""
d = 1.11 - 1.10
d1 = 2.11 - 2.10
dif = d1 - d
if 0.0000001 < d1 - d < 0.0000001:
    print("Equals")
else:
    print("Different")