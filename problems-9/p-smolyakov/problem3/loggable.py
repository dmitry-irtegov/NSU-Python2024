#!/usr/bin/env python3
from datetime import datetime


class _LogEntry:
    def __init__(self, func):
        self.timestamp = datetime.now()
        self.func = func


    def __str__(self):
        return f'{self.timestamp} :: {self.func.__name__} :: '


class _CallLogEntry(_LogEntry):
    def __init__(self, func, args, kwargs):
        _LogEntry.__init__(self, func)
        self.func = func
        self.args = args
        self.kwargs = kwargs


    def __str__(self):
        return _LogEntry.__str__(self) + f'Call with args {self.args[1:]} and kwargs {self.kwargs}'


class _RetLogEntry(_LogEntry):
    def __init__(self, func, res):
        _LogEntry.__init__(self, func)
        self.func = func
        self.res = res


    def __str__(self):
        return _LogEntry.__str__(self) + f'Return with result: {self.res}'


class _ExceptionLogEntry(_LogEntry):
    def __init__(self, func, exception):
        _LogEntry.__init__(self, func)
        self.func = func
        self.exception = exception


    def __str__(self):
        return _LogEntry.__str__(self) + f'Raised {repr(self.exception)}'


class _LogStorage:
    def __init__(self):
        self._list = []


    def __str__(self):
        res = ''
        for entry in self._list:
            res += str(entry) + '\n'
        return res


class Loggable:
    def __init__(self):
        self.__log_store = _LogStorage()

        if hasattr(self.__class__, 'is_hooked'):
            return
            
        def hook(orig_func, *args, **kwargs):
            loglist = args[0].__log_store._list

            loglist.append(_CallLogEntry(orig_func, args, kwargs))
            res = None
            try:
                res = orig_func(*args, **kwargs)
            except Exception as e:
                loglist.append(_ExceptionLogEntry(orig_func, e))
                raise e
            else:
                loglist.append(_RetLogEntry(orig_func, res))
            return res

        def genhook(func):
            return lambda *args, **kwargs: hook(func, *args, **kwargs)

        funcs = filter(callable, self.__class__.__dict__.values())
        for func in funcs:
            setattr(self.__class__, func.__name__, genhook(func))

        setattr(self.__class__, 'is_hooked', True)


    def log_storage(self):
        return self.__log_store

    
class _ClassWithLogging(Loggable):
    def a(self):
        print('sideeffect')
        return 123

    def mnogo(self, one, two, three='named', four='args'):
        pass

    def exceptionness(self):
        raise RuntimeError('errortext')

    def __str__(self):
        return 'string'
        

if __name__ == '__main__':
    one = _ClassWithLogging()
    one.a()
    print(str(one))
    one.mnogo(1, 2, 3)

    two = _ClassWithLogging()
    two.mnogo(1, 2, four = 'GAGAGGAGAGAG')
    try:
        two.exceptionness()
    except RuntimeError:
        pass

    print('LOG FOR one')
    print(str(one.log_storage()))

    print('LOG FOR two')
    print(str(two.log_storage()))
