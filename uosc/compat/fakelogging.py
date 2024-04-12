import sys

DEBUG, INFO, WARNING, ERROR, CRITICAL = range(5)


class Logger:
    def __init__(self, name):
        self.name = name
        self.level = DEBUG

    def log(self, level=DEBUG, msg="", *args):
        if self.level > level:
            return
        print("%s: %s" % (self.name, msg % args), file=sys.stderr)

    def debug(self, msg, *args):
        self.log(DEBUG, msg, *args)

    def setLevel(self, level):
        self.level = level

    exception = critical = error = warning = info = debug


log = Logger("uosc.fakelogger")


def basicConfig(*args, **kwargs):
    pass


def getLogger(name=None):
    return log
