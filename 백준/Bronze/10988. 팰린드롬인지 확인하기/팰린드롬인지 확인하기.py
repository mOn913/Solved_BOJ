w = input()
length = len(w)
isPalindrome = True
for i in range(length//2):
    if w[i] != w[length-i-1]:
        isPalindrome = False
        break
print(int(isPalindrome))