num = int(input())
wordList = []
for i in range(num):
    word = str(input())
    wordList.append(word)

cnt = len(wordList)
for word in wordList:
  wordSet = list(set(word))
  spellList = []  
  spellList.append(word[0])
  for i in range(1, len(word)):
    if word[i] != word[i-1]:
      spellList.append(word[i])
  if len(wordSet) != len(spellList):
    cnt -= 1

print(cnt)
