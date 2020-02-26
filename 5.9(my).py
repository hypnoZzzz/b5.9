import time


class Timing:
    def __init__(self, runs_function):
        self.runs = 1000
        self.run_func = runs_function

    def __call__(self, *args, **kwargs):
        i = 0
        for _ in range(self.runs):
            t0 = time.time()
            self.run_func(*args, **kwargs)
            t1 = time.time()
            i += (t1 - t0)
        i /= self.runs
        funcs = self.run_func.__name__
        print("[Timing] Cреднее время %s, %s запусков: %.5f sec" % (funcs, self.runs, i))
        return self.run_func(*args, **kwargs)

    def __enter__(self):
        print('enter')
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print('exit')


@Timing
def fib(up_to_n):
    seq = [1]
    a, b = 1, 2
    while b < up_to_n:
        c = a + b
        a = b
        b = c
        seq.append(a)
    return seq
print(sum(x for x in fib(4_000_000) if x % 2 == 0))