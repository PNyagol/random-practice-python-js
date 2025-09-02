import time
start = time.time()
print(start)
print("Start it a heavy computation...")
for i in range(100000):
    pass

end = time.time()
print(end)
execution_time = end - start
print(f"The execution took {execution_time: .4f} seconds")