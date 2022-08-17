from . import _Generic


class _Network(_Generic):
    _icon_dir = "resources/generic/network"


class Router(_Network):
    _icon = "router.png"


class Switch(_Network):
    _icon = "switch.png"
