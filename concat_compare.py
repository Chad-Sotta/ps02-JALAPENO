import time

start = time.time()
result = ""

for i in  range (1, 100001):
    result += str(i)
print("+= Time:", time.time() - start)
