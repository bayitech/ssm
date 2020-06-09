# -*- coding: utf-8 -*-
import json
import logging

'''
configuration file decoder

This program decodes json format configuration file used to setup testing environment


'''


class ConfigDecoder:
    """
    JSON file format is used to provide test setup information. This class reads JSON
    file and decode any information needed.
    """
    dev_id = []
    testcase = []
    cfg_file = "../../data/config.json"

    def __init__(self, cfg_file: str):
        self.cfg_file = cfg_file

        # open config file and load it
        logging.info("Opening a configuration file " + self.cfg_file + " for loading...")

        with open(self.cfg_file) as fp:
            self.config = json.load(fp)
        print(self.config)
        return


cfg = ConfigDecoder()
