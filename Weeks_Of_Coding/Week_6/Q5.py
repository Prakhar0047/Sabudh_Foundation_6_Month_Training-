N = int(input())
input_str = []

for x in range(N):
	input_str.append(input())

Q = int(input())
query = []

for x in range(N):
	query.append(input())

count = []
for x in query:
	c = input_str.count(x)
	count.append(c)

print(*count)