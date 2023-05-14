import time

print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)
print("\n")
current_time = time.time()
for x in range(0,11):
	print(x)
print("\n")
total_time = time.time() - current_time
print(total_time)
