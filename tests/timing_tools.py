from contextlib import contextmanager
import time


@contextmanager
def get_timing() -> float:
    start_time = end_time = time.perf_counter() 
    yield lambda: end_time - start_time
    end_time = time.perf_counter() 


def time_it(func):
    def wrapper(*args, **kwargs):
        with get_timing() as t:
            _ = func(*args, **kwargs)
        return t()
    return wrapper
