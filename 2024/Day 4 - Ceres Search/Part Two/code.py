lines = [line.strip() for line in open("2024/Day 4 - Ceres Search/Part Two/input.txt").readlines()]

ans = 0

def dfs(i, j):
    if i == 0 or i == len(lines) - 1 or j == 0 or j == len(lines[i]) - 1:
        return 0  

    strs = ['','']

    strs[0] += lines[i - 1][j - 1] + lines[i][j] + lines[i + 1][j + 1]
    strs[1] += lines[i - 1][j + 1] + lines[i][j] + lines[i + 1][j - 1]

    if (strs[0] == "SAM" or strs[0] == "MAS") and (strs[1] == "SAM" or strs[1] == "MAS"):
        return 1

    return 0 

for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j] == "A":
            ans += dfs(i, j)

print(ans)
