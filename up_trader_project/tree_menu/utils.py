import functools
import time
from typing import Union

from django.db import connection, reset_queries
from django.db.models import QuerySet

from tree_menu.templatetags import tree_menu


def query_debugger(func: tree_menu
                   ) -> dict[str, Union[QuerySet, str, list[str]]]:
    """
    Декоратор. Подсчитывает у обрабатываемой функции количество запросов
    в базу данных и продолжительность её выполнения.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs
                ) -> dict[str, Union[QuerySet, str, list[str]]]:
        """
        Обёртка для функции. Обнуляет количество запросов в БД, подсчитывает
        их количество, запускает таймер, происходит выполнение обернутой
        функции, останавливается таймер и извлекается количество запросов.
        На печать выводится название обёрнутой функции (за счёт декоратора
        `wraps`), количество запросов и время выполнения обёрнутой функции.
        """
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
