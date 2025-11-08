from types import ModuleType
import webbrowser
from functools import partial
from importlib import import_module
from typing import TypeVar
from collections.abc import Callable

import vnpy
from vnpy.event import EventEngine

from .qt import QtCore, QtGui, QtWidgets
from .widget import (
    BaseMonitor,
    TickMonitor,
    OrderMonitor,
    TradeMonitor,
    PositionMonitor,
    AccountMonitor,
    LogMonitor,
    ActiveOrderMonitor,
    ConnectDialog,
    ContractManager,
    TradingWidget,
    AboutDialog,
    GlobalDialog
)
from ..engine import MainEngine, BaseApp
from ..utility import get_icon_path, TRADER_DIR
from ..locale import _


WidgetType = TypeVar("WidgetType", bound="QtWidgets.QWidget")

class MainWindow(QtWidgets.QMainWindow):
    