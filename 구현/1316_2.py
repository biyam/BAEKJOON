ans = 0
for T in range(int(input())):
  s = input() 
  flag = True
  for i in range(len(s)):
    for j in range(i):
      for k in range(j):
        if s[i] == s[k] and s[i] != s[j]:
          flag = False
  if flag:
    ans += 1
print(ans)