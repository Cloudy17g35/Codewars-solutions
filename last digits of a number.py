def solution(n,d):
    return [int(i) for i in list(str(n))[-d:]] if d > 0 else []
