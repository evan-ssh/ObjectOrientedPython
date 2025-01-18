import functools

@functools.cache
def fibonnaci(n):
    if n < 2:
        return n
    return fibonnaci(n - 1) + (n - 2)

print(fibonnaci(40))