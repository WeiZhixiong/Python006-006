#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
import logging
import threading
from pathlib import Path

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

HOST = '127.0.0.1'
PORT = 88
listen_addr = (HOST, PORT)


class Writer:
    """
    解析 client 传输的数据，并写入相应的文件
    """
    def __init__(self):
        self.has_filename = False
        self.filename = ""

    def write_to_file(self, write_data):
        if self.has_filename:
            with open(self.filename, 'ab') as f:
                f.write(write_data)
        else:
            first_part = write_data[:1028]
            if b"\r\n\r\n" not in first_part:
                raise Exception("no filename")
            else:
                first_part = first_part.split(b"\r\n\r\n", 1)
                if len(first_part[0]) > 0:
                    self.filename = Path("received_" + Path(first_part[0].decode()).name)
                    if self.filename.exists():
                        raise Exception("already has file %s, exit" % self.filename)
                    self.has_filename = True
                else:
                    raise Exception("filename length must greater than 0")
                logging.info(f"start receive file {self.filename}")
                with open(self.filename, 'wb') as f:
                    f.write(first_part[1])
                    f.write(write_data[1028:])


def worker(conn, client_addr):
    """
    处理单一 socket connection
    """
    logging.info("create connection; "
                 "client ip: %s, port: %d" % client_addr)
    conn_explaintion = r"""欢迎使用文件上传服务, 请使用 utf-8 编码, 文件名不能超过 1024 字节. 
    上传数据格式要求: {{ filename }}\r\n\r\n{{ file_content }}""" + "\r\n"
    conn.send(conn_explaintion.encode())
    write_buffer = []
    write_buffer_len = 0
    writer = Writer()

    while True:
        receive_data = conn.recv(1024)
        if receive_data:
            write_buffer.append(receive_data)
            write_buffer_len += 1
            if write_buffer_len > 4096:
                write_data = b''.join(write_buffer)
                try:
                    writer.write_to_file(write_data)
                except Exception as err:
                    logger.error(err)
                    conn.send(str(err).encode())
                    conn.close()
                    break
                write_buffer = []
                write_buffer_len = 0
        else:
            write_data = b''.join(write_buffer)
            try:
                writer.write_to_file(write_data)
            except Exception as err:
                logger.error(err)
            logger.info("close connection; "
                        "client ip: %s, port: %d" % client_addr)
            conn.close()
            break


def main():
    logger.info("start listen %s:%d" % listen_addr)
    echo_server = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    echo_server.bind(listen_addr)
    echo_server.listen(5)
    while True:
        conn, client_addr = echo_server.accept()
        t = threading.Thread(target=worker, args=(conn, client_addr))
        t.start()


if __name__ == "__main__":
    main()
