#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
import logging
from pathlib import Path

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

FILE_SERVER_HOST = '127.0.0.1'
PORT = 88
file_server_addr = (FILE_SERVER_HOST, PORT)


def main():
    file_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    file_client.connect(file_server_addr)

    resp_data = file_client.recv(1024)
    if resp_data:
        print(resp_data.decode())

    file_name = input("请输入要发送的文件路径: ")
    send_file = Path(file_name)

    if not send_file.exists():
        logger.error(f"{send_file} file not exist.")
        exit(1)

    file_client.send(f"{send_file}\r\n\r\n".encode())

    with open(send_file, "rb") as f:
        file_client.send(f.read())
    logging.info(f"upload file {send_file} success")

    file_client.close()


if __name__ == "__main__":
    main()
