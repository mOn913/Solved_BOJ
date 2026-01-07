n = int(input()) 
group_word_count = 0 

for i in range(n):
    isGroupWord = True
    appeared = [] # 나타난 문자 리스트
    word = input() 
    for j in range(len(word)):
        if word[j] in appeared: # 문자가 appeared 리스트에 있을 때
            if word[j-1] != word[j]: # 바로 이전 문자와 같지 않다면
                isGroupWord = False # group word가 아님
                break
        else:
            appeared.append(word[j]) # appeard에 추가
    if isGroupWord: # 문자를 모두 순회했음에도 isGroupWord가 True라면
        group_word_count += 1 # Group Word 이므로 count 1 증가

print(group_word_count)