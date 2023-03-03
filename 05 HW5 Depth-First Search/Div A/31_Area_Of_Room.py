from collections import defaultdict

def dfs(graph, visited, now):
    visited[now] = True
    for neigh in graph[now]:
        if not visited[neigh]:
            dfs(graph, visited, neigh)
    ans.append(now)

# read input
N = int(input())
graph = defaultdict(list)  # just for cleaner code
matrix_input = []
for i in range(N):  # assume N by N
    line = input()
    for j in range(N):
        if line[j] == '.':  # will check neighbors from left and above, if exist make and edge
            if line[j-1] == '.':
                graph[(i, j)].append((i, j-1))
                graph[(i, j-1)].append((i, j))
            if matrix_input[i-1][j] == '.':
                graph[(i, j)].append((i-1, j))
                graph[(i-1, j)].append((i, j))
    matrix_input.append(line)
row, col = map(int, input().split())  # wil -1 to make indexation consistent
row -= 1
col -= 1

visited = {}  # will keep what vertexes dfs visited
for key in graph.keys():
    visited[key] = False
ans = []  # a global variable, could use just int var but list is easier for debugging
dfs(graph, visited, (row, col))  # dfs checks within the component
print(len(ans))  # each vertex is of area 1

'''
Time Complexity: O(N^2)  # to read N^2 but also beside this works for O(N^2) in case of complete graph
Auxiliary Space Complexity: O(N^2)
Test cases:
5
*****
*...*
*****
*...*
*****
2 3
ans: 3
3
***
*.*
***
2 2
ans: 1
5
*****
*...*
*...*
*...*
*****
2 3
ans: 9'''