import time

start = time.time()
result = ",".join(str(x) for x in range(1, 10001))

print(result)
print("Time:", time.time() - start)