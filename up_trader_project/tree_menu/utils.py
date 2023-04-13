import functools
import time

from django.db import connection, reset_queries


def query_debugger(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        reset_queries()
        start_queries = len(connection.queries)
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        end_queries = len(connection.queries)

        print(f'View (function name): {func.__name__}')
        print(f'Queries quantity: {end_queries - start_queries}')
        print(f'Execution time: {(end - start):.2f}s')
        return result
    return wrapper
