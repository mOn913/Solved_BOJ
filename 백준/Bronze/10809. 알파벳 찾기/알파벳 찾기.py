s = input()
a_to_z = list('abcdefghijklmnopqrstuvwxyz')
first_appeard = [-1] * 26
for i in range(len(s)):
    for j in range(26):
        if s[i] == a_to_z[j] and first_appeard[j] == -1:
            first_appeard[j] = i
print (' '.join(str(w) for w in first_appeard))