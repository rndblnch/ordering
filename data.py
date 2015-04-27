import random

for name in "ABCDEFGHI":
	print(name, *(random.random() for _ in range(20)), sep='\t')


