#!/usr/bin/env python
# ! -*- coding:utf-8 -*-

import logging


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
        logging.basicConfig(filename=file, filemode='w', format='%(asctime)s %(levelname)-8s %(message)s',
                            datefmt='%Y-%m-%d %H:%M:%S', level=logging.INFO)
        #  logging.FileHandler(self.file_name)
        console = logging.StreamHandler()
        console.setLevel(logging.INFO)
        logging.info('HELLO')
        return

    def stp_logging(self, message: str):
        logging.info(message)
        return


logger = STPLogging()
logger.stp_logging("yes baby")
