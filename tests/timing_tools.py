import time
from contextlib import contextmanager


@contextmanager
def get_timing() -> float:
    start_time = end_time = time.perf_counter()
    yield lambda: end_time - start_time
    end_time = time.perf_counter()
