
import math

# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(input())  # read a line with a single integer
for j in range(1, t + 1):
  mushroom_len = int(input())  # read a list of integers, 2 in this case
  mushroom_list= [int(s) for s in input().split(" ")]  # read a list of integers, 2 in this case
  result_1 = 0
  result_2 = 0  
  i = 0
  while i < mushroom_len-1:
        if mushroom_list[i]>mushroom_list[i+1]:
            result_1+= mushroom_list[i]-mushroom_list[i+1]
        i+=1
  
  i = 0
  Max = 0
  while i < mushroom_len-1:
        if mushroom_list[i]-mushroom_list[i+1]> Max :
            Max = mushroom_list[i]-mushroom_list[i+1]
        i+=1
  
  i = 0
  while i < mushroom_len-1:
        if mushroom_list[i] <  Max:
            result_2+=mushroom_list[i]
        else:
            result_2+= Max
        i+=1
  # print(mushroom_list)
  print("Case #{}: {} {}".format(j, result_1, result_2))
  # check out .format's specification for more formatting options
