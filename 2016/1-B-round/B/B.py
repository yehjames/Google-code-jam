


t = int(input())  # read a line with a single integer
for x in range(1, t + 1):
      # line = str(input())
      C, J = [s for s in input().split(" ")]  # read a list of integers, 2 in this case
      C= list(C)
      J=list(J)
      L = len(C)
      result_C = []
      result_J = []
      large = None
      for i in range(L):
            if C[i] == "?" and J[i] == "?" and large == None:
                 C[i] = str(0)
                 J[i] = str(0)
            elif C[i] == "?" and J[i] == "?" and large == C:
                 C[i] = str(0)
                 J[i] = str(9)
            elif C[i] == "?" and J[i] == "?" and large == J:
                 C[i]= str(9)
                 J[i]=str(0)
            
            elif  C[i] != "?" and J[i] == "?" and large == None:
                 J[i] = C[i]
            elif  C[i] != "?" and J[i] == "?" and large == C:
                 J[i] = str(9)
            elif  C[i] != "?" and J[i] == "?" and large == J:
                 J[i]=str(0)
            
            elif  C[i] == "?" and J[i] != "?" and large == None:
                 C[i] = J[i]
            elif  C[i] == "?" and J[i] != "?" and large == C:
                 C[i] = str(0)
            elif  C[i] == "?" and J[i] != "?" and large == J:
                 C[i]= str(9)


            elif int(C[i]) > int(J[i]):
                  large = C
            elif int(C[i]) < int(J[i]):
                  large = J

      print("Case #{}: {} {}".format(x, "".join(C), "".join(J)))
  # check out .format's specification for more formatting options