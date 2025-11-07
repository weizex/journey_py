from collections.abc import Callable
from collections import defaultdict
from queue import Empty, Queue
from threading import Thread
from time import sleep
from typing import Any

'''
callable 本质上是类型提示， 不是实际的对象
起到一个函数签名检查的作用，用它来:一个对象的类型，就可以对对象进行参数检查
'''

class Event:
    def _init_(self, type: str, data: Any = None):
        self.type = type
        self.data = data

HandlerType = Callable[[Event], None]

class EventEngine:
    def __init__(self, interval: int = 1)->None:
        self._interval: int = interval
        self._queue: Queue = Queue()
        self._handlers: defaultdict = defaultdict(list)
        self._active: bool = False
        self._timer: Thread = Thread(target=self._run_timer)

        self._thread: Thread = Thread(target=self._run)
        self._general_handlers: list = []

    def _run(self)->None:
        while self._active:
            try:
                event: Event = self._queue.get(block=True, timeout=1)
                self._process(event)
            except Empty:
                pass
    
    def _process(self, event: Event) -> None:
        if event.type in self._handlers:
            [handler(event) for handler in self._handlers[event.type]]
        for handler in self._general_handlers:
            handler(event)

    def _run_timer(self) -> None:
        """
        Sleep by interval second(s) and then generate a timer event.
        """
        while self._active:
            sleep(self._interval)
            event: Event = Event(EVENT_TIMER)
            self.put(event)

    def start(self) -> None:
        """
        Start event engine to process events and generate timer events.
        """
        self._active = True
        self._thread.start()
        self._timer.start()

    def stop(self) -> None:
        """
        Stop event engine.
        """
        self._active = False
        self._timer.join()
        self._thread.join()

    def put(self, event: Event) -> None:
        """
        Put an event object into event queue.
        """
        self._queue.put(event)

    def register(self, type: str, handler: HandlerType) -> None:
        if type not in self._handlers[type]:
            self._handlers[type].append(handler)
        #注意这两种写法的细微区别，前者需要进行两次引用，在多线程下
        '''
        handler_list: list = self._handlers[type]
        if handler not in handler_list:
            handler_list.append(handler)
        python的可变对象的赋值，传递操作都默认是传递引用，
        要想创建独立的对象，需要copy，切片，构造函数
        python的浅拷贝的概念也是这种机制带来的
        更深刻的，python中的变量名只是对象的标签，给他的值才是真正的对象单独储存于内存中，a = b本身只是共享同一对象的标签
        而c中变量名是对内存空间的直接命名，a就是内存中数据本省，可以修改
        而python中a的重新赋值是把这个标签贴到其他地方
        '''
    

    def unregister(self, type: str, handler: HandlerType) -> None:
        if handler in self._handlers[type]:
            self._handlers[type].remove(handler)
            
        if not self._handlers[type]:
            self._handlers.pop(type)


    def register_general(self, handler: HandlerType) -> None:
        if handler not in self._general_handlers:
            self._general_handlers.append(handler)

    def unregister_general(self, handler: HandlerType) -> None:
        """
        Unregister an existing general handler function.
        """
        if handler in self._general_handlers:
            self._general_handlers.remove(handler)