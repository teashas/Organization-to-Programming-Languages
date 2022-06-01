#! python3
# -*- coding: utf-8 -*-
"""
File: CS 332 Final Project: timer.py
Description: Decorator class Timer to output evaluation time
"""
__author__ = "Jordan Buck, Letsy Gonzalez, Saima Teasha"

import time
import math
from contextlib import ContextDecorator
from dataclasses import dataclass, field


@dataclass
class Timer(ContextDecorator):
    """
    Implementarion of a dataclass timer to use as a decorator.
    """

    _start_time: float = field(default=None, init=False, repr=False)
    last: float = field(default=math.nan, init=False, repr=False)

    def start(self) -> None:
        """Start a new timer"""
        self._start_time = time.perf_counter()

    def stop(self) -> float:
        """Stop the timer, and report the elapsed time"""
        if self._start_time is None:
            print("Uh oh")

        # Calculate elapsed time
        self.last = time.perf_counter() - self._start_time
        self._start_time = None

        return self.last

    def __enter__(self) -> "Timer":
        """Start a new timer as a context manager"""
        self.start()
        return self

    def __exit__(self, *exc_info) -> None:
        """Stop the context manager timer"""
        self.stop()
        print(self.last)
