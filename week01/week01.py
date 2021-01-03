#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
from datetime import datetime
from pathlib import PurePath, Path

log_day = datetime.strftime(datetime.now(), "%Y%m%d")
log_dir = Path("/var/log/python-%s" % log_day)
log_file = PurePath(log_dir, "week01.log")

if not log_dir.exists():
    log_dir.mkdir(parents=True)

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
