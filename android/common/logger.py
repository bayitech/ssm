#!/usr/bin/env python
# ! -*- coding:utf-8 -*-

import logging
import sys

class STPLogging:
    """
    Logging facility
    """

    # file name should be unique per testcase run
    # suggested format is %(testcase).%(asctime).log
    file_name = ""

    def __init__(self, file="../../data/testcase.log"):
        # update file name
        self.file_name = file

        # change basic configuration for logging
        logging.basicConfig(filename=file, filemode='w', format='%(asctime)s %(funcName)s %(levelname)s: %(message)s',
                            datefmt='%Y-%m-%d %H:%M:%S', level=logging.INFO)
        # logging.getLogger().addHandler(logging.StreamHandler(sys.stdout))

        console = logging.StreamHandler(sys.stdout)
        # set a format which is simpler for console use
        formatter = logging.Formatter("%(asctime)s %(levelname)s: %(message)s")
        console.setFormatter(formatter)
        # add the handler to the root logger
        logging.getLogger('').addHandler(console)
        return

    def stp_logging(self, message: str):
        logging.info(message)
        return


logger = STPLogging()
logger.stp_logging("baby")
