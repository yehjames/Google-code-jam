import random
for _ in range(1000):
    result = ""
    for i in range(random.randint(10, 20)):
        sign=["+","-"]
        result += sign[random.randint(0, 1)]
    print(result)