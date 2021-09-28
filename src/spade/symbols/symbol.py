"""This module holds the Symbol, ComputationalGraph, and ComputationalGraphNode classes and methods to help construct
a computational graph."""
from typing import Optional


class Symbol:
    """The Symbol class is the superclass representing all components of differential equation. Superclasses
    VectorField, ScalarField, Function, Constant, Operator"""

    def __init__(self, name: str):
        self.name = name

    def __repr__(self):
        return f'{self.name} <{type(self).__name__}>'

    def __str__(self):
        return self.name


class ComputationalGraphNode:
    """The ComputationalGraphNode class is a wrapper around the Symbol class that provides Graph functionality
    for usage within the ComputationalGraph class"""

    def __init__(
            self, symbol: Symbol,
            parent: 'ComputationalGraphNode' = None,
            children: list['ComputationalGraphNode'] = None
    ):
        self.symbol = symbol
        self.parent = parent
        self.children = children


class ComputationalGraph:
    """The ComputationalGraph class stores the context and computational relations between all information in a set
    of coupled differential equations (of which, each component is stored in child classes of the Symbol class."""

    def __init__(self):
        self.context: list[Symbol] = []
        self.__graph: Optional[ComputationalGraphNode] = None
