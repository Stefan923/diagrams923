from graphviz import Digraph
from pathlib import Path
from typing import Union, List, Dict

import uuid
import os


class Diagram:
    __out_formats = ("png", "jpg", "svg", "pdf", "dot")

    _default_graph_attrs = {
        "pad": "2.0",
        "splines": "ortho",
        "nodesep": "0.60",
        "ranksep": "0.75",
        "fontname": "Sans-Serif",
        "fontsize": "15",
        "fontcolor": "#2D3436",
    }

    def __init__(self):
        self.out_formats = []
        self.show = True
        self.graph = Digraph("default", filename="../default_filename")

        for key, value in self._default_graph_attrs.items():
            self.graph.graph_attr[key] = value

    def add_out_format(self, out_format: str) -> None:
        if out_format in self.__out_formats:
            self.out_formats.append(out_format)

    def render(self) -> None:
        for out_format in self.out_formats:
            self.graph.render(format=out_format, view=self.show, quiet=True)

    def add_node(self, node_id: str, label: str, **attributes) -> None:
        self.graph.node(node_id, label=label, **attributes)

    def add_edge(self, tail_node: "Node", head_node: "Node", edge: "Edge"):
        self.graph.edge(tail_node.id, head_node.id, **edge.attributes)


class Node:

    _icon_dir = None
    _icon = None

    _height = 1.9

    def __init__(self, diagram: Diagram, label: str = "", **attributes: Dict):
        self._id = self.get_random_id()
        self._diagram = diagram

        padding = 0.4 * (label.count('\n'))
        self._attributes = {}
        self._attributes = {
            "shape": "none",
            "height": str(self._height + padding),
            "image": self._load_icon(),
        } if self._icon else {}

        self._attributes.update(**attributes)

    def _load_icon(self):
        basedir = Path(os.path.abspath(os.path.dirname(__file__)))
        return os.path.join(basedir.parent, self._icon_dir, self._icon)

    @property
    def id(self):
        return self._id

    def connect(self, node: "Node", edge: "Edge"):
        if not isinstance(node, Node):
            ValueError(f"{node} is not a valid Node")
        if not isinstance(edge, Edge):
            ValueError(f"{edge} is not a valid Edge")

        self._diagram.add_edge(self, node, edge)
        return node

    @staticmethod
    def get_random_id():
        return uuid.uuid4().hex


class Edge:

    _default_edge_attrs = {
        "fontcolor": "#2D3436",
        "fontname": "Sans-Serif",
        "fontsize": "13",
    }

    def __init__(
        self,
        node: Node = None,
        **attributes: Dict
    ):
        self._node = node
        self._forward = True
        self._reverse = False
        self._attributes = {}

        for key, value in self._default_edge_attrs:
            self._attributes[key] = value

        self._attributes.update(attributes)

    @property
    def attributes(self) -> Dict:
        if self._forward and self._reverse:
            direction = "both"
        elif self._forward:
            direction = "forward"
        elif self._reverse:
            direction = "back"
        else:
            direction = "none"
        return {**self._attributes, "dir": direction}

    def append(self, other: Union[List[Node], List["Edge"]], forward=None, reverse=None) -> List["Edge"]:
        result = []
        for o in other:
            if isinstance(o, Edge):
                o._forward = forward if forward else o._forward
                o._reverse = forward if forward else o._reverse
                self._attributes = o.attributes.copy()
                result.append(o)
            else:
                result.append(Edge(o, forward=forward, reverse=reverse, **self._attributes))
        return result

    def connect(self, other: Union[Node, "Edge", List[Node]]):
        if isinstance(other, list):
            for node in other:
                self._node.connect(node, self)
            return other
        elif isinstance(other, Edge):
            self._attributes = other._attributes.copy()
            return self
        else:
            if self._node is not None:
                return self._node.connect(other, self)
            else:
                self._node = other
                return self
