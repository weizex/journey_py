from abc import ABC
from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .engine import BaseEngine


class BaseApp(ABC):
    app_name: str
    app_module: str
    app_path: Path
    display_name: str
    engine_class: type["BaseEngine"]
    #理解这种type机制也很简单，type本身是一种对象，叫类对象，也就是说，定义的类本身（不是其实例），
    #也是一个实例对象，这个实例对应的类是类的类，也即type
    widget_name: str
    icon_name: str