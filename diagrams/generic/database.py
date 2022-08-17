from . import _Generic


class _Database(_Generic):
    _icon_dir = "resources/generic/database"


class Database(_Database):
    _icon = "database.png"


class DataCenter(_Database):
    _icon = "datacenter.png"
