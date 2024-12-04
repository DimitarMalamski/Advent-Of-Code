lines = [line.strip() for line in open("2024/Day 4 - Ceres Search/Part One/input.txt").readlines()]

ans = 0

def dfs(i, j):
    strs = ["X", "X", "X", "X", "X", "X", "X", "X"]

    for x in range(1, 4):
        if j + x < len(lines[i]):
            strs[0] += lines[i][j + x]

        if j - x >= 0:
            strs[1] += lines[i][j - x]

        if i - x >= 0:
            strs[2] += lines[i - x][j]

        if i + x < len(lines):
            strs[3] += lines[i + x][j]

        if i - x >= 0 and j + x < len(lines[i]):
            strs[4] += lines[i - x][j + x]

        if i + x < len(lines) and j + x < len(lines[i]):
            strs[5] += lines[i + x][j + x]

        if i + x < len(lines) and j - x >= 0:
            strs[6] += lines[i + x][j - x]

        if i - x >= 0 and j - x >= 0:
            strs[7] += lines[i - x][j - x]

    cnt = 0
    for str in strs:
        cnt += 1 if str == "XMAS" else 0

    return cnt


for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j] == "X":
            ans += dfs(i, j)

print(ans)
