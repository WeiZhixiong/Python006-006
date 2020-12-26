#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
from datetime import datetime
import os

log_day = datetime.strftime(datetime.now(), "%Y%m%d")
log_dir = "/var/log/python-%s" % log_day
log_file = log_dir + "/week01.log"

if not os.path.exists(log_dir):
    os.makedirs(log_dir)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(filename)s| %(message)s",
    filename=log_file,
)


def main():
    logging.info("execute main.")
    print("hello, %s" % __name__)


if __name__ == "__main__":
    main()
