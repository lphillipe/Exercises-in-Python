def fn(x):
    if x <= 0:
        return 0
    return x + fn(x - 1)


print(fn(4))