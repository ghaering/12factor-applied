import logging
import logging.handlers
import os

def get_logger(syslog_address):
    """
    Set up and return logger.

    The logger logs to syslog via the specified syslog_address.
    """
    handler = logging.handlers.SysLogHandler(address=syslog_address)
    logger = logging.getLogger("worker")
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)
    return logger

class Worker(object):
    def __init__(self, logger):
        self.logger = logger

    def work(self):
        self.logger.debug("starting worker")
        pass # actual implementation here

def main():
    syslog_address = os.environ.get("SYSLOG_ADDRESS", "/dev/log")

    worker = Worker(get_logger(syslog_address))
    worker.work()

if __name__ == "__main__":
    main()
