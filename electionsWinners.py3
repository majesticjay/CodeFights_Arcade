def electionsWinners(v, k):
    m = max(v)    
    return int(v.count(m) == 1) if k == 0 else len([n for n in v if m < n + k])
