n = int(input())

scores_list = list(map(int, input().split()))

scores_list.sort()

for i in range(-1, -len(scores_list), -1):
    current_element = scores_list[i]
    i -= 1
    if scores_list[i] < current_element:
        print(scores_list[i])
        break
