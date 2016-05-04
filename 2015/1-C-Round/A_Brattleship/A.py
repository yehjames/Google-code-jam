t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    R, C, W = [int(s) for s in input().split(" ")]  # read a list of integers, 2 in this case
    if C%W != 0:
        result = (C//W)*R+(W-1)+1
    else:
        result = (C//W)*R+(W-1)

    print("Case #{}: {}".format(i, result))
  # check out .format's specification for more formatting options