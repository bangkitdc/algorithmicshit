def determinant(n):
	if len(n) == 1:
		return n[0][0]
	res = 0
	for i in range(len(n)):
		res += (1 if i % 2 == 0 else -1) * n[0][i] * determinant([j[:i] + j[(i+1):] for j in n[1:]])
	return res

n = []

x = int(input())
for i in range(x):
	n.append(list(map(int, input().split())))

print(f'det = {determinant(n)}')

# find the co-factors
# for j in range(len(m)):
# 	for i in m[1:]:
# 		print(i[:j] + i[(j+1):])
