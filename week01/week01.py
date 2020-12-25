#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
from datetime import datetime

log_day = datetime.strftime(datetime.now(), "%Y%m%d")
log_file = "/var/log/python-%s/week01.log" % log_day

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(filename)s| %(message)s",
    filename=log_file,
)


def main():
    logging.info("execute main.")
    print("hello, %s", __name__)


if __name__ == "__main__":
    main()
