def findMinHeightTrees(n, edges):
	adj = [[] for i in range(n)]
	for e in edges:
		u, v = e
		adj[u].append(v)
		adj[v].append(u)

	leaves = []
	for i in range(len(adj)):
		if len(adj[i]) == 1:
			leaves.append(i)
	# print(adj)
	# print(leaves)
	nodes = n															
	while nodes > 2:
		nodes -= len(leaves)
		# print('>>>.====',leaves)
		curLen = len(leaves)
		newLeaves = []
		for i in (range(curLen)):
			leaf = leaves[i]
			# print('leaf', leaf)
			# print(adj)
			parent = adj[leaf].pop()
			adj[parent].remove(leaf)
			if len(adj[parent]) == 1:
				newLeaves.append(parent)
		leaves = newLeaves
	# print('res' ,leaves)
	return leaves

n = 6
edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]

findMinHeightTrees(n ,edges)
		
		