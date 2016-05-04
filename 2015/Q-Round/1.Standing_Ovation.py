
# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.



  # check out .format's specification for more formatting options



# f = open('A-small-practice.in.txt', 'r')

# for line in f.readlines():
    
#     if str(line) == "100":
#         pass
#     print(line)

#     # print(str(line), end='')
#     s_max, sequence = line.split(" ")
#     print(s_max, sequence)

t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):  
  n, m = [s for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
  
  list_a= [int(x) for x in str(m)]
  # print(n,list_a[0:n])
  # answer = int(n) - sum(list_a[0:int(n)]) if int(n) - sum(list_a[0:int(n)]) >= 0 else 0
  answer = 0
  j = 0
  while j < len(list_a):
    if list_a[j] !=0:
        answer += j - (sum(list_a[0:j])+answer) if j - (sum(list_a[0:j])+answer) >= 0 else 0

    j+=1 



  print "Case #{}: {} ".format(i, answer)


