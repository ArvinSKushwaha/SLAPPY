"""This module defines constant types, including the Vector and Scalar classes."""
from .symbol import Symbol


class Vector(Symbol):
    def __init__(self, name: str, dim: int):
        super().__init__(name)

        self.dim = dim


class Scalar(Symbol):
    def __init__(self, name: str):
        super().__init__(name)
