def liner_search(alf , text):
    for x in range(len(alf)):
        if alf[x] == text:
            return x
    return None


def binary_search(alf, left, right, text):
    while True:
        middle = (left + right) // 2
        if text < alf[middle]:
            right = middle - 1
        if text > alf[middle]:
            left = middle + 1
        else:
            return middle
        if left > right:
            return None


def naive_search(text, pattern):
    n = len(text)
    m = len(pattern)

    for i in range(n - m + 1):
        for j in range(m):
            if text[i + j] != pattern[j]:
                break
        else:  # выполняется, если цикл завершился без break
            return i

    return -1


def rabin_karp_search(S, P):
    def simple_hash(s):
        h = 0
        for c in s:
            h += ord(c)
        return h

    n = len(S)
    m = len(P)

    if m == 0 or n < m:
        return -1

    original_hash = simple_hash(P)
    temp_hash = simple_hash(S[0:m])

    for i in range(n - m + 1):
        if original_hash == temp_hash:
            if S[i:i + m] == P:
                return i

        if i < n - m:
            temp_hash = temp_hash - ord(S[i]) + ord(S[i + m])

    return -1

