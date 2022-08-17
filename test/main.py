from diagrams import *
from diagrams.generic.device import *


def test_diagram():
    diagram = Diagram()
    diagram.add_out_format("png")

    computer1 = Computer(diagram)
    diagram.add_node(computer1, "Home PC")
    computer2 = Computer(diagram)
    diagram.add_node(computer2, "Office PC")
    mobile = Mobile(diagram)
    diagram.add_node(mobile, "Own Phone")

    edge1 = Edge(computer1)
    edge1.connect(computer2)
    edge1.connect(mobile)

    diagram.render()


if __name__ == '__main__':
    test_diagram()