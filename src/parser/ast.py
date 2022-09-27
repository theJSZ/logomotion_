# pylint: disable=missing-class-docstring,missing-function-docstring,too-few-public-methods
""" Abstract Syntax Tree node definitions, returned by the parser. """
from entities.symbol_table import SymbolTable
from entities.error_values import ErrorValues
from entities.error_info import ErrorInfo

class Node:
    def __init__(self, node_type, children=None, leaf=None):
        self.type = node_type
        self.children = children if children else []
        self.leaf = leaf
        self.value = None

    def __str__(self):
        result = f"({self.type}"

        if self.leaf:
            result += f", {self.leaf if self.leaf else 'None'}"
        result += f", value: {self.value}"

        if self.children:
            result += ", children: ["
            result += ", ".join((child.__str__() for child in self.children))
            result += "]"

        result += ")"

        return result
    
    def check_for_errs(self, children, err_msg=""):
        """ check for errorvalues, if doesnt exist, create one
        """
        errs = []
        for child in children:
            if isinstance(child.value, ErrorValues):
                errs += child.value.errors
        ev = ErrorValues()
        if err_msg:
            ei = ErrorInfo(self, err_msg)
            ev.add_error(ei)
        ev.errors = errs
        return ev

class Start(Node):
    def __init__(self, children=None):
        super().__init__("Start", children)


class StatementList(Node):
    def __init__(self, children=None):
        super().__init__("StatementList", children, None)


class Statement(Node):
    def __init__(self, children=None):
        super().__init__("Statement", children, None)


class Command(Node):
    pass


class BinOp(Node):
    def __init__(self, children, leaf):
        super().__init__("BinOp", children, leaf)

    def eval(self):
        for child in self.children:
            if type(child.value) not in (int, float, ErrorValues):
                print("PRIIT")
                self.value = self.check_for_errs(self.children, "virhe: binop muksu muu kuin int tai float")
                return
            elif isinstance(child.value, ErrorValues):
                print("PRUUT")
                self.value = self.check_for_errs(self.children)
                return
        if self.leaf == "+":
            self.value = self.children[0].value + self.children[1].value
        elif self.leaf == "-":
            self.value = self.children[0].value - self.children[1].value
        elif self.leaf == "*":
            self.value = self.children[0].value * self.children[1].value
        elif self.leaf == "/":
            self.value = self.children[0].value / self.children[1].value
        else:
            self.value = "ERROR"

class UnaryOp(Node):
    def __init__(self, children, leaf):
        super().__init__("UnaryOp", children, leaf)


class Number(Node):
    def __init__(self, leaf):
        super().__init__("Number", children=None, leaf=leaf)

    def eval(self):
        self.value = self.leaf


class Float(Node):
    def __init__(self, leaf):
        super().__init__("Float", children=None, leaf=leaf)

    def eval(self):
        self.value = self.leaf


class Bool(Node):
    def __init__(self, leaf):
        super().__init__("Bool", children=None, leaf=leaf)


class Identifier(Node):
    def __init__(self, leaf):
        super().__init__("Ident", children=None, leaf=leaf)


class Deref(Node):
    def __init__(self, leaf):
        super().__init__("Deref", children=None, leaf=leaf)

    def eval(self):
        symbol_table = SymbolTable()
        self.value = symbol_table.lookup(self.leaf)


class StringLiteral(Node):
    def __init__(self, leaf):
        super().__init__("StringLiteral", children=None, leaf=leaf)


class If(Node):
    def __init__(self, children, leaf):
        super().__init__("If", children, leaf)


class IfElse(Node):
    def __init__(self, children, leaf):
        super().__init__("IfElse", children, leaf)
