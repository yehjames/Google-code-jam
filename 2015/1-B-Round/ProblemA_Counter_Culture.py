import collections
# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    n = int(input())  # read a list of integers, 2 in this case
    D = collections.OrderedDict([[10**0, 1], [10**1, 1+(9) ], [10**2, 1+9+(9+1+9)], [10**3, 1+9+9+1+9+(9+1+99)], 
        [10**4, 1+9+9+1+9+9+1+99+(99+1+99)], [10**5, 1+9+9+1+9+9+1+99+99+1+99+(99+1+999)], 
        [10**6, 1+9+9+1+9+9+1+99+99+1+99+99+1+999+(999+1+999)]])
    if len(str(n)) == 1:
        result =  n
    else: 
        # print("num: "+str(n))
        length= len(str(n))
        # print("length: "+str(length))
        # print("right: "+str(n)[(length/2):])
        # print("left: "+str(n)[0:length/2][::-1])
        right = int(str(n)[(length/2):])
        if n in D:
            result = D[n]
        elif str(right)[-1] != "0":
            left = int(str(n)[0:length/2][::-1])
            swap = 0
            if left  > 1:
                swap = 1
            result = (right-1)+(left)+D[10**(length-1)]+swap
        
        elif str(right)[-1] == "0":
            n=n-1
            length= len(str(n))
            right = int(str(n)[(length/2):])
            left = int(str(n)[0:length/2][::-1])
            swap = 0
            if left  > 1:
                swap = 1
            result = (right-1)+(left)+D[10**(length-1)]+swap+1

    print("Case #{}: {}".format(i, result))
  # check out .format's specification for more formatting options