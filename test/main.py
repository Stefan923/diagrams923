from diagrams import *
from diagrams.generic.device import *


def test_diagram():
    diagram = Diagram()
    diagram.add_out_format("png")
    diagram.set_file_name("../test_output/default_filename")

    computer1 = Computer(diagram)
    diagram.add_node(computer1, "Home PC")
    computer2 = Computer(diagram)
    diagram.add_node(computer2, "Office PC")
    mobile = Mobile(diagram)
    diagram.add_node(mobile, "Own Phone")
    tablet = Tablet(diagram)
    diagram.add_node(tablet, "Child's Tablet")

    edge1 = Edge(computer1)
    edge1.connect(computer2)
    edge1.connect(mobile)
    edge2 = Edge(mobile)
    edge2.connect(tablet)

    diagram.render()


if __name__ == '__main__':
    test_diagram()
