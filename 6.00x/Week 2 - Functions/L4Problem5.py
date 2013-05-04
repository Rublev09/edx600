def clip(lo, x, hi):
    return min(max(lo, x), hi)

print(clip(4,5,6))


