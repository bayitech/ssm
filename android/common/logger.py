import logging

class STPLogging:
    """
    Logging facility
    """
    logging.basicConfig(format='%(asctime)s %(levelname)s {%(module)s} [%(funcName)s] %(message)s',
                        datefmt='%Y-%m-%d,%H:%M:%S:%f', level=logging.INFO)
    logging.FileHandler()
