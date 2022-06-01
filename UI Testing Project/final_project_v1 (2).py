#! python3
# -*- coding: utf-8 -*-
"""
File: CS 332 Final Project: final_project_v1.0.0.py
Description: Python UI aspect of testing differences to Swift
"""
__author__ = "Jordan Buck, Letsy Gonzalez, Saima Teasha"
__version__ = "1"

import tkinter as tk
from tkinter import ttk
from timer import Timer


class PushButtons(tk.Tk):
    """
    Creates a pushable button.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Python UI")
        _sq_size = 400
        self.minsize(_sq_size, _sq_size)

        ttk.Label(self,
                  text="Python UI",
                  font=("TkDefaultFont", 24)
                  ).grid(row=0, column=0, columnspan=3, padx=_sq_size/2)
        ttk.Button(self,
                   text="Push Me",
                   command=self.push_me).grid(column=1, row=1, padx=_sq_size/2, pady=20)

    @Timer()
    def push_me(self) -> None:
        """Function of Push Me button"""


if __name__ == '__main__':
    instance = PushButtons()
    instance.mainloop()
