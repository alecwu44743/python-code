# 1+0 -> start : 0
# 1+3 2+4 -> start : 1*3
# 3+6 4+7 5+8 -> start : 2*3
# 5+12 6+13 7+14 8+15 -> start : 2*(2*3)

add = 0

for row in range(0, 4):
    if row == 0:
        print(str(0))
    # else: