#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Module to initialise the logging.
"""

import sys
import os
import logging
from logging.handlers import TimedRotatingFileHandler

def initLogger(logFilePath):
    root_logger = logging.getLogger()
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s [%(process)d] - %(levelname)s - %(message)s',
        datefmt='[%Y-%m-%d %H:%M:%S]')
    root_logger.setLevel(logging.DEBUG)

    ch = logging.StreamHandler()
    ch.setFormatter(formatter)
    ch.setLevel(logging.INFO)

    # Only log degug to stdout if asked
    if os.environ.get('DEBUG', '') != '':
        root_logger.setLevel(logging.DEBUG)
        logging.debug('DEBUG logging is ON')

    fh = TimedRotatingFileHandler(filename = logFilePath,
            when = 'midnight', backupCount = 30)

    fh.setFormatter(formatter)
    # Always log debug into the file
    fh.setLevel(logging.DEBUG)

    root_logger.addHandler(fh)
    root_logger.addHandler(ch)

    logging.info('Container logging enabled.')
