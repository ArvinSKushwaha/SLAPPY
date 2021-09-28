"""This module handles the Operator class and its subclasses, each of which represent an operation on a Symbol.
Instructions on extending these classes will be given in the documentation."""
from .symbol import Symbol


class Operator(Symbol):
    """The Operator class superclasses all operations on Fields, Functions, and Constants."""
    ...


class Add(Operator):
    """The Add class represents the summation operation."""
    def __init__(self):
        super().__init__("+")
        ...


class Subtract(Operator):
    """The Subtract class represents the subtraction operation."""
    def __init__(self):
        super().__init__("-")
        ...


class Multiply(Operator):
    """The Multiply class represents the multiplication operation."""
    def __init__(self):
        super().__init__("*")
        ...


class Divide(Operator):
    """The Divide class represents the division operation."""
    def __init__(self):
        super().__init__("/")
        ...


class Grad(Operator):
    """The Grad class represents the gradient operation."""
    def __init__(self):
        super().__init__("∇")
        ...


class Div(Operator):
    """The Div class represents the divergence operation."""
    def __init__(self):
        super().__init__("∇•")
        ...


class Curl(Operator):
    """The Curl class represents the curl operation."""
    def __init__(self):
        super().__init__("∇⨯")
        ...


class Laplacian(Operator):
    """The Laplacian class represents the laplacian operation."""
    def __init__(self):
        super().__init__("∇²")
        ...
