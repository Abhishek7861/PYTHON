s1 = input()
s2 = input()
seq = ""
Matrix = [[0 for x in range(len(s1)+2)] for y in range(len(s2)+2)]
for i in range(len(s1)):
    for j in range(len(s2)):
        if s1[i] == s2[j]:
            Matrix[i+1][j+1] = Matrix[i][j]+1
        else:
            Matrix[i + 1][j + 1] = max(Matrix[i][j+1], Matrix[i+1][j])


print("Longest Common Subsequence:", (Matrix[len(s1)][len(s2)]))
i = len(s1)
j = len(s2)
while (i != 0) and (j != 0):
    if Matrix[i][j] != max(Matrix[i][j-1], Matrix[i-1][j]):
        seq = seq+s1[i-1]
        i = i-1
        j = j-1
    elif Matrix[i][j] == Matrix[i-1][j]:
        i = i-1

    elif Matrix[i][j] == Matrix[i][j-1]:
        j = j-1

print("Sequence", seq)
