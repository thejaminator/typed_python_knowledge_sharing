import time

"""
Hello world of python types

To compile (with mypc)
>>> mypyc fib.py
To run compiled
>>> python -c "import fib"
To run uncompiled
>>> python fib.py

"""


def fib_untyped(n):
    """
    :param n: int
    :return: int
    """
    if n <= 1:
        return 1
    else:
        return n * fib(n - 1)


def fib(n: int) -> int:
    if n <= 1:
        return 1
    else:
        return n * fib(n - 1)


t0 = time.time()
fib(32)
print(time.time() - t0)
