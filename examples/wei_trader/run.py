import sys
#sys是与解释器交互，如path，argv，stdio等
import os
#与os交互，如path子模块，执行系统命令，文件创建等

'''__file__总是脚本文件本身的路径
要获取执行脚本的路径，需要通过os.getcwd()获取
os执行abspath也是根据cwd而非脚本文件位置，这要注意'''
from vnpy_ctastrategy import CtaStrategyApp
from vnpy_ctabacktester import CtaBacktesterApp

from vnpy_datamanager import DataManagerApp
from vnpy_ctp import CtpGateway
current_path = os.path.abspath(__file__)
root_path = os.path.dirname(os.path.dirname(os.path.dirname(current_path)))
if root_path not in sys.path:
    sys.path.append(root_path)

print(sys.path)

from core.trader.exam import Exam
a = Exam()
print(a.x)
from core.event.engine import EventEngine
from core.trader.engine import MainEngine
from core.trader.ui import MainWindow, create_qapp


def main():
    """"""
    qapp = create_qapp()

    event_engine = EventEngine()

    main_engine = MainEngine(event_engine)

    main_engine.add_gateway(CtpGateway)
    # main_engine.add_gateway(CtptestGateway)
    # main_engine.add_gateway(MiniGateway)
    # main_engine.add_gateway(FemasGateway)
    # main_engine.add_gateway(SoptGateway)
    # main_engine.add_gateway(UftGateway)
    # main_engine.add_gateway(EsunnyGateway)
    # main_engine.add_gateway(XtpGateway)
    # main_engine.add_gateway(ToraStockGateway)
    # main_engine.add_gateway(ToraOptionGateway)
    # main_engine.add_gateway(IbGateway)
    # main_engine.add_gateway(TapGateway)
    # main_engine.add_gateway(DaGateway)
    # main_engine.add_gateway(RohonGateway)
    # main_engine.add_gateway(TtsGateway)

    # main_engine.add_app(PaperAccountApp)
    main_engine.add_app(CtaStrategyApp)
    main_engine.add_app(CtaBacktesterApp)
    # main_engine.add_app(SpreadTradingApp)
    # main_engine.add_app(AlgoTradingApp)
    # main_engine.add_app(OptionMasterApp)
    # main_engine.add_app(PortfolioStrategyApp)
    # main_engine.add_app(ScriptTraderApp)
    # main_engine.add_app(ChartWizardApp)
    # main_engine.add_app(RpcServiceApp)
    # main_engine.add_app(ExcelRtdApp)
    main_engine.add_app(DataManagerApp)
    # main_engine.add_app(DataRecorderApp)
    # main_engine.add_app(RiskManagerApp)
    # main_engine.add_app(WebTraderApp)
    # main_engine.add_app(PortfolioManagerApp)

    main_window = MainWindow(main_engine, event_engine)
    main_window.showMaximized()

    print("created and showed")

    qapp.exec()


if __name__ == "__main__":
    main()
