from __future__ import annotations
from abc import ABC, abstractmethod
import re
from typing import Callable
import operator


def parse(rows: list[str]) -> Node:
    nodes: dict[str, Node] = {}
    for row in rows:
        match re.split(r"[: ]+", row):
            case [name, value]:
                nodes[name] = ValueNode(name, int(value))
            case [name, left, operation, right]:
                left_node = UnresolvedNode(left)
                right_node = UnresolvedNode(right)
                match operation:
                    case "*":
                        node = MultiplicationNode(name, left_node, right_node)
                    case "/":
                        node = DivisionNode(name, left_node, right_node)
                    case "+":
                        node = AdditionNode(name, left_node, right_node)
                    case "-":
                        node = SubtractionNode(name, left_node, right_node)
                nodes[name] = node
    root = nodes["root"]
    root._resolve_child_nodes(nodes)
    return root


class Node(ABC):
    def __init__(self, name: str) -> None:
        self._name = name

    @property
    @abstractmethod
    def value(self) -> int:
        pass

    @property
    def name(self) -> str:
        return self._name

    @abstractmethod
    def _resolve_child_nodes(self, nodes: dict[str, Node]) -> None:
        pass


class ValueNode(Node):
    def __init__(self, name: str, value: int) -> None:
        self._value = value
        super().__init__(name)

    def __repr__(self) -> str:
        return f"{self.name}: {self.value}"

    @property
    def value(self) -> int:
        return self._value

    def _resolve_child_nodes(self, nodes: dict[str, Node]) -> None:
        pass


class BinaryNode(Node):
    def __init__(self, name: str, operation: Callable[[int, int], int], left: Node, right: Node) -> None:
        self.operation = operation
        self.left = left
        self.right = right
        super().__init__(name)

    @property
    def value(self) -> int:
        return self.operation(self.left.value, self.right.value)

    def _resolve_child_nodes(self, nodes: dict[str, Node]) -> None:
        self.left = nodes[self.left.name]
        self.right = nodes[self.right.name]
        self.left._resolve_child_nodes(nodes)
        self.right._resolve_child_nodes(nodes)


class MultiplicationNode(BinaryNode):
    def __init__(self, name: str, left: Node, right: Node) -> None:
        super().__init__(name, operator.mul, left, right)

    def __repr__(self) -> str:
        return f"{self.name}: {self.left.name} * {self.right.name}"


class DivisionNode(BinaryNode):
    def __init__(self, name: str, left: Node, right: Node) -> None:
        super().__init__(name, operator.floordiv, left, right)

    def __repr__(self) -> str:
        return f"{self.name}: {self.left.name} / {self.right.name}"


class AdditionNode(BinaryNode):
    def __init__(self, name: str, left: Node, right: Node) -> None:
        super().__init__(name, operator.add, left, right)

    def __repr__(self) -> str:
        return f"{self.name}: {self.left.name} + {self.right.name}"


class SubtractionNode(BinaryNode):
    def __init__(self, name: str, left: Node, right: Node) -> None:
        super().__init__(name, operator.sub, left, right)

    def __repr__(self) -> str:
        return f"{self.name}: {self.left.name} - {self.right.name}"


class UnresolvedNode(Node):
    def __init__(self, name: str) -> None:
        super().__init__(name)

    def __repr__(self) -> str:
        return f"{self.name}: <unresolved>"

    def value(self) -> int:
        raise (ValueError(f"Unresolved node {self.name}"))

    def _resolve_child_nodes(self, nodes: dict[str, Node]) -> None:
        raise (ValueError(f"Unresolved node {self.name}"))
