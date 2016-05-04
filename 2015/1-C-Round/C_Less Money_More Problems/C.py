t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    C, D, V = [int(s) for s in input().split(" ")]  # read a list of integers, 2 in this case
    Q = [int(s) for s in input().split(" ")]
    N=0
    add=0
    while N < V:
       # N = The largest value we can produce. 
       # X = The smallest value we cannot produce.
        X= N+1
        if len(Q)!=0 and Q[0] <= X:
            X = Q.pop(0)
        else:
            add += 1
        N += X*C

    

    print("Case #{}: {}".format(i, add))
  # check out .format's specification for more formatting options
# Queue<Integer> Q = new ArrayDeque<>();
#       for (int i = 0; i < D; i++) {
#         Q.add(scan.nextInt());
#       }

#       long N = 0;
#       int add = 0;
#       while (N < V) {
#         // X = The smallest value we cannot produce.
#         long X = N + 1;
#         if (!Q.isEmpty() && Q.peek() <= X) {
#           // Use pre-existing denomination we haven't used.
#           X = Q.poll();
#         } else {
#           // No way to produce N+1, add a new denomination.
#           add++;
#         }
#         N += X * C;
#       }