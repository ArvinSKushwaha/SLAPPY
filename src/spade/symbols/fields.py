"""This module defines the VectorField and ScalarField classes, as well as the Field class (which allows for
flexibility in defining the involved systems)."""
from .symbol import Symbol


class Field(Symbol):
    def __init__(self, name: str, input_dims: int, output_dims: int):
        super().__init__(name)

        self.input_dims = input_dims
        self.output_dims = output_dims


class VectorField(Field):
    def __init__(self, name: str, dims: int):
        super().__init__(name, dims, dims)


class ScalarField(Field):
    def __init__(self, name: str, dims: int):
        super().__init__(name, dims, 1)
