from . import _Generic


class _Device(_Generic):
    _icon_dir = "resources/generic/device"


class Computer(_Device):
    _icon = "computer.png"


class Mobile(_Device):
    _icon = "mobile.png"


class Tablet(_Device):
    _icon = "tablet.png"
