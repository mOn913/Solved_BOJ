word = input().upper()
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
             'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
freq = [0] * 26

for w in word:
    for i in range(26):
        if alphabet[i] == w:
            freq[i] += 1
            break

max_val = max(freq)
max_count = freq.count(max_val)
if max_count == 1:
    print(alphabet[freq.index(max_val)])
else:
    print("?")