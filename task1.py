def unite(a: list, b: list):
	return [i for i in set(a+b) if i in a and i in b]


print(unite([3,2,1], [3,2,0]))
# result: [2,3]