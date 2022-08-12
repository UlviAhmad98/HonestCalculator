n = int(input())
value_list = []

for _ in range(n):
    n = int(input())
    value_list.append(n)

print(sum(value_list) / len(value_list))
