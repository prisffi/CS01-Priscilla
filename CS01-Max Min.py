Nub = int(input())
list = []
for i in range(Nub):
    Num = input()
    if Num == "":break
    list.append(int(Num))
print(list)
print(min(list))
print(max(list))