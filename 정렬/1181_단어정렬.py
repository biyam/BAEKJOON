lst = []
for i in range(int(input())):
  lst.append(input())
lst = list(set(lst))

final_list = []

# 단어의 길이와 단어를 같이 리스트화 시켜 저장
for j in lst:
    final_list.append((len(j), j))     

# sort()는 len(j), j 에서 앞을 먼저 정렬후에 앞의 조건이 일치하면 뒤를 정렬한다.
final_list.sort()                       

for len_voca, voca in final_list:
    print(voca)