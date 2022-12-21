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
    root = nodes[Node.ROOT]
    root._resolve_child_nodes(nodes)
    return root


class Node(ABC):
    HUMAN = "humn"
    ROOT = "root"

    def __init__(self, name: str) -> None:
        self._name = name
        self._parent = self

    @property
    @abstractmethod
    def value(self) -> int:
        pass

    @property
    def name(self) -> str:
        return self._name

    @property
    def parent(self) -> Node:
        return self._parent

    @parent.setter
    def parent(self, value: Node) -> None:
        self._parent = value

    @abstractmethod
    def part2(self, value: int = 0) -> int:
        pass

    @abstractmethod
    def has_human(self) -> bool:
        pass

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

    def part2(self, value: int = 0) -> int:
        if self.has_human():
            return value
        raise ValueError("I am not human.")

    def has_human(self) -> bool:
        return self.name == Node.HUMAN

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

    def part2(self, value: int = 0) -> int:
        if not self.has_human():
            raise ValueError("No humans here.")
        if self.name == Node.ROOT:
            if self.left.has_human():
                return self.left.part2(self.right.value)
            return self.right.part2(self.left.value)
        return self._do_part2(value)

    @abstractmethod
    def _do_part2(self, value: int) -> int:
        pass

    def has_human(self) -> bool:
        return self.name == Node.HUMAN or self.left.has_human() or self.right.has_human()

    def _resolve_child_nodes(self, nodes: dict[str, Node]) -> None:
        self.left = nodes[self.left.name]
        self.right = nodes[self.right.name]
        self.left.parent = self
        self.right.parent = self
        self.left._resolve_child_nodes(nodes)
        self.right._resolve_child_nodes(nodes)


class MultiplicationNode(BinaryNode):
    def __init__(self, name: str, left: Node, right: Node) -> None:
        super().__init__(name, operator.mul, left, right)

    def __repr__(self) -> str:
        return f"{self.name}: {self.left.name} * {self.right.name}"

    def _do_part2(self, value) -> int:
        if self.left.has_human():
            return self.left.part2(value // self.right.value)
        return self.right.part2(value // self.left.value)

class DivisionNode(BinaryNode):
    def __init__(self, name: str, left: Node, right: Node) -> None:
        super().__init__(name, operator.floordiv, left, right)

    def __repr__(self) -> str:
        return f"{self.name}: {self.left.name} / {self.right.name}"

    def _do_part2(self, value) -> int:
        if self.left.has_human():
            return self.left.part2(value * self.right.value)
        return self.right.part2(self.left.value // value)


class AdditionNode(BinaryNode):
    def __init__(self, name: str, left: Node, right: Node) -> None:
        super().__init__(name, operator.add, left, right)

    def __repr__(self) -> str:
        return f"{self.name}: {self.left.name} + {self.right.name}"

    def _do_part2(self, value) -> int:
        if self.left.has_human():
            return self.left.part2(value - self.right.value)
        return self.right.part2(value - self.left.value)


class SubtractionNode(BinaryNode):
    def __init__(self, name: str, left: Node, right: Node) -> None:
        super().__init__(name, operator.sub, left, right)

    def __repr__(self) -> str:
        return f"{self.name}: {self.left.name} - {self.right.name}"

    def _do_part2(self, value) -> int:
        if self.left.has_human():
            return self.left.part2(value + self.right.value)
        return self.right.part2(self.left.value - value)


class UnresolvedNode(Node):
    def __init__(self, name: str) -> None:
        super().__init__(name)

    def __repr__(self) -> str:
        return f"{self.name}: <unresolved>"

    def value(self) -> int:
        raise (ValueError(f"Unresolved node {self.name}"))

    def part2(self, value: int = 0) -> int:
        raise (ValueError(f"Unresolved node {self.name}"))

    def has_human(self) -> bool:
        raise (ValueError(f"Unresolved node {self.name}"))

    def _resolve_child_nodes(self, nodes: dict[str, Node]) -> None:
        raise (ValueError(f"Unresolved node {self.name}"))
