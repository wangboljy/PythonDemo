import os
import logging
from common.LogConfig import LogConf

log_fmt = '%(asctime)s|%(levelname)s|%(filename)s:%(funcName)s:%(lineno)d|%(message)s'


class Whisper(object):
    loggerSet = {}

    @staticmethod
    def getLogger(logName=LogConf["logName"], fileName=LogConf["logFile"]):
        if logName in Whisper.loggerSet:
            return Whisper.loggerSet.get(logName)

        dir = os.path.dirname(fileName)
        if dir and (not os.path.isdir(dir)):
            os.makedirs(dir)
        handler = logging.FileHandler(fileName)
        formatter = logging.Formatter(log_fmt)
        handler.setFormatter(formatter)
        logger = logging.getLogger(logName)
        logger.addHandler(handler)
        logger.setLevel(logging.DEBUG)

        Whisper.loggerSet[logName] = logger
        return logger
