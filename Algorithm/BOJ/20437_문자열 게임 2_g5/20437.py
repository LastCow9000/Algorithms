# boj 20437 문자열 게임 2 g5
# noj.am/20437
import sys; inp = sys.stdin.readline
import string

def process_words(words):
    alpha_idx = {a:[] for a in string.ascii_lowercase}

    for idx, c in enumerate(words):
        alpha_idx[c].append(idx)

    return alpha_idx

def find_length(alpha_idx, K):
    min_length = 1e9
    max_length = -1

    for k, v in alpha_idx.items():
        if len(v) < K:
            continue

        for idx in range(len(v) - K + 1):
            length = v[idx + K - 1] - v[idx] + 1
            if length < min_length:
                min_length = length
            if length > max_length:
                max_length = length

    return (min_length, max_length)

def solution():
    T = int(inp())
    for _ in range(T):
        words = inp().rstrip()
        K = int(inp())

        alpha_idx = process_words(words)
        min_length, max_length = find_length(alpha_idx, K)

        print(-1) if max_length == -1 else print(*[min_length, max_length])

solution()