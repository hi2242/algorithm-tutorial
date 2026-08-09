from itertools import permutations

def solution(n, weak, dist):
    dist_length = len(dist)
    weak_length = len(weak)
    answer = dist_length + 1
    for i in range(weak_length):
        weak.append(weak[i] + n)

    for i in range(weak_length):
        for friends in list(permutations(dist, dist_length)):
            count = 1
            position = weak[i] + friends[count - 1]

            for j in range(i, i + weak_length):
                if position < weak[j]:
                    count += 1
                    if count > dist_length:
                        break
                    position = weak[j] + friends[count - 1]
            answer = min(answer, count)

    answer = -1 if answer > dist_length else answer
    return answer