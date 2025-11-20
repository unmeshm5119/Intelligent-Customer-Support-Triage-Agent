import json
import time


class SimpleLogger:
def info(self, msg: str, **kwargs):
print(json.dumps({'ts': time.time(), 'level': 'info', 'msg': msg, **kwargs}))


def error(self, msg: str, **kwargs):
print(json.dumps({'ts': time.time(), 'level': 'error', 'msg': msg, **kwargs}))
