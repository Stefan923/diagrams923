from diagrams import *
from diagrams.generic.device import Computer


def test_diagram():
    diagram = Diagram()
    diagram.add_out_format("png")
    computer = Computer(diagram)
    diagram.add_node(computer, "Home PC")
    diagram.render()


if __name__ == '__main__':
    test_diagram()