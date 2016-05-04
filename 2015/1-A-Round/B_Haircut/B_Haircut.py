import functools
def gcd(a, b):
    """Return greatest common divisor using Euclid's Algorithm."""
    while b:      
        a, b = b, a % b
    return a

def lcm(a, b):
    """Return lowest common multiple."""
    return a * b // gcd(a, b)

def lcmm(*args):
    """Return lcm of args."""   
    return functools.reduce(lcm, args)


# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(input())  # read a line with a single integer
for j in range(1, t + 1):
  B, N = [int(s) for s in input().split(" ")]   # read a list of integers, 2 in this case
  barbers_list= [int(s) for s in input().split(" ")]  # read a list of integers, 2 in this case
  l = lcmm(*barbers_list) 
  
  cycle = 0
  print(l)
  for num in barbers_list :
    cycle += l // num 
  print(cycle)
  
  N=N%cycle
  if N == 0:
      print("Case #{}: {} {}".format(j, B))
      continue
  if N <= B:
      print("Case #{}: {} {}".format(j, N))
      continue
  time=0
  number=0
  while True:
      available_list=range(1,B+1)
      bust_list=[]
    
      for i in range(N):
        busy_list.append(available_list.pop(0))
        if not available_list:

       time+=1  
    


  # print(mushroom_list)
  # print(B, N, barbers_list)
  print("Case #{}: {} {}".format(j, B, N))
  # check out .format's specification for more formatting options
